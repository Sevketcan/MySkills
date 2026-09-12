#!/usr/bin/env bash
set -euo pipefail

REPOSITORY="Sevketcan/MySkills"
BRANCH="main"
DRY_RUN=0
LIST_ONLY=0
TEMP_DIR=""

usage() {
  printf '%s\n' \
    'Usage: install.sh [--dry-run] [--list]' \
    '' \
    'Installs every package in this repository into the Codex skills directory.'
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --list) LIST_ONLY=1 ;;
    -h|--help) usage; exit 0 ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

cleanup() {
  if [ -n "$TEMP_DIR" ] && [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
  fi
}
trap cleanup EXIT

SCRIPT_DIR=""
if [ -n "${BASH_SOURCE[0]:-}" ] && [ -f "${BASH_SOURCE[0]}" ]; then
  SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
fi

if [ -n "$SCRIPT_DIR" ] && [ -d "$SCRIPT_DIR/skills" ]; then
  SOURCE_ROOT="$SCRIPT_DIR"
else
  command -v curl >/dev/null 2>&1 || {
    printf 'curl is required for remote installation.\n' >&2
    exit 1
  }
  TEMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/myskills.XXXXXX")
  ARCHIVE="$TEMP_DIR/repository.tar.gz"
  curl -fsSL "https://github.com/$REPOSITORY/archive/refs/heads/$BRANCH.tar.gz" -o "$ARCHIVE"
  tar -xzf "$ARCHIVE" -C "$TEMP_DIR"
  SOURCE_ROOT="$TEMP_DIR/MySkills-$BRANCH"
fi

SOURCE_SKILLS="$SOURCE_ROOT/skills"
[ -d "$SOURCE_SKILLS" ] || {
  printf 'skills directory not found in source package.\n' >&2
  exit 1
}

CODEX_ROOT="${CODEX_HOME:-${HOME}/.codex}"
TARGET_SKILLS="$CODEX_ROOT/skills"
TIMESTAMP=$(date -u +%Y%m%dT%H%M%SZ)
BACKUP_ROOT="$CODEX_ROOT/skill-backups/$TIMESTAMP"

list_packages() {
  for package_path in "$SOURCE_SKILLS"/*; do
    [ -d "$package_path" ] || continue
    [ -f "$package_path/SKILL.md" ] || continue
    basename "$package_path"
  done
}

if [ "$LIST_ONLY" -eq 1 ]; then
  list_packages
  exit 0
fi

mkdir -p "$TARGET_SKILLS"
installed=0
updated=0
unchanged=0

for source_path in "$SOURCE_SKILLS"/*; do
  [ -d "$source_path" ] || continue
  [ -f "$source_path/SKILL.md" ] || continue
  package_name=$(basename "$source_path")
  target_path="$TARGET_SKILLS/$package_name"

  if [ -d "$target_path" ] && diff -qr "$source_path" "$target_path" >/dev/null 2>&1; then
    printf 'unchanged  %s\n' "$package_name"
    unchanged=$((unchanged + 1))
    continue
  fi

  if [ "$DRY_RUN" -eq 1 ]; then
    if [ -e "$target_path" ]; then
      printf 'would update  %s\n' "$package_name"
    else
      printf 'would install %s\n' "$package_name"
    fi
    continue
  fi

  staging_path="$TARGET_SKILLS/.myskills-$package_name-$TIMESTAMP-$$"
  cp -R "$source_path" "$staging_path"

  if [ -e "$target_path" ]; then
    mkdir -p "$BACKUP_ROOT"
    mv "$target_path" "$BACKUP_ROOT/$package_name"
    if ! mv "$staging_path" "$target_path"; then
      mv "$BACKUP_ROOT/$package_name" "$target_path"
      printf 'Failed to update %s; original restored.\n' "$package_name" >&2
      exit 1
    fi
    printf 'updated    %s\n' "$package_name"
    updated=$((updated + 1))
  else
    mv "$staging_path" "$target_path"
    printf 'installed  %s\n' "$package_name"
    installed=$((installed + 1))
  fi
done

if [ "$DRY_RUN" -eq 1 ]; then
  printf 'Dry run complete; no files changed.\n'
else
  printf 'Done: %s installed, %s updated, %s unchanged. Restart Codex to reload skills.\n' \
    "$installed" "$updated" "$unchanged"
  if [ -d "$BACKUP_ROOT" ]; then
    printf 'Backup: %s\n' "$BACKUP_ROOT"
  fi
fi

