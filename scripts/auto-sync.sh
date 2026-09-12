#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
REPOSITORY_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
STATE_ROOT="${MYSKILLS_STATE_ROOT:-${HOME}/Library/Application Support/MySkills}"
VALIDATOR_PYTHON="${MYSKILLS_VALIDATOR_PYTHON:-$STATE_ROOT/venv/bin/python}"
LOCK_DIR="$STATE_ROOT/sync.lock"
BRANCH="main"

mkdir -p "$STATE_ROOT"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  exit 0
fi
cleanup() {
  rmdir "$LOCK_DIR" 2>/dev/null || true
}
trap cleanup EXIT

log() {
  printf '[%s] %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*"
}

cd "$REPOSITORY_ROOT"

if [ ! -x "$VALIDATOR_PYTHON" ]; then
  log "validator environment missing; run scripts/install-macos-autosync.sh"
  exit 1
fi
if [ "$(git branch --show-current)" != "$BRANCH" ]; then
  log "stopped: repository is not on $BRANCH"
  exit 1
fi
if ! git diff --cached --quiet; then
  log "stopped: repository already has staged changes"
  exit 1
fi

git fetch --quiet origin "$BRANCH"
read -r ahead behind < <(git rev-list --left-right --count "HEAD...origin/$BRANCH")
if [ "$behind" -gt 0 ]; then
  log "stopped: origin/$BRANCH is ahead by $behind commit(s); pull/reconcile manually"
  exit 1
fi

"$SCRIPT_DIR/export-local.sh" >/dev/null
"$VALIDATOR_PYTHON" "$SCRIPT_DIR/validate_collection.py" >/dev/null
python3 "$SCRIPT_DIR/build_manifest.py" >/dev/null

git add -- skills manifest.json

SECRET_PATTERN='(gh[opusr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY)'
if git grep --cached -I -E -q "$SECRET_PATTERN" -- skills; then
  git restore --staged -- skills manifest.json
  log "stopped: a possible credential or private key was detected"
  exit 1
fi

if ! git diff --cached --quiet; then
  timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  git commit --quiet -m "Sync Codex skills $timestamp"
  ahead=$((ahead + 1))
  log "committed skill changes"
fi

if [ "$ahead" -gt 0 ]; then
  git push --quiet origin "$BRANCH"
  log "pushed $ahead commit(s) to origin/$BRANCH"
else
  log "no skill changes"
fi

