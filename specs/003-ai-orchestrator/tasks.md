# Tasks: AI Orchestrator

**Input**: Design documents from `/specs/003-ai-orchestrator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Mock-based logic tests and end-to-end integration scenarios.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and base script setup

- [X] T001 Initialize `orchestrator.py` with base loop and argument parsing (VAULT_ROOT, --interval) in repository root
- [X] T002 Create verification test suite in `tests/test_orchestrator.py`
- [X] T003 [P] Implement state persistence logic (load/save) for `.orchestrator_state.json` in `orchestrator.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core logic for monitoring and reasoning engine interaction

- [X] T004 Implement `/Needs_Action` monitoring and file discovery logic in `orchestrator.py`
- [X] T005 [P] Implement utility for updating `Dashboard.md` (status and activity logs) in `orchestrator.py`
- [X] T006 [P] Implement `gemini-cli` subprocess invocation wrapper with context passing in `orchestrator.py`

---

## Phase 3: User Story 1 - Hands-Free Task Processing (Priority: P1) 🎯 MVP

**Goal**: Automate the pickup and processing of tasks in /Needs_Action

**Independent Test**: Drop a file in /Needs_Action and verify it moves to /Done after a simulated reasoning session.

### Tests for User Story 1

- [X] T007 [P] [US1] Create mock test for task pickup and state transition in `tests/test_orchestrator.py`
- [X] T008 [P] [US1] Create mock test for iteration tracking and completion detection in `tests/test_orchestrator.py`

### Implementation for User Story 1

- [X] T009 [US1] Implement main orchestration logic: find file -> update state -> invoke agent -> handle output in `orchestrator.py`
- [X] T010 [US1] Implement "Ralph Wiggum" loop logic (multi-step reasoning) in `orchestrator.py`
- [X] T011 [US1] Implement final archival logic (move to `/Done` or `/Rejected`) in `orchestrator.py`

**Checkpoint**: Orchestrator can successfully process a single task from start to finish autonomously.

---

## Phase 4: User Story 2 - Real-Time Dashboard Feedback (Priority: P2)

**Goal**: Provide live status updates in Obsidian during processing

**Independent Test**: Verify that Dashboard.md status string changes from "Ready" to "Thinking" to "Done" automatically.

### Implementation for User Story 2

- [X] T012 [US2] Map internal orchestrator states to Dashboard status strings (Thinking, Acting, Waiting) in `orchestrator.py`
- [X] T013 [US2] Implement automated "Recent Activity" logging for each processed task in `orchestrator.py`
- [X] T014 [US2] Verify Dashboard UI updates live in VS Code/Obsidian preview during a full loop

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Safety, error handling, and final documentation

- [X] T015 [P] Implement safety guard: halt and mark as failed if iteration count > 5 in `orchestrator.py`
- [X] T016 [P] Add robust error handling for missing dependencies (Gemini CLI) or folder access errors
- [X] T017 Finalize `README.md` with "Always-On" setup instructions for the Orchestrator
