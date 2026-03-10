# Tasks: AI Vault Foundation

**Input**: Design documents from `/specs/001-ai-vault-foundation/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Included as per `plan.md` testing strategy (Python `unittest`).

**Organization**: Tasks are grouped by setup, foundation, and user story to enable incremental implementation.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Initialize repository structure and verify Python 3.13 environment
- [X] T002 Create initial `init_vault.py` with basic argument parsing (VAULT_ROOT, --force, --dry-run) in repository root
- [X] T003 Create directory for verification tests in `tests/test_init_vault.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure and template definitions

- [X] T004 Define directory structure constants in `init_vault.py` (Inbox, Needs_Action, Done, Logs, Accounting, Approved, Rejected, Pending_Approval)
- [X] T005 [P] Create markdown templates for `Dashboard.md` in `init_vault.py` (or `templates/dashboard.md`)
- [X] T006 [P] Create markdown templates for `Company_Handbook.md` in `init_vault.py` (or `templates/handbook.md`)
- [X] T007 [P] Create markdown templates for `Business_Goals.md` in `init_vault.py` (or `templates/goals.md`)
- [X] T008 [P] Create markdown templates for `README.md` in `init_vault.py` (or `templates/readme.md`)

---

## Phase 3: User Story 1 - Initial Vault Setup (Priority: P1) 🎯 MVP

**Goal**: Create standardized directory structure and core documentation

**Independent Test**: Run `python init_vault.py --dry-run` and verify logged output, then run normally and check `ls -R`

### Tests for User Story 1

- [X] T009 [P] [US1] Create unit test for directory existence in `tests/test_init_vault.py`
- [X] T010 [P] [US1] Create unit test for core file existence in `tests/test_init_vault.py`
- [X] T011 [P] [US1] Create unit test for file content/headers in `tests/test_init_vault.py`

### Implementation for User Story 1

- [X] T012 [US1] Implement directory creation logic using `pathlib` in `init_vault.py`
- [X] T013 [US1] Implement file writing logic with templates in `init_vault.py`
- [X] T014 [US1] Implement conflict handling (Safe Skip default vs --force) in `init_vault.py`
- [X] T015 [US1] Implement error handling for non-writable paths (E-001) in `init_vault.py`

**Checkpoint**: At this point, running `python init_vault.py` should result in a fully compliant Obsidian vault structure.

---

## Phase 4: User Story 2 - Watcher Integration Point (Priority: P2)

**Goal**: Ensure `/Needs_Action` is correctly accessible and documented

**Independent Test**: Verify `Needs_Action` exists and is referenced in `Dashboard.md` and `README.md`

### Implementation for User Story 2

- [X] T016 [US2] Update `Dashboard.md` template to include a section linking to "Recent Items in Needs_Action"
- [X] T017 [US2] Update `README.md` to document the purpose of `/Needs_Action` for watchers

**Checkpoint**: Vault structure is optimized for future watcher automation.

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Final verification and documentation

- [X] T018 [P] Verify `init_vault.py` against `vault-api.md` contract
- [X] T019 [P] Run all tests in `tests/test_init_vault.py` and ensure they pass
- [X] T020 Finalize `quickstart.md` with any implementation-specific details

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Base environment and script skeleton
- **Foundational (Phase 2)**: Template definitions - BLOCKS US1
- **User Story 1 (Phase 3)**: Core implementation - BLOCKS US2 (for full context)
- **User Story 2 (Phase 4)**: Polish to the foundation
- **Polish (Final Phase)**: Final verification

### Parallel Opportunities

- All templates in Phase 2 can be developed in parallel.
- Tests (T009-T011) can be developed in parallel with or before implementation (T12-T15).

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete setup and template definitions.
2. Implement directory and file creation (US1).
3. Validate by opening the result in Obsidian.

### Incremental Delivery

1. Foundation Script → Creates folders and files.
2. Template refinement → Improves Dashboard/Handbook content.
3. Test suite → Ensures stability for future Silver/Gold tier enhancements.
