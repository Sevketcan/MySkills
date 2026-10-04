import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('sync', Path(__file__).resolve().parents[1] / 'scripts/sync-local.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)
SKILL = b'---\nname: demo\ndescription: A demo skill.\nallowed-tools:\n  - Bash\n  - Read\n---\nUse $CODEX_HOME and ~/.codex/skills.\n'


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.roots = [root / name for name in ['repo', 'codex', 'claude']]
        self.state = root / 'state/local-sync.json'
        self.put(0, 'demo/SKILL.md', SKILL)

    def put(self, index, path, data):
        file = self.roots[index] / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(data)
        return file

    def run_sync(self, **kwargs):
        return sync.synchronize(*self.roots, self.state, **kwargs)

    def test_retired_package_is_not_imported_from_old_installation(self):
        self.put(1, 'game-feel/SKILL.md', SKILL.replace(b'name: demo', b'name: game-feel'))
        self.run_sync()
        self.assertFalse((self.roots[0] / 'game-feel').exists())
        self.assertFalse((self.roots[2] / 'game-feel').exists())
        # Excluding legacy copies is not permission to delete their contents.
        self.assertTrue((self.roots[1] / 'game-feel/SKILL.md').exists())
        self.assertEqual(self.run_sync(), 0)

    def test_retired_nested_entrypoint_is_not_restored_but_guide_is_shared(self):
        self.put(0, 'unity-skills~/SKILL.md', SKILL.replace(b'name: demo', b'name: unity-skills'))
        old = 'unity-skills~/skills/animator/SKILL.md'
        self.put(1, old, SKILL.replace(b'name: demo', b'name: unity-animator'))
        guide = 'unity-skills~/skills/animator/GUIDE.md'
        self.put(0, guide, b'# Animator API guide\n')
        self.run_sync()
        self.assertFalse((self.roots[0] / old).exists())
        self.assertEqual((self.roots[1] / guide).read_bytes(), b'# Animator API guide\n')
        self.assertEqual(self.run_sync(), 0)

    def test_creation_both_directions_and_idempotency(self):
        self.run_sync()
        self.assertIn(b'CLAUDE_CONFIG_DIR', (self.roots[2] / 'demo/SKILL.md').read_bytes())
        self.put(2, 'from-claude/SKILL.md', SKILL.replace(b'name: demo', b'name: from-claude'))
        self.put(1, 'from-codex/SKILL.md', SKILL.replace(b'name: demo', b'name: from-codex'))
        self.run_sync()
        for root in self.roots:
            self.assertTrue((root / 'from-claude/SKILL.md').exists())
            self.assertTrue((root / 'from-codex/SKILL.md').exists())
        self.assertEqual(self.run_sync(), 0)

    def test_edit_from_claude_and_backup(self):
        self.run_sync()
        f = self.roots[2] / 'demo/SKILL.md'
        f.write_bytes(f.read_bytes() + b'Claude edit\n')
        self.run_sync()
        self.assertIn(b'Claude edit', (self.roots[1] / 'demo/SKILL.md').read_bytes())
        self.assertTrue(list(self.state.parent.glob('backups/*/1/demo/SKILL.md')))
        self.assertEqual(self.run_sync(), 0)

    def test_edit_from_codex(self):
        self.run_sync()
        file = self.roots[1] / 'demo/SKILL.md'
        file.write_bytes(file.read_bytes() + b'Codex edit\n')
        self.run_sync()
        self.assertIn(b'Codex edit', (self.roots[2] / 'demo/SKILL.md').read_bytes())
        self.assertEqual(self.run_sync(), 0)

    def test_independent_file_edits_merge(self):
        self.run_sync()
        self.put(1, 'demo/a.txt', b'Codex')
        self.put(2, 'demo/b.txt', b'Claude')
        self.run_sync()
        for root in self.roots:
            self.assertEqual((root / 'demo/a.txt').read_bytes(), b'Codex')
            self.assertEqual((root / 'demo/b.txt').read_bytes(), b'Claude')

    def test_conflicts_do_not_write(self):
        self.run_sync()
        original_state = self.state.read_bytes()
        self.put(1, 'demo/a.txt', b'Codex')
        self.put(2, 'demo/a.txt', b'Claude')
        with self.assertRaisesRegex(ValueError, 'Conflicting'):
            self.run_sync()
        self.assertFalse((self.roots[0] / 'demo/a.txt').exists())
        self.assertEqual(self.state.read_bytes(), original_state)

    def test_deletions_restore(self):
        self.run_sync()
        (self.roots[2] / 'demo/SKILL.md').unlink()
        self.run_sync()
        self.assertTrue((self.roots[2] / 'demo/SKILL.md').exists())

    def test_bootstrap_backs_up_divergent_claude(self):
        self.put(2, 'demo/SKILL.md', SKILL + b'Old copy')
        with self.assertRaises(ValueError):
            self.run_sync()
        self.run_sync(bootstrap=True)
        self.assertNotIn(b'Old copy', (self.roots[2] / 'demo/SKILL.md').read_bytes())
        self.assertTrue(list(self.state.parent.glob('backups/*/2/demo/SKILL.md')))

    def test_invalid_and_secret_files_do_not_write(self):
        self.put(2, 'bad/SKILL.md', b'Invalid')
        with self.assertRaises(ValueError):
            self.run_sync()
        self.assertFalse(self.state.exists())
        (self.roots[2] / 'bad/SKILL.md').unlink()
        self.put(0, 'demo/key.txt', b'sk-' + b'A' * 30)
        with self.assertRaisesRegex(ValueError, 'credential'):
            self.run_sync()
        self.assertFalse((self.roots[1] / 'demo/key.txt').exists())

    def test_secret_detector_ignores_word_suffix(self):
        self.put(0, 'demo/topics.json', b'lattice-operators-mask-operators-reference-topic')
        self.run_sync()

    def test_dry_run(self):
        self.run_sync(dry_run=True)
        self.assertFalse(self.state.exists())
        self.assertFalse(self.roots[1].exists())

    def test_alias_and_claude_exceptions(self):
        self.put(0, 'unity-skills~/SKILL.md', SKILL.replace(b'name: demo', b'name: unity-skills'))
        self.put(2, 'unity-skills/SKILL.md', b'External copy stays intact')
        self.put(0, 'demo/agents/openai.yaml', b'Codex only')
        self.run_sync()
        self.assertEqual((self.roots[2] / 'unity-skills/SKILL.md').read_bytes(), b'External copy stays intact')
        self.assertFalse((self.roots[2] / 'demo/agents/openai.yaml').exists())

    def test_literal_claude_paths_preserved_when_editing(self):
        content = SKILL + b'Example Claude path: ~/.claude/skills/example\n'
        self.put(0, 'demo/SKILL.md', content)
        self.run_sync()
        file = self.roots[2] / 'demo/SKILL.md'
        file.write_bytes(file.read_bytes() + b'New instruction\n')
        self.run_sync()
        self.assertEqual((self.roots[0] / 'demo/SKILL.md').read_bytes(), content + b'New instruction\n')
        self.assertEqual(self.run_sync(), 0)

    def test_file_mode(self):
        file = self.put(0, 'demo/run.sh', b'#!/bin/sh\n')
        file.chmod(0o755)
        self.run_sync()
        self.assertEqual((self.roots[2] / 'demo/run.sh').stat().st_mode & 0o777, 0o755)


if __name__ == '__main__':
    unittest.main()
