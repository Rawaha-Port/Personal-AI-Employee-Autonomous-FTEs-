# Tasks: Local File System Watcher

**Input**: Design documents from `/specs/002-filesystem-watcher/`
**Prerequisites**: plan.md (required), spec.md (required)

**Tests**: Unit tests for file movement and name collision logic.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (e.g., US1)

## Phase 1: Setup

- [X] T001 Create `watchers/` directory in repository root
- [X] T002 Initialize `watchers/filesystem_watcher.py` with basic argument parsing (VAULT_ROOT, --interval)
- [X] T003 Create `tests/test_filesystem_watcher.py` for verification

---

## Phase 2: Foundational

- [X] T004 Define file discovery logic for `/Inbox` in `watchers/filesystem_watcher.py`
- [X] T005 [P] Define filename transformation logic (prefixing timestamp) in `watchers/filesystem_watcher.py`
- [X] T006 [P] Implement structured logging to `/Logs/watcher.log` (JSON format)

---

## Phase 3: User Story 1 - Automated Task Detection (Priority: P1)

**Goal**: Monitor `/Inbox` and move files to `/Needs_Action`

### Implementation for User Story 1

- [X] T007 [US1] Implement main polling loop with 1-second interval in `watchers/filesystem_watcher.py`
- [X] T008 [US1] Implement atomic move logic with `shutil` in `watchers/filesystem_watcher.py`
- [X] T009 [US1] Implement collision handling (appending index if file exists in `/Needs_Action`)
- [X] T010 [US1] Verify end-to-end loop: drop file in `/Inbox` -> check `/Needs_Action`

---

## Phase N: Polish

- [X] T011 [P] Ensure graceful shutdown on `Ctrl+C` (SIGINT)
- [X] T012 Finalize instructions in `README.md` on how to start the watcher
