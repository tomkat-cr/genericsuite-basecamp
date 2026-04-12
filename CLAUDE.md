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

- Project Brief (goals, audience, scope, constraints) @specs/projectBrief.md
- Directory Structure: @specs/directoryStructure.md
- Product Context (ecosystem overview and feature set): @specs/productContext.md
- System Patterns (architecture and design patterns): @specs/systemPatterns.md
- Tech Context (technology stack, versions, dependencies): @specs/techContext.md
- Active Context (current work focus and next steps): @specs/activeContext.md

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
```

## Code Style Guidelines

### Python (docs dependencies, scripts)
- Formatter: `autopep8`
- Linter: `Flake8`
- Python version: `3.12+` (< 4.0)
- Dependency management: `uv` (preferred) or `pipenv`

### JavaScript / TypeScript (ExampleApp, FastAPI Template UI)
- Formatter: `Prettier`
- Linter: `ESLint` with per-package configs
- Node.js version: `20+`
- Package manager: `npm` workspaces (preferred) or `pnpm 10.12.4+`
- Build tool: `Vite` (preferred) or `Webpack`
- Monorepo orchestration: `TurboRepo`

### Documentation (Markdown)
- All docs written in Markdown with minimal HTML
- Enhanced syntax via `pymdown-extensions`
- Documentation must be available in **English and Spanish** (`docs/en/` and `docs/es/`)
- Follow progressive disclosure: overview → section summary → detail page

### Shell Scripts

- All shell scripts must be POSIX-compliant (bash/zsh compatible).
- Use `#!/bin/bash` shebang.
- Always call bash scripts with `bash`, not `sh`.
- Use `set -euo pipefail` for safety.
- Quote all variable expansions: `"${var}"`.
- Handle macOS vs Linux differences (e.g., prefer `perl -pi -e` over `sed -i`).
- Avoid bash-specific features unless necessary, and if so, document them clearly.
- Provide clear usage examples and error messages.
- Don't use `read -p "Any prompt: " VAR`, use `echo "Any prompt: "` and `read VAR < /dev/tty`.

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

- **Never commit `.env` files** — only `.env.example` templates are committed
- All secrets (API keys, DB credentials, JWT secrets) must be in `.env` files
- HTTPS required for all production deployments
- Run `npm audit` / `pip-audit` regularly for dependency vulnerability scanning
- CORS settings are configured per-environment via `APP_CORS_ORIGIN_{STAGE}` env vars


## Key Environment Variables

File: `.env`

```bash
# Documentation FTP publishing
REMOTE_HOST=...
REMOTE_USERNAME=...
REMOTE_PASSWORD=...
REMOTE_DIRECTORY_PATH=...

# Documentation translation
OPENAI_API_KEY=...
OPENAI_MODEL=...
```

File: `docs/code/exampleapp/apps/ui/.env`

```bash
# Example App - UI
APP_LOCAL_DOMAIN_NAME=...
FRONTEND_LOCAL_PORT=...
APP_API_URL_DEV=...
BACKEND_LOCAL_PORT=...
REACT_APP_DEBUG=1
```

File: `docs/code/exampleapp/apps/api-fastapi/.env`
File: `docs/code/exampleapp/apps/api-flask/.env`
File: `docs/code/exampleapp/apps/api-chalice/.env`
File: `docs/code/exampleapp/apps/mcp-server/.env`

```bash
# Example App - Backend
APP_SECRET_KEY=...
APP_SUPERADMIN_EMAIL=...
APP_DB_ENGINE_QA=...
APP_DB_NAME_QA=...
APP_DB_URI_QA=...
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_QA=...
FDA_API_KEY=...
OPENAI_API_KEY=...
FLASK_SECRET_KEY=...
```

File: `docs/code/fastapitemplate/.env`

```bash
# FastApiTemplate App - UI
APP_LOCAL_DOMAIN_NAME=...
FRONTEND_LOCAL_PORT=...
APP_API_URL_DEV=...
BACKEND_LOCAL_PORT=...
REACT_APP_DEBUG=1

# FastApiTemplate App - Backend
APP_SECRET_KEY=...
APP_SUPERADMIN_EMAIL=...
APP_DB_ENGINE_QA=...
APP_DB_NAME_QA=...
APP_DB_URI_QA=...
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_QA=...
FDA_API_KEY=...
OPENAI_API_KEY=...
FLASK_SECRET_KEY=...
```

## Supported Backend Frameworks

| Framework | Default Port | Notes |
|---|---|---|
| FastAPI | 5011 | Async, auto OpenAPI docs |
| Flask | 5021 | Lightweight, flexible |
| AWS Chalice | 5001 | Serverless / Lambda |
| MCP Server | — | Model Context Protocol, AI integration |

## Supported Databases

MongoDB, DynamoDB, PostgreSQL (AWS RDS), MySQL (AWS RDS), Supabase

## Deployment Targets

Local, AWS (Lambda + DynamoDB/RDS), GCP, Azure, VPS (with optional Cloudflare Tunnel)

## Important Notes

- The `AGENTS.md` file (if present) is a symlink to `CLAUDE.md` — edit only `CLAUDE.md`.