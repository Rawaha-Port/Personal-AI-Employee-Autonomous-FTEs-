import argparse
import os
import pathlib
import sys
from datetime import datetime

# Core Directory Structure
DIRECTORIES = [
    "Inbox",
    "Needs_Action",
    "Done",
    "Logs",
    "Accounting",
    "Approved",
    "Rejected",
    "Pending_Approval"
]

# Core Markdown Templates
DASHBOARD_TEMPLATE = """---
type: dashboard
status: online
last_updated: {date}
---

# 🚀 AI Employee Dashboard

## 📊 Overview
- **Bank Balance Summary**: [PENDING]
- **Active Projects**: [INITIALIZED]

## 📥 Recent Items in Needs_Action
(Automatically populated by reasoning engine)

## 🕒 Recent Activity
- [ {date} ] Vault initialized.
"""

HANDBOOK_TEMPLATE = """---
type: handbook
version: 1.0.0
last_amended: {date}
---

# 📖 Company Handbook

## 📜 Rules of Engagement
1. **Local-First**: All data must stay in this vault.
2. **HITL Safety**: Sensitive actions require approval via `/Pending_Approval`.
3. **Auditability**: All actions must be logged in `/Logs`.

## 🤖 Reasoning Engine Protocol
- Read from `/Needs_Action`.
- Create `/Plans/PLAN_*.md` before execution.
- Log all actions to `/Logs/YYYY-MM-DD.json`.
"""

GOALS_TEMPLATE = """---
type: goals
period: Q1-2026
last_updated: {date}
---

# 🎯 Business Goals

## 📈 Q1 2026 Objectives
- [ ] Initialize AI Employee Foundation
- [ ] Setup first Watcher (Gmail/WhatsApp)
- [ ] Automate weekly billing audit

## 📁 Active Projects
1. **Project Vault Foundation**: Initializing core structure.
"""

README_TEMPLATE = """# 🏰 AI Employee Vault: Internal Documentation

This is a local-first, agent-driven automation hub.

## 🏗️ Architecture Overview

The system operates on a **Perception → Reasoning → Action** loop:

1.  **Perception (Watchers)**: Lightweight Python "Watchers" (e.g., Gmail, WhatsApp) sense external signals and drop `.md` files into the `/Needs_Action` folder.
2.  **Reasoning (Gemini CLI)**: The core reasoning engine (Gemini CLI) reads the `/Needs_Action` folder, interprets the priority, and generates a structured `Plan.md` in Obsidian.
3.  **Action (MCP & HITL)**: 
    -   **HITL (Human-in-the-Loop)**: For sensitive actions (payments, public posts), Gemini CLI creates an approval request in `/Pending_Approval`. 
    -   **MCP (Model Context Protocol)**: Once approved (file moved to `/Approved`), Gemini CLI executes the action via an MCP server (e.g., sending an email or social media post).

All actions are logged in a structured JSON format in `/Logs` for full auditability.

---

## 📂 Vault Structure

-   `/Inbox`: General landing for files and unstructured data.
-   `/Needs_Action`: Active tasks and signals for the reasoning engine.
-   `/Pending_Approval`: Sensitive actions waiting for human consent.
-   `/Approved`: Items authorized for execution.
-   `/Done`: Historical record of completed tasks.
-   `/Logs`: Structured JSON audit trail of all AI operations.
-   `/Accounting`: Financial records and transaction logs.

## 🚀 Getting Started
1. Run `init_vault.py` to ensure structure is intact.
2. Configure watchers in the `watchers/` directory.
3. Start the reasoning engine (Gemini CLI) pointed at this directory.
"""

def create_vault(vault_path, force=False, dry_run=False):
    vault_path = pathlib.Path(vault_path).resolve()
    current_date = datetime.now().strftime("%Y-%m-%d")

    # E-001: Check if parent path is writable
    if not os.access(vault_path.parent, os.W_OK):
        print(f"Error E-001: Parent directory {vault_path.parent} is not writable.")
        sys.exit(1)

    print(f"Initializing vault at: {vault_path}")
    if dry_run:
        print("[DRY RUN] No changes will be made.")

    # Create directories
    for folder in DIRECTORIES:
        folder_path = vault_path / folder
        if dry_run:
            print(f"[DRY RUN] Would create directory: {folder_path}")
        else:
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"Verified directory: {folder_path}")

    # Files to create
    files = {
        "Dashboard.md": DASHBOARD_TEMPLATE.format(date=current_date),
        "Company_Handbook.md": HANDBOOK_TEMPLATE.format(date=current_date),
        "Business_Goals.md": GOALS_TEMPLATE.format(date=current_date),
        "README.md": README_TEMPLATE
    }

    # Create files
    for filename, content in files.items():
        file_path = vault_path / filename
        if dry_run:
            print(f"[DRY RUN] Would create file: {file_path}")
            continue

        if file_path.exists() and not force:
            print(f"Skipping existing file: {file_path} (use --force to overwrite)")
            continue

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Written file: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Initialize the AI Employee Vault.")
    parser.add_argument(
        "vault_root",
        nargs="?",
        default=os.getcwd(),
        help="Path to the vault root (default: current directory)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files if they exist"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Log actions without creating directories/files"
    )

    args = parser.parse_args()
    create_vault(args.vault_root, args.force, args.dry_run)

if __name__ == "__main__":
    main()
