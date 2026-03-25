# Tasks: Gmail Watcher

**Input**: Design documents from `/specs/004-gmail-watcher/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Mock-based logic tests and end-to-end integration scenarios.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (e.g., US1)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and base script setup

- [X] T001 Initialize `watchers/gmail_watcher.py` with base loop and argument parsing (VAULT_ROOT, --interval) in `watchers/`
- [X] T002 Create verification test suite in `tests/test_gmail_watcher.py`
- [X] T003 [P] Configure OAuth 2.0 credentials and implement token persistence logic (`token.json`) in `watchers/gmail_watcher.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core logic for monitoring and API interaction

- [X] T004 Implement Gmail API client with Google Client Library in `watchers/gmail_watcher.py`
- [X] T005 [P] Implement message discovery logic (Unread/Important label filtering) in `watchers/gmail_watcher.py`
- [X] T006 [P] Implement structured logging to `/Logs/watcher.log` (JSON format)

---

## Phase 3: User Story 1 - Automated Email Sensing (Priority: P1) 🎯 MVP

**Goal**: Monitor Gmail and move new tasks to /Needs_Action

**Independent Test**: Send an email and verify it appears as a markdown file in /Needs_Action.

### Implementation for User Story 1

- [X] T007 [US1] Implement email parsing logic (extract From, Subject, Body) in `watchers/gmail_watcher.py`
- [X] T008 [US1] Implement duplicate detection (MessageID cache) in `watchers/gmail_watcher.py`
- [X] T009 [US1] Implement file generation logic (markdown with frontmatter) in `watchers/gmail_watcher.py`
- [X] T010 [US1] Verify end-to-end: new email in Gmail -> file in `/Needs_Action`

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Safety, error handling, and final documentation

- [X] T011 [P] Ensure graceful shutdown on `Ctrl+C` (SIGINT)
- [X] T012 Finalize instructions in `README.md` on how to set up the Gmail API credentials

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Script skeleton and OAuth management
- **Foundational (Phase 2)**: Core API client and discovery logic - BLOCKS US1
- **User Story 1 (Phase 3)**: Core email sensing and task generation
- **Polish (Final Phase)**: Final documentation and shutdown handling

### Implementation Strategy

### MVP First (User Story 1 Only)

1. Setup and Foundational API client.
2. Implement email parsing and file generation (US1).
3. Validate by sending an email and observing task file creation.

### Incremental Delivery

1. Gmail Watcher Script → Polls and creates markdown tasks.
2. Duplicate Detection → Ensures each email becomes a unique task.
3. Documentation → Clear setup instructions for API credentials.
