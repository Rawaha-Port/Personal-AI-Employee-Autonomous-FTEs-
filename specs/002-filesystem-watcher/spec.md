# Feature Specification: Local File System Watcher

**Feature Branch**: `002-filesystem-watcher`  
**Created**: 2026-03-10  
**Status**: Draft  
**Input**: User description: "Implement Local File System Watcher for Inbox Monitoring"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Automated Task Detection (Priority: P1)

As a Digital FTE owner, I want my system to automatically "see" new files I drop into the `/Inbox` so that I don't have to manually move them to `/Needs_Action` for the reasoning engine.

**Why this priority**: High. This is the "Perception" part of the PRA loop.

**Independent Test**: Drop a file in `/Inbox` and verify it appears in `/Needs_Action` within 5 seconds.

**Acceptance Scenarios**:

1. **Given** the watcher is running, **When** a file is created in `/Inbox`, **Then** the watcher moves it to `/Needs_Action`.
2. **Given** a new file in `/Inbox`, **When** the watcher moves it, **Then** it prepends the current timestamp to the filename to avoid collisions.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST monitor the `/Inbox` directory for new file creation.
- **FR-002**: System MUST move newly detected files from `/Inbox` to `/Needs_Action`.
- **FR-003**: System MUST prepend an ISO-8601 timestamp to the filename during move (e.g., `2026-03-10_10-00-00_file.md`).
- **FR-004**: System MUST handle duplicate filenames by appending a unique ID if necessary.
- **FR-005**: System MUST log its activity to a local `watcher.log` or the vault `/Logs` folder.

### Key Entities *(include if feature involves data)*

- **Watcher**: A background process that monitors the filesystem.
- **Inbox Event**: A filesystem signal indicating a new file.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Detection and move operation completes in under 2 seconds.
- **SC-002**: 100% of files dropped in `/Inbox` are successfully moved to `/Needs_Action`.
- **SC-003**: The watcher can run as a persistent background process.

## Assumptions
- The user has Python installed and the vault structure from Tier 1 is present.
- We will use the `watchdog` library or a simple polling loop if dependencies are restricted.
- The watcher only monitors the root of the `/Inbox` folder.
