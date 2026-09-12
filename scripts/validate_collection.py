#!/usr/bin/env python3
"""Validate every Codex skill entry point in the collection."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if not match:
        raise ValueError("missing or malformed YAML frontmatter")
    value = yaml.safe_load(match.group(1))
    if not isinstance(value, dict):
        raise ValueError("frontmatter must be a mapping")
    return value


def main() -> int:
    errors: list[str] = []
    names: dict[str, Path] = {}
    files = sorted(SKILLS_ROOT.rglob("SKILL.md"))
    if not files:
        errors.append("no SKILL.md files found")

    for path in files:
        relative = path.relative_to(ROOT)
        try:
            data = frontmatter(path)
            unexpected = set(data) - ALLOWED_KEYS
            if unexpected:
                errors.append(f"{relative}: unexpected keys: {', '.join(sorted(unexpected))}")
            name = data.get("name")
            description = data.get("description")
            if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name) or len(name) > 64:
                errors.append(f"{relative}: invalid skill name {name!r}")
            elif name in names:
                errors.append(f"{relative}: duplicate name {name!r}; first seen at {names[name]}")
            else:
                names[name] = relative
            if not isinstance(description, str) or not description.strip():
                errors.append(f"{relative}: description must be a non-empty string")
        except (OSError, UnicodeError, yaml.YAMLError, ValueError) as exc:
            errors.append(f"{relative}: {exc}")

    package_count = sum(
        1 for path in SKILLS_ROOT.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()
    )
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(files)} skills in {package_count} packages; names are unique.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

