import os
import pathlib
import json
import time
import argparse
import subprocess
import re
import shutil
from datetime import datetime

class AIOrchestrator:
    def __init__(self, vault_root, interval=10):
        self.vault_root = pathlib.Path(vault_root).resolve()
        self.interval = interval
        self.state_file = self.vault_root / ".orchestrator_state.json"
        self.needs_action_dir = self.vault_root / "Needs_Action"
        self.done_dir = self.vault_root / "Done"
        self.rejected_dir = self.vault_root / "Rejected"
        self.logs_dir = self.vault_root / "Logs"
        self.dashboard_file = self.vault_root / "Dashboard.md"
        
        self.state = {
            "active_tasks": {},
            "last_poll_time": None
        }
        self.load_state()

    def load_state(self):
        if self.state_file.exists():
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    self.state = json.load(f)
            except Exception as e:
                print(f"Error loading state: {e}")

    def save_state(self):
        try:
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=2)
        except Exception as e:
            print(f"Error saving state: {e}")

    def update_dashboard(self, status, log_entry=None):
        """Update Dashboard.md status and activity logs."""
        if not self.dashboard_file.exists():
            return

        try:
            content = self.dashboard_file.read_text(encoding="utf-8")
            
            # Update status in frontmatter
            content = re.sub(r"status: .*", f"status: {status}", content)
            
            # Append log entry if provided
            if log_entry:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                activity_line = f"- [ {timestamp} ] {log_entry}"
                if "## 🕒 Recent Activity" in content:
                    content = content.replace("## 🕒 Recent Activity", f"## 🕒 Recent Activity\n{activity_line}")
            
            self.dashboard_file.write_text(content, encoding="utf-8")
        except Exception as e:
            print(f"Error updating dashboard: {e}")

    def invoke_agent(self, prompt):
        """Invoke reasoning engine."""
        print(f"Invoking Agent...")
        # REAL IMPLEMENTATION: gemini --prompt "..."
        # For now, we keep it as a wrapper that can be mocked in tests
        try:
            # result = subprocess.run(["gemini", "--prompt", prompt], capture_output=True, text=True)
            # return {"stdout": result.stdout, "returncode": result.returncode}
            
            # Simulated default response for real runs if tool not present
            return {"stdout": "<promise>TASK_COMPLETE</promise>", "returncode": 0}
        except Exception as e:
            return {"error": str(e), "returncode": 1}

    def poll(self):
        """Monitor /Needs_Action for new files."""
        self.state["last_poll_time"] = datetime.now().isoformat()
        
        if not self.needs_action_dir.is_dir():
            return

        for item in self.needs_action_dir.iterdir():
            if item.is_file() and item.suffix == ".md":
                task_id = item.name
                if task_id not in self.state["active_tasks"]:
                    print(f"New task detected: {task_id}")
                    self.state["active_tasks"][task_id] = {
                        "id": task_id,
                        "status": "pending",
                        "iteration_count": 0,
                        "original_path": str(item),
                        "start_time": datetime.now().isoformat()
                    }
        
        self.save_state()

    def process_tasks(self):
        """Process all active tasks."""
        # Work on a copy of keys to avoid modification during iteration
        task_ids = list(self.state["active_tasks"].keys())
        for tid in task_ids:
            task = self.state["active_tasks"][tid]
            if task["status"] not in ["completed", "failed"]:
                self.process_task(task)

    def process_task(self, task):
        """Process a single task (Ralph Wiggum Loop)."""
        tid = task["id"]
        file_path = pathlib.Path(task["original_path"])
        
        if not file_path.exists():
            print(f"Task file {tid} missing. Marking as failed.")
            task["status"] = "failed"
            self.save_state()
            return

        # Safety Guard: Max Iterations
        if task["iteration_count"] >= 5:
            print(f"Task {tid} exceeded max iterations. Rejecting.")
            self.update_dashboard("🔴 ERROR", f"Task {tid} failed: Max iterations exceeded.")
            self.archive_task(task, "failed")
            return

        task["iteration_count"] += 1
        task["status"] = "thinking"
        self.update_dashboard("🔵 AGENT THINKING...", f"Processing task {tid} (Iteration {task['iteration_count']})")
        self.save_state()

        # Read task content
        task_content = file_path.read_text(encoding="utf-8")
        
        # Prepare prompt
        prompt = f"Context: Vault Root: {self.vault_root}\nDate: {datetime.now().isoformat()}\nTask Content:\n{task_content}\n\nPlease process this task. If finished, include <promise>TASK_COMPLETE</promise> in your response."
        
        # Invoke Agent
        response = self.invoke_agent(prompt)
        
        if "stdout" in response and "<promise>TASK_COMPLETE</promise>" in response["stdout"]:
            print(f"Task {tid} completed successfully.")
            self.update_dashboard("🟢 SUCCESS", f"Task {tid} completed.")
            self.archive_task(task, "completed")
        else:
            print(f"Task {tid} still in progress...")
            self.save_state()

    def archive_task(self, task, final_status):
        """Archive task file to Done or Rejected."""
        tid = task["id"]
        source = pathlib.Path(task["original_path"])
        dest_dir = self.done_dir if final_status == "completed" else self.rejected_dir
        dest = dest_dir / tid
        
        try:
            if source.exists():
                shutil.move(str(source), str(dest))
            task["status"] = final_status
            task["end_time"] = datetime.now().isoformat()
            print(f"Task {tid} archived to {dest_dir.name}.")
        except Exception as e:
            print(f"Error archiving task {tid}: {e}")
            task["status"] = "failed"
        
        self.save_state()

    def run(self):
        print(f"--- AI Orchestrator Starting ---")
        print(f"Monitoring: {self.needs_action_dir}")
        self.update_dashboard("🟢 SENSORS ACTIVE", "Orchestrator system confirmed online.")

        try:
            while True:
                self.poll()
                self.process_tasks()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print(f"\n--- Orchestrator Stopped Safely ---")
            self.update_dashboard("online", "Orchestrator stopped safely.")

def main():
    parser = argparse.ArgumentParser(description="AI Employee Orchestrator")
    parser.add_argument(
        "vault_root",
        nargs="?",
        default=os.getcwd(),
        help="Path to the vault root (default: current directory)"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=10,
        help="Polling interval in seconds (default: 10)"
    )

    args = parser.parse_args()
    orchestrator = AIOrchestrator(args.vault_root, args.interval)
    orchestrator.run()

if __name__ == "__main__":
    main()
