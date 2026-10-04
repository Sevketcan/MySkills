# MySkills

Portable skill collection maintained for the `Sevketcan` setup, installable into both Codex and Claude Code. The repository contains only user-installed skills; Codex system skills and plugin caches are intentionally excluded.

## Skill layout after the October 2026 review

The personal collection has **43 packages and 43 discoverable entry points**, down from 48 packages and 137 entry points. Unity and Blender module documents are `GUIDE.md` references routed through their parent skill, rather than independent skills. Five general game-programming cookbooks now live under `skills/gdd-studio/references/engine-neutral/`.

See [the audit](docs/skill-audit-2026-10-04.md) for decisions, measured inventory changes and remaining plugin overlaps. The reduction measures catalog size, not an established improvement in model task performance.

For an existing installation, run the local installer with `--target both --all` (`-Target both -All` on Windows). It replaces package trees, backs up the five former standalone packages outside the skill catalog, and refreshes Claude's normally skipped Unity/full-stack copies. Restart both agents afterward. `retired-skills.json` prevents old package/entry-point copies from being imported again by sync or export; it does not silently delete files from other machines. Install the update before using an older installation.

## Install everything

macOS or Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/Sevketcan/MySkills/main/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/Sevketcan/MySkills/main/install.ps1 | iex
```

Both installers default to Codex and place packages under `$CODEX_HOME/skills` or, when `CODEX_HOME` is unset, the standard `~/.codex/skills` directory. Existing packages with the same name are moved to a timestamped `skill-backups` directory before replacement. Skills that are not part of this repository are left untouched.

Restart Codex after installation so the new skill catalog is loaded.

## Install into Claude Code

The same packages install as Claude Code personal skills:

```bash
./install.sh --target claude          # ~/.claude/skills (or $CLAUDE_CONFIG_DIR/skills)
./install.sh --target both            # Codex and Claude Code in one run
```

```powershell
.\install.ps1 -Target claude
.\install.ps1 -Target both
```

Codex and Claude Code read the same `SKILL.md` format, so the packages are copied verbatim except for three adjustments the installer makes on the way into the Claude skills directory:

| Adjustment | Reason |
| --- | --- |
| `allowed-tools` YAML lists are rewritten as `allowed-tools: Bash, Read` | Claude Code expects a comma-separated string |
| `unity-skills~` is installed as `unity-skills` | Claude Code skill directories may not contain a tilde |
| `$CODEX_HOME`/`~/.codex/skills` references become `$CLAUDE_CONFIG_DIR`/`~/.claude/skills`, and Codex-only `agents/` manifests are dropped | the paths must resolve inside the Claude installation |

The repository files themselves stay in their Codex form; the rewrite happens in a staging copy, so `--target both` keeps each installation correct.

`fullstack-dev` and `unity-skills` are skipped for the Claude target because Claude Code already provides them from another source. Pass `--all` (PowerShell: `-All`) to install them anyway; the existing copies are moved into `~/.claude/skill-backups/<timestamp>` first.

Restart Claude Code, or run `/doctor` in an interactive session, to reload the skill catalog.

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

Every push is checked by GitHub Actions for valid frontmatter, unique skill names, descriptions within the Claude Code length limit, package names that are installable under both agents, a current manifest, script syntax, and repeatable installation into clean Codex and Claude directories.

## Single source and project profiles

See [the maintenance workflow](docs/skill-maintenance.md) for source selection, opt-in project profiles, new-skill admission and paired Codex/Claude trials.

After installing personal skills, preview and apply the Unity source selection with Python 3.11+:

    python3 scripts/configure-skill-sources.py
    python3 scripts/configure-skill-sources.py --apply

This writes backed-up per-skill overrides; it keeps the Unity plugin enabled, preserves its six unique skills and leaves MCP settings untouched. Run it again after plugin updates, then restart Codex. Claude currently has no Unity plugin installed, so its personal packages already supply one source.

New entry points need evidence and positive/negative trigger examples in skill-reviews.json. Project preferences are opt-in templates bundled in fullstack-dev rather than defaults for every app.

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

The launch agent now synchronizes personal skills in **both directions** between
`~/.codex/skills`, `~/.claude/skills`, and this repository, then validates, commits,
and pushes changes to `origin/main`. It watches both directories and checks every
five minutes (including edits inside existing packages).

On first setup the installer bootstraps from the repository/Codex copies, imports
Claude-only packages and files, and backs up any overwritten Claude files. If the
repository and Codex disagree, setup stops for manual reconciliation. Later runs
remember the last synchronized content and detect which side changed each file.
Different files can change on different sides; divergent edits to the same file
stop the entire run without writing files. Resolve by making the conflicting
copies identical, then run the sync again.

Claude path references and `allowed-tools` formatting are converted automatically.
Codex-only `agents/` files stay in Codex and the repository. Claude's separately
provided `fullstack-dev` and `unity-skills` remain excluded from sharing. System
skills, plugin caches, evaluation artifacts, environment files and private keys
are excluded. Removing a file from one side restores it from another; automatic
sync does not propagate deletions. For arbitrary removals, stop the agent and remove
them from all three locations before restarting. The reviewed retirements in
`retired-skills.json` are excluded from sync/export and archived by the installer.

Local synchronization can also be run without Git operations (requires PyYAML):

```bash
"$HOME/Library/Application Support/MySkills/venv/bin/python" scripts/sync-local.py --dry-run
"$HOME/Library/Application Support/MySkills/venv/bin/python" scripts/sync-local.py
```

The baseline and backups live under
`~/Library/Application Support/MySkills/` (`local-sync.json` and `backups/`).
`CODEX_HOME` and `CLAUDE_CONFIG_DIR` support custom locations; the installer saves
both for the background agent. `MYSKILLS_STATE_ROOT` can isolate a manual test's
baseline and backups. Never reuse a baseline with different roots.

A staged change, invalid skill, credential match, conflict, non-`main` branch, or
remote-ahead state stops the background run. It never force-pushes or pulls through
a conflict. Logs are recorded in:

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
- `threejs-game-director`, its eight sibling `threejs-*` skills, and their templates originated from [majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills) at commit `e5f301d548bb18c530afbece78cd25082f4cda9c`, MIT licensed. The image, 3D, and audio generators use their respective third-party APIs only when explicitly requested and configured with a user-provided key.
- The optional `game-ui-ux`, `game-feel`, `input-systems`, `save-systems`, and `procedural-gen` cookbooks under `gdd-studio/references/engine-neutral/` originated from [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) at commit `b105e1cf617adf0b68ed98790a716bbb60993179`, Apache-2.0 licensed.
- `playwright` ships its own `LICENSE.txt` and `NOTICE.txt`.
- `fullstack-dev` is a personal package maintained in this repository.

Copies of the collection-level upstream notices are kept under `third_party/`. Redistribution here does not replace or broaden those licenses.
