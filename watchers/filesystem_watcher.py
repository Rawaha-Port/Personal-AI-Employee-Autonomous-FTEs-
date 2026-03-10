import os
import pathlib
import shutil
import time
import argparse
import json
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")

def log_event(vault_path, event_type, details):
    log_dir = pathlib.Path(vault_path) / "Logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "watcher.log"
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "details": details
    }
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

def process_inbox(vault_path):
    vault_path = pathlib.Path(vault_path).resolve()
    inbox_path = vault_path / "Inbox"
    needs_action_path = vault_path / "Needs_Action"
    
    # Check if directories exist
    if not inbox_path.is_dir() or not needs_action_path.is_dir():
        return

    for item in inbox_path.iterdir():
        if item.is_file():
            timestamp = get_timestamp()
            new_filename = f"{timestamp}_{item.name}"
            dest_path = needs_action_path / new_filename
            
            # Handle potential collision (extremely unlikely with timestamp)
            counter = 1
            while dest_path.exists():
                dest_path = needs_action_path / f"{timestamp}_{counter}_{item.name}"
                counter += 1
            
            try:
                shutil.move(str(item), str(dest_path))
                print(f"Moved: {item.name} -> {dest_path.name}")
                log_event(vault_path, "file_moved", {
                    "original": item.name,
                    "new": dest_path.name,
                    "destination": "Needs_Action"
                })
            except Exception as e:
                print(f"Error moving {item.name}: {e}")
                log_event(vault_path, "error", {"file": item.name, "error": str(e)})

def main():
    parser = argparse.ArgumentParser(description="AI Employee File System Watcher")
    parser.add_argument(
        "vault_root",
        nargs="?",
        default=os.getcwd(),
        help="Path to the vault root (default: current directory)"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=2,
        help="Polling interval in seconds (default: 2)"
    )

    args = parser.parse_args()
    vault_path = pathlib.Path(args.vault_root).resolve()

    print(f"--- AI Employee Watcher Starting ---")
    print(f"Monitoring: {vault_path / 'Inbox'}")
    print(f"Press Ctrl+C to stop.")

    try:
        while True:
            process_inbox(vault_path)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print(f"\n--- Watcher Stopped Safely ---")

if __name__ == "__main__":
    main()
