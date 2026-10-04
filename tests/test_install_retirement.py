"""Upgrade behavior must preserve retired user files and respect dry-run."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]

class RetirementInstallTests(unittest.TestCase):
    def test_dry_run_backup_and_repeat_install_both_agents(self):
        with tempfile.TemporaryDirectory() as tmp:
            roots = [Path(tmp) / 'codex', Path(tmp) / 'claude']
            packages = json.loads((REPO / 'retired-skills.json').read_text())['packages']
            env = dict(os.environ, CODEX_HOME=str(roots[0]), CLAUDE_CONFIG_DIR=str(roots[1]))
            for root in roots:
                for package in packages:
                    file = root / 'skills' / package / 'custom.md'
                    file.parent.mkdir(parents=True)
                    file.write_text('preserve my edits')
            expected = len(list((REPO / 'skills').glob('*/SKILL.md')))
            command = ['bash', str(REPO / 'install.sh'), '--target', 'both', '--all']
            subprocess.run(command + ['--dry-run'], env=env, check=True, capture_output=True)
            self.assertTrue(all((r / 'skills' / p / 'custom.md').exists() for r in roots for p in packages))
            subprocess.run(command, env=env, check=True, capture_output=True)
            for root in roots:
                for package in packages:
                    self.assertFalse((root / 'skills' / package).exists())
                    backups = list((root / 'skill-backups').glob('*/' + package + '/custom.md'))
                    self.assertEqual(len(backups), 1)
                    self.assertEqual(backups[0].read_text(), 'preserve my edits')
                self.assertEqual(len(list((root / 'skills').rglob('SKILL.md'))), expected)
            repeat = subprocess.run(command, env=env, check=True, capture_output=True, text=True)
            self.assertEqual(repeat.stdout.count(f'{expected} unchanged'), 2)
