# Habilidades de IA

Habilidades de agentes de IA para el ecosistema [GenericSuite](https://genericsuite.carlosjramirez.com) — un **repositorio de plugins Claude Skills**. Las habilidades son directorios autocontenidos bajo `skills/`, cada uno con un `SKILL.md` y recursos empaquetados opcional (referencias, scripts, evals), organizados en grupos de plugins en [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json).

## La Suite App-Builder (`gs-app-builder-suite`)

Construye una aplicación GenericSuite completa — frontend en React, backend en FastAPI, CRUD impulsado por JSON, asistente de IA, servidor MCP — a partir de una conversación.

El punto de entrada es `/gs-app-builder`, que detecta greenfield vs. brownfield, entrevista para el brief de la app y dirige las habilidades especializadas a continuación con un punto de control tras cada fase:

| Habilidad | Propósito |
|---|---|
| `gs-app-builder` | **Orquestador** — detección de modo, entrevista del brief de la app, impulsa todo el flujo |
| `app-starter` | Arranca una nueva app desde el `fastapitemplate` de basecamp (esqueleto + renombrado, inicialización del entorno, lista de verificación de `.env`, instalación, primera ejecución) |
| `config-builder` | Genera los archivos JSON `config_dbdef` del frontend/backend para una entidad CRUD |
| `menu-builder` | Añade entradas de menú a `backend/app_main_menu.json` (fusión idempotente) |
| `endpoints-builder` | Registra entidades en `backend/endpoints.json` (fusión idempotente; omite hijos de arrays) |
| `jsx-code-builder` | Genera los componentes del editor CRUD de React a partir de las configuraciones JSON del frontend |
| `python-fastapi-code-builder` | Ruteadores de FastAPI personalizados + módulos de capa de abstracción del modelo para endpoints no CRUD |
| `python-ai-code-builder` | Conecta el asistente de IA de GenericSuite al backend (router, índice de funciones GPT, lista de verificación del entorno) |
| `python-ai-tools-code-builder` | Genera pares LangChain `@tool`/`*_func` y los registra en el índice de funciones GPT |
| `jsx-ai-code-builder` | Añade características de IA al frontend (botsones de chat en campos, página de chatbot, shell de la app genericsuite-ai) |
| `mcp-builder` | Construye/expande el servidor MCP exponiendo las herramientas de IA de la app y los endpoints CRUD |

> El orquestador invoca las demás habilidades por nombre, así que instala el plugin completo `gs-app-builder-suite` — una instalación independiente de `gs-app-builder` por sí sola no puede impulsar el flujo.

Las apps existentes de GenericSuite también son compatibles: la suite las detecta y funciona de forma aditiva (fusiones JSON idempotentes, preservación del índice, modo MCP EXTEND). Se niegan directorios con código que no sea de GenericSuite — la adaptación (`gs-adopt`) es un alcance futuro.

## Otros grupos de plugins

| Plugin | Habilidades |
|---|---|
| `agents-skills` | `build-agents-md` (generador de AGENTS.md), `skill-creator` (meta-habilidad: crear/probar/evaluar/empacar habilidades) |

## Instalación

### Claude Code

Usando el **mercado de plugins Claude Code**:

```bash
claude

/plugin marketplace add tomkat-cr/genericsuite-skills

/plugin install gs-app-builder-suite@genericsuite-skills
```

### Skills CLI

Usando la **CLI de Skills de Vercel ([skills.sh](https://skills.sh))**:

```bash
npx skills add tomkat-cr/genericsuite-skills
```

## Quick start

### 1. Construye una Aplicación Completa (Orquestador)

Ejecuta el flujo interactivo completo para construir una app greenfield o ampliar un proyecto GenericSuite existente:

```
# Greenfield: Bootstrap y construcción de una app full-stack completa
/gs-app-builder ./my-app "un sistema de gestión de inventario con productos y almacenes, además de un chatbot de IA"

# Brownfield: Agregar una nueva entidad y características a un código base de GenericSuite existente
/gs-app-builder ./ "agregar una entidad de proveedores con detalles de contacto y un endpoint de métricas personalizado"
```

### 2. Habilidades del App Builder, paso a paso

Ejecuta habilidades específicas directamente para actualizaciones modulares o incrementales:

#### Creación de Proyecto (Scaffolding)
```
# Bootstrap una nueva aplicación full-stack GenericSuite
/app-starter ./my-app
```

#### Creación de Entidad CRUD
```
# Generar archivos JSON frontend y backend config_dbdef
/config-builder "crear archivos JSON config_dbdef para una entidad de productos con nombre, SKU, precio y stock"

# Añadir entrada al menú de navegación
/menu-builder "añadir Productos bajo el menú Inventario en app_main_menu.json"

# Registrar endpoints de backend
/endpoints-builder "registrar los endpoints de la entidad productos en backend/endpoints.json"

# Generar componentes editor CRUD de React
/jsx-code-builder "generar componentes React CRUD para productos a partir de la configuración JSON del frontend"
```

#### Enrutadores Personalizados e Integración AI / MCP
```
# Generar enrutador personalizado de FastAPI y abstracciones de modelo
/python-fastapi-code-builder "crear un enrutador personalizado para ajustes de stock en bulk con modelo de validación"

# Conectar el asistente de IA y las herramientas al backend y frontend
/python-ai-code-builder "conectar el enrutador de IA de GenericSuite al backend"
/python-ai-tools-code-builder "generar un LangChain @tool calculate_reorder_point y registrar en ai_gpt_fn_index.py"
/jsx-ai-code-builder "añadir el shell del asistente de chatbot de IA y los botones IA a nivel de campo en la UI de React"

# Construir o ampliar el servidor MCP (Model Context Protocol)
#mcp-builder "exponer las herramientas de IA de la app y los endpoints CRUD a través de un servidor MCP"
```

### 3. Utilidades de Repositorio y Meta-Habilidades

```
# Generar o actualizar la documentación AGENTS.md para cualquier proyecto
/build-agents-md ./

# Crear, evaluar, evaluar comparativamente o optimizar una habilidad
/skill-creator "crear una nueva habilidad para migraciones de esquemas de base de datos"
```

## Desarrollo

- La mayoría de las habilidades incluyen `evals/evals.json`; las pruebas de salida generada se ejecutan en `playground/` (ignoradas por Git, excepto el fixture `gs-billing-app`).
- Validar una habilidad: `(cd skills/skill-creator && python3 -m scripts.quick_validate ../../skills/<name>)`
- Empaquetar una habilidad: `(cd skills/skill-creator && python3 -m scripts.package_skill ../../skills/<name> ../../dist)`
- Los exemplares de referencia bajo `skills/*/references/` se sincronizan desde una checkout de Basecamp — nunca editarlos manualmente: `BASECAMP_DIR=../genericsuite-basecamp make sync-references`