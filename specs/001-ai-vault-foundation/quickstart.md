# Quickstart: AI Vault Foundation

## Prerequisite
- Python 3.13+
- Obsidian (installed locally)

## Installation & Setup

1. **Clone the repository** (if not already done).
2. **Navigate to the vault root** where you want to initialize the AI Employee Vault.
3. **Run the initialization script**:

   ```bash
   python init_vault.py
   ```

4. **Open in Obsidian**:
   - Launch Obsidian.
   - Choose "Open folder as vault".
   - Select the root directory where you ran the script.

## Core Files Overview

- **Dashboard.md**: Your command center. Monitor activity here.
- **Needs_Action/**: The landing zone for all new watcher signals.
- **Company_Handbook.md**: Defines the rules Gemini CLI will follow.

## Next Steps
1. Configure your first **Watcher** (e.g., Gmail or WhatsApp).
2. Start **Gemini CLI** pointed at this vault.
