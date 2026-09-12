#!/usr/bin/env bash
set -euo pipefail

REPOSITORY="Sevketcan/MySkills"
BRANCH="main"
DRY_RUN=0
LIST_ONLY=0
INCLUDE_ALL=0
TARGET="codex"
TEMP_DIR=""
WORK_DIR=""

# Packages that Claude Code already provides from another source. Installing them
# as personal skills would shadow or duplicate the existing copy, so they are
# skipped for the claude target unless --all is given.
CLAUDE_SKIP="fullstack-dev unity-skills"

usage() {
  printf '%s\n' \
    'Usage: install.sh [--target codex|claude|both] [--all] [--dry-run] [--list]' \
    '' \
    'Installs every package in this repository into the skills directory of the' \
    'selected agent.' \
    '' \
    '  --target codex   install into $CODEX_HOME/skills (default: ~/.codex/skills)' \
    '  --target claude  install into $CLAUDE_CONFIG_DIR/skills (default: ~/.claude/skills)' \
    '  --target both    install into both locations' \
    '  --all            also install packages that are skipped by default' \
    "                   for the claude target ($CLAUDE_SKIP)" \
    '  --dry-run        report what would change without writing anything' \
    '  --list           print the package names for the selected target'
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --list) LIST_ONLY=1 ;;
    --all) INCLUDE_ALL=1 ;;
    --target)
      [ "$#" -ge 2 ] || { printf -- '--target requires a value\n' >&2; exit 2; }
      TARGET="$2"
      shift
      ;;
    --target=*) TARGET="${1#--target=}" ;;
    -h|--help) usage; exit 0 ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

case "$TARGET" in
  codex|claude|both) ;;
  *) printf 'Unknown target: %s (expected codex, claude or both)\n' "$TARGET" >&2; exit 2 ;;
esac

cleanup() {
  for dir in "$TEMP_DIR" "$WORK_DIR"; do
    if [ -n "$dir" ] && [ -d "$dir" ]; then
      rm -rf "$dir"
    fi
  done
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

TIMESTAMP=$(date -u +%Y%m%dT%H%M%SZ)

# Codex allows a trailing tilde in a package directory name; Claude Code requires
# lowercase letters, digits and hyphens only.
claude_package_name() {
  printf '%s' "${1%\~}"
}

is_claude_skipped() {
  case " $CLAUDE_SKIP " in
    *" $1 "*) return 0 ;;
    *) return 1 ;;
  esac
}

# Rewrites a staged copy of a package into the form Claude Code expects:
#   * `allowed-tools` as a comma-separated string instead of a YAML list
#   * Codex skill-home paths pointed at the Claude skills directory
#   * Codex-only agent manifests dropped
transform_for_claude() {
  package_dir="$1"

  rm -rf "$package_dir/agents"

  find "$package_dir" -type f -name SKILL.md -print | while IFS= read -r skill_file; do
    grep -q '^allowed-tools:[[:space:]]*$' "$skill_file" || continue
    awk '
      BEGIN { fence = 0; collecting = 0; tools = "" }
      /^---[[:space:]]*$/ && fence < 2 {
        if (collecting) { print "allowed-tools: " tools; collecting = 0; tools = "" }
        fence++
        print
        next
      }
      fence == 1 && collecting && /^[[:space:]]*-[[:space:]]*/ {
        item = $0
        sub(/^[[:space:]]*-[[:space:]]*/, "", item)
        sub(/[[:space:]]+$/, "", item)
        tools = (tools == "" ? item : tools ", " item)
        next
      }
      fence == 1 && collecting {
        print "allowed-tools: " tools
        collecting = 0
        tools = ""
        print
        next
      }
      fence == 1 && /^allowed-tools:[[:space:]]*$/ { collecting = 1; next }
      { print }
    ' "$skill_file" >"$skill_file.myskills-tmp"
    mv "$skill_file.myskills-tmp" "$skill_file"
  done

  find "$package_dir" -type f -name '*.md' -print | while IFS= read -r doc_file; do
    grep -q 'CODEX_HOME\|\.codex/skills' "$doc_file" || continue
    sed -e 's|\${CODEX_HOME:-\$HOME/\.codex}|${CLAUDE_CONFIG_DIR:-$HOME/.claude}|g' \
        -e 's|CODEX_HOME|CLAUDE_CONFIG_DIR|g' \
        -e 's|~/\.codex/skills|~/.claude/skills|g' \
        -e 's|\.codex/skills|.claude/skills|g' \
        "$doc_file" >"$doc_file.myskills-tmp"
    mv "$doc_file.myskills-tmp" "$doc_file"
  done
}

list_packages() {
  target="$1"
  for package_path in "$SOURCE_SKILLS"/*; do
    [ -d "$package_path" ] || continue
    [ -f "$package_path/SKILL.md" ] || continue
    package_name=$(basename "$package_path")
    if [ "$target" = "claude" ]; then
      package_name=$(claude_package_name "$package_name")
      if [ "$INCLUDE_ALL" -eq 0 ] && is_claude_skipped "$package_name"; then
        printf '%s (skipped: already provided to Claude; use --all to override)\n' "$package_name"
        continue
      fi
    fi
    printf '%s\n' "$package_name"
  done
}

install_target() {
  target="$1"

  if [ "$target" = "claude" ]; then
    agent_root="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}"
    agent_label="Claude Code"
  else
    agent_root="${CODEX_HOME:-${HOME}/.codex}"
    agent_label="Codex"
  fi

  target_skills="$agent_root/skills"
  backup_root="$agent_root/skill-backups/$TIMESTAMP"

  installed=0
  updated=0
  unchanged=0
  skipped=0

  if [ "$DRY_RUN" -eq 0 ]; then
    mkdir -p "$target_skills"
  fi

  for source_path in "$SOURCE_SKILLS"/*; do
    [ -d "$source_path" ] || continue
    [ -f "$source_path/SKILL.md" ] || continue
    package_name=$(basename "$source_path")

    if [ "$target" = "claude" ]; then
      package_name=$(claude_package_name "$package_name")
      if [ "$INCLUDE_ALL" -eq 0 ] && is_claude_skipped "$package_name"; then
        printf 'skipped    %s (already provided to Claude)\n' "$package_name"
        skipped=$((skipped + 1))
        continue
      fi
    fi

    target_path="$target_skills/$package_name"
    prepared_path="$WORK_DIR/$target/$package_name"
    mkdir -p "$WORK_DIR/$target"
    rm -rf "$prepared_path"
    cp -R "$source_path" "$prepared_path"
    if [ "$target" = "claude" ]; then
      transform_for_claude "$prepared_path"
    fi

    if [ -d "$target_path" ] && diff -qr "$prepared_path" "$target_path" >/dev/null 2>&1; then
      printf 'unchanged  %s\n' "$package_name"
      unchanged=$((unchanged + 1))
      rm -rf "$prepared_path"
      continue
    fi

    if [ "$DRY_RUN" -eq 1 ]; then
      if [ -e "$target_path" ]; then
        printf 'would update  %s\n' "$package_name"
      else
        printf 'would install %s\n' "$package_name"
      fi
      rm -rf "$prepared_path"
      continue
    fi

    staging_path="$target_skills/.myskills-$package_name-$TIMESTAMP-$$"
    rm -rf "$staging_path"
    cp -R "$prepared_path" "$staging_path"
    rm -rf "$prepared_path"

    if [ -e "$target_path" ]; then
      mkdir -p "$backup_root"
      mv "$target_path" "$backup_root/$package_name"
      if ! mv "$staging_path" "$target_path"; then
        mv "$backup_root/$package_name" "$target_path"
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
    printf 'Dry run complete for %s; no files changed.\n' "$agent_label"
  else
    printf 'Done (%s): %s installed, %s updated, %s unchanged, %s skipped. Restart %s to reload skills.\n' \
      "$agent_label" "$installed" "$updated" "$unchanged" "$skipped" "$agent_label"
    if [ -d "$backup_root" ]; then
      printf 'Backup: %s\n' "$backup_root"
    fi
  fi
}

if [ "$TARGET" = "both" ]; then
  TARGETS="codex claude"
else
  TARGETS="$TARGET"
fi

if [ "$LIST_ONLY" -eq 1 ]; then
  for target in $TARGETS; do
    if [ "$TARGET" = "both" ]; then
      printf '# %s\n' "$target"
    fi
    list_packages "$target"
  done
  exit 0
fi

WORK_DIR=$(mktemp -d "${TMPDIR:-/tmp}/myskills-stage.XXXXXX")

for target in $TARGETS; do
  if [ "$TARGET" = "both" ]; then
    printf '# %s\n' "$target"
  fi
  install_target "$target"
done
