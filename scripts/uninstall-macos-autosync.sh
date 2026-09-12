#!/usr/bin/env bash
set -euo pipefail

LABEL="com.sevketcan.myskills-autosync"
PLIST_PATH="${HOME}/Library/LaunchAgents/$LABEL.plist"
domain="gui/$(id -u)"

launchctl bootout "$domain/$LABEL" >/dev/null 2>&1 || true
if [ -f "$PLIST_PATH" ]; then
  rm -f "$PLIST_PATH"
fi
printf 'MySkills auto-sync disabled. Validator state was kept under: %s\n' \
  "${HOME}/Library/Application Support/MySkills"

