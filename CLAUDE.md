# CLAUDE.md

This file provides guidance to AI Coding Assistants (Claude Code, Gemini CLI, Cursor, Antigravity, etc.) when working with code in this repository.

## Project Overview

GenericSuite Basecamp is the central documentation and starting point repository for the GenericSuite ecosystem — a comprehensive full-stack development framework.

## Context

This project contains:

- MkDocs-based documentation site (published to a FTP website and readthedocs.io): `mkdocs_root/en/index.md`
- Configuration guide and template files: `mkdocs_root/code/index.md`
- FastAPI Template monorepo (ReactJS UI + FastAPI/MCP Server): `mkdocs_root/code/fastapitemplate/README.md`
- ExampleApp monorepo (ReactJS UI + FastAPI/Flask/Chalice/MCP Server): `mkdocs_root/code/exampleapp/README.md`

Deeper project context (memory bank) — read these on demand, they are not auto-loaded:

- Project Brief (goals, audience, scope, constraints): `docs/projectBrief.md`
- Directory Structure: `docs/directoryStructure.md`
- Product Context (ecosystem overview and feature set): `docs/productContext.md`
- System Patterns (architecture and design patterns): `docs/systemPatterns.md`
- Tech Context (technology stack, versions, dependencies): `docs/techContext.md`

## Build and Run Commands

Run `make help` to list all targets.

## Code Style Guidelines

- Follow the code style guidelines in @docs/codeStyle.md

## Testing Instructions

### Python backends
```bash
pytest                # Run all tests (from backend app directory)
```

### JavaScript / React
```bash
npm test              # Jest + React Testing Library
```

There is no project-level test runner; run tests from within each app directory (e.g., `mkdocs_root/code/exampleapp/apps/api-fastapi/`).

## Security Considerations

- Follow the security considerations in @docs/security.md

## Key Environment Variables

- Follow env vars in @docs/keyEnvVars.md

## Important Notes

- The files `AGENTS.md`, `GEMINI.md`, etc. (if present) have only a referece to `@CLAUDE.md` — edit only `CLAUDE.md`.
- Skills live in `.ai/skills/` (source of truth); symlinked under `.agents/skills/`, `.claude/skills/`, `.codex/skills/`, `.gemini/skills/`, and `.devin/skills/`.
