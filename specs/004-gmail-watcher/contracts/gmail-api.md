# Contract: Gmail Watcher API

## Interface: gmail_watcher.py

This script polls Gmail and generates task files in `/Needs_Action`.

### Inputs
- **Environment Variables**:
  - `GMAIL_CLIENT_SECRET`: Path to the Google Cloud OAuth 2.0 JSON file.
  - `VAULT_ROOT`: Path to the vault root directory.
- **Arguments**:
  - `--interval`: Polling frequency in seconds (default 300).

### Outputs (Filesystem)
- **Task Files**: Creates files in `/Needs_Action/EMAIL_[Timestamp]_[Subject].md` containing:
    - Frontmatter (sender, subject, date, message_id)
    - Body content

### Error Taxonomy
- `ERR-GMAIL-001`: Authentication failed (Invalid/Expired credentials).
- `ERR-GMAIL-002`: Network/API connection error.
- `ERR-GMAIL-003`: Insufficient API quota/Rate limit exceeded.
