# Habilidades de IA

El repositorio [genericsuite-skills](https://github.com/tomkat-cr/genericsuite-skills) es una colección de plugins de Claude Skills para el ecosistema GenericSuite. Su pieza central es la **suite de constructores de aplicaciones** (`gs-app-builder-suite`): un conjunto de habilidades de agentes de IA que construyen una aplicación completa de GenericSuite — frontend React, backend FastAPI, CRUD impulsado por JSON, asistente de IA y servidor MCP — a partir de una conversación.

## La suite app-builder

El punto de entrada es `/gs-app-builder`. Detecta si el directorio objetivo es una app nueva (greenfield) o un proyecto GenericSuite existente (brownfield, manejado de forma aditiva), te entrevista para obtener un *resumen de la aplicación*, y luego impulsa las habilidades especializadas con un punto de control tras cada fase:

| Habilidad | Propósito |
|---|---|
| `gs-app-builder` | Orquestador: detección de modo, entrevista del *resumen de la aplicación*, orquesta el flujo de principio a fin |
| `app-starter` | Inicia una nueva app desde el monorepo basecamp `fastapitemplate` |
| `config-builder` | Genera los archivos JSON frontend/backend `config_dbdef` por cada entidad CRUD |
| `menu-builder` | Agrega entradas a `backend/app_main_menu.json` de forma idempotente |
| `endpoints-builder` | Registra entidades en `backend/endpoints.json` de forma idempotente |
| `jsx-code-builder` | Genera los componentes del editor CRUD de React a partir de las configuraciones JSON |
| `python-fastapi-code-builder` | Endpoints FastAPI personalizados y módulos de lógica de negocio en la capa de abstracción genericsuite-be |
| `python-ai-code-builder` | Conecta al asistente de IA de GenericSuite (enrutador, índice de funciones GPT, lista de verificación del entorno) |
| `python-ai-tools-code-builder` | Herramientas LangChain específicas de la aplicación para el asistente, registradas en el índice |
| `jsx-ai-code-builder` | Funciones de IA del frontend: botones de chat por campo, página de chatbot, shell de la App genericsuite-ai |
| `mcp-builder` | Servidor MCP que expone las herramientas de IA de la aplicación y los endpoints CRUD |

## Instalación

**Código Claude:**

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
/gs-app-builder ./my-app "una aplicación de inventario con productos y almacenes, con un chatbot IA"
```

El repositorio también incluye `agents-skills` (generación de AGENTS.md, meta-habilidad de creador de habilidades) y `release-prep-skills` (notas de lanzamiento bilingües). Consulta el [README de genericsuite-skills](https://github.com/tomkat-cr/genericsuite-skills#readme) para flujos de trabajo de desarrollo y evaluación.