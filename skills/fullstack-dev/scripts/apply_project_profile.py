#!/usr/bin/env python3
"""Preview or install an opt-in profile, preserving existing project instructions."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]

def apply_profile(project, apply=False):
    source = ROOT / 'assets/project-profile'
    existing = [project / name for name in ('AGENTS.md', 'CLAUDE.md') if (project / name).exists()]
    if any(p.is_symlink() for p in existing):
        raise ValueError('Instruction symlinks require an explicit project-specific merge')
    for path in existing:
        if path.read_bytes() != (source / path.name).read_bytes():
            raise ValueError(f'{path} has existing instructions; merge the profile manually, no files changed')
    missing = [name for name in ('AGENTS.md','CLAUDE.md') if not (project/name).exists()]
    if apply:
        if not project.is_dir():
            raise ValueError('Project directory does not exist')
        for name in missing:
            shutil.copy2(source/name, project/name)
    return missing

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('project', type=Path)
    p.add_argument('--apply', action='store_true')
    a = p.parse_args()
    try:
        missing = apply_profile(a.project.resolve(), a.apply)
    except ValueError as exc:
        p.exit(1, str(exc) + '\n')
    print(('Installed: ' if a.apply else 'Would install: ') + ', '.join(missing))
