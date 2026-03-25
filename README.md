# 🏰 AI Employee Vault: Digital FTE Foundation

**Current Achievement Tier: 🥈 SILVER (Functional Assistant)**

This repository implements a local-first, autonomous "Digital FTE" (Full-Time Equivalent) powered by **Gemini CLI** and managed via **Obsidian**. It follows a privacy-centric, human-in-the-loop architecture designed for proactive business and personal automation.

---

## 🏗️ Architecture Overview

The system operates on a **Perception → Reasoning → Action** loop:

1.  **Perception (Watchers)**: 
    - **Filesystem Watcher**: Monitors `/Inbox` for new tasks.
    - **Gmail Watcher**: Polls Gmail for "Important/Unread" emails and converts them into structured markdown files in `/Needs_Action/` with full metadata.
2.  **Reasoning (Gemini CLI / Orchestrator)**: The `orchestrator.py` persistent process reads the `/Needs_Action` folder, interprets task priority (using the "Ralph Wiggum" loop), and manages the lifecycle (Thinking -> Acting -> Done).
3.  **Action (MCP & HITL)**: 
    -   **HITL (Human-in-the-Loop)**: Sensitive actions (payments, public posts) are staged in `/Pending_Approval`. The Orchestrator proceeds only once a human moves the file to `/Approved`.
    -   **MCP (Model Context Protocol)**: Once approved, Gemini CLI executes the action via an MCP server.

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

---

## 🚀 Setup & Installation

### Prerequisites
- **Python 3.12+**
- **Obsidian** (Local installation)
- **Gemini CLI** (Set as the primary reasoning engine)

### Initialization
Run the initialization script in the root of your desired vault directory:

```bash
python3 init_vault.py
```

### Start the Watcher (The Senses)
To enable automated task sensing, start the background watchers:

```bash
# Filesystem watcher
python3 watchers/filesystem_watcher.py . --interval 1 &
# Gmail watcher (Requires GMAIL_CLIENT_SECRET environment variable)
python3 watchers/gmail_watcher.py . --interval 300 &
```

### Start the Orchestrator (The Brain)
To enable autonomous reasoning and task processing, start the orchestrator in the background:

```bash
python3 orchestrator.py . --interval 10
```

This script will monitor `/Needs_Action`, invoke the reasoning engine (Gemini CLI), update your Dashboard live, and archive completed tasks to `/Done`.

---

## 🛡️ Security Disclosure: Credential Handling

Security is a core mandate of this architecture:
1.  **Zero-Leak Policy**: No API keys, tokens, or credentials are stored in the Obsidian vault or committed to Git.
2.  **Environment Variables**: All secrets are managed via a local `.env` file, which is explicitly ignored in `.gitignore`.
3.  **Local-First Processing**: Personal data is processed locally by Gemini CLI. Data only leaves the system via encrypted API calls to known providers (e.g., Google, WhatsApp) during approved actions.
4.  **HITL Safeguards**: All sensitive actions (financials, outbound communications) require manual human approval by moving a file from `/Pending_Approval` to `/Approved`.

---

## 📹 Demo Video
*(Link to 5-10 minute demo video will be placed here upon final submission)*

---

## 📝 Hackathon Submission Details
- **Tier Declaration**: 🥉 BRONZE
- **Submission Form**: [Submit Here](https://forms.gle/JR9T1SJq5rmQyGkGA)
- **Developed by**: [Your Name/Team Name]

---

## 🛠️ Development (SDD)
This project follows **Spec-Driven Development (SDD)**:
1.  **Spec**: Define what the feature does in `spec.md`.
2.  **Plan**: Define architecture and tech stack in `plan.md`.
3.  **Tasks**: Breakdown implementation into granular steps in `tasks.md`.
4.  **PHR**: Every interaction is recorded in `history/prompts/` for traceability.

---
*Developed for the Personal AI Employee Hackathon 2026.*
