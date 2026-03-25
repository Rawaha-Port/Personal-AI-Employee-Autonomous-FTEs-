# Feature Specification: AI Orchestrator

**Feature Branch**: `003-ai-orchestrator`  
**Created**: 2026-03-10  
**Status**: Draft  
**Input**: User description: "Implement the AI Orchestrator for autonomous reasoning and task processing"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Hands-Free Task Processing (Priority: P1)

As a Digital FTE owner, I want the system to automatically start working on files in `/Needs_Action` so that I don't have to manually "nudge" the agent every time a new message or file arrives.

**Why this priority**: High. This is the core requirement for the Silver Tier (Functional Assistant). It moves the system from "manual" to "autonomous."

**Independent Test**: Drop a file into `/Needs_Action` and verify that the Orchestrator notices it and triggers a simulated "Reasoning" session without user intervention.

**Acceptance Scenarios**:

1. **Given** the Orchestrator is running, **When** a file is detected in `/Needs_Action`, **Then** the Orchestrator reads the file and transitions the system status to "Thinking".
2. **Given** a task is in progress, **When** the Agent completes the steps, **Then** the Orchestrator moves the original file to `/Done`.

---

### User Story 2 - Real-Time Dashboard Feedback (Priority: P2)

As a Digital FTE owner, I want to see exactly what step my AI Employee is on (Thinking, Planning, Acting) by looking at my Dashboard, so I can monitor its progress without opening a terminal.

**Why this priority**: Medium. Crucial for the "Management Dashboard" (Obsidian) experience.

**Independent Test**: Monitor `Dashboard.md` while a task is being processed and verify the status string updates automatically.

**Acceptance Scenarios**:

1. **Given** a task is picked up, **When** reasoning begins, **Then** `Dashboard.md` status is updated to "🔵 AGENT THINKING...".
2. **Given** reasoning is complete, **When** acting begins, **Then** `Dashboard.md` status is updated to "🟡 AGENT ACTING...".

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST monitor the `/Needs_Action` directory for timestamped files.
- **FR-002**: System MUST invoke the Reasoning Engine (Gemini CLI) for each detected task.
- **FR-003**: System MUST implement the "Ralph Wiggum" loop pattern, allowing for multiple reasoning iterations if a task is not yet complete.
- **FR-004**: System MUST update the `Dashboard.md` frontmatter `status` and `Recent Activity` log after each state transition.
- **FR-005**: System MUST maintain a local state file (e.g., `.orchestrator_state.json`) to track active task IDs and iteration counts.
- **FR-006**: System MUST move processed files to `/Done` (Success) or `/Rejected` (Failure) based on the reasoning engine's output.

### Key Entities *(include if feature involves data)*

- **Orchestrator**: The master process governing the reasoning loop.
- **Task State**: The current lifecycle phase of an actionable item (Pending, Thinking, Planning, Acting, Completed).
- **Iteration Count**: Number of times the agent has attempted a specific task in the current loop.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Automated pickup of new files from `/Needs_Action` within 30 seconds of arrival.
- **SC-002**: 100% of state transitions (Thinking -> Acting) are reflected in `Dashboard.md`.
- **SC-003**: Orchestrator successfully halts execution if a task exceeds a maximum of 5 iterations (safety guard).

## Assumptions
- The `filesystem_watcher.py` is running and providing files to `/Needs_Action`.
- Gemini CLI is available as a command-line tool for invocation.
- We will use a Python-based orchestrator script for consistency with the watcher.
