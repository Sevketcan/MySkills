# MySkills

Portable Codex skill collection maintained for the `Sevketcan` setup. The repository contains only user-installed skills; Codex system skills and plugin caches are intentionally excluded.

## Install everything

macOS or Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/Sevketcan/MySkills/main/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/Sevketcan/MySkills/main/install.ps1 | iex
```

Both installers place packages under `$CODEX_HOME/skills` or, when `CODEX_HOME` is unset, the standard `~/.codex/skills` directory. Existing packages with the same name are moved to a timestamped `skill-backups` directory before replacement. Skills that are not part of this repository are left untouched.

Restart Codex after installation so the new skill catalog is loaded.

## Inspect before installing

Clone the repository and use the dry-run mode:

```bash
git clone https://github.com/Sevketcan/MySkills.git
cd MySkills
./install.sh --list
./install.sh --dry-run
./install.sh
```

PowerShell equivalents:

```powershell
git clone https://github.com/Sevketcan/MySkills.git
Set-Location MySkills
.\install.ps1 -List
.\install.ps1 -DryRun
.\install.ps1
```

The deterministic [manifest.json](manifest.json) records every top-level package and every nested skill entry point.

Every push is checked by GitHub Actions for valid Codex frontmatter, unique skill names, a current manifest, script syntax, and repeatable installation into a clean Codex directory.

## Maintain the collection

On the primary machine, refresh the repository from the active Codex installation:

```bash
./scripts/export-local.sh
python3 ./scripts/build_manifest.py
git diff --stat
```

`export-local.sh` skips `.system`, evaluation fixtures, caches, local environment files, credentials, and private-key files. It does not remove repository packages that disappeared locally unless `--prune` is supplied. Review the diff and source/license implications before committing.

### Automatic sync on macOS

Install the background sync once:

```bash
./scripts/install-macos-autosync.sh
```

The launch agent reacts to changes under `~/.codex/skills` and also checks every five minutes. When exported content changes, it validates all skills, rebuilds the manifest, scans for common credential formats, commits only `skills/` and `manifest.json`, and pushes to `origin/main`.

It never force-pushes or pulls through a conflict. A staged change, failed validation, detected secret, non-`main` branch, or remote-ahead state stops the run and is recorded in:

```text
~/Library/Logs/MySkills-autosync.log
~/Library/Logs/MySkills-autosync-error.log
```

Disable it with:

```bash
./scripts/uninstall-macos-autosync.sh
```

## Sources and licenses

This is a mixed-license collection. Each upstream package remains subject to its original license:

- Most standalone Unity packages originated from [Unity-Technologies/skills](https://github.com/Unity-Technologies/skills) and use the Unity Companion License.
- `unity-skills~` originated from [Besty0728/Unity-Skills](https://github.com/Besty0728/Unity-Skills), MIT licensed, with local integration changes documented in its files.
- `gdd-studio` adapts MIT-licensed ideas from [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios).
- `game-balance-lab` records its source acknowledgements in `skills/game-balance-lab/references/source-and-license.md`.
- `playwright` ships its own `LICENSE.txt` and `NOTICE.txt`.
- `fullstack-dev` is a personal package maintained in this repository.

Copies of the collection-level upstream notices are kept under `third_party/`. Redistribution here does not replace or broaden those licenses.
