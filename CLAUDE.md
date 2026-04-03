# CLAUDE.md - GenericSuite Basecamp

> This file must stay **in sync** with `AGENTS.md`. Whenever you change one, mirror the same change in the other so both tools continue to work correctly.

## Project Overview

GenericSuite Basecamp is the central documentation and starting point repository for the GenericSuite ecosystem — a comprehensive full-stack development framework. This repo contains:
- **MkDocs-based documentation site** (published to GitHub Pages + ReadTheDocs)
- **ExampleApp monorepo** (`docs/code/exampleapp/`) — React UI + FastAPI/Flask/Chalice/MCP Server backends
- **FastAPI Template monorepo** (`docs/code/fastapitemplate/`)
- **Specs/memory bank** (`specs/`) — project context files

## Context

For deeper project context, read these files in order:

1. [Project Brief](./specs/projectBrief.md) — goals, audience, scope, constraints
2. [Product Context](./specs/productContext.md) — ecosystem overview and feature set
3. [Active Context](./specs/activeContext.md) — current work focus and next steps
4. [System Patterns](./specs/systemPatterns.md) — architecture and design patterns
5. [Tech Context](./specs/techContext.md) — technology stack, versions, dependencies

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

## Directory Structure

```
genericsuite-basecamp/
├── docs/                            # MkDocs content (source of truth)
│   ├── en/                          # English documentation
│   ├── es/                          # Spanish documentation
│   ├── code/                        # Code examples
│   │   ├── configuration-guide/     # Configuration guide validation rules files
│   │   ├── exampleapp/              # ExampleApp monorepo
│   │   │   ├── apps/                # exampleapp turborepo apps
│   │   │   │   ├── api-fastapi/     # FastAPI backend
│   │   │   │   ├── api-flask/       # Flask backend
│   │   │   │   ├── api-chalice/     # AWS Chalice backend
│   │   │   │   ├── config_dbdef/    # GenericSuite database/forms configuration files
│   │   │   │   ├── mcp-server/      # MCP Server backend
│   │   │   │   └── ui/              # React frontend
│   │   │   ├── assets/              # exampleapp documentation assets (images)
│   │   │   ├── packages/            # exampleapp turborepo packages
│   │   │   └── scripts/             # exampleapp specific scripts
│   │   ├── fastapitemplate/         # FastAPI Template monorepo
│   │   │   ├── assets/              # fastapitemplate documentation assets (images)
│   │   │   ├── config_dbdef/        # GenericSuite database/forms configuration files
│   │   │   ├── deploy/              # Docker/Podman containerization deployment
│   │   │   ├── scripts/             # fastapitemplate specific scripts
│   │   │   ├── server/              # FastAPI backend
│   │   │   └── ui/                  # React frontend
│   │   ├── genericsuite-be-scrips/  # Backend script templates for AWS deployments
│   │   └── genericsuite-configs/    # GenericSuite configuration JSON file examples
│   └── stylesheets/                 # Custom CSS
├── docs_for_ftp/                    # Mirror copy for FTP publishing (temporary files)
├── specs/                           # Project memory bank (context docs)
├── scripts/                         # Build, deploy, translation scripts
├── mkdocs.yml                       # MkDocs configuration
└── Makefile                         # All task automation
```

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
