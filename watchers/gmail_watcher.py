import os
import pathlib
import json
import time
import argparse
import re
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes for Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

class GmailWatcher:
    def __init__(self, vault_root, interval=300):
        self.vault_root = pathlib.Path(vault_root).resolve()
        self.interval = interval
        self.inbox_dir = self.vault_root / "Inbox"
        self.needs_action_dir = self.vault_root / "Needs_Action"
        self.logs_dir = self.vault_root / "Logs"
        self.token_file = self.vault_root / "token.json"
        self.cache_file = self.vault_root / ".gmail_cache.json"
        self.creds = None
        self.service = None
        
        # Ensure directories exist
        self.needs_action_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        
        self.load_credentials()
        if self.creds:
            self.service = build('gmail', 'v1', credentials=self.creds)
            self.cache = self.load_cache()

    def load_credentials(self):
        """T003: Configure OAuth 2.0 credentials and implement token persistence."""
        if self.token_file.exists():
            self.creds = Credentials.from_authorized_user_file(str(self.token_file), SCOPES)
        
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                client_secret = os.environ.get("GMAIL_CLIENT_SECRET")
                if not client_secret:
                    print("Error: GMAIL_CLIENT_SECRET environment variable not set.")
                    return
                flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
                self.creds = flow.run_local_server(port=0)
            
            with open(self.token_file, "w") as token:
                token.write(self.creds.to_json())

    def load_cache(self):
        if self.cache_file.exists():
            with open(self.cache_file, "r") as f:
                return json.load(f)
        return []

    def save_cache(self, cache):
        with open(self.cache_file, "w") as f:
            json.dump(cache, f)

    def log_event(self, event_type, details):
        """T006: Implement structured logging to /Logs/watcher.log."""
        log_file = self.logs_dir / "watcher.log"
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": event_type,
            "details": details
        }
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")

    def poll_gmail(self):
        """T005: Implement message discovery logic (Unread/Important label filtering)."""
        if not self.service:
            return

        try:
            results = self.service.users().messages().list(
                userId='me', q='is:unread is:important'
            ).execute()
            messages = results.get('messages', [])
            
            for msg in messages:
                msg_id = msg['id']
                if msg_id not in self.cache:
                    self.process_email(msg_id)
                    self.cache.append(msg_id)
            
            if messages:
                self.save_cache(self.cache)
        except Exception as e:
            print(f"Error polling Gmail: {e}")
            self.log_event("error", {"error": str(e)})

    def process_email(self, msg_id):
        """T007, T008, T009: Implement email parsing and file generation."""
        msg = self.service.users().messages().get(userId='me', id=msg_id, format='full').execute()
        
        headers = {h['name']: h['value'] for h in msg['payload']['headers']}
        sender = headers.get('From', 'Unknown')
        subject = headers.get('Subject', 'No Subject')
        date = headers.get('Date', datetime.now().isoformat())
        
        # Extract body from snippet or payload
        body = msg.get('snippet', 'No content')

        # Sanitize filename
        clean_subject = re.sub(r'[^\w\s-]', '', subject).strip().replace(' ', '_')
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        filename = f"EMAIL_{timestamp}_{clean_subject[:20]}.md"
        
        content = f"""---
type: email
message_id: {msg_id}
from: {sender}
subject: {subject}
received: {date}
---

# {subject}

{body}
"""
        filepath = self.needs_action_dir / filename
        filepath.write_text(content, encoding="utf-8")
        
        print(f"Created task: {filename}")
        self.log_event("file_created", {"original": msg_id, "new": filename})

    def run(self):
        print(f"--- Gmail Watcher Starting ---")
        try:
            while True:
                self.poll_gmail()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print(f"\n--- Watcher Stopped Safely ---")

def main():
    parser = argparse.ArgumentParser(description="Gmail Watcher for AI Employee Vault")
    parser.add_argument("vault_root", nargs="?", default=os.getcwd())
    parser.add_argument("--interval", type=int, default=300)
    args = parser.parse_args()
    
    watcher = GmailWatcher(args.vault_root, args.interval)
    watcher.run()

if __name__ == "__main__":
    main()
