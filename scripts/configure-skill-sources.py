#!/usr/bin/env python3
"""Disable duplicate Unity plugin skills, preserving plugin-only skills and tools."""
import argparse
import datetime
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]
START = '# BEGIN MYSKILLS SOURCE SELECTION'
END = '# END MYSKILLS SOURCE SELECTION'

def configure(codex, plugin_dir, personal, config, packages, apply=False):
    original = config.read_text() if config.exists() else ''
    # Remove only our own complete, previously generated block.
    if original.count(START) != original.count(END) or original.count(START) > 1:
        raise ValueError('Malformed source selection block; no configuration changed')
    base = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', original, flags=re.S)
    parsed = tomllib.loads(base)
    manual = {str(Path(v['path']).expanduser().resolve()) for v in parsed.get('skills', {}).get('config', [])}
    disabled = []
    for name in packages:
        theirs = plugin_dir / 'skills' / name / 'SKILL.md'
        ours = personal / name / 'SKILL.md'
        if not theirs.is_file():
            continue
        if not ours.is_file():
            raise ValueError(f'Missing personal counterpart: {ours}; no configuration changed')
        if str(theirs.resolve()) in manual or str(theirs.parent.resolve()) in manual:
            raise ValueError(f'Existing manual override for {theirs}; reconcile before applying')
        disabled.append(theirs.resolve())
    # An absent plugin may be legitimate on another machine: do not alter config.
    if not disabled:
        return {'disabled_count': 0, 'changed': False, 'status': 'plugin not present'}
    block = START + '\n' + '\n'.join(
        '[[skills.config]]\npath = ' + json.dumps(str(p)) + '\nenabled = false\n'
        for p in disabled
    ) + END + '\n'
    proposed = base.rstrip() + '\n\n' + block
    after = tomllib.loads(proposed)
    assert after.get('mcp_servers') == parsed.get('mcp_servers')
    assert after.get('plugins') == parsed.get('plugins')
    changed = proposed != original
    backup = None
    if apply and changed:
        backup = codex / 'skill-backups' / ('source-config-' + datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
        backup.mkdir(parents=True)
        if config.exists():
            shutil.copy2(config, backup / 'config.toml')
        config.parent.mkdir(parents=True, exist_ok=True)
        fd, temp = tempfile.mkstemp(prefix='.myskills-config-', dir=config.parent)
        try:
            with os.fdopen(fd, 'w') as f:
                f.write(proposed)
            if config.exists():
                os.chmod(temp, config.stat().st_mode & 0o777)
            os.replace(temp, config)
        finally:
            if os.path.exists(temp):
                os.unlink(temp)
    return {'disabled_count': len(disabled), 'changed': changed, 'applied': apply,
            'backup': str(backup) if backup else None,
            'plugin_only_skills': sorted(p.parent.name for p in (plugin_dir / 'skills').glob('*/SKILL.md')
                                        if p.parent.name not in packages)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Write config after backing it up; default is preview')
    parser.add_argument('--codex-root', type=Path, default=Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')))
    parser.add_argument('--plugin-dir', type=Path, help='Exact installed Unity plugin release directory')
    args = parser.parse_args()
    policy = json.loads((ROOT / 'skill-sources.json').read_text())
    directory = args.plugin_dir
    if directory is None:
        # Use the version actually installed, not the lexicographically greatest cache.
        import subprocess
        environment = dict(os.environ, CODEX_HOME=str(args.codex_root))
        listing = json.loads(subprocess.check_output(['codex', 'plugin', 'list', '--json'], text=True, env=environment))
        installed = [p for p in listing.get('installed', []) if p.get('name') == policy['plugin'] and p.get('enabled')]
        if not installed:
            print(json.dumps({'disabled_count': 0, 'status': 'enabled Unity plugin not found'}))
            return
        entry = installed[0]
        source = entry['source']
        if source['source'] == 'local':
            directory = Path(source['path'])
        else:
            directory = args.codex_root / 'plugins/cache' / entry['marketplaceName'] / entry['name'] / entry['version']
    print(json.dumps(configure(args.codex_root, directory, args.codex_root / 'skills',
                               args.codex_root / 'config.toml', policy['duplicate_packages'], args.apply),
                     ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
