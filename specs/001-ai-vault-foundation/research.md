# Research: AI Vault Foundation

## Decision: Initialization Strategy
- **Decision**: Use a Python-based initialization script (`init_vault.py`) located in the root directory.
- **Rationale**: Python provides cross-platform support for directory operations and is already a required component of the tech stack. It allows for better error handling and template management than a simple shell script.
- **Alternatives considered**: 
    - **Shell Script**: Rejected because it's less portable across Windows/Linux (Obsidian users may be on either).
    - **Manual Creation**: Rejected to ensure consistency and meet "Bronze Tier" automation requirements.

## Decision: Documentation Templates
- **Decision**: Embed Markdown templates directly within the Python script or as separate template files in a `.templates` folder.
- **Rationale**: Keeps the core files (`Dashboard.md`, `Company_Handbook.md`) consistent with the project's constitution and architectural vision from day one.
- **Alternatives considered**: 
    - **Obsidian Community Plugins**: Rejected to maintain "local-first" and minimal dependency principles.

## Decision: Folder Structure
- **Decision**: Strictly follow the structure defined in the feature spec and hackathon document.
- **Rationale**: Ensures compatibility with future "Watcher" and "Orchestrator" scripts.
- **Alternatives considered**: None (Mandated by Spec).
