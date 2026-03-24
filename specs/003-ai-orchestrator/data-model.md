# Data Model: AI Orchestrator

## Entities

### OrchestratorState
Represents the persistent state of the orchestration loop.
- **Attributes**:
  - `active_tasks`: A map of Task IDs to their current `TaskMetadata`.
  - `last_poll_time`: ISO-8601 timestamp of the last `/Needs_Action` scan.

### TaskMetadata
Tracks the lifecycle and safety metrics for a single task.
- **Attributes**:
  - `id`: Unique identifier (derived from filename).
  - `status`: One of `pending`, `thinking`, `planning`, `acting`, `completed`, `failed`.
  - `iteration_count`: Current number of reasoning cycles (Safety limit: 5).
  - `original_path`: Absolute path to the file in `/Needs_Action`.
  - `start_time`: When the orchestrator first picked up the task.

### DashboardUpdate
Model for updating the Obsidian dashboard.
- **Attributes**:
  - `status_string`: The descriptive status (e.g., "🔵 AGENT THINKING...").
  - `log_entry`: A line to append to the "Recent Activity" section.
