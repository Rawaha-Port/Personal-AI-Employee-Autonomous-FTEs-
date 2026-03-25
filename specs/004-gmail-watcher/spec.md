# Feature Specification: Gmail Watcher

**Feature Branch**: `004-gmail-watcher`
**Created**: 2026-03-10
**Status**: Draft
**Input**: User description: "Implement Gmail Watcher for automated task sensing"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Automated Email Sensing (Priority: P1)

As a Digital FTE owner, I want my system to automatically "sense" new, important emails from my Gmail account and convert them into actionable tasks in my `/Needs_Action` folder, so that I don't miss urgent business requests.

**Why this priority**: High. This expands the "Perception" layer beyond the filesystem, making the AI Employee truly aware of incoming external communications.

**Independent Test**: Send an email to the connected account and verify a corresponding `.md` file appears in `/Needs_Action`.

**Acceptance Scenarios**:

1. **Given** the Gmail Watcher is authenticated, **When** a new email is received with high priority/unread status, **Then** the watcher creates a task file in `/Needs_Action`.
2. **Given** an email is processed, **When** the watcher successfully creates the file, **Then** it marks the email as "processed" (or moves it to a specific label) to avoid duplicate task creation.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST monitor the connected Gmail account for unread, high-priority emails.
- **FR-002**: System MUST convert the email (From, Subject, Body) into a structured markdown file in `/Needs_Action`.
- **FR-003**: System MUST include metadata in the markdown file's frontmatter: `type: email`, `from: [sender]`, `subject: [subject]`, `received: [timestamp]`.
- **FR-004**: System MUST handle duplicate detection using the email's unique message ID.
- **FR-005**: System MUST log all sensing operations to `/Logs/watcher.log` in JSON format.

### Key Entities

- **Email Task**: The parsed markdown representation of an incoming email.
- **MessageID**: The unique identifier provided by the Gmail API to prevent duplicates.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Email detection and markdown file generation completes within 60 seconds of email receipt.
- **SC-002**: System successfully filters for "important/unread" emails to reduce noise.
- **SC-003**: 0% duplicate task creation for the same email.

## Assumptions
- The user has access to a Google Cloud Platform account to generate API credentials.
- The Gmail API is enabled for the account.
- The `google-api-python-client` and `google-auth` libraries are available.
