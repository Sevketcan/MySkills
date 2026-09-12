param(
    [switch]$DryRun,
    [switch]$List
)

$ErrorActionPreference = "Stop"
$Repository = "Sevketcan/MySkills"
$Branch = "main"
$TemporaryRoot = $null

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

    $CodexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
    $TargetSkills = Join-Path $CodexRoot "skills"
    $Timestamp = [DateTime]::UtcNow.ToString("yyyyMMddTHHmmssZ")
    $BackupRoot = Join-Path $CodexRoot "skill-backups/$Timestamp"
    $Packages = Get-ChildItem -Path $SourceSkills -Directory | Where-Object {
        Test-Path (Join-Path $_.FullName "SKILL.md")
    } | Sort-Object Name

    if ($List) {
        $Packages.Name
        return
    }

    New-Item -ItemType Directory -Force -Path $TargetSkills | Out-Null
    $Installed = 0
    $Updated = 0

    foreach ($Package in $Packages) {
        $Target = Join-Path $TargetSkills $Package.Name
        if ($DryRun) {
            $Action = if (Test-Path $Target) { "would update " } else { "would install" }
            Write-Output ("{0} {1}" -f $Action, $Package.Name)
            continue
        }

        $Staging = Join-Path $TargetSkills (".myskills-{0}-{1}" -f $Package.Name, [guid]::NewGuid().ToString("N"))
        Copy-Item -Path $Package.FullName -Destination $Staging -Recurse

        if (Test-Path $Target) {
            New-Item -ItemType Directory -Force -Path $BackupRoot | Out-Null
            $Backup = Join-Path $BackupRoot $Package.Name
            Move-Item -Path $Target -Destination $Backup
            try {
                Move-Item -Path $Staging -Destination $Target
            }
            catch {
                Move-Item -Path $Backup -Destination $Target
                throw "Failed to update $($Package.Name); original restored. $($_.Exception.Message)"
            }
            Write-Output ("updated    {0}" -f $Package.Name)
            $Updated++
        }
        else {
            Move-Item -Path $Staging -Destination $Target
            Write-Output ("installed  {0}" -f $Package.Name)
            $Installed++
        }
    }

    if ($DryRun) {
        Write-Output "Dry run complete; no files changed."
    }
    else {
        Write-Output ("Done: {0} installed, {1} updated. Restart Codex to reload skills." -f $Installed, $Updated)
        if (Test-Path $BackupRoot) {
            Write-Output ("Backup: {0}" -f $BackupRoot)
        }
    }
}
finally {
    if ($TemporaryRoot -and (Test-Path $TemporaryRoot)) {
        Remove-Item -Path $TemporaryRoot -Recurse -Force
    }
}

