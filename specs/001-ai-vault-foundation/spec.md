# Feature Specification: AI Employee Vault Foundation

**Feature Branch**: `001-ai-vault-foundation`  
**Created**: 2026-03-10  
**Status**: Draft  
**Input**: User description: "Implement AI Employee Vault Foundation (Bronze Tier)"

## Clarifications

### Session 2026-03-10
- Q: How should the system handle existing files in the vault root during initialization? → A: Safe Skip (Default): Only create missing directories and files; skip any that already exist.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Initial Vault Setup (Priority: P1)

As a Digital FTE owner, I want to have a standardized directory structure and core documentation in my Obsidian vault so that my reasoning engine can immediately begin processing tasks.

**Why this priority**: High. Without the core structure, the reasoning engine has no place to read from or write to.

**Independent Test**: Verify that `/Inbox`, `/Needs_Action`, and `/Done` folders exist and that `Dashboard.md` and `Company_Handbook.md` are present.

**Acceptance Scenarios**:

1. **Given** a new Obsidian vault, **When** the foundation script is run, **Then** all mandatory folders (`/Inbox`, `/Needs_Action`, `/Done`) are created.
2. **Given** the mandatory folders exist, **When** I check the vault root, **Then** `Dashboard.md` and `Company_Handbook.md` are initialized with templates.

---

### User Story 2 - Watcher Integration Point (Priority: P2)

As a developer, I want a clear landing zone for Watcher scripts (`/Needs_Action`) so that I can easily drop external signals into the vault for the reasoning engine.

**Why this priority**: Medium. This is the primary input channel for the AI Employee.

**Independent Test**: Drop a dummy `.md` file into `/Needs_Action` and verify it stays there for processing.

**Acceptance Scenarios**:

1. **Given** the `/Needs_Action` folder, **When** a new markdown file is created there, **Then** it is accessible by the reasoning engine (Gemini CLI).

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST create the directory structure: `/Inbox`, `/Needs_Action`, `/Done`, `/Logs`, `/Accounting`, `/Approved`, `/Rejected`, `/Pending_Approval`.
- **FR-002**: System MUST initialize `Dashboard.md` with sections for "Recent Activity", "Active Projects", and "Bank Balance Summary".
- **FR-003**: System MUST initialize `Company_Handbook.md` with core "Rules of Engagement" derived from the Constitution.
- **FR-004**: System MUST initialize `Business_Goals.md` with templates for Q1 metrics and active projects.
- **FR-005**: System MUST provide a `README.md` at the vault root explaining the structure to human users.
- **FR-006**: System MUST safely skip existing directories and files by default during initialization to prevent data loss.

### Key Entities *(include if feature involves data)*

- **Vault**: The local Obsidian-based knowledge base.
- **Actionable Item**: A markdown file in `/Needs_Action` representing a task or signal.
- **Log Entry**: A structured record of an AI action stored in `/Logs`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Vault directory creation takes under 10 seconds.
- **SC-002**: All 8 mandatory folders and 4 core markdown files are present after initialization.
- **SC-003**: `Dashboard.md` correctly renders in Obsidian without syntax errors.
- **SC-004**: System is ready to accept the first watcher script within 1 hour of setup.

## Assumptions
- The user has already installed Obsidian and created the root directory.
- Python 3.13 and Node.js 24+ are available for subsequent tiers (Silver/Gold).
