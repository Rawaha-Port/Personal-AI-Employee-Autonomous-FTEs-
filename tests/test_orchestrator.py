import unittest
import pathlib
import tempfile
import shutil
import json
import os
from unittest.mock import patch, MagicMock
from orchestrator import AIOrchestrator

class TestAIOrchestrator(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.vault_path = pathlib.Path(self.test_dir)
        (self.vault_path / "Needs_Action").mkdir()
        (self.vault_path / "Done").mkdir()
        (self.vault_path / "Rejected").mkdir()
        (self.vault_path / "Logs").mkdir()
        (self.vault_path / "Dashboard.md").write_text("status: online\n## 🕒 Recent Activity", encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_state_persistence(self):
        """T003: Verify state persistence logic (load/save)."""
        orch = AIOrchestrator(self.vault_path)
        orch.state["active_tasks"]["test_id"] = {"status": "thinking"}
        orch.save_state()
        
        # New instance should load the state
        orch2 = AIOrchestrator(self.vault_path)
        self.assertIn("test_id", orch2.state["active_tasks"])
        self.assertEqual(orch2.state["active_tasks"]["test_id"]["status"], "thinking")

    def test_task_discovery(self):
        """T004: Verify task discovery in /Needs_Action."""
        (self.vault_path / "Needs_Action" / "task1.md").touch()
        orch = AIOrchestrator(self.vault_path)
        orch.poll()
        self.assertIn("task1.md", orch.state["active_tasks"])
        self.assertEqual(orch.state["active_tasks"]["task1.md"]["status"], "pending")

    @patch("orchestrator.AIOrchestrator.invoke_agent")
    def test_task_processing_and_archival(self, mock_invoke):
        """T009, T011: Verify task processing and move to /Done."""
        task_file = self.vault_path / "Needs_Action" / "task1.md"
        task_file.write_text("Hello", encoding="utf-8")
        
        mock_invoke.return_value = {"stdout": "<promise>TASK_COMPLETE</promise>", "returncode": 0}
        
        orch = AIOrchestrator(self.vault_path)
        orch.poll()
        orch.process_tasks()
        
        # Should be moved to Done
        self.assertFalse((self.vault_path / "Needs_Action" / "task1.md").exists())
        self.assertTrue((self.vault_path / "Done" / "task1.md").exists())
        self.assertEqual(orch.state["active_tasks"]["task1.md"]["status"], "completed")

    @patch("orchestrator.AIOrchestrator.invoke_agent")
    def test_ralph_wiggum_loop(self, mock_invoke):
        """T010: Verify Ralph Wiggum loop logic (multi-step)."""
        task_file = self.vault_path / "Needs_Action" / "loop_task.md"
        task_file.write_text("Keep going", encoding="utf-8")
        
        # First call: no completion signal
        # Second call: completion signal
        mock_invoke.side_effect = [
            {"stdout": "Thinking...", "returncode": 0},
            {"stdout": "<promise>TASK_COMPLETE</promise>", "returncode": 0}
        ]
        
        orch = AIOrchestrator(self.vault_path)
        orch.poll()
        
        # Process once
        orch.process_tasks()
        self.assertEqual(orch.state["active_tasks"]["loop_task.md"]["iteration_count"], 1)
        self.assertEqual(orch.state["active_tasks"]["loop_task.md"]["status"], "thinking")
        self.assertTrue(task_file.exists())
        
        # Process again
        orch.process_tasks()
        self.assertEqual(orch.state["active_tasks"]["loop_task.md"]["iteration_count"], 2)
        self.assertEqual(orch.state["active_tasks"]["loop_task.md"]["status"], "completed")
        self.assertFalse(task_file.exists())

if __name__ == "__main__":
    unittest.main()
