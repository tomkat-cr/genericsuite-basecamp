# AI Skills

The [genericsuite-skills](https://github.com/tomkat-cr/genericsuite-skills) repository is a Claude Skills plugin collection for the GenericSuite ecosystem. Its centerpiece is the **app-builder suite** (`gs-app-builder-suite`): a set of AI agent skills that build a complete GenericSuite application — React frontend, FastAPI backend, JSON-driven CRUD, AI assistant and MCP server — from a conversation.

## The app-builder suite

The entry point is `/gs-app-builder`. It detects whether the target directory is a brand-new app (greenfield) or an existing GenericSuite project (brownfield, handled additively), interviews you into an *app brief*, and then drives the specialized skills with a checkpoint after each phase:

| Skill | Purpose |
|---|---|
| `gs-app-builder` | Orchestrator: mode detection, app-brief interview, drives the flow end to end |
| `app-starter` | Bootstraps a new app from the basecamp `fastapitemplate` monorepo |
| `config-builder` | Generates the `config_dbdef` frontend/backend JSON files per CRUD entity |
| `menu-builder` | Adds entries to `backend/app_main_menu.json` idempotently |
| `endpoints-builder` | Registers entities in `backend/endpoints.json` idempotently |
| `jsx-code-builder` | Generates the React CRUD editor components from the JSON configs |
| `python-fastapi-code-builder` | Custom FastAPI endpoints + business-logic modules on the genericsuite-be abstraction layer |
| `python-ai-code-builder` | Wires the GenericSuite AI assistant (router, GPT-functions index, env checklist) |
| `python-ai-tools-code-builder` | App-specific LangChain tools for the assistant, registered in the index |
| `jsx-ai-code-builder` | Frontend AI features: field chat buttons, chatbot page, genericsuite-ai App shell |
| `mcp-builder` | MCP server exposing the app's AI tools and CRUD endpoints |

## Installation

**Claude Code:**

```
/plugin marketplace add tomkat-cr/genericsuite-skills
/plugin install gs-app-builder-suite@genericsuite-skills
```

**skills CLI ([skills.sh](https://skills.sh)):**

```bash
npx skills add tomkat-cr/genericsuite-skills
```

## Quick start

```
/gs-app-builder ./my-app "an inventory app with products and warehouses, with an AI chatbot"
```

The repository also ships `agents-skills` (AGENTS.md generation, skill-creator meta-skill). See the [genericsuite-skills README](https://github.com/tomkat-cr/genericsuite-skills#readme) for development and evaluation workflows.
