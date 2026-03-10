# Contract: Vault Initialization API

## Interface: init_vault.py

This is a filesystem-based API for initializing the AI Employee Vault.

### Inputs
- **Environment Variables**:
  - `VAULT_ROOT`: Path where the vault will be created (Defaults to current working directory).
- **Arguments**:
  - `--force`: Overwrite existing files if they exist.
  - `--dry-run`: Log actions without creating directories/files.

### Outputs (Filesystem)

#### Directory Structure
- `/Inbox`
- `/Needs_Action`
- `/Done`
- `/Logs`
- `/Accounting`
- `/Approved`
- `/Rejected`
- `/Pending_Approval`

#### Mandatory Files
- `Dashboard.md`: Frontmatter with `type: dashboard`, `status: online`.
- `Company_Handbook.md`: Frontmatter with `type: handbook`, `version: 1.0.0`.
- `Business_Goals.md`: Frontmatter with `type: goals`, `period: Q1-2026`.
- `README.md`: Basic Markdown documentation.

### Error Taxonomy
- `E-001`: VAULT_ROOT path not writable.
- `E-002`: VAULT_ROOT already contains existing folders (and --force not set).
