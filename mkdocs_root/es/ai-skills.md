# Habilidades de IA

El [genericsuite-skills](https://github.com/tomkat-cr/genericsuite-skills) repositorio es una colección de plugins Claude Skills para el ecosistema GenericSuite. Su pieza central es el **app-builder suite** (`gs-app-builder-suite`): un conjunto de habilidades de agentes de IA que construyen una aplicación completa de GenericSuite — frontend en React, backend con FastAPI, CRUD impulsado por JSON, asistente de IA y servidor MCP — a partir de una conversación.

## La suite app-builder

El punto de entrada es `/gs-app-builder`. Detecta si el directorio objetivo es una aplicación completamente nueva (greenfield) o un proyecto GenericSuite existente (brownfield, manejado de forma aditiva), te entrevista para obtener un *resumen de la aplicación*, y luego dirige las habilidades especializadas con un punto de control tras cada fase:

| Habilidad | Propósito |
|---|---|
| `gs-app-builder` | Orquestador: detección de modo, entrevista del brief de la app, dirige el flujo de principio a fin |
| `app-starter` | Inicializa una nueva app desde el monorepo basecamp `fastapitemplate` |
| `config-builder` | Genera los archivos JSON de frontend/backend `config_dbdef` por cada entidad CRUD |
| `menu-builder` | Agrega entradas a `backend/app_main_menu.json` de forma idempotente |
| `endpoints-builder` | Registra entidades en `backend/endpoints.json` de forma idempotente |
| `jsx-code-builder` | Genera los componentes del editor CRUD de React a partir de las configuraciones JSON |
| `python-fastapi-code-builder` | Endpoints personalizados de FastAPI + módulos de lógica de negocio sobre la capa de abstracción genericsuite-be |
| `python-ai-code-builder` | Conecta el asistente de IA de GenericSuite (router, índice de funciones GPT, checklist del entorno) |
| `python-ai-tools-code-builder` | Herramientas LangChain específicas de la app para el asistente, registradas en el índice |
| `jsx-ai-code-builder` | Características de IA del frontend: botones de chat por campo, página del chatbot, shell de la App genericsuite-ai |
| `mcp-builder` | Servidor MCP que expone las herramientas de IA de la app y los endpoints CRUD |

## Instalación

**Claude Code:**

```
/plugin marketplace add tomkat-cr/genericsuite-skills
/plugin install gs-app-builder-suite@genericsuite-skills
```

**CLI de skills ([skills.sh](https://skills.sh)):**

```bash
npx skills add tomkat-cr/genericsuite-skills
```

## Inicio rápido

```
/gs-app-builder ./my-app "an inventory app with products and warehouses, with an AI chatbot"
```

El repositorio también incluye `agents-skills` (generación de AGENTS.md, meta-skill de creador de skills). Consulta el [README de genericsuite-skills](https://github.com/tomkat-cr/genericsuite-skills#readme) para flujos de desarrollo y evaluación.