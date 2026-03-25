# Contract: Orchestrator API

## Interface: orchestrator.py

This script governs the autonomous reasoning loop.

### Inputs
- **Environment Variables**:
  - `VAULT_ROOT`: Path to the Obsidian vault.
- **Directories Monitored**:
  - `/Needs_Action`: Scanned for new `.md` files.

### Outputs & Side Effects
- **Reasoning Engine Invocation**: Executes `gemini --prompt "..."`.
- **Dashboard Updates**: Modifies `Dashboard.md` frontmatter and log.
- **State Persistence**: Writes to `.orchestrator_state.json`.
- **File Archival**: Moves files to `/Done` or `/Rejected`.

### Error Taxonomy
- `ERR-ORCH-001`: Gemini CLI not found in PATH.
- `ERR-ORCH-002`: Max iterations (5) exceeded for task.
- `ERR-ORCH-003`: Vault structure invalid (missing mandatory folders).
