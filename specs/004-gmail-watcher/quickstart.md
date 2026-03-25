# Quickstart: Gmail Watcher

## Prerequisites
- Google Cloud Project with Gmail API enabled.
- OAuth 2.0 Credentials (JSON file) downloaded from GCP Console.
- Python 3.12+ and `google-api-python-client` library.

## Setup

1. **Configure OAuth 2.0**:
   - Download the `credentials.json` file from GCP.
   - Set the path as an environment variable:
     ```bash
     export GMAIL_CLIENT_SECRET=/path/to/credentials.json
     ```

2. **Start the Watcher**:
   ```bash
   python3 watchers/gmail_watcher.py . --interval 300
   ```

3. **Authentication**:
   - On the first run, the watcher will open a browser window for Google authentication.
   - Once authenticated, a `token.json` file will be generated in the local directory.

## Integration Scenario
1. **Receive Email**: An email arrives in your inbox.
2. **Detection**: The Gmail Watcher detects it as unread/important.
3. **Task Creation**: The watcher writes an `EMAIL_[ID].md` file to `/Needs_Action`.
4. **Autonomous Reasoning**: The Orchestrator (Orchestrator) picks up the file, plans the response, and updates the Dashboard.
