# Implementation Plan: Gmail Watcher

**Branch**: `004-gmail-watcher` | **Date**: 2026-03-10 | **Spec**: [specs/004-gmail-watcher/spec.md](specs/004-gmail-watcher/spec.md)
**Input**: Feature specification from `/specs/004-gmail-watcher/spec.md`

## Summary
The Gmail Watcher is a background Python script that polls a connected Gmail account for unread, important emails. It parses the email content into a structured markdown file (`/Needs_Action/EMAIL_*.md`), maintaining a local cache of `MessageIDs` to avoid duplicate task generation. This integrates with the AI Orchestrator to fully automate external task sensing.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: `google-api-python-client`, `google-auth-httplib2`, `google-auth-oauthlib`
**Storage**: Local Filesystem (Vault folders + `.gmail_cache.json`)
**Testing**: Mock API testing with `unittest.mock`.
**Target Platform**: Linux (WSL), macOS, Windows
**Project Type**: Background Sentinel Script
**Performance Goals**: Latency < 60 seconds from email receipt to task creation.
**Constraints**: Must respect Gmail API quota.
**Scale/Scope**: Monitors only important/unread emails.

## Constitution Check

- ✅ **I. Local-First**: Processes email content locally within the vault.
- ✅ **II. Perception-Reasoning-Action**: Fulfills the "Perception" role for email.
- ✅ **V. Auditability**: Logs all sensing operations to `/Logs/watcher.log`.

## Project Structure

### Documentation (this feature)

```text
specs/004-gmail-watcher/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── gmail-api.md
└── tasks.md
```

### Source Code

```text
watchers/
└── gmail_watcher.py       # The background Gmail watcher
```

## Phase 0: Outline & Research
- Decision: Use the Google Client Library for Gmail API interaction.
- Decision: Maintain a local JSON cache of `MessageID`s to prevent duplicate tasks.
- Decision: Use the `Labels` filtering mechanism in Gmail API to focus on "Unread/Important".

## Phase 1: Design & Contracts
- Entity `EmailTask` defined in `data-model.md`.
- Filesystem contract defined in `contracts/gmail-api.md`.
- Integration test scenario documented in `quickstart.md`.
