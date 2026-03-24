# Implementation Plan: AI Orchestrator

**Branch**: `003-ai-orchestrator` | **Date**: 2026-03-10 | **Spec**: [specs/003-ai-orchestrator/spec.md](specs/003-ai-orchestrator/spec.md)
**Input**: Feature specification from `/specs/003-ai-orchestrator/spec.md`

## Summary
The AI Orchestrator is the "Brain" automation for the Digital FTE. It is a persistent Python script that monitors `/Needs_Action`, invokes Gemini CLI to process tasks, and manages the task lifecycle (Thinking -> Acting -> Done). It implements the "Ralph Wiggum" loop pattern to allow for multi-step reasoning and maintains a real-time status dashboard in Obsidian.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: `os`, `pathlib`, `subprocess`, `json`, `time`, `datetime`
**Storage**: Local Filesystem (Vault folders + `.orchestrator_state.json`)
**Testing**: Mocking `subprocess.run` to simulate Gemini CLI responses and verifying filesystem state transitions.
**Target Platform**: Linux (WSL), macOS, Windows
**Project Type**: Background Orchestration Script
**Performance Goals**: Pickup latency < 10 seconds; Dashboard update < 1 second.
**Constraints**: Must respect the 5-iteration safety limit for the Ralph Wiggum loop.
**Scale/Scope**: Processes files in `/Needs_Action` one at a time.

## Constitution Check

- ✅ **I. Local-First**: Processes only local vault data.
- ✅ **II. Perception-Reasoning-Action**: Serves as the central link between Perception (Watcher) and Action.
- ✅ **III. HITL Safety**: Will be extended in future tasks to detect `Pending_Approval` requirements.
- ✅ **IV. Autonomous Persistence**: Implements the "Ralph Wiggum" loop pattern.
- ✅ **V. Auditability**: Logs all transitions and agent invocations.

## Project Structure

### Documentation (this feature)

```text
specs/003-ai-orchestrator/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── orchestrator-api.md
└── tasks.md             # To be created next
```

### Source Code (repository root)

```text
orchestrator.py          # Main orchestration script
tests/
└── test_orchestrator.py # Logic verification tests
```

**Structure Decision**: Root script for easy access, consistent with `init_vault.py`.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A       | N/A        | N/A                                 |

## Phase 0: Outline & Research
- Decision: Use a polling interval of 10 seconds for the orchestrator.
- Decision: Capture Gemini CLI stdout/stderr to determine if a task is "Complete" or needs another iteration.

## Phase 1: Design & Contracts
- State model defined in `data-model.md`.
- API Contract defined in `contracts/orchestrator-api.md`.
- Integration test scenario documented in `quickstart.md`.
