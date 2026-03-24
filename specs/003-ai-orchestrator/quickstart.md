# Quickstart: AI Orchestrator

## Prerequisite
- Python 3.13+
- Gemini CLI installed and authenticated
- AI Vault Foundation (Tier 1) initialized

## Setup

1. **Ensure your Watcher is running**:
   ```bash
   python watchers/filesystem_watcher.py . --interval 2
   ```

2. **Start the Orchestrator**:
   ```bash
   python orchestrator.py . --interval 10
   ```

## Integration Scenario (The "Full Loop")

1. **Drop a file** into `/Inbox`.
2. **Watch the Watcher** move it to `/Needs_Action`.
3. **Watch the Orchestrator** detect the file and update `Dashboard.md` to "Thinking".
4. **Observe the Agent** process the task and move it to `/Done`.
5. **Verify the Success** by reading the completion log in `Dashboard.md`.
