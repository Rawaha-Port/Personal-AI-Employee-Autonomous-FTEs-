# Research: Gmail Watcher

## Decision: API Integration
- **Decision**: Use the Google Python Client Library (`google-api-python-client` and `google-auth`) with OAuth 2.0.
- **Rationale**: This is the industry-standard, secure way to access Gmail programmatically. It handles token rotation and authentication securely.
- **Alternatives considered**: 
    - **IMAP/SMTP**: Rejected as it is becoming deprecated by Google and less secure/flexible than the Gmail API.

## Decision: Duplicate Detection
- **Decision**: Store a local cache of processed `MessageIDs` in a flat JSON file (`.gmail_cache.json`).
- **Rationale**: Simple, efficient, and sufficient for the scale of a personal AI Employee. Prevents redundant task creation.
- **Alternatives considered**: 
    - **Cloud-based DB**: Rejected to maintain the "local-first" principle and keep infrastructure simple for the Bronze/Silver tiers.

## Decision: Polling Frequency
- **Decision**: Default polling interval of 300 seconds (5 minutes).
- **Rationale**: Strikes a balance between responsiveness and adhering to Gmail API quota limits (to prevent being flagged).
- **Alternatives considered**: 
    - **Push Notifications (Pub/Sub)**: Rejected as it's overly complex for the Silver Tier; requires public-facing endpoints or tunnels.
