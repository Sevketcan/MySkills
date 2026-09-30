#!/usr/bin/env python3
"""Conflict-aware, file-level sync between repository, Codex and Claude Code."""
from __future__ import annotations

import argparse
import difflib
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import uuid

import yaml

SKIP_CLAUDE = {'fullstack-dev', 'unity-skills~'}
EXCLUDED = {'.system', '.git', 'evals', '__pycache__', '.DS_Store', '.env', '.env.local'}
SECRET = re.compile(rb'(?<![A-Za-z0-9_-])(?:gh[opusr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY)')


def ignored(path):
    return any(p in EXCLUDED or p.startswith('.myskills-') for p in path.parts) or path.suffix in {'.pyc', '.pem', '.key'} or 'credentials' in path.name


def transform(data, path, claude=False, reverse=False):
    if path.suffix != '.md':
        return data
    text = data.decode('utf-8')
    if reverse:
        text = text.replace('${CLAUDE_CONFIG_DIR:-$HOME/.claude}', '${CODEX_HOME:-$HOME/.codex}').replace('CLAUDE_CONFIG_DIR', 'CODEX_HOME').replace('.claude/skills', '.codex/skills')
    elif claude:
        text = text.replace('${CODEX_HOME:-$HOME/.codex}', '${CLAUDE_CONFIG_DIR:-$HOME/.claude}').replace('CODEX_HOME', 'CLAUDE_CONFIG_DIR').replace('.codex/skills', '.claude/skills')
    if path.name == 'SKILL.md':
        match = re.match(r'^---\n(.*?)\n---(?:\n|$)', text, re.S)
        if match:
            header = match.group(1)
            tools = yaml.safe_load(header).get('allowed-tools')
            if isinstance(tools, str):
                tools = [item.strip() for item in tools.split(',')]
            if isinstance(tools, list):
                # Normalize just this field, preserving all other frontmatter.
                replacement = 'allowed-tools: ' + ', '.join(tools) if claude else 'allowed-tools:\n' + '\n'.join('  - ' + item for item in tools)
                header = re.sub(r'^allowed-tools:[^\n]*(?:\n[ \t]+-[^\n]*)*', lambda _: replacement, header, flags=re.M)
                text = text[:match.start(1)] + header + text[match.end(1):]
    return text.encode('utf-8')



def from_claude(data, reference, path):
    """Apply Claude edits to the canonical text without rewriting literal examples."""
    if path.suffix != '.md':
        return data
    canonical = reference.decode('utf-8')
    expected = transform(reference, path, claude=True).decode('utf-8')
    incoming = transform(transform(data, path), path, claude=True).decode('utf-8')
    if incoming == expected:
        return reference
    mapping = difflib.SequenceMatcher(None, canonical, expected, autojunk=False).get_opcodes()

    def position(offset):
        for _, a, b, c, d in mapping:
            if c <= offset <= d:
                if d == c:
                    return a
                return a + round((offset - c) * (b - a) / (d - c))
        return len(canonical)

    edits = difflib.SequenceMatcher(None, expected, incoming, autojunk=False).get_opcodes()
    for tag, a, b, c, d in reversed(edits):
        if tag != 'equal':
            replacement = incoming[c:d].replace('${CLAUDE_CONFIG_DIR:-$HOME/.claude}', '${CODEX_HOME:-$HOME/.codex}').replace('CLAUDE_CONFIG_DIR', 'CODEX_HOME').replace('.claude/skills', '.codex/skills')
            canonical = canonical[:position(a)] + replacement + canonical[position(b):]
    return transform(canonical.encode('utf-8'), path)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def scan(root, claude, aliases):
    result = {}
    if not root.exists():
        return result
    for package in sorted(root.iterdir()):
        if package.name.startswith('.') or not package.is_dir() or not (package / 'SKILL.md').is_file():
            continue
        if package.is_symlink():
            raise ValueError(f'Symlinked package is unsupported: {package}')
        name = aliases.get(package.name, package.name) if claude else package.name
        for file in package.rglob('*'):
            relative = file.relative_to(package)
            if ignored(relative) or not file.is_file():
                continue
            if file.is_symlink():
                raise ValueError(f'Symlinked file is unsupported: {file}')
            if claude and (name in SKIP_CLAUDE or 'agents' in relative.parts):
                continue
            key = (Path(name) / relative).as_posix()
            if key in result:
                raise ValueError(f'Package alias collision: {key}')
            raw = file.read_bytes()
            result[key] = (transform(raw, relative, reverse=claude), raw, file, file.stat().st_mode & 0o777)
    return result


def synchronize(repo, codex, claude, state, bootstrap=False, dry_run=False):
    roots = [root.resolve() for root in [repo, codex, claude]]
    repo, codex, claude = roots
    aliases = {p.name.rstrip('~'): p.name for root in [repo, codex] if root.exists() for p in root.iterdir() if p.is_dir()}
    trees = [scan(root, i == 2, aliases) for i, root in enumerate(roots)]
    for key, (_, raw, file, mode) in list(trees[2].items()):
        reference = next((tree[key][0] for tree in trees[:2] if key in tree), None)
        if reference is not None:
            trees[2][key] = (from_claude(raw, reference, Path(key)), raw, file, mode)
    binding = [str(p.resolve()) for p in roots]
    saved = json.loads(state.read_text()) if state.exists() else {'roots': binding, 'files': {}}
    if saved['roots'] != binding:
        raise ValueError('Sync state belongs to different skill directories')
    if bootstrap and saved['files']:
        raise ValueError('Bootstrap is only allowed before the first sync')
    merged, modes, conflicts = {}, {}, []
    for key in sorted(set().union(*(set(t) for t in trees))):
        values = [(i, t[key][0]) for i, t in enumerate(trees) if key in t]
        base = saved['files'].get(key)
        changes = {data for _, data in values if digest(data) != base}
        if len(changes) > 1:
            # First setup is explicit: preserve repository/Codex as authority,
            # while importing Claude-only files. All overwritten files are backed up.
            primary = {data for i, data in values if i != 2}
            if bootstrap and len(primary) == 1:
                chosen = next(iter(primary))
            else:
                conflicts.append(key)
                continue
        else:
            chosen = next(iter(changes)) if changes else values[0][1]
        if SECRET.search(chosen):
            raise ValueError(f'Possible credential in {key}; no files were changed')
        merged[key] = chosen
        modes[key] = next(t[key][3] for t in trees if key in t and t[key][0] == chosen)
    if conflicts:
        raise ValueError('Conflicting changes; no files were changed:\n' + '\n'.join(conflicts))
    # Validate the entire proposed collection before mutating any installation.
    with tempfile.TemporaryDirectory(prefix='myskills-validate-') as tmp:
        proposed = Path(tmp) / 'skills'
        for key, data in merged.items():
            file = proposed / key
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_bytes(data)
        spec = importlib.util.spec_from_file_location('validator', Path(__file__).with_name('validate_collection.py'))
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        validator.ROOT, validator.SKILLS_ROOT = Path(tmp), proposed
        if validator.main():
            raise ValueError('Proposed skill collection failed validation; no files were changed')
    writes = []
    for key, data in merged.items():
        path = Path(key)
        for i, root in enumerate(roots):
            if i == 2 and (path.parts[0] in SKIP_CLAUDE or 'agents' in path.parts[1:]):
                continue
            target_relative = Path(path.parts[0].rstrip('~'), *path.parts[1:]) if i == 2 else path
            target = root / target_relative
            output = transform(data, path, claude=True) if i == 2 else data
            before = target.read_bytes() if target.exists() else None
            if before != output:
                writes.append((i, target_relative, target, before, output, modes[key]))
    for tree in trees:
        for _, raw, file, _ in tree.values():
            if not file.exists() or file.read_bytes() != raw:
                raise ValueError(f'File changed during sync; retry: {file}')
    print(f'{"Would sync" if dry_run else "Syncing"} {len(writes)} files; deletions are restored, not propagated.')
    if dry_run:
        return len(writes)
    for _, _, target, before, _, _ in writes:
        if target.is_symlink() or any(p.is_symlink() for p in target.parents):
            raise ValueError(f'Symlink destination is unsupported: {target}')
        if (target.read_bytes() if target.exists() else None) != before:
            raise ValueError(f'File changed during sync; retry: {target}')
    backup = state.parent / 'backups' / uuid.uuid4().hex
    for i, relative, target, before, output, mode in writes:
        if target.is_symlink() or any(p.is_symlink() for p in target.parents):
            raise ValueError(f'Symlink destination is unsupported: {target}')
        if before is not None:
            old = backup / str(i) / relative
            old.parent.mkdir(parents=True, exist_ok=True)
            old.write_bytes(before)
        target.parent.mkdir(parents=True, exist_ok=True)
        fd, temporary = tempfile.mkstemp(prefix='.myskills-', dir=target.parent)
        try:
            with os.fdopen(fd, 'wb') as handle:
                handle.write(output)
            os.chmod(temporary, mode)
            os.replace(temporary, target)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    state.parent.mkdir(parents=True, exist_ok=True)
    temporary = state.with_suffix('.tmp')
    temporary.write_text(json.dumps({'roots': binding, 'files': {k: digest(v) for k, v in merged.items()}}, indent=2) + '\n')
    os.replace(temporary, state)
    if backup.exists():
        print(f'Backup: {backup}')
    return len(writes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bootstrap', action='store_true', help='First setup: prefer repository/Codex over existing Claude differences; back up overwritten files')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    home = Path.home()
    repo = Path(__file__).resolve().parents[1] / 'skills'
    codex = Path(os.environ.get('CODEX_HOME', home / '.codex')) / 'skills'
    claude = Path(os.environ.get('CLAUDE_CONFIG_DIR', home / '.claude')) / 'skills'
    state_root = Path(os.environ.get('MYSKILLS_STATE_ROOT', home / 'Library/Application Support/MySkills'))
    state_root.mkdir(parents=True, exist_ok=True)
    with (state_root / 'local-sync.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            synchronize(repo, codex, claude, state_root / 'local-sync.json', args.bootstrap, args.dry_run)
        except (ValueError, OSError, yaml.YAMLError) as exc:
            parser.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()
