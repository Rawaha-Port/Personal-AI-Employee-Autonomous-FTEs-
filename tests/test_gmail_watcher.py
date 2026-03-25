import unittest
import pathlib
import tempfile
import shutil
import os
from watchers.gmail_watcher import GmailWatcher

class TestGmailWatcher(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.vault_path = pathlib.Path(self.test_dir)
        (self.vault_path / "Logs").mkdir()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_initialization(self):
        """T002: Verify watcher initialization and directory creation."""
        watcher = GmailWatcher(self.vault_path)
        self.assertTrue(watcher.needs_action_dir.is_dir())
        self.assertTrue(watcher.logs_dir.is_dir())

if __name__ == "__main__":
    unittest.main()
