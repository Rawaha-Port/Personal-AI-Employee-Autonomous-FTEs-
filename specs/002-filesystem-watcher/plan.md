# Implementation Plan: Local File System Watcher

**Branch**: `002-filesystem-watcher` | **Date**: 2026-03-10 | **Spec**: [specs/002-filesystem-watcher/spec.md](specs/002-filesystem-watcher/spec.md)
**Input**: Feature specification from `/specs/002-filesystem-watcher/spec.md`

## Summary
The goal is to implement a background Python "Watcher" that monitors the `/Inbox` folder and automatically moves files to `/Needs_Action`. This script serves as the "Perception" layer of the AI Employee's PRA loop. We will use a polling loop for simplicity and to avoid external dependency issues (`watchdog` might require compilation or extra steps in certain environments).

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: `os`, `pathlib`, `shutil`, `time`, `datetime`, `json`
**Storage**: Local Filesystem
**Testing**: Mock filesystem testing via `unittest`.
**Target Platform**: Linux (WSL), macOS, Windows
**Project Type**: Background Sentinel Script
**Performance Goals**: Latency from creation in `/Inbox` to `/Needs_Action` < 2 seconds.
**Constraints**: Must be lightweight; minimal CPU usage.
**Scale/Scope**: Monitors `/Inbox` folder only.

## Constitution Check

- ✅ **I. Local-First & Privacy-Centric**: Only processes local files; no data leaves the machine.
- ✅ **II. Perception-Reasoning-Action**: Fulfills the "Perception" role in the loop.
- ✅ **III. Auditability**: Logs all move actions to `/Logs`.

## Project Structure

### Documentation (this feature)

```text
specs/002-filesystem-watcher/
├── plan.md
├── spec.md
└── tasks.md
```

### Source Code (repository root)

```text
watchers/
└── filesystem_watcher.py   # The background watcher script
```

**Structure Decision**: Place all watchers in a dedicated `watchers/` directory.

## Phase 0: Outline & Research
- Decision: Use a polling-based approach with a 1-second interval for simplicity and maximum portability.
- Decision: Prepend a `YYYY-MM-DD_HHMMSS_` prefix to filenames during the move.

## Phase 1: Design & Contracts
- The script will follow a `while True` loop pattern.
- Error handling for file permission issues and name collisions.
