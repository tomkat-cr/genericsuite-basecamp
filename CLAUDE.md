# CLAUDE.md - GenericSuite Basecamp

## Project Overview

GenericSuite Basecamp is the central documentation and starting point repository for the GenericSuite ecosystem — a comprehensive full-stack development framework.

## Context

This project contains:

- MkDocs-based documentation site (published to a FTP website and readthedocs.io): @docs/en/index.md
- Configuration guide and template files: @docs/code/index.md
- FastAPI Template monorepo (ReactJS UI + FastAPI/MCP Server): @docs/code/fastapitemplate/README.md
- ExampleApp monorepo (ReactJS UI + FastAPI/Flask/Chalice/MCP Server): @docs/code/exampleapp/README.md

Deeper project context (memory bank):

- Project Brief (goals, audience, scope, constraints) @ai_docs/projectBrief.md
- Directory Structure: @ai_docs/directoryStructure.md
- Product Context (ecosystem overview and feature set): @ai_docs/productContext.md
- System Patterns (architecture and design patterns): @ai_docs/systemPatterns.md
- Tech Context (technology stack, versions, dependencies): @ai_docs/techContext.md
- Active Context (current work focus and next steps): @ai_docs/activeContext.md

## Build and Run Commands

### Documentation

```bash
make install          # Install Python/MkDocs dependencies
make serve            # Start local docs server at http://localhost:8015
make run              # prepare_all + serve (full pipeline)
make build            # Build static site to site/
make transfer         # Full publish to GitHub Pages + ReadTheDocs
make translate_uncommitted  # Translate uncommitted docs in docs/ via AI
```

### ExampleApp

```bash
make exampleapp-install       # Install all ExampleApp dependencies (Node.js)
make exampleapp-run           # Start all services (UI + all backends)
make exampleapp-update        # Update dependencies
make exampleapp-clean         # Remove node_modules, dist, build artifacts
make exampleapp-create-ssl-certs  # Generate SSL certs for HTTPS dev
```

### FastAPI Template

```bash
make fastapitemplate-install  # Install dependencies
make fastapitemplate-run      # Start dev server
make fastapitemplate-update   # Update dependencies
make fastapitemplate-clean    # Clean artifacts
```

### Other

```bash
make clean            # Clean npm cache, venv, pytest cache
make clean-all        # clean + exampleapp-clean + fastapitemplate-clean
make sample_code_prepare  # Prepare sample code to use latest packages
make generate_openapi     # Generate OpenAPI schema from fastapitemplate server
make sast-test             # Run SAST testing
make agents_md_link        # Link AGENTS.md and CLAUDE.md files
```

## Code Style Guidelines

- Follow the code style guidelines in @ai_docs/codeStyle.md

## Testing Instructions

### Python backends
```bash
pytest                # Run all tests (from backend app directory)
```

### JavaScript / React
```bash
npm test              # Jest + React Testing Library
```

There is no project-level test runner; run tests from within each app directory (e.g., `docs/code/exampleapp/apps/api-fastapi/`).

## Security Considerations

- Follow the security considerations in @ai_docs/security.md

## Key Environment Variables

- Follow env vars in @ai_docs/keyEnvVars.md

## Supported Backend Frameworks

| Framework | Default Port | Notes |
|---|---|---|
| FastAPI | 5011 | Async, auto OpenAPI docs |
| Flask | 5021 | Lightweight, flexible |
| AWS Chalice | 5001 | Serverless / Lambda |
| MCP Server | — | Model Context Protocol, AI integration |

## Supported Databases

- MongoDB
- DynamoDB
- PostgreSQL
- MySQL
- Supabase

## Deployment Targets

- Local (with optional Cloudflare Tunnel)
- AWS (Lambda or EC2)
- GCP (future)
- Azure (future)
- VPS

## Important Notes

- The `AGENTS.md` file (if present) is a symlink to `CLAUDE.md` — edit only `CLAUDE.md`.
- Skills, commands, rules, and sub-agents are located in the `.claude/` directory.
