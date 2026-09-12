#!/usr/bin/env bash
set -euo pipefail

if [ "$(uname -s)" != "Darwin" ]; then
  printf 'This installer is for macOS launchd.\n' >&2
  exit 1
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
REPOSITORY_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
LABEL="com.sevketcan.myskills-autosync"
STATE_ROOT="${HOME}/Library/Application Support/MySkills"
LOG_ROOT="${HOME}/Library/Logs"
PLIST_PATH="${HOME}/Library/LaunchAgents/$LABEL.plist"
CODEX_ROOT="${CODEX_HOME:-${HOME}/.codex}"
INTERVAL="${MYSKILLS_INTERVAL:-300}"

case "$INTERVAL" in
  ''|*[!0-9]*) printf 'MYSKILLS_INTERVAL must be an integer number of seconds.\n' >&2; exit 2 ;;
esac
if [ "$INTERVAL" -lt 60 ]; then
  printf 'MYSKILLS_INTERVAL must be at least 60 seconds.\n' >&2
  exit 2
fi

command -v python3 >/dev/null 2>&1 || {
  printf 'python3 is required.\n' >&2
  exit 1
}

mkdir -p "$STATE_ROOT" "$LOG_ROOT" "${HOME}/Library/LaunchAgents"
if [ ! -x "$STATE_ROOT/venv/bin/python" ]; then
  python3 -m venv "$STATE_ROOT/venv"
fi
"$STATE_ROOT/venv/bin/python" -m pip install --quiet --disable-pip-version-check PyYAML==6.0.2

REPOSITORY_ROOT="$REPOSITORY_ROOT" \
LABEL="$LABEL" \
PLIST_PATH="$PLIST_PATH" \
CODEX_SKILLS="$CODEX_ROOT/skills" \
INTERVAL="$INTERVAL" \
LOG_ROOT="$LOG_ROOT" \
python3 - <<'PY'
import os
import plistlib
from pathlib import Path

payload = {
    "Label": os.environ["LABEL"],
    "ProgramArguments": [
        "/bin/bash",
        str(Path(os.environ["REPOSITORY_ROOT"]) / "scripts" / "auto-sync.sh"),
    ],
    "WorkingDirectory": os.environ["REPOSITORY_ROOT"],
    "RunAtLoad": True,
    "StartInterval": int(os.environ["INTERVAL"]),
    "WatchPaths": [os.environ["CODEX_SKILLS"]],
    "ProcessType": "Background",
    "StandardOutPath": str(Path(os.environ["LOG_ROOT"]) / "MySkills-autosync.log"),
    "StandardErrorPath": str(Path(os.environ["LOG_ROOT"]) / "MySkills-autosync-error.log"),
}
with Path(os.environ["PLIST_PATH"]).open("wb") as handle:
    plistlib.dump(payload, handle, sort_keys=True)
PY

domain="gui/$(id -u)"
launchctl bootout "$domain/$LABEL" >/dev/null 2>&1 || true
launchctl bootstrap "$domain" "$PLIST_PATH"
launchctl kickstart -k "$domain/$LABEL"

printf 'MySkills auto-sync installed.\n'
printf 'Interval: %s seconds, plus directory-change triggers.\n' "$INTERVAL"
printf 'Log: %s/MySkills-autosync.log\n' "$LOG_ROOT"
printf 'Errors: %s/MySkills-autosync-error.log\n' "$LOG_ROOT"

