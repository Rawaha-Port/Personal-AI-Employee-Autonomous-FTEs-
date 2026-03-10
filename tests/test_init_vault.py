import unittest
import pathlib
import tempfile
import shutil
import os
from init_vault import DIRECTORIES, main as init_main

class TestVaultInit(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.vault_path = pathlib.Path(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def run_init(self, args=None):
        if args is None:
            args = [str(self.vault_path)]
        else:
            args = [str(self.vault_path)] + args
        
        # Mock sys.argv
        import sys
        old_argv = sys.argv
        sys.argv = ["init_vault.py"] + args
        try:
            init_main()
        finally:
            sys.argv = old_argv

    def test_directory_creation(self):
        """T009: Verify all mandatory directories are created."""
        self.run_init()
        for folder in DIRECTORIES:
            folder_path = self.vault_path / folder
            self.assertTrue(folder_path.is_dir(), f"Directory {folder} was not created")

    def test_file_creation(self):
        """T010: Verify all core markdown files are created."""
        self.run_init()
        core_files = ["Dashboard.md", "Company_Handbook.md", "Business_Goals.md", "README.md"]
        for file in core_files:
            file_path = self.vault_path / file
            self.assertTrue(file_path.is_file(), f"File {file} was not created")

    def test_file_content_headers(self):
        """T011: Verify file content and frontmatter headers."""
        self.run_init()
        
        # Check Dashboard.md
        dashboard_content = (self.vault_path / "Dashboard.md").read_text()
        self.assertIn("type: dashboard", dashboard_content)
        self.assertIn("# 🚀 AI Employee Dashboard", dashboard_content)

        # Check Handbook.md
        handbook_content = (self.vault_path / "Company_Handbook.md").read_text()
        self.assertIn("type: handbook", handbook_content)
        self.assertIn("# 📖 Company Handbook", handbook_content)

if __name__ == "__main__":
    unittest.main()
