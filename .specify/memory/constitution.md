<!--
  Sync Impact Report:
  - Version change: N/A → 1.0.0
  - List of modified principles (old title → new title if renamed):
    - [PRINCIPLE_1_NAME] → I. Local-First & Privacy-Centric
    - [PRINCIPLE_2_NAME] → II. Perception-Reasoning-Action Loop
    - [PRINCIPLE_3_NAME] → III. Human-in-the-Loop (HITL) Safety (NON-NEGOTIABLE)
    - [PRINCIPLE_4_NAME] → IV. Autonomous Persistence (The "Ralph Wiggum" Loop)
    - [PRINCIPLE_5_NAME] → V. Auditability & Transparency
    - [PRINCIPLE_6_NAME] → VI. Spec-Driven Development (SDD)
  - Added sections:
    - Security & Compliance
    - Development Workflow
  - Removed sections:
    - N/A
  - Templates requiring updates (✅ updated / ⚠ pending) with file paths:
    - ✅ .specify/templates/plan-template.md (Alignment verified)
    - ✅ .specify/templates/spec-template.md (Alignment verified)
    - ✅ .specify/templates/tasks-template.md (Alignment verified)
  - Follow-up TODOs if any placeholders intentionally deferred:
    - None.
-->

# AI Employee Vault Constitution

## Core Principles

### I. Local-First & Privacy-Centric
All personal and business data MUST remain within the local Obsidian vault. Secrets, API tokens, and session 
data MUST NOT be committed to version control and MUST be managed via `.env` files or secure local secret 
managers. Cloud-based components (Platinum tier) MUST only handle non-sensitive drafts and metadata, 
requiring local approval for final execution.

### II. Perception-Reasoning-Action Loop
The system architecture MUST follow the Perception (Watchers) -> Reasoning (Gemini CLI) -> Action (MCP/HITL) 
loop. Gemini CLI acts as the primary reasoning engine, interpreting signals from `/Needs_Action` and 
generating structured `Plan.md` files before executing any external actions via Model Context Protocol (MCP) 
servers.

### III. Human-in-the-Loop (HITL) Safety (NON-NEGOTIABLE)
Sensitive actions—including but not limited to financial payments, external social media posts, and outgoing 
emails to new contacts—MUST require explicit human approval. The reasoning engine MUST generate an approval 
request in `/Pending_Approval`, and the action MUST ONLY proceed once the file is moved to `/Approved` by 
a human.

### IV. Autonomous Persistence (The "Ralph Wiggum" Loop)
For multi-step or complex tasks, the system SHOULD employ the "Ralph Wiggum" loop pattern. The reasoning 
engine MUST continue iterating on a task, checking its own progress against the `Plan.md` and state files, 
until the task is moved to `/Done` or a maximum iteration limit is reached.

### V. Auditability & Transparency
Every action taken by the AI MUST be logged in a structured JSON format within `/Vault/Logs/`. Logs MUST 
include a timestamp, action type, actor, target, parameters, and approval status. This ensures a permanent, 
human-readable record of all autonomous operations.

### VI. Spec-Driven Development (SDD)
All new features, watchers, or MCP servers MUST follow the Spec-Driven Development workflow. This includes 
creating a `spec.md`, followed by a `plan.md` and `tasks.md`, with mandatory Prompt History Records (PHR) 
created after every significant interaction.

## Security & Compliance
- **Credential Protection**: Never log, print, or commit secrets. Rigorously protect `.env` and `.git`.
- **Sandboxing**: All action-oriented code MUST support a `--dry-run` flag for safe testing.
- **Rate Limiting**: Autonomous actions MUST be rate-limited to prevent API abuse or runaway processes.
- **Data Isolation**: Ensure that PII (Personally Identifiable Information) is handled only by local components.

## Development Workflow
- **Gemini CLI Protocol**: Use `grep_search` and `read_file` to validate assumptions before editing files.
- **Surgical Changes**: Prefer the smallest viable diff; do not refactor unrelated code.
- **Validation**: Every change MUST be verified by running existing tests or creating new ones.
- **Documentation**: All architectural decisions MUST be recorded as ADRs in `history/adr/`.

## Governance
- This Constitution takes absolute precedence over all other general workflows and tool defaults.
- Amendments require a version bump and an update to the Sync Impact Report.
- Compliance is checked during the `Constitution Check` gate in the planning phase.
- Gemini CLI is the authoritative reasoning engine for all "Reasoning" layer operations.

**Version**: 1.0.0 | **Ratified**: 2026-03-10 | **Last Amended**: 2026-03-10
