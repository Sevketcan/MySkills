#!/usr/bin/env python3
"""Build a deterministic manifest for all packaged Codex skill entry points."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
OUTPUT = ROOT / "manifest.json"
NAME_PATTERN = re.compile(r"^name:\s*['\"]?([^'\"\n]+)['\"]?\s*$", re.MULTILINE)


def skill_name(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing YAML frontmatter: {path}")
    match = NAME_PATTERN.search(text.split("---", 2)[1])
    if not match:
        raise ValueError(f"Missing skill name: {path}")
    return match.group(1).strip()


def main() -> int:
    packages = []
    all_names: dict[str, str] = {}
    for package in sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir()):
        entrypoint = package / "SKILL.md"
        if not entrypoint.is_file():
            continue
        discovered = []
        for skill_file in sorted(package.rglob("SKILL.md")):
            name = skill_name(skill_file)
            relative = skill_file.relative_to(ROOT).as_posix()
            if name in all_names:
                raise ValueError(
                    f"Duplicate skill name {name!r}: {all_names[name]} and {relative}"
                )
            all_names[name] = relative
            discovered.append({"name": name, "path": relative})
        packages.append(
            {
                "directory": package.name,
                "entrypoint": entrypoint.relative_to(ROOT).as_posix(),
                "skill_count": len(discovered),
                "skills": discovered,
            }
        )

    manifest = {
        "schema_version": 1,
        "package_count": len(packages),
        "skill_count": len(all_names),
        "packages": packages,
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}: {len(packages)} packages, {len(all_names)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

