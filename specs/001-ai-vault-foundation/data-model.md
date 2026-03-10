# Data Model: AI Vault Foundation

## Entities

### Vault
The root container for all AI Employee data and communication.
- **Attributes**:
  - `path`: Absolute filesystem path to the Obsidian vault.
  - `folders`: List of mandatory directories (`/Inbox`, `/Needs_Action`, `/Done`, `/Logs`, `/Accounting`, `/Approved`, `/Rejected`, `/Pending_Approval`).
  - `files`: List of mandatory documents (`Dashboard.md`, `Company_Handbook.md`, `Business_Goals.md`, `README.md`).

### ActionableItem
A unit of work for the AI reasoning engine.
- **Attributes**:
  - `file_path`: Path to the `.md` file in `/Needs_Action`.
  - `type`: Category (e.g., email, message, task).
  - `status`: Lifecycle state (`pending`, `in_progress`, `done`).

### LogEntry
A structured record of an operation performed by Gemini CLI.
- **Attributes**:
  - `timestamp`: ISO-8601 creation time.
  - `action_type`: The MCP or file operation performed.
  - `actor`: `gemini-cli`.
  - `approval_status`: (`approved`, `not_required`).
