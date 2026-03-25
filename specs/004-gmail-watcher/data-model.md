# Data Model: Gmail Watcher

## Entities

### EmailTask
Represents a parsed email that is ready to be handled as an action item.
- **Attributes**:
  - `message_id`: Unique identifier from the Gmail API.
  - `sender`: The "From" email address.
  - `subject`: The subject line.
  - `body`: The body content of the email.
  - `received_timestamp`: ISO-8601 formatted date of arrival.
  - `status`: Lifecycle state (`pending`, `processed`, `archived`).

### CacheEntry
Keeps track of processed emails to prevent duplicate task creation.
- **Attributes**:
  - `message_id`: The identifier of the processed message.
  - `processed_at`: Timestamp when it was first added to `/Needs_Action`.
