# Research: AI Orchestrator

## Decision: Loop Implementation (Ralph Wiggum)
- **Decision**: Use a Python-based orchestrator script that monitors `/Needs_Action` and maintains a state file (`.orchestrator_state.json`).
- **Rationale**: Python allows for complex loop logic, state persistence, and easy interaction with the filesystem. It can invoke Gemini CLI as a subprocess and pass the necessary context.
- **Alternatives considered**: 
    - **Shell Script Loop**: Rejected because managing state and complex iteration logic (Ralph Wiggum) is brittle in bash.
    - **Cron Job**: Rejected because it's less "real-time" and harder to manage long-running multi-step tasks.

## Decision: Reasoning Engine Invocation
- **Decision**: Invoke Gemini CLI using `subprocess` in Python, passing the file content from `/Needs_Action` as part of the prompt.
- **Rationale**: This allows the Orchestrator to "feed" the agent and capture its output/state for the next iteration.
- **Alternatives considered**: 
    - **Direct API Call**: Rejected to maintain consistency with the Gemini CLI tool and its established environment/tools.

## Decision: State Tracking
- **Decision**: Store active task IDs, status, and iteration counts in a hidden JSON file (`.orchestrator_state.json`) in the vault root.
- **Rationale**: Provides persistence across script restarts and ensures safety guards (iteration limits) are respected.
- **Alternatives considered**: 
    - **In-memory only**: Rejected because a script crash would lose all context of what was being processed.
