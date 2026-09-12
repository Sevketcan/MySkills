#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=0
PRUNE=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --prune) PRUNE=1 ;;
    -h|--help)
      printf '%s\n' 'Usage: export-local.sh [--dry-run] [--prune]'
      exit 0
      ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; exit 2 ;;
  esac
  shift
done

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
REPOSITORY_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODEX_ROOT="${CODEX_HOME:-${HOME}/.codex}"
SOURCE_SKILLS="$CODEX_ROOT/skills"
TARGET_SKILLS="$REPOSITORY_ROOT/skills"

[ -d "$SOURCE_SKILLS" ] || {
  printf 'Codex skills directory not found: %s\n' "$SOURCE_SKILLS" >&2
  exit 1
}
command -v rsync >/dev/null 2>&1 || {
  printf 'rsync is required for export.\n' >&2
  exit 1
}

mkdir -p "$TARGET_SKILLS"
rsync_args=(
  -a
  --exclude '.system/'
  --exclude '.git/'
  --exclude 'evals/'
  --exclude '__pycache__/'
  --exclude '*.pyc'
  --exclude '.DS_Store'
  --exclude '.env'
  --exclude '.env.local'
  --exclude '*.pem'
  --exclude '*.key'
  --exclude '*credentials*'
)
if [ "$DRY_RUN" -eq 1 ]; then
  rsync_args+=(--dry-run --itemize-changes)
fi
if [ "$PRUNE" -eq 1 ]; then
  rsync_args+=(--delete)
fi

rsync "${rsync_args[@]}" "$SOURCE_SKILLS/" "$TARGET_SKILLS/"

if [ "$DRY_RUN" -eq 0 ]; then
  python3 "$SCRIPT_DIR/build_manifest.py"
  git -C "$REPOSITORY_ROOT" status --short
else
  printf 'Dry run complete; no files changed.\n'
fi
