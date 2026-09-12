param(
    [ValidateSet("codex", "claude", "both")]
    [string]$Target = "codex",
    [switch]$All,
    [switch]$DryRun,
    [switch]$List
)

$ErrorActionPreference = "Stop"
$Repository = "Sevketcan/MySkills"
$Branch = "main"
$TemporaryRoot = $null
$WorkRoot = $null

# Packages that Claude Code already provides from another source. Installing them
# as personal skills would shadow or duplicate the existing copy, so they are
# skipped for the claude target unless -All is given.
$ClaudeSkip = @("fullstack-dev", "unity-skills")

function Get-TreeFingerprint([string]$Path) {
    $Separators = [char[]]@('\', '/')
    $Root = (Resolve-Path $Path).Path.TrimEnd($Separators)
    $Lines = Get-ChildItem -Path $Root -File -Recurse | Sort-Object FullName | ForEach-Object {
        $Relative = $_.FullName.Substring($Root.Length).TrimStart($Separators).Replace('\', '/')
        $Hash = (Get-FileHash -Algorithm SHA256 -Path $_.FullName).Hash
        "{0}`t{1}" -f $Relative, $Hash
    }
    $Payload = [Text.Encoding]::UTF8.GetBytes(($Lines -join "`n"))
    $Hasher = [Security.Cryptography.SHA256]::Create()
    try {
        return [BitConverter]::ToString($Hasher.ComputeHash($Payload)).Replace("-", "")
    }
    finally {
        $Hasher.Dispose()
    }
}

# Codex allows a trailing tilde in a package directory name; Claude Code requires
# lowercase letters, digits and hyphens only.
function Get-ClaudePackageName([string]$Name) {
    return $Name.TrimEnd('~')
}

# Rewrites a staged copy of a package into the form Claude Code expects:
#   * `allowed-tools` as a comma-separated string instead of a YAML list
#   * Codex skill-home paths pointed at the Claude skills directory
#   * Codex-only agent manifests dropped
function Convert-PackageForClaude([string]$PackageDir) {
    $Agents = Join-Path $PackageDir "agents"
    if (Test-Path $Agents) {
        Remove-Item -Path $Agents -Recurse -Force
    }

    Get-ChildItem -Path $PackageDir -File -Recurse -Filter "SKILL.md" | ForEach-Object {
        $Text = [IO.File]::ReadAllText($_.FullName)
        if ($Text -notmatch '(?m)^allowed-tools:[ \t]*$') { return }
        $Newline = if ($Text -match "`r`n") { "`r`n" } else { "`n" }
        $Lines = $Text -split "`r?`n"
        $Output = New-Object System.Collections.Generic.List[string]
        $Fence = 0
        $Collecting = $false
        $Tools = New-Object System.Collections.Generic.List[string]
        foreach ($Line in $Lines) {
            if ($Fence -lt 2 -and $Line -match '^---[ \t]*$') {
                if ($Collecting) {
                    $Output.Add("allowed-tools: " + ($Tools -join ", "))
                    $Collecting = $false
                    $Tools.Clear()
                }
                $Fence++
                $Output.Add($Line)
                continue
            }
            if ($Fence -eq 1 -and $Collecting -and $Line -match '^[ \t]*-[ \t]*(.+?)[ \t]*$') {
                $Tools.Add($Matches[1])
                continue
            }
            if ($Fence -eq 1 -and $Collecting) {
                $Output.Add("allowed-tools: " + ($Tools -join ", "))
                $Collecting = $false
                $Tools.Clear()
                $Output.Add($Line)
                continue
            }
            if ($Fence -eq 1 -and $Line -match '^allowed-tools:[ \t]*$') {
                $Collecting = $true
                continue
            }
            $Output.Add($Line)
        }
        [IO.File]::WriteAllText($_.FullName, ($Output -join $Newline))
    }

    Get-ChildItem -Path $PackageDir -File -Recurse -Filter "*.md" | ForEach-Object {
        $Text = [IO.File]::ReadAllText($_.FullName)
        if ($Text -notmatch 'CODEX_HOME|\.codex/skills') { return }
        $Text = $Text.Replace('${CODEX_HOME:-$HOME/.codex}', '${CLAUDE_CONFIG_DIR:-$HOME/.claude}')
        $Text = $Text.Replace('CODEX_HOME', 'CLAUDE_CONFIG_DIR')
        $Text = $Text.Replace('~/.codex/skills', '~/.claude/skills')
        $Text = $Text.Replace('.codex/skills', '.claude/skills')
        [IO.File]::WriteAllText($_.FullName, $Text)
    }
}

function Install-Target {
    param(
        [string]$Name,
        [System.IO.DirectoryInfo[]]$Packages,
        [string]$Timestamp,
        [string]$StagingRoot
    )

    if ($Name -eq "claude") {
        $AgentRoot = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $HOME ".claude" }
        $AgentLabel = "Claude Code"
    }
    else {
        $AgentRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
        $AgentLabel = "Codex"
    }

    $TargetSkills = Join-Path $AgentRoot "skills"
    $BackupRoot = Join-Path $AgentRoot "skill-backups/$Timestamp"
    $Installed = 0
    $Updated = 0
    $Unchanged = 0
    $Skipped = 0

    if (-not $DryRun) {
        New-Item -ItemType Directory -Force -Path $TargetSkills | Out-Null
    }

    foreach ($Package in $Packages) {
        $PackageName = $Package.Name
        if ($Name -eq "claude") {
            $PackageName = Get-ClaudePackageName $PackageName
            if ((-not $All) -and ($ClaudeSkip -contains $PackageName)) {
                Write-Output ("skipped    {0} (already provided to Claude)" -f $PackageName)
                $Skipped++
                continue
            }
        }

        $Target = Join-Path $TargetSkills $PackageName
        $Prepared = Join-Path (Join-Path $StagingRoot $Name) $PackageName
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Prepared) | Out-Null
        if (Test-Path $Prepared) { Remove-Item -Path $Prepared -Recurse -Force }
        Copy-Item -Path $Package.FullName -Destination $Prepared -Recurse
        if ($Name -eq "claude") {
            Convert-PackageForClaude $Prepared
        }

        if ((Test-Path $Target -PathType Container) -and
            (Get-TreeFingerprint $Prepared) -eq (Get-TreeFingerprint $Target)) {
            Write-Output ("unchanged  {0}" -f $PackageName)
            $Unchanged++
            Remove-Item -Path $Prepared -Recurse -Force
            continue
        }
        if ($DryRun) {
            $Action = if (Test-Path $Target) { "would update " } else { "would install" }
            Write-Output ("{0} {1}" -f $Action, $PackageName)
            Remove-Item -Path $Prepared -Recurse -Force
            continue
        }

        $Staging = Join-Path $TargetSkills (".myskills-{0}-{1}" -f $PackageName, [guid]::NewGuid().ToString("N"))
        Copy-Item -Path $Prepared -Destination $Staging -Recurse
        Remove-Item -Path $Prepared -Recurse -Force

        if (Test-Path $Target) {
            New-Item -ItemType Directory -Force -Path $BackupRoot | Out-Null
            $Backup = Join-Path $BackupRoot $PackageName
            Move-Item -Path $Target -Destination $Backup
            try {
                Move-Item -Path $Staging -Destination $Target
            }
            catch {
                Move-Item -Path $Backup -Destination $Target
                throw "Failed to update $PackageName; original restored. $($_.Exception.Message)"
            }
            Write-Output ("updated    {0}" -f $PackageName)
            $Updated++
        }
        else {
            Move-Item -Path $Staging -Destination $Target
            Write-Output ("installed  {0}" -f $PackageName)
            $Installed++
        }
    }

    if ($DryRun) {
        Write-Output ("Dry run complete for {0}; no files changed." -f $AgentLabel)
    }
    else {
        Write-Output ("Done ({0}): {1} installed, {2} updated, {3} unchanged, {4} skipped. Restart {0} to reload skills." -f $AgentLabel, $Installed, $Updated, $Unchanged, $Skipped)
        if (Test-Path $BackupRoot) {
            Write-Output ("Backup: {0}" -f $BackupRoot)
        }
    }
}

try {
    $SourceRoot = $PSScriptRoot
    if ([string]::IsNullOrWhiteSpace($SourceRoot) -or -not (Test-Path (Join-Path $SourceRoot "skills"))) {
        $TemporaryRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("myskills-" + [guid]::NewGuid().ToString("N"))
        New-Item -ItemType Directory -Path $TemporaryRoot | Out-Null
        $Archive = Join-Path $TemporaryRoot "repository.zip"
        Invoke-WebRequest "https://github.com/$Repository/archive/refs/heads/$Branch.zip" -OutFile $Archive
        Expand-Archive -Path $Archive -DestinationPath $TemporaryRoot
        $SourceRoot = Join-Path $TemporaryRoot "MySkills-$Branch"
    }

    $SourceSkills = Join-Path $SourceRoot "skills"
    if (-not (Test-Path $SourceSkills)) {
        throw "skills directory not found in source package."
    }

    $Timestamp = [DateTime]::UtcNow.ToString("yyyyMMddTHHmmssZ")
    $Packages = Get-ChildItem -Path $SourceSkills -Directory | Where-Object {
        Test-Path (Join-Path $_.FullName "SKILL.md")
    } | Sort-Object Name

    $Targets = if ($Target -eq "both") { @("codex", "claude") } else { @($Target) }

    if ($List) {
        foreach ($Name in $Targets) {
            if ($Target -eq "both") { Write-Output ("# {0}" -f $Name) }
            foreach ($Package in $Packages) {
                $PackageName = $Package.Name
                if ($Name -eq "claude") {
                    $PackageName = Get-ClaudePackageName $PackageName
                    if ((-not $All) -and ($ClaudeSkip -contains $PackageName)) {
                        Write-Output ("{0} (skipped: already provided to Claude; use -All to override)" -f $PackageName)
                        continue
                    }
                }
                Write-Output $PackageName
            }
        }
        return
    }

    $WorkRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("myskills-stage-" + [guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $WorkRoot | Out-Null

    foreach ($Name in $Targets) {
        if ($Target -eq "both") { Write-Output ("# {0}" -f $Name) }
        Install-Target -Name $Name -Packages $Packages -Timestamp $Timestamp -StagingRoot $WorkRoot
    }
}
finally {
    if ($TemporaryRoot -and (Test-Path $TemporaryRoot)) {
        Remove-Item -Path $TemporaryRoot -Recurse -Force
    }
    if ($WorkRoot -and (Test-Path $WorkRoot)) {
        Remove-Item -Path $WorkRoot -Recurse -Force
    }
}
