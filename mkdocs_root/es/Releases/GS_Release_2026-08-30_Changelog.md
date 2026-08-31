# 20260830 - v1.0.0

![GS_Release_2026-08-30_Image_1A.png](./images/GS_Release_2026-08-30_Image_1A.jpeg)

Fecha: 2026-08-30

## Summary

Presentamos la v1.0.0: ¡El GenericSuite Superproyecto está en vivo! 🚀

Este lanzamiento marca un hito fundamental para el ecosistema: se introducen un **paquete de desarrollo de aplicaciones móviles Flutter**, **habilidades de generación de código**, **habilidades de herramientas y políticas de seguridad**, y una **aplicación móvil de documentación**. Además, GenericSuite ahora se distribuye como un unificado **Superproyecto**, reuniendo los 16 paquetes como submódulos de git bajo un único monorepo, con automatización compartida y contexto de IA-agente que guía a cada paquete por igual. Es el lanzamiento estructural más grande en la historia de GenericSuite, y viene acompañado de una intensa pasade endurecimiento y expansión en todas las áreas.

Principales beneficios profesionales:

- **Nuevos paquetes**: `genericsuite-mobile`, `genericsuite-mobile-exampleapp` (para desarrollo de apps móviles con Flutter), `genericsuite-basecamp-app` (aplicación móvil de documentación), `genericsuite-skills` (habilidades de generación de aplicaciones), `genericsuite-security` (herramientas y políticas de seguridad), y `genericsuite-fe-scripts` (scripts comunes de frontend), todos debutan en este ciclo, además de una nueva ruta de despliegue OpenTofu (Terraform).

- **Un ecosistema, un hogar**: El nuevo Superproyecto orquesta todos los paquetes de GenericSuite — frontend, backend, móvil, scripts, docs y ahora seguridad — desde una raíz única, con archivos de contexto `AGENTS.md`/`GEMINI.md`/`CLAUDE.md` atravesados por cada paquete para asistentes de codificación IA.

- **Seguridad, en todas partes**: Python 3.14 y Node.js 26 en todo, ecosistema con licencia MIT, decenas de correcciones CVE (axios, LangChain/aiohttp, Vite, Forge), limitación de tasas en FastAPI/Flask, y una nueva **Suite de Seguridad GenericSuite** — cinco habilidades Claude nacidas directamente de responder al gusano de la cadena de suministro npm Shai-Hulud.

- **Relaciones 1-1 y 1-N, en todas partes**: El nuevo tipo de campo `select_table` llega a los editores CRUD de React y Flutter, sumándose al soporte de Flutter `childComponents` para relaciones 1-N.

- **Almacenamiento y secretos multinube**: GCP Cloud Storage y Azure Blob Storage se unen a AWS S3, además de GCP Secret Manager y Azure Key Vault como backends de secretos — genericsuite-be empieza a comunicarse con los tres grandes proveedores de nube.

- **Despliegues de AWS con OpenTofu**: la nueva ruta de despliegue OpenTofu (Terraform) junto a CloudFormation para despliegues en AWS.

Consulta el registro completo de cambios para todos los detalles de los 16 paquetes.

*IMPORTANTE*: revisa la [Guía de Migración 20260830 - v1.0.0](./GS_Release_2026-08-30_Migration_Guide.md) para migrar de la versión anterior a la nueva.

## GenericSuite Superproject

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite/pull/2](https://github.com/tomkat-cr/genericsuite/pull/2)
* Tag: [https://github.com/tomkat-cr/genericsuite/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite/releases/tag/1.0.0)

### Pull Request Overview

Presentando la estructura del GenericSuite superproyecto

Esta solicitud de extracción establece el GenericSuite Superproject como una capa de orquestación de monorepo, reuniendo los 16 paquetes de GenericSuite como submódulos de git bajo un único repositorio. Añade scripts de automatización para sincronizar y gestionar los paquetes, documentación a nivel de proyecto y archivos de contexto de AI Coding Assistant, sentando las bases para lanzamientos coordinados de todo el ecosistema como este.

Puntos destacados

- Capa de orquestación de monorepo: todos los paquetes de GenericSuite (`genericsuite-fe`, `genericsuite-be`, `genericsuite-be-ai`, `genericsuite-fe-ai`, `genericsuite-basecamp`, y más) now son gestionados como submódulos de git bajo `packages/`, con `make update-packages` para sincronizarlos.
- Contexto de AI Coding Assistant: `AGENTS.md`, `GEMINI.md`, y `CLAUDE.md` brindan a Claude Code, Gemini CLI, Cursor, Antigravity, y otros asistentes una guía consistente a lo largo de todo el ecosistema.
- Nueva habilidad de AI de notas de lanzamiento: la habilidad automátiza la recopilación de changelogs, PRs y etiquetas en cada paquete para producir este mismo changelog de lanzamiento y sus resúmenes en redes sociales.

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Added
- Añadir: Presentación de la estructura del GenericSuite superproyecto con submódulos de git, scripts de automatización y documentación del proyecto, para facilitar la gestión, el cambio y el despliegue del proyecto en su conjunto [GS-319].
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los AI Coding Assistants [GS-303].
- Añadir la habilidad `release-notes` al directorio `.ai./skills`, para generar notas de lanzamiento y resúmenes para redes sociales del proyecto [GS-191].

##### Changed
- Licencia cambiada a MIT [FA-244].
- Renombrar AWS_S3_BUCKET_NAME a AWS_S3_BUCKET_NAME_FE en el archivo .env y .env.example [GS-328].
- `webpack.config.js` y `config-overrides.js`: comentarios sobre los polyfills del módulo central de Node.js han sido desactivados; se añadieron notas de instalación para volver a habilitarlos si es necesario [GS-338].
- Actualizar .npmignore para incluir archivos y directorios adicionales para Claude Code, AI Agents y OpenTofu [GS-327].
- Actualizar la versión a 1.0.0 en package.json, package-lock.json y version.txt para reflejar el último lanzamiento [GS-327].

##### Fixed
- getFieldElementsYupValidations() no funcionaba con action=CREATION, por ejemplo tenía problemas en la creación de usuarios (clave API de OpenAI y modelo requeridos cuando tenían valores nulos). Por ahora, las validaciones de Yup están desactivadas [GS-251].
- La versión del paquete `bson` fijada a 7.2.0 para corregir el error "Uncaught TypeError: globalThis?.process?.getBuiltinModule is not a function" tras actualizar vite a la versión 8 [GS-268].
- `tsconfig.json` le faltaba un `exclude` para `*.test.tsx`, de modo que cada archivo de prueba generaba su propio stub `.d.ts` en `dist/esm` y `dist/cjs` durante la build de Rollup. Dado que `dist` está completamente incluido en el paquete npm publicado, se generaron ~24 archivos de declaración inútiles con cada lanzamiento [GS-338].
- `rollup.config.mjs`: se añadieron `bson` y `js-md5` al arreglo `external`. Ambos son dependencias pares reales usadas en `src/lib/services/id.utilities.jsx` y `md5.utilities.jsx`, pero estaban ausentes de `external`, por lo que Rollup los empaquetaba directamente en `dist` en lugar de tratarlos como dependencias pares suministradas por el consumidor [GS-338].
- Se eliminó una entrada falsa `"with"` de la configuración `resolve.fallback` de webpack — `with` no es un módulo central de Node.js, así que el fallback nunca hacía nada [GS-338].
- "config-overrides.js" actualizado para corregir errores al ejecutar la app con RUN_BUNDLER="react-scripts" [GS-338] y refactorizado para usar fileURLToPath en la resolución de rutas y limpiar logs de depuración no usados [GS-327].
- Documentación de instalación de la dependencia "process" en el archivo "webpack.config.js" para corregir errores al ejecutar la app [GS-338].
- "generic.editor.rfc.common.jsx" y "generic.editor.rfc.service.jsx" corregidos para mostrar errores de configuración eventual en listados de hijos, y actualizados para mostrar el nombre del editor en los mensajes de error [GS-327].
- "vite.config.mjs" actualizado para corregir el mensaje "(!) Your Vite config uses features that are unsupported by `configLoader: 'native'`, which is planned to become the default in a future major version of Vite: `__dirname` (vite.config.mjs:54:42). Use `import.meta.dirname` instead" tras la actualización a vite 8 [GS-268].

##### Security
- Actualizar dependencias a las versiones más recientes: crypto-browserify@^3.12.1, downshift@^9.4.0, react-icons@^5.7.0, react-markdown@^10.1.0, react-syntax-highlighter@^16.1.1 [GS-219] [GS-214].
- Actualizar axios@^1.19.0 para corregir vulnerabilidades de seguridad [GS-219]:
  - SSRF, inyección de datos sensibles, modificación insegura de atributos, etc. (varias entradas). Ver detalle en la lista original.
- Actualizar yup@^1.7.1 para corregir vulnerabilidades [GS-219]:
  - Inyección de código arbitraria y otros problemas en lodash y lodash-es [GS-219].
- Actualizar react-router-dom@^7.18.2 para corregir vulnerabilidad [GS-219]:
  - Varios vectores de seguridad en rutas y CSRF, entre otros [GS-219].
- "react" y "react-dom" ahora tienen dependencias pares con "^18.2.0" (sin afectar este código porque solo usa BrowserRouter/Routes/Route/Link/Navigate; React/ReactDOM se actualizarán a 19 en la próxima versión para corregir la vulnerabilidad mencionada) [GS-219].
- Subir la versión de Node.js en .nvmrc a 26 [GS-339].
- Los archivos de configuración `users_user_history.json`, `users_config.json` y `users_api_keys.json` ahora utilizan el parámetro "mandatoryFilters" en la configuración del backend para garantizar que el historial de usuarios, la configuración y las claves API estén forzados al usuario actual [GS-327].
- Los archivos `users_user_history_admin.json`, `users_config_admin.json` y `users_api_keys_admin.json` no usan el parámetro "mandatoryFilters" para permitir que el superusuario vea todo el historial de usuarios, configuraciones y claves API al editar usuarios [GS-327].
- Actualizar @babel/core a ^7.29.7 para corregir vulnerabilidad de lectura arbitraria mediante comentario sourceMappingURL ([CVE-2026-49356]) [GS-219].

##### Removed
- El directorio `scripts/` se movió a la [biblioteca de scripts frontend](https://github.com/tomkat-cr/genericsuite-fe-scripts) [GS-107].
- Dependencias pares no utilizadas: `react-icons`, `web-vitals`, `fs`, `json-loader`, `with`, `constants-browserify`, `crypto-browserify`, `os-browserify`, `stream-browserify`, `tty-browserify`, `url`, `vm-browserify`. Ninguna se importa en `src/`; las dependencias CRUD-editor ya están requeridas de forma transitiva a través de la dependencia pares de `genericsuite` para quien las necesite, y los shims de Node.js solo se usaban en las configuraciones dev-server opcionales de webpack/`react-app-rewired` [GS-338].
- Dependencias de desarrollo no utilizadas: `@babel/cli`, `@babel/preset-stage-0`, `@rollup/plugin-typescript`, `file-loader`, `path`, `url-loader` (mismo razonamiento que en `genericsuite-fe`), y `whatwg-fetch` (no se necesita en pruebas aquí). `@testing-library/user-event` se mantuvo — a diferencia de `genericsuite-fe`, se usa realmente en `ChatCodeBlock.test.tsx` [GS-338].
- Dependencias innecesarias (css-loader, postcss-loader, style-loader) y otras: el usuario puede importarlas si webpack o GitHub pages se van a usar en su app [GS-338].
- Atributo `'id="copyButton"'` eliminado del componente `<ChatCopyButton />` [GS-327].

## GenericSuite Frontend AI

### Package, Pull Request and Tag

* Package: [https://www.npmjs.com/package/genericsuite-ai/v/1.3.0](https://www.npmjs.com/package/genericsuite-ai/v/1.3.0)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/11](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/11)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/12](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/12)
* Tag: [https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.3.0](https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.3.0)

### Pull Request Overview

Documentación de agentes IA, scripts movidos a GS FE Scripts, licencia MIT y actualizaciones de seguridad

Replica el lanzamiento central de FE: documentos de agente IA, reacondicionamiento de licencia MIT y movimiento del directorio de scripts a `genericsuite-fe-scripts`. Añade pulido de UI de ChatBot (botón de copiar con icono, mejor renderizado de bloques de código) y corrige un error de resolución de dependencias de Formik que afecta a ExampleApp/FastApiTemplate, junto con el mismo gran barrido de dependencias de seguridad que FE Core más mejoras de jest/rollup-plugin-typescript.

Puntos destacados

- Corregido el fallo "Could not resolve dependency: formik@2.4.5" que sacaba de quicio a consumidores de ExampleApp/FastApiTemplate [GS-254].
- Bloques de código de conversación de ChatBot: botón de copiar con icono y mejoras de renderizado [GS-214].
- `scripts/` movido a `genericsuite-fe-scripts`; Licencia cambiada a MIT [GS-107] [FA-244].
- Seguridad: actualizaciones de axios, yup, react-router-dom, jest, rollup-plugin-typescript2/typescript, y @babel/core para corregir numerosas vulnerabilidades de alto/críticas, incluyendo problemas de ejecución remota de código [GS-219].
- Limpieza de construcción/dependencias: se eliminaron dependencias pares/dev no utilizadas (css-loader, postcss-loader, gh-pages, etc.) [GS-338].

### CHANGELOG.md

#### [1.3.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los AI Coding Assistants [GS-303].
- Añadir pruebas SAST [GS-315].
- Añadir biblioteca de scripts frontend [GS-107].

##### Changed
- Licencia cambiada a MIT [FA-244].
- Renombrar AWS_S3_BUCKET_NAME a AWS_S3_BUCKET_NAME_FE en el archivo .env [GS-328].
- Bloques de código de diálogo de ChatBot mejorados: reemplazar el botón de copiar por un icono y mejorar el diseño [GS-214].
- Añadir script "tailwind-build" para desplegar_* y ejecutar_* en Makefile [GS-214].
- `webpack.config.js` y `config-overrides.js`: comentarios sobre polyfills del módulo central de Node.js han sido desactivados; se añadieron notas de instalación para reactivarlos si el grafo de dependencias de un consumidor lo requiere [GS-338].
- Actualizar la versión a 1.3.0 en package.json, package-lock.json y version.txt para reflejar el último lanzamiento [GS-327].

##### Fixed
- Error "Could not resolve dependency: formik@2.4.5" en `ExampleApp`, `FastApiTemplate` y todas las apps que usan `genericsuite-fe-ai` como dependencia [GS-254].
- Error "installHook.js:1 TypeError: JY.default.includes is not a function" cuando se hacen clic en ciertas conversaciones de ChatBot y la página se queda vacía [GS-214].
- `tsconfig.json` le faltaba un `exclude` para `*.test.tsx`, por lo que cada archivo de prueba generaba su propio `.d.ts` en `dist/esm` y `dist/cjs` durante la build de Rollup. Estas 14 filas sobrantes ya estaban en el repo y se enviaban en `dist/` con cada npm publish [GS-338].
- Eliminar entrada falsa `"with"` de la configuración `resolve.fallback` de `config-overrides.js` — `with` no es un módulo central de Node.js, así que el fallback nunca hacía nada [GS-338].
- El `rollup.config.mjs`: eliminar `formik` del array `external` — no es una dependencia par declarada y no se importa en `src/` (restante de la configuración de Rollup de `genericsuite-fe`) [GS-338].
- "config-overrides.js" actualizado para corregir errores al ejecutar la app con RUN_BUNDLER="react-scripts" [GS-338], y refactor para usar fileURLToPath y limpiar logs de depuración no usados [GS-327].
- Documentación de instalación de la dependencia "process" en el archivo "webpack.config.js" para corregir errores al ejecutar la app [GS-338].

##### Security
- json5, postcss y prismjs arreglados por vulnerabilidades al actualizar sus paquetes dependientes [GS-214].
- Actualizar dependencias a las versiones más recientes: crypto-browserify, downshift, react-icons, react-markdown, react-syntax-highlighter [GS-219] [GS-214].
- Actualizar axios@^1.19.0 para corregir vulnerabilidades de seguridad [GS-219]:
  - SSRF, inyección de datos sensibles, contaminación de prototipos, etc. (varias entradas). Ver listado completo.
- Actualizar yup@^1.7.1 para corregir vulnerabilidades [GS-219]:
  - Inyección de código arbitraria en lodash/lodash-es [GS-219].
- Actualizar react-router-dom@^7.18.2 para corregir vulnerabilidad [GS-219]:
  - Varias vectores de seguridad en rutas y CSRF, entre otros [GS-219].
- Actualizar jest, jest-environment-jsdom y babel-jest para corregir vulnerabilidades [GS-219].
- Actualizar rollup-plugin-typescript2 a ^0.37.0 y TypeScript a ^5.3.3 para corregir vulnerabilidades [GS-219].
- Otras vulnerabilidades de seguridad cubiertas por las actualizaciones de dependencias [GS-219]:
  - Varias dependencias y herramientas relacionadas con seguridad.
- Actualizar React y React-DOM a dependencias pares ^18.2.0 (sin afectar este código; se planea la actualización a 19 en la próxima versión para corregir vulnerabilidad de react-router-dom) [GS-219].
- Bump Node.js en .nvmrc a 26 [GS-339].
- Actualizar @babel/core a ^7.29.7 para corregir vulnerabilidad ([CVE-2026-49356]) [GS-219].

##### Removed
- El directorio `scripts/` se movió a la [biblioteca de scripts frontend](https://github.com/tomkat-cr/genericsuite-fe-scripts) [GS-107].
- Dependencias pares no utilizadas: varias listas largas de dependencias que ya no se requieren en `genericsuite-fe` [GS-338].
- Dependencias de desarrollo no necesarias eliminadas según lo anterior [GS-338].
- Atributo `id="copyButton"` eliminado del componente `<ChatCopyButton />` [GS-327].

## GenericSuite Frontend Scripts

### Package, Pull Request and Tag

* Package: [https://www.npmjs.com/package/genericsuite-fe-scripts/v/1.0.0](https://www.npmjs.com/package/genericsuite-fe-scripts/v/1.0.0)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/2](https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/2)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/3](https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/3)
* Tag: [https://github.com/tomkat-cr/genericsuite-fe-scripts/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-fe-scripts/releases/tag/1.0.0)

### Pull Request Overview

Crear la biblioteca GS FE scripts, despliegue frontend expandido para ser utilizado en landing pages, pruebas SAST, OpenTofu para despliegue de FE

El lanzamiento inicial de la biblioteca de scripts frontend de GenericSuite — separada del directorio `scripts/` de `genericsuite-fe` en su propio paquete independiente y reutilizable. Amplía el despliegue frontend de S3 para admitir landing pages (no solo la app principal) y añade un pipeline de despliegue completo basado en OpenTofu (S3 privado + CloudFront con Origin Access Control, enrutamiento SPA de errores, TLS 1.2 y estado remoto S3) paralelo al despliegue existente con bash-script.

Puntos destacados

- Nueva biblioteca independiente de scripts frontend, extraída de `genericsuite-fe` [GS-107].
- Nuevo módulo OpenTofu `frontend-hosting`: S3 privado + CloudFront (OAC, TLSv1.2_2021, enrutamiento SPA) con pipeline completo `aws_tf_deploy_to_s3.sh` [GS-334].
- Despliegue FE S3 ampliado para admitir landing pages, no solo la app principal [GS-328].

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Added
- Crear la biblioteca de scripts frontend [GS-107].
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a AI Coding Assistants [GS-303].
- Despliegue de infraestructura OpenTofu (Terraform-compatible) en `scripts/aws_tf`: módulo de alojamiento frontend (`frontend-hosting`) (S3 privado + CloudFront con Origin Access Control, redirección a https, TLSv1.2_2021, enrutamiento SPA) y pipeline completo `aws_tf_deploy_to_s3.sh` (aplicar tofu + construir + sincronizar S3 + invalidación de CloudFront), con estado remoto S3 — paralelo al existente `aws_deploy_to_s3.sh`, que permanece sin cambios [GS-334].

##### Changed
- Cambiar el despliegue FE S3 para usar en Landing Pages [GS-328].
- Renombrar AWS_S3_BUCKET_NAME a AWS_S3_BUCKET_NAME_FE en el archivo .env y scripts [GS-328].
- Mejorar `aws_deploy_to_s3.sh`: establecer valores por defecto para RUN_BUNDLER, UPDATE_BUILD y BUILD_DIR si no se especifican vía CLI. Mejorar el manejo del nombre del bucket y las verificaciones de CloudFront. Actualizar la homepage de package.json durante el despliegue y restaurarla solo al finalizar si RUN_BUNDLER != none. Usar BUILD_DIR para establecer el directorio de build, de modo que el despliegue móvil (que no usa react-vite) pueda realizarse.
- Actualizar .npmignore para incluir archivos y directorios adicionales para Claude Code, AI Agents y OpenTofu [GS-327].

##### Security
- Actualizar la versión de Node.js en .nvmrc a 26 [GS-339].

## GenericSuite Backend Core

### Package, Pull Request and Tag

* Package: [https://pypi.org/project/genericsuite/0.4.0/](https://pypi.org/project/genericsuite/0.4.0/)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-be/pull/16](https://github.com/tomkat-cr/genericsuite-be/pull/16)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-be/pull/16](https://github.com/tomkat-cr/genericsuite-be/pull/19)
* Tag: [https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.4.0](https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.4.0)

### Pull Request Overview

OPENSPEC, mejorar documentación de IA, mejorar medidas de seguridad, licencia MIT y pruebas unitarias

Este lanzamiento añade implementaciones de abstracción para GCP Cloud Storage y Azure Blob Storage (emulando el soporte de AWS S3 existente), además de backends de secretos para GCP Secret Manager y Azure Key Vault — extendiendo el diseño multicloud a dos proveedores más. También añade limitación de tasa en FastAPI/Flask, cobertura de pruebas unitarias general, un resolver de relaciones 1-1 `select_table` a través de todos los motores de DB, relicensing a MIT y un pase de dependencias de seguridad (pyjwt, cryptography, urllib3) más una corrección de path traversal en `app_context.py`.

Highlights

- Soporte completo para GCP Cloud Storage y Azure Blob Storage (subir/eliminar/URL prefirmada/recuperación) [GS-318] [GS-317].
- Nuevos backends de secretos `get_secrets()` para GCP Secret Manager y Azure Key Vault [GS-318] [GS-317].
- Campo `select_table`: resolver de relaciones 1-1 agnóstico al motor (DynamoDB BatchGetItem / MongoDB `$lookup` caminos rápidos) [GS-259].
- Limitación de tasas (`slowapi`) integrada en endpoints de FastAPI y Flask [GS-332].
- Seguridad: actualización de pyjwt, cryptography, urllib3; corrección de vulnerabilidad de traversal en `app_context.py`; migración a Python 3.14 [GS-219] [GS-337].

### CHANGELOG.md

#### [0.4.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a AI Coding Assistants [GS-303].
- Pruebas SAST [GS-315].
- Pruebas unitarias generales [GS-21].
- Nueva variable de entorno AWS_SSL_CERTIFICATE_ARN_BE añadida al `.env.example` [GS-328].
- Soporte de almacenamiento GCP Cloud Storage (GCS): implementación completa de `upload_file_to_storage`, `remove_from_storage`, `get_gcs_presigned_url`, `storage_retieval` y `prepare_asset_url` en `genericsuite/util/gcp.py` [GS-318].
- Soporte de Azure Blob Storage: implementación completa de `upload_file_to_storage`, `remove_from_storage`, `get_blob_presigned_url` (tokens SAS), `storage_retieval` y `prepare_asset_url` en `genericsuite/util/azure.py` [GS-317].
- Soporte de GCP Secret Manager: implementación real de `get_secrets()` en `genericsuite/util/gcp_secrets.py` usando el SDK `google-cloud-secret-manager`; requiere la variable de entorno `GCP_PROJECT_ID` [GS-318].
- Soporte de Azure Key Vault: implementación real de `get_secrets()` en `genericsuite/util/azure_secrets.py` usando los SDKs `azure-keyvault-secrets` + `azure-identity`; requiere `AZURE_KEYVAULT_URL` [GS-317].
- Grupos de dependencias opcionales `gcp` y `azure` en `pyproject.toml` para instalación diferida de SDKs [GS-317] [GS-318].
- Nuevas variables de entorno documentadas en `.env.example`: `GCP_PROJECT_ID`, `GCS_CHATBOT_ATTACHMENTS_BUCKET_*`, `AZURE_STORAGE_ACCOUNT_NAME`, `AZURE_STORAGE_ACCOUNT_KEY`, `AZURE_CHATBOT_ATTACHMENTS_CONTAINER_*`, `AZURE_KEYVAULT_URL`, `CLOUD_STORAGE_PRESIGNED_EXPIRY`, `CLOUD_STORAGE_PRESIGNED_ACTIVE` [GS-317] [GS-318].
- Pruebas unitarias para almacenamiento GCS (`tests/test_gcp_storage.py`), Azure Blob storage (`tests/test_azure_storage.py`), GCP Secret Manager (`tests/test_util_gcp_secrets.py`), y Azure Key Vault (`tests/test_util_azure_secrets.py`) [GS-317] [GS-318].
- Introducir variable de entorno `DEBUG_CORS` en FastAPI `create_app.py` para registrar orígenes CORS durante el desarrollo. Mejora la capacidad de depuración para la configuración de CORS [GS-329].
- `slowapi` para limitación de tasa en FastAPI [GS-332].
- Integrar límite de tasa en endpoints de FastAPI y Flask [GS-332].
- Campo `select_table`: tipo de campo 1-1 en listados y lecturas. Nuevos atributos JSON `related_table`, `local_field`, `related_key`, `description_fields`, `description_separator`, `related_filter`; filas ahora incluyen `{field}_description`. Resolver `$in` agnóstico del motor para todos los DB, con caminos rápidos en DynamoDB BatchGetItem y MongoDB `$lookup` [GS-259].

##### Fixed
- Encabezados de API Key MCP y problemas de autenticación de API Key: modificar get_access_token para incluir todos los encabezados, actualizar mcp_authenticate_api_key para que requiera solo user_id en base a MCP_MANDATORY_USER_ID, mejorar la asignación de user_id cuando solo se proporciona API Key [GS-243].

##### Changed
- Licencia cambiada a MIT [FA-244].
- Actualizar configuración de CORS en `create_app.py` para manejar múltiples orígenes separándolos si la cadena `CORS_ORIGIN` contiene comas [GS-329].
- Actualizar configuración de CORS en `framework_abstraction.py` para establecer `Access-Control-Allow-Origin` a '*' al manejar múltiples orígenes, ya que FastAPI gestiona la división de orígenes internamente [GS-329].
- Quitar autenticación de solicitudes para flexibilidad [GS-329].
- Y añadir rate limit en `logs.py` para el endpoint `/logs` [GS-332].
- Mejoras en comentarios sobre cómo especificar C0301 y E501 para lint en `config.py`
- Reemplazar revisión de código de Gemini de Github por SonarQube y Claude [GS-336].
- Modificar Makefile para permitir argumentos opcionales para la subida de twine durante la publicación en producción, p. ej. "--verbosity" [GS-327].
- Actualizar versión a 0.4.0 en package.json, pyproject.toml y setup.py [GS-327].

##### Security
- Actualizar dependencies para corregir vulnerabilidades de configuración: pyjwt, cryptography, urllib3, y otros [GS-219] (detalles en la lista original).
- Actualizar `pytest`, `pytest-cov`, `twine`, `fastapi`, `pytest-mock`, para corregir vulnerabilidades [GS-219].
- Actualizar ddgs, y fijar `urllib3` a ^2.7.0 para corregir vulnerabilidad de envío de contenido comprimido [GS-219].
- Fijar Node.js a 26 en `.nvmrc` [GS-339].
- Migrar a Python 3.14 [GS-337].
- Otros cambios de seguridad y mejoras varias [GS-219].

##### Removed
- El directorio `scripts/` se movió a la [biblioteca de scripts frontend](https://github.com/tomkat-cr/genericsuite-fe-scripts) [GS-107].
- Conjunto de dependencias y devDependencies no utilizadas eliminadas de forma extensa (ver listado completo en fuente original) [GS-338].
- El atributo `'id="copyButton"'` eliminado del componente `<ChatCopyButton />` [GS-327].

## GenericSuite Backend AI

### Package, Pull Request and Tag

* Package: [https://pypi.org/project/genericsuite-ai/0.4.0/](https://pypi.org/project/genericsuite-ai/0.4.0/)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/14](https://github.com/tomkat-cr/genericsuite-be-ai/pull/14)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/15](https://github.com/tomkat-cr/genericsuite-be-ai/pull/15)
* Tag: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.4.0](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.4.0)

### Pull Request Overview

Mejorar documentación de IA y abordar vulnerabilidades de seguridad

Una edición enfocada en seguridad e higiene: documentación de onboarding de IA, pruebas SAST, relicensing a MIT y herramientas de revisión de código migradas de GitHub Gemini a SonarQube + Claude. El grueso del cambio es un pase de actualización de dependencias de seguridad en la pila LangChain (langchain, langchain-openai, langchain-core, langchain-community) que corrige vulnerabilidades de traversal, SSRF, ReDoS y deserialización, además de actualizaciones de pytest/twine/fastapi/aiohttp/cryptography/pyjwt y una migración a Python 3.14.

Highlights

- Pila LangChain actualizada (langchain, langchain-openai, langchain-core, langchain-community) corrigiendo vulnerabilidades de alto riesgo de traversal, SSRF, ReDoS y deserialización insegura [GS-219].
- cryptography y pyjwt actualizados para corregir problemas de construcción de rutas y SSRF/falsificación de tokens [GS-219].
- Licencia cambiada a MIT; revisión de código movida a SonarQube + Claude [FA-244] [GS-336].
- Migración a Python 3.14; Node.js actualizado a v26 en `.nvmrc` [GS-337] [GS-339].

### CHANGELOG.md

#### [0.4.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a AI Coding Assistants [GS-303].
- Pruebas SAST [GS-315].
- Pruebas unitarias generales [GS-21].
- Nueva variable de entorno AWS_SSL_CERTIFICATE_ARN_BE añadida al `.env.example` [GS-328].
- Soporte de GCP Cloud Storage (GCS): implementación completa de `upload_file_to_storage`, `remove_from_storage`, `get_gcs_presigned_url`, `storage_retieval` y `prepare_asset_url` en `genericsuite/util/gcp.py` [GS-318].
- Soporte de Azure Blob Storage: implementación completa de `upload_file_to_storage`, `remove_from_storage`, `get_blob_presigned_url` (tokens SAS), `storage_retieval` y `prepare_asset_url` en `genericsuite/util/azure.py` [GS-317].
- Soporte de GCP Secret Manager: implementación real de `get_secrets()` en `genericsuite/util/gcp_secrets.py` usando el SDK `google-cloud-secret-manager`; requiere `GCP_PROJECT_ID` [GS-318].
- Soporte de Azure Key Vault: implementación real de `get_secrets()` en `genericsuite/util/azure_secrets.py` usando `azure-keyvault-secrets` + `azure-identity` [GS-317].
- Grupos de dependencias opcionales `gcp` y `azure` en `pyproject.toml` para instalación perezosa de SDKs [GS-317] [GS-318].
- Nuevas variables de entorno documentadas en `.env.example`: `GCP_PROJECT_ID`, `GCS_CHATBOT_ATTACHMENTS_BUCKET_*`, `AZURE_STORAGE_ACCOUNT_NAME`, `AZURE_STORAGE_ACCOUNT_KEY`, `AZURE_CHATBOT_ATTACHMENTS_CONTAINER_*`, `AZURE_KEYVAULT_URL`, `CLOUD_STORAGE_PRESIGNED_EXPIRY`, `CLOUD_STORAGE_PRESIGNED_ACTIVE` [GS-317] [GS-318].
- Pruebas unitarias para almacenamiento GCS (`tests/test_gcp_storage.py`), Azure Blob storage (`tests/test_azure_storage.py`), GCP Secret Manager (`tests/test_util_gcp_secrets.py`), y Azure Key Vault (`tests/test_util_azure_secrets.py`) [GS-317] [GS-318].
- Introducción de variable de entorno `DEBUG_CORS` en FastAPI `create_app.py` para registrar orígenes CORS durante el desarrollo. Mejora de capacidades de depuración para la configuración de CORS [GS-329].
- `slowapi` para limitación de tasa en FastAPI [GS-332].
- Integración de limitación de tasa en endpoints de FastAPI y Flask [GS-332].
- Campo `select_table`: tipo de campo 1-1 resuelto en listados y lecturas. Nuevos atributos JSON `related_table`, `local_field`, `related_key`, `description_fields`, `description_separator`, `related_filter`; las filas ahora incluyen `{field}_description`. Resolver tipo `$in` agnóstico para todos los motores DB, con caminos rápidos en DynamoDB BatchGetItem y MongoDB `$lookup` [GS-259].

##### Fixed
- Encabezados de API Key MCP y problemas de autenticación de API Key: modificar get_access_token para incluir todos los encabezados, actualizar mcp_authenticate_api_key para requerir solo user_id según MCP_MANDATORY_USER_ID, mejorar la asignación de user_id cuando solo se proporciona API Key [GS-243].

##### Changed
- Licencia cambiada a MIT [FA-244].
- Actualizar la capa de abstracción de FastAPI CORS para manejar orígenes múltiples y dividirlos si es necesario [GS-329].
- Actualizar configuración de CORS en `framework_abstraction.py` para que `Access-Control-Allow-Origin` sea '*', gestionando múltiples orígenes (FastAPI maneja la división internamente) [GS-329].
- Eliminar autenticación de solicitudes para mayor flexibilidad [GS-329].
- Añadir rate limit en `logs.py` para el endpoint `/logs` [GS-332].
- Mejoras en comentarios sobre cómo especificar condiciones de lint C0301 y E501 en `config.py`.
- Reemplazar revisión de código de Gemini por SonarQube y Claude [GS-336].
- Modificar Makefile para permitir argumentos opcionales para la subida de twine durante la publicación en producción, por ejemplo, "--verbosity" [GS-327].
- Actualizar versión a 0.4.0 en package.json, pyproject.toml y setup.py [GS-327].

##### Security
- Actualizar `pyjwt` a "^2.13.0" para corregir vulnerabilidades [GS-219]:
  - Verificación indebida de firma criptográfica.
  - Varios problemas de seguridad relacionados con JWKS y scheme allowlist.
- Actualizar cryptography a "^50.0.0" para corregir vulnerabilidades [GS-219].
- Evitar caracteres no permitidos en nombres de archivos derivados de user_id u ObjectId en `app_context.py` [GS-219].
- Actualizar `urllib3` a "^2.7.0" para corregir vulnerabilidades [GS-219].
- Corregir vulnerabilidad de traversal en `app_context.py` [GS-219].
- Migrar a Python 3.14 [GS-337].
- Subir versión de Node.js en .nvmrc a 26 [GS-339].

##### Removed
- El directorio `scripts/` se movió a la [biblioteca de scripts frontend](https://github.com/tomkat-cr/genericsuite-fe-scripts) [GS-107].
- Grupos de dependencias pares no utilizados (muchos listados) y devDependencies eliminadas que ya no se requieren [GS-338].
- Atributo `id="copyButton"` eliminado del componente `<ChatCopyButton />` [GS-327].

## GenericSuite Frontend Scripts

### Package, Pull Request and Tag

* Package: [https://www.npmjs.com/package/genericsuite-fe-scripts/v/1.0.0](https://www.npmjs.com/package/genericsuite-fe-scripts/v/1.0.0)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/2](https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/2)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/3](https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/3)
* Tag: [https://github.com/tomkat-cr/genericsuite-fe-scripts/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-fe-scripts/releases/tag/1.0.0)

### Pull Request Overview

Crear la biblioteca GS FE scripts, despliegue frontend expandido para uso en landing pages, pruebas SAST, OpenTofu para despliegue de FE

La primera versión de la biblioteca de scripts frontend de GenericSuite — separada del directorio `scripts/` de `genericsuite-fe` en su propio paquete independiente y reutilizable. Amplía el despliegue frontend de S3 para soportar landing pages (no solo la app principal) y añade un pipeline completo de despliegue basado en OpenTofu (S3 privado + CloudFront con Origin Access Control, enrutamiento de errores SPA, TLS 1.2 y estado remoto S3) paralelo al despliegue existente de bash-script.

Highlights

- Nueva biblioteca independiente de scripts frontend, extraída de `genericsuite-fe` [GS-107].
- Nuevo módulo OpenTofu `frontend-hosting`: S3 privado + CloudFront (OAC, TLSv1.2_2021, SPA routing) con pipeline completo `aws_tf_deploy_to_s3.sh` [GS-334].
- Despliegue FE S3 ampliado para soportar landing pages, no solo la app principal [GS-328].

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Added
- Crear la biblioteca de scripts frontend [GS-107].
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a AI Coding Assistants [GS-303].
- Despliegue OpenTofu (Iac compatible con Terraform) en `scripts/aws_tf`: módulo de hosting frontend (`frontend-hosting`), estado remoto de S3 con bloqueo nativo (`bootstrap-tf-state.sh`) y módulos/Stacks para buckets S3, tablas DynamoDB, KMS, Secrets Manager, ECR, ACM/Route53 para dominios de apps, EC2+ALB y Lambda+API Gateway — paralelos a los scripts de CloudFormation existentes, que permanecen sin cambios [GS-334].

##### Changed
- Cambiar despliegue FE S3 para ser utilizado en Landing Pages [GS-328].
- Renombrar AWS_S3_BUCKET_NAME a AWS_S3_BUCKET_NAME_FE en el archivo .env y scripts [GS-328].
- Mejorar `aws_deploy_to_s3.sh`: establecer valores por defecto para RUN_BUNDLER, UPDATE_BUILD y BUILD_DIR si no se especifican vía CLI. Mejorar manejo de nombre de bucket y comprobaciones de CloudFront. Actualizar homepage de package.json durante el despliegue y restaurarla tras la finalización solo si RUN_BUNDLER != none. Usar BUILD_DIR para definir el directorio de build, de modo que el despliegue móvil —que no es react-vite— pueda realizarse.
- Actualizar .npmignore para incluir archivos y directorios adicionales para Claude Code, AI Agents y OpenTofu [GS-327].

##### Security
- Subir la versión de Node.js en .nvmrc a 26 [GS-339].

## GenericSuite Backend Core

### Package, Pull Request and Tag

* Package: [https://pypi.org/project/genericsuite/0.4.0/](https://pypi.org/project/genericsuite/0.4.0/)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-be/pull/16](https://github.com/tomkat-cr/genericsuite-be/pull/16)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-be/pull/16](https://github.com/tomkat-cr/genericsuite-be/pull/19)
* Tag: [https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.4.0](https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.4.0)

### Pull Request Overview

OPENSPEC, mejorar documentación de IA, mejorar medidas de seguridad, licencia MIT y pruebas unitarias

Este lanzamiento añade implementaciones completas de abstracción para GCP Cloud Storage y Azure Blob Storage (emulando el soporte existente de AWS S3), además de backends de secretos para GCP Secret Manager y Azure Key Vault — ampliando el diseño multicloud a dos proveedores más. También añade limitación de tasa en FastAPI/Flask, cobertura de pruebas unitarias general, un resolver de relaciones 1-1 `select_table` a través de todos los motores de DB, relicensing a MIT y un pase de dependencias de seguridad (pyjwt, cryptography, urllib3) más una corrección de path traversal en `app_context.py`.

Highlights

- Soporte completo para GCP Cloud Storage y Azure Blob Storage (subir/remover/URL prefirmada/recuperación) [GS-318] [GS-317].
- Nuevos backends de secretos `get_secrets()` para GCP Secret Manager y Azure Key Vault [GS-318] [GS-317].
- Campo `select_table`: resolución de relaciones 1-1 independiente del motor (DynamoDB BatchGetItem / MongoDB `$lookup` caminos rápidos) [GS-259].
- Limitación de tasas (`slowapi`) integrada en endpoints de FastAPI y Flask [GS-332].
- Seguridad: actualizaciones de pyjwt, cryptography, urllib3; corrección de traversal en `app_context.py`; migración a Python 3.14 [GS-219] [GS-337].

### CHANGELOG.md

#### [0.4.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a AI Coding Assistants [GS-303].
- Pruebas SAST [GS-315].
- Pruebas unitarias generales [GS-21].
- AWS_SSL_CERTIFICATE_ARN_BE en `.env.example` [GS-328].
- Soporte de GCP Cloud Storage (GCS): implementación completa de `upload_file_to_storage`, `remove_from_storage`, `get_gcs_presigned_url`, `storage_retieval` y `prepare_asset_url` en `genericsuite/util/gcp.py` [GS-318].
- Soporte de Azure Blob Storage: implementación completa de `upload_file_to_storage`, `remove_from_storage`, `get_blob_presigned_url` (tokens SAS), `storage_retieval` y `prepare_asset_url` en `genericsuite/util/azure.py` [GS-317].
- Soporte de GCP Secret Manager: implementación real de `get_secrets()` en `genericsuite/util/gcp_secrets.py` usando el SDK `google-cloud-secret-manager`; requiere `GCP_PROJECT_ID` [GS-318].
- Soporte de Azure Key Vault: implementación real de `get_secrets()` en `genericsuite/util/azure_secrets.py` usando los SDKs `azure-keyvault-secrets` + `azure-identity` [GS-317].
- Grupos de dependencias opcionales `gcp` y `azure` en `pyproject.toml` para instalación perezosa de SDKs [GS-317] [GS-318].
- Nuevas variables de entorno documentadas en `.env.example`: `GCP_PROJECT_ID`, `GCS_CHATBOT_ATTACHMENTS_BUCKET_*`, `AZURE_STORAGE_ACCOUNT_NAME`, `AZURE_STORAGE_ACCOUNT_KEY`, `AZURE_CHATBOT_ATTACHMENTS_CONTAINER_*`, `AZURE_KEYVAULT_URL`, `CLOUD_STORAGE_PRESIGNED_EXPIRY`, `CLOUD_STORAGE_PRESIGNED_ACTIVE` [GS-317] [GS-318].
- Pruebas unitarias para almacenamiento GCS (`tests/test_gcp_storage.py`), Azure Blob storage (`tests/test_azure_storage.py`), GCP Secret Manager (`tests/test_util_gcp_secrets.py`), y Azure Key Vault (`tests/test_util_azure_secrets.py`) [GS-317] [GS-318].
- Introducir variable de entorno `DEBUG_CORS` en FastAPI `create_app.py` para registrar orígenes CORS durante el desarrollo. Mejora de capacidades de depuración para la configuración de CORS [GS-329].
- `slowapi` para limitación de tasa en FastAPI [GS-332].
- Integrar limitación de tasa en FastAPI y Flask endpoints [GS-332].
- Campo `select_table`: 1-1 resolución de relaciones en listados y lecturas. Nuevos atributos JSON `related_table`, `local_field`, `related_key`, `description_fields`, `description_separator`, `related_filter`; filas ahora incluyen `{field}_description`. Resolución agnóstica a motor para `_in` en todos los DB, con rutas rápidas para DynamoDB BatchGetItem y MongoDB `$lookup` [GS-259].

##### Fixed
- Encabezados de API Key MCP y autenticación de API Key: ajustar get_access_token para incluir todos los encabezados, actualizar `mcp_authenticate_api_key` para requerir solo `user_id` según MCP_MANDATORY_USER_ID, mejorar la asignación de `user_id` cuando solo se proporciona API Key [GS-243].

##### Changed
- Licencia cambiada a MIT [FA-244].
- Actualizar la capa de abstracción de CORS de FastAPI en `create_app.py` para manejar orígenes múltiples separándolos si la cadena `CORS_ORIGIN` contiene comas [GS-329].
- Actualizar la configuración de CORS en `framework_abstraction.py` para devolver `Access-Control-Allow-Origin` a '*' para manejar múltiples orígenes, ya que FastAPI gestiona la división de orígenes internamente [GS-329].
- Eliminar la autenticación de solicitudes para mayor flexibilidad [GS-329].
- Añadir rate limit en `logs.py` para el endpoint `/logs` [GS-332].
- Mejorar comentarios sobre cómo especificar C0301 y E501 en `config.py`.
- Reemplazar revisión de código de Github Gemini por SonarQube y Claude [GS-336].
- Modificar Makefile para permitir argumentos opcionales para subida de twine durante la publicación de producción, p. ej. "--verbosity" [GS-327].
- Actualizar versión a 0.4.0 en package.json, pyproject.toml y setup.py [GS-327].

##### Security
- Actualizar `langchain` y otras dependencias para corregir vulnerabilidades de seguridad en la pila LangChain [GS-219].
- Actualizar `pyjwt`, `cryptography`, `urllib3` y otras dependencias para corregir vulnerabilidades relevantes [GS-219].
- Migrar a Python 3.14 [GS-337].
- Subir versión de Node.js en .nvmrc a 26 [GS-339].

##### Removed
- El directorio `scripts/` se movió a la [biblioteca de scripts frontend](https://github.com/tomkat-cr/genericsuite-fe-scripts) [GS-107].
- Dependencias pares no utilizadas: (... lista extensa eliminada por claridad) [GS-338].
- Dependencias de desarrollo no utilizadas: `@babel/cli`, `@babel/preset-stage-0`, `@rollup/plugin-typescript`, `file-loader`, `path`, `url-loader` (misma justificación que en `genericsuite-fe`), y `whatwg-fetch` (no se necesita aquí). `@testing-library/user-event` se mantiene — se utiliza en `ChatCodeBlock.test.tsx` [GS-338].
- Eliminación de numerosos módulos de desarrollo innecesarios y ajustes de configuración para reducir dependencias no esenciales [GS-338].
- Atributo `'id="copyButton"'` del componente `<ChatCopyButton />` eliminado [GS-327].

## GenericSuite BaseCamp

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-basecamp/pull/19](https://github.com/tomkat-cr/genericsuite-basecamp/pull/19)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-basecamp/pull/22](https://github.com/tomkat-cr/genericsuite-basecamp/pull/22)
* Tag: [https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.6.0](https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.6.0)

### Pull Request Overview

Renombrar docs a mkdocs_root + otros

Este pull request es una actualización amplia de documentación y herramientas que abarca todo el ecosistema GenericSuite: el sitio de documentación fue reorganizado (`docs/` → `mkdocs_root/`, `specs/` → `docs/`), se añadieron nuevas documentaciones para Desarrollo móvil, Habilidades IA, GS FE Scripts y una guía de despliegue OpenTofu, la licencia del proyecto se movió a MIT, se aplicaron pruebas SAST y correcciones de vulnerabilidad de dependencias en ExampleApp y FastApiTemplate, y el puntero del repositorio principal cambió de GS Basecamp al nuevo GS Superproject.

Highlights

- Reorganización del sitio de documentación: `docs/` renombrado a `mkdocs_root/`, nuevas páginas para Mobile Development, AI Skills, GS FE Scripts y guía de despliegue OpenTofu; y el repositorio principal apunta ahora a GS Superproject.
- Seguridad y cumplimiento: pruebas SAST integradas, actualizaciones de dependencias (cryptography, crypto-browserify, correcciones de CVE en `@babel/core`), migración a Python 3.14, licencia MIT, y aplicación de `mandatoryFilters` para tablas de historial de usuarios/config/API-key.
- Herramientas para desarrolladores: scripts para crear nuevos proyectos desde plantillas, renombrar apps, refactor de Makefile para usar `genericsuite-fe-scripts`, y tres nuevas habilidades de IA (`add-doc`, `sample-code-update`, `translate-docs`).
- CRUD Editor y configuración: campo `select_table` y opciones de selección en línea para el CRUD Editor documentados.

### CHANGELOG.md

#### [1.6.0] - 2026-08-30

##### Added
- Nueva imagen de arquitectura para la página de índice de documentación [GS-327].
- Añadir página de documentación de Habilidades IA [GS-254].
- Añadir página de documentación de Habilidades de Seguridad [GS-339].
- Documentación de GS FE Scripts [GS-107].
- Sección de documentación de Desarrollo móvil: instalación de GenericSuite Flutter, CRUD driven por JSON, childComponents (relaciones 1-N) y los tokens de tematización Apple-clean, entre otros [GS-261].
- Guía de despliegue OpenTofu (`mkdocs_root/en/Deployment-Guide/opentofu.md`) que cubre los stacks IaC de genericsuite-fe-scripts y genericsuite-be-scripts, con una entrada de navegación en `mkdocs.yml` [GS-334].
- GS Superproject, Security Suite y GS FE Scripts en la página de repositorios [GS-319].
- Pruebas SAST [GS-315]
- Documentación de campo `select_table` para añadir soporte a relaciones 1-1 en páginas de listado/datos CRUD [GS-259].
- Navegación en español para la sección de Mobile Development [GS-261].
- Introducción del modelo `SelectElementItem` para opciones de selección en línea en la configuración del editor CRUD. Actualización del campo `select_elements` para soportar IDs predefinidos y objetos `{title, value}` en línea [GS-254].
- Variables de entorno AWS_SSL_CERTIFICATE_ARN_FE y AWS_SSL_CERTIFICATE_ARN_BE [GS-328].
- Soporte multi-origin CORS para FastAPI en `aws_big_lambda/template-sam.yml` [GS-329].
- `make create-supad` para servidor exampleapp/fastapitemplate [GS-306].
- Scripts para copiar e inicializar un nuevo proyecto desde "fastapitemplate" y "exampleapp": `scripts/new-project-from-template.sh` y `scripts/rename-app.sh` [GS-306].
- Nuevas definiciones de habilidades de IA (`.ai/skills/`): add-doc, sample-code-update, translate-docs
- Dependencia `zipp` añadida a main requirements.txt para abordar una vulnerabilidad según Snyk [GS-219].

##### Changed
- Renombrar `docs/` a `mkdocs_root/` [GS-208].
- Renombrar `specs/` a `docs/` [GS-208].
- `.venv/` añadido a `.gitignore` y `.dockerignore`.
- `run_translate_uncommitted.sh` crea y elimina el entorno virtual `.venv` [GS-316].
- Licencia cambiada a MIT [FA-244].
- Mejorar la documentación de ARN de certificados SSL en el backend core para mayor claridad sobre uso de `AWS_SSL_CERTIFICATE_ARN_FE` y `AWS_SSL_CERTIFICATE_ARN_BE` entre backend y scripts de frontend [GS-328].
- Inicializar la variable APP_ENVS en `update_additional_envvars.sh` para variables de entorno específicas de la aplicación [GS-329].
- Actualizar Makefile de FastApiTemplate con nuevos objetivos utilitarios, y sustituir `tomkat-cr` por `github-username` en `.env.example` [GS-306]
- Separar la estructura de directorios de CLAUDE.md para hacerla más pequeña [GS-303].
- Actualizar configuración de FastAPI template con instrucciones para ejecutar `new-project-from-template.sh` usando `curl` [GS-306].
- Añadir referencia de FastApiTemplate a la guía de configuración principal [GS-254].
- FastApiTemplate: refactor de nombres de componentes UI: `_components` > `components`, `_images` > `images`, y `_constants` > `constants` [GS-306].
- Actualizar servidor de exampleap/fastapitemplate y scripts de desarrollo de mcp-server para gestión dinámica de entornos, de modo que se pueda definir stage ejecutando `STAGE=dev make dev` (package.json ahora usa la variable STAGE en "dev": "make run_${STAGE:-qa}") [GS-306].
- FastApiTemplate: hacer que los archivos `.env.example` muestren valores por defecto para reducir cambios del usuario al iniciar el proyecto [GS-306].
- Mejorar AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar mejor contexto e instrucciones a AI Coding Assistants [GS-303].
- Incluir directorios `.claude`, `.agents`, `.codex`, `.cursor` y `.gemini` para compartir habilidades/comandos desde el directorio `.ai` [GS-254]
- Renombrar '.claude' a '.ai'
- Corregir gráficos de directorio con líneas finales
- Modificar documentación de la función `food_moment_in_user` para mayor claridad sobre referencias de usuario. Mejorar documentación de operaciones de momentos de comida [GS-254].
- ExampleApp: manejo de excepciones amplio en el endpoint de FDA food [GS-254].
- `mkdocs.yml` — una línea de navegación ('AI Skills'), verificado `build-safe` frente a la convención de carpeta i18n [GS-254].
- ExampleApp: Actualizar dependencias en `package.json` y `pnpm-lock.yaml` para dotenv y turbo [GS-254]
- ExampleApp: Actualizar versiones de `aiohappyeyeballs` y `aiohttp` en archivos uv.lock para apps API.
- ExampleApp y FastApiTemplate: Refactor de Makefile para usar `genericsuite-fe-scripts` para comandos de build y deployment en la UI (`UI app`) [GS-107].
- Actualizar `index.md` para mayor claridad y contenido sobre características de Generic Suite (una línea más descripción breve para referencia rápida, logos centrados, nueva imagen de arquitectura) [GS-327].
- Actualizar Makefile con instrucciones de uso de ramas usando la variable BRANCH para preparar código desde la rama develop.
- Frontend-Development/GenericSuite-Core: eliminar `@babel/cli`, `@babel/preset-stage-0`, `@testing-library/user-event`, `file-loader`, `path`, `url-loader` de la etapa de instalación de dependencias de desarrollo; ya no son necesarios para el pipeline de build/pruebas de `genericsuite-fe` [GS-338].
- Frontend-Development/GenericSuite-Core: eliminar dependencias innecesarias (css-loader, postcss-loader, style-loader, express, gh-pages) de la misma documentación.
- ASDT documentation para LangGraph y Smolagents planificada, no soportada aún.
- Unificación de formato de CHANGELOG.
- Repositorio principal para GS Superproject en lugar de GS Basecamp: `repo_url: https://github.com/tomkat-cr/genericsuite` [GS-319].
- Publicación de post en inglés principal para redirigir a `https://www.carlosjramirez.com/en/genericsuite`.
- Mover el segundo banner de aniversario a la sección de lanzamientos.
- Reemplazar revisión de código de Github Gemini por SonarQube y Claude [GS-336].
- Mejorar el script de traducción para soportar modo 'changed' para traducir archivos Markdown actualizados. Añadido manejo de argumentos para selección de modo y lógica para identificar archivos cambiados en mkdocs_root/en. El modo por defecto es 'changed' y puede configurarse a 'uncommitted' para archivos sin confirmar. Esto mejora la flexibilidad de los procesos de traducción [GS-252].

##### Fixed
- `mkdocs_transfer_site.sh` elimina los directorios `docs_for_ftp` y `site`, y usa `.venv` en lugar de `venv` para evitar múltiples entornos Python [GS-301].
- `new-project-from-template.sh` maneja ramas e entrada de plantilla del usuario porque no se preguntaba debido a la asignación de valores predeterminados temprana [GS-306]
- Nueva validación de NAME solo si está seteado (scripts/new-project-from-template.sh) [GS-306]
- Documentación de BASECAMP_BRANCH sobre valor por defecto a "main" (scripts/new-project-from-template.sh) [GS-306]
- `scripts/rename-app.sh` — nueva pasada de renombrado de archivos para fastapitemplate* (arreglo de leftovers de openapi.json/yaml; probado en un directorio desechable, 5/5 comprobaciones, reproducido por el reviewer IA `packages/genericsuite-skills/skills/python-fastapi-code-builder` de IA) [GS-254].
- Error "Could not resolve dependency: formik@2.4.5" en ExampleApp [GS-254].
- Transferir scripts para usar "mkdocs_root" en lugar de "docs" [GS-208].
- `config-overrides.js` actualizado para corregir errores al ejecutar la app con RUN_BUNDLER="react-scripts" [GS-338].
- Valores AWS_S3_BUCKET_NAME* de FastApiTemplate en `.env.example`.
- Transferir scripts para usar "mkdocs_root" en lugar de "docs" [GS-208].

##### Security
- Actualizar dependencias en exampleapp y fastapitemplate en archivos de bloqueo de paquetes para múltiples aplicaciones. Cambios relevantes incluyen: cryptography, crypto-browserify, downshift, react-icons, react-markdown, react-syntax-highlighter, react-router-dom y yup [GS-219].
- Migrar a Python 3.14 [GS-337].
- Añadir documentación de rate limiter a GS BE Core `.env.example` [GS-332].
- Subir versión de Node.js en .nvmrc a 26 [GS-339].
- exampleapp y fastapitemplate: configuración de `users_user_history.json`, `users_config.json` y `users_api_keys.json` con `mandatoryFilters` para forzar al usuario actual [GS-327].
- exampleapp y fastapitemplate: configuración de `users_user_history_admin.json`, `users_config_admin.json` y `users_api_keys_admin.json` sin `mandatoryFilters` para permitir ver historial completo al editar usuarios [GS-327].
- exampleapp y fastapitemplate: Actualizar @babel/core a ^7.29.7 para corregir vulnerabilidad de lectura de archivos [CVE-2026-49356] [GS-219].

##### Removed
- AGENTS.md symlink [GS-303]
- `activeContext.md` movido al directorio del GS Superproject [GS-319]
- ".ai/settings.json" hooks específicos de MacOS (mover a ~/.claude/settings.json).
- Como Webpack no se usa en exampleapp y fastapitemplate, eliminar dependencias no necesarias (css-loader, postcss-loader, style-loader, react-icons, web-vitals, fs, json-loader, with, constants-browserify, crypto-browserify, os-browserify, stream-browserify, tty-browserify, url, vm-browserify, @babel/cli, @babel/preset-stage-0, @rollup/plugin-typescript, @testing-library/user-event, file-loader, url-loader, path, gh-pages, express, express-rate-limit)

## GenericSuite BaseCamp App

### Package, Pull Request and Tag

* Pull Request: https://github.com/tomkat-cr/genericsuite-basecamp-app/pull/2
* Tag: https://github.com/tomkat-cr/genericsuite-basecamp-app/releases/tag/1.0.0+4

### Pull Request Overview

Desarrollo inicial

Esta versión ("GS Doc", la aplicación móvil de visualización de documentación Flutter) añade archivos de contexto de IA, pruebas SAST y un conjunto de objetivos Makefile para abrir emuladores de iOS/Android, al tiempo que completa la migración desde el antiguo submódulo git `genericsuite-basecamp` en favor de obtener la documentación a través de `GS_BASECAMP_PATH`.

Highlights

- Nueva variable de entorno `GS_BASECAMP_PATH` y `run_docs_converter.sh` para clonar o reutilizar un checkout local de GenericSuite Basecamp
- Nuevos targets `make open-ios-simulator` / `open-android-emulator` para desarrollo local
- El submódulo `genericsuite-basecamp` se elimina en favor del flujo impulsado por `GS_BASECAMP_PATH`
- Licencia cambiada a MIT [FA-244]; corregidos problemas de imágenes que no se mostraban tras el cambio de prefijo de idioma [GS-252]

### CHANGELOG.md

#### [1.0.0+4] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a AI Coding Assistants [GS-303].
- Añadir pruebas SAST [GS-315].
- Variable de entorno `GS_BASECAMP_PATH` para especificar la ruta del repositorio GenericSuite Basecamp.
- Contenido de `README.md` con prerequisitos, instalación y uso [GS-303].
- `make open-ios-simulator` para abrir el simulador de Apple iOS.
- `open-android-emulator` y el script `open-android-emulator.sh`.

##### Changed
- Renombrar `assets/docs/` a `assets/mkdocs_root/` [GS-208].
- `run_docs_converter.sh` clonará el repo de GenericSuite Basecamp en el directorio `./genericsuite-basecamp` si `GS_BASECAMP_PATH` está vacío, de lo contrario usará la ruta especificada en `GS_BASECAMP_PATH`.
- Licencia cambiada a MIT [FA-244].

##### Fixed
- Las imágenes se muestran correctamente tras añadir el prefijo de idioma a la ruta [GS-252].

##### Removed
- Submódulo Git genericsuite-basecamp

## GenericSuite Gitops

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-gitops/pull/6](https://github.com/tomkat-cr/genericsuite-gitops/pull/6)
* Tag: [https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.5.0](https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.5.0)

### Pull Request Overview

Mejorar documentación de IA y mejorar la estructura de directorios

Una versión de mantenimiento enfocada: archivos de contexto de IA, pruebas SAST, renombramiento de directorios (`docs/` → `help/`, `specs/` → `docs/`), y migración a licencia MIT.

Highlights

- AGENTS.md, GEMINI.md y CLAUDE.md para agregar contexto a los agentes IA [GS-303]
- Pruebas SAST añadidas [GS-315]
- Unificación de estructura de directorios: `docs/` renombrado a `help/`, `specs/` renombrado a `docs/` [GS-303]
- Licencia cambiada a MIT [FA-244]

### CHANGELOG.md

#### [0.5.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a AI Coding Assistants [GS-303].
- Añadir Pruebas SAST [GS-315].

##### Changed
- Renombrar directorio `docs/` a `help/` [GS-303].
- Renombrar directorio `specs/` a `docs/` [GS-303].
- Licencia cambiada a MIT en archivos README.md [FA-244].

## GenericSuite App Maker (GSAM)

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/15](https://github.com/tomkat-cr/genericsuite-app-maker/pull/15)
* Tag: [https://github.com/tomkat-cr/genericsuite-app-maker/releases/tag/0.6.0](https://github.com/tomkat-cr/genericsuite-app-maker/releases/tag/0.6.0)

### Pull Request Overview

Documentación de IA + pruebas SAST + correcciones de vulnerabilidades + errores tipográficos y de redacción en README

Esta versión añade documentación de IA y pruebas SAST a GSAM, limpia la redacción del README y actualiza las dependencias de `requirements.txt` a sus últimas versiones para cerrar vulnerabilidades conocidas.

Highlights

- Archivos AGENTS.md, GEMINI.md y CLAUDE.md de IA añadidos, más pruebas SAST [GS-303] [GS-315]
- Targets de Makefile para `upgrade` y `update` para mantenimiento de dependencias [GS-219]
- Dependencias en `requirements.txt` actualizadas para corregir vulnerabilidades [GS-219]
- Se regeneró el lockfile y se eliminaron varios paquetes transitorios no usados (cohere, mistralai, gotrue, etc.) [GS-219]

### CHANGELOG.md

#### [0.6.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto y instrucciones a AI Coding Assistants [GS-303].
- Añadir pruebas SAST [GS-315].
- Objetivos de Makefile para "upgrade" y "update" [GS-219].

##### Changed
- Correcciones tipográficas en README [GS-128].

##### Security
- Actualizar dependencias a las versiones más recientes [GS-219].
- Migrar a Python 3.14 [GS-337]
- `gsam_ottomator_agent/base_python_docker/Dockerfile` usa Python 3.14 [GS-337]

##### Removed
- Regenerar lockfile elimina paquetes que no estaban presentes previamente: cohere, mistralai, gotrue, etc. [GS-219].

## GenericSuite Mobile

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-mobile/pull/2](https://github.com/tomkat-cr/genericsuite-mobile/pull/2)
* Tag: [https://github.com/tomkat-cr/genericsuite-mobile/releases/tag/0.5.0](https://github.com/tomkat-cr/genericsuite-mobile/releases/tag/0.5.0)

### Pull Request Overview

Desarrollo inicial de GenericSuite Mobile para Flutter

Este lanzamiento trae soporte de relaciones 1-N `childComponents` en el Editor CRUD de Flutter (secciones secundarias pulsables, edición a pantalla completa, subtipos `array`/`table` que coinciden con el comportamiento de genericsuite-fe), un sistema de tokens de tema limpio de Apple basado en `shadcn_ui`, y una gran tanda de correcciones defensivas de errores en el editor CRUD, formularios, manejo de autenticación/sesión y navegación — además de pruebas SAST y el campo `select_table` heredado de 0.4.2.

Highlights

- Soporte de `childComponents` (1-N) en el Editor CRUD de Flutter, a la par de genericsuite-fe [GS-261].
- Nuevo sistema de temas basado en Apple-clean `shadcn_ui` con contrato de fusión de `defaultThemeParams` [GS-261].
- Amplia pasada de correcciones de errores: decodificación de JWT, filtrado de disposed, timeouts, llamadas API sincrónicas, etc. [GS-327].
- Campo `select_table` con resolución de descripciones de registros relacionados, heredado de 0.4.2 [GS-259].

### CHANGELOG.md

#### [0.5.0] - 2026-08-30

##### Added
- Soporte de `childComponents` (relaciones 1-N) en el Editor CRUD de Flutter: los componentes hijos declarados en la configuración JSON del frontend se muestran como secciones pulsables en el formulario de edición, se abren a pantalla completa con el registro padre como `parentData`, y soportan ediciones de `child_listing` con subtipos `array` y `table` (incluidos los payloads de escritura `<array_name>`/`<array_name>_old`), replicando el comportamiento del CRUD Editor de genericsuite-fe [GS-261].
- Tokens de tema con estilo Apple-limpio en `theme_config_defaults.dart` (`accentColor`, `borderRadius` 12px, `fontFamily`/`textTheme` con Inter vía google_fonts, texto casi negro `textColor`, colores semánticos del sistema iOS) y contrato de fusión `defaultThemeParams` para que las apps sólo sobrescriban las claves necesarias [GS-261].
- `shadcn_ui` (port de flutter-shadcn-ui) ahora es raíz del árbol de widgets mediante `ShadApp.custom`; `CreateGsApp` construye el tema MaterialApp a partir de los tokens genéricos; los botones Save/Cancel usan ShadButton [GS-261].
- `buildGsShadTheme()` construye `ShadThemeData` a partir de los tokens de tema genéricos; nuevo parámetro `shadColorSchemeName` para seleccionar el esquema base de shadcn (`green` por defecto; cualquier valor de `ShadColorScheme.fromName`), con `accentColor` que sobrescribe `primary`/`ring` y los tokens GS de superficie/texto/errores aplicados mediante `copyWith` [GS-261].
- Nuevos comandos de Makefile: "lint" y "test".
- Cobertura de pruebas para el proyecto [GS-327].

##### Changed
- Color de acento por defecto cambiado de azul a verde; la barra de aplicación y el cajón usan superficies blancas con texto casi negro; versión de genericsuite_flutter actualizada a 0.5.0 [GS-261].
- La configuración detallada en README.md se movió a la documentación de GS Basecamp [GS-261].

##### Fixed
- http_service.dart [GS-327]:
  1. getJwtPayload usa ascii.decode(...) en lugar de utf8.decode(...) para decodificar el payload del JWT. Cualquier afirmación con caracteres no ASCII lanza FormatException, rompiendo verificaciones de login-gate, loadConfig y current_user_service.dart.
  2. No hay `.timeout(...)` en ninguna llamada http.get/post/put/delete/patch (a diferencia de ip_address_service.dart, que sí lo usa), así que una conexión colgada bloquea al llamador indefinidamente.
  3. La ruta de éxito 200/201 (json.decode(response.body)) tampoco tiene try/catch; la rama de error sí lo tiene. Flags de depuración (debugJwtToken, debugConfigValues) imprimirían JWTs/claves API si se activaran, actualmente están desactivados.
  4. Añadir anotaciones de tipos a `bToA(str)`.
- create_gs_app.dart: payload["exp"] * 1000 no tiene check de null; un token con payload que carece de exp (o un token mal formado donde `getJwtPayload` devuelve `{}`) provoca una excepción en `build()`, deteniendo el inicio de la app en lugar de volver a la página de inicio de sesión. Verificado por lectura directa [GS-327].
- crud_editor.dart [GS-327]:
  1. _saveItem: si `isCreation` y `editorConfig['createReenter']` es true tras un guardado exitoso, el método retorna sin llamar `setState()`; `_isLoading` se activa con `setState()` pero luego se reasigna, por lo que el spinner de carga podría quedar activo indefinidamente.
  2. No hay comprobaciones de mounted después de `await` antes de `setState`/_`setStateAndShowMessages` (p. ej. en `_buildListItem` onTap, `initState` `_loadConfig().then`); navegar fuera durante la solicitud puede lanzar "setState() called after dispose()".
  3. `json.decode(localApiResp['resultset'])` en `_loadSelectedItem` sin `try/catch` a diferencia de `_loadItems`, y `int.parse(...['rows_affected'])` sin protección.
  4. `_getSelectFieldsOptions` — espera secuencial en un bucle en lugar de `Future.wait`, encadenando llamadas de red innecesariamente.
- crud_editor_commons.dart [GS-327]:
  1. `(buildChildRowToSave)`: `parentData` indexado por `keyPair['parentElementName']` sin revisión de null.
  2. `parentData` puede estar vacío/faltante (p. ej. `_setEndpointFilter` no hace nada), por lo que guardar/eliminar en un editor `child_listing` puede lanzar `NoSuchMethodError`.
- form_field_service.dart [GS-327]:
  1. Casos de `select` y `select_component` configuran `DropdownButtonFormField.initialValue` sin verificar que el valor exista entre los elementos, a diferencia del caso `select_table` que verifica con `containsKey(...) ? value : null`.
  2. Datos editados obsoletos fallan al abrir el formulario. Campos numéricos convierten con `double.parse`/`int.parse` en cada pulsación; borrar el campo o escribir `./-` lanza `FormatException` no capturada.
  3. `TextEditingController(text: ...)` creado en línea en `build()` para la mayoría de tipos de campo y nunca eliminado; cada reconstrucción filtra el controlador anterior y restablece el cursor/foco en todos los campos de la pantalla.
- app_drawer.dart [GS-327]:
  1. `Icon(item['callable']['icon'])` rompe si `item['element']` no es clave en `callables`; sin fallback/guard.
  2. `_loadConfig().then(...)` no tiene manejo de errores; las excepciones se vuelven errores async no manejados.
- error_reporter_widget.dart: `ScaffoldMessenger.of(context).showSnackBar(...)` se llama de forma sincrónica dentro de `build()` — anti-patrón conocido de Flutter que debe diferirse con `addPostFrameCallback`, como en `homepage.dart` en otro lugar.
- login.dart [GS-327]:
  1. `_usernameController`/`_passwordController` se crean pero el widget no tiene `dispose()`, ocasionando fuga de ambos controladores de texto.
  2. `apiResponse['resultset']['token']` se accede sin comprobación de `resultset`. Campo "password" no tiene autocompletado desactivado.
- current_user_service.dart: `if (data['error'] == 'Not Found')` nunca puede ser verdadero ya que `http_service.dart` siempre devuelve `error` como booleano; este branch es código muerto [GS-327].
- logout_service.dart: llamadas a `storage.delete(...)` para jwt/api_key/user_data no esperan a su finalización antes de navegar; la app podría terminarse con credenciales antiguas en almacenamiento seguro [GS-327].
- routing_services.dart: se añadió `item['callable']['type'] = 'async'` (por defecto) | 'sync' para permitir llamadas síncronas/asíncronas y manejar el cambio en `logout_service.dart` [GS-327].
- locator_service.dart: `registerLazySingleton` sin guardia `isRegistered`; reiniciar configuración (hot restart, remount, tests) lanza por duplicación de registro [GS-327].
- timestamp_utilities.dart: formateo de 12 horas no maneja medianoche de forma especial; la hora 0 se muestra como "0:MM AM" en lugar de "12:MM AM" [GS-327].
- homepage.dart: `loadHomeData(true)` se llama directamente como el `future` del `FutureBuilder`; esto vuelve a disparar la llamada API en cada reconstrucción antes de que haya datos [GS-327].
- deviceid_service.dart: dependencia implícita de orden en `setupStorageLocator()` debe ejecutarse primero [GS-327].
- back_button.dart: `Navigator.of(context, rootNavigator: true).pop(context)` pasando `context` como resultado de la salida parece no intencional [GS-327].
- La guardia de guardado de CRUD Editor y otras partes han sido ajustadas para arreglar varios comportamientos problemáticos descritos en la extensa lista de cambios [GS-261].
- `suggestion_dropdown`: el texto tipificado ahora se almacena en la fila en memoria (`selectedItem`) al cambiar y al guardar, para alinear con el comportamiento de genericsuite-fe [GS-261].
- `suggestion_dropdown`: las filas de sugerencias se leen de la misma forma en que los listados de CRUD decodifican `resultset` (lista ya decodificada, cadena JSON o `{resultset: [...]}` anidado), para que el overlay muestre opciones cuando la API devuelve filas [GS-261].
- `suggestion_dropdown`: al seleccionar una sugerencia ya no se copian las claves de la tabla relacionada (`_id`, `name`, …) a la fila guardada. Solo el campo del formulario y `autocomplete_fields` se escriben, en línea con genericsuite-fe [GS-261].
- El campo de contraseña muestra hash SHA-256 en lugar de texto plano. La contraseña inicial debe estar en blanco [GS-261].

##### Removed
- El directorio `flutter_project_template`. Utilizar [genericsuite-mobile-exampleapp](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp) en su lugar [GS-261].

#### [0.4.2] - 2026-04-20

##### Added
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a AI Coding Assistants [GS-303].
- Añadir campo `select_table` en Flutter CRUD editor: listado y formulario de solo lectura muestran la descripción del registro relacionado (backend `{field}_description` con fallback en caché del cliente); crear/editar renderiza un dropdown poblado desde la tabla relacionada [GS-259].

##### Changed
- Correcciones menores en README.md.
- Licencia cambiada a MIT [FA-244].
- Actualizar `.gitignore` para incluir directorios de IA Agents [GS-303].

##### Fixed
- Mejorar manejo de errores en `create_gs_app.dart` y `ip_address_service.dart` para mayor estabilidad y arreglar despliegue Flutter web [GS-252].

## GenericSuite Mobile ExampleApp

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/pull/2](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/pull/2)
* Tag: [https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/releases/tag/1.0.0+1](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/releases/tag/1.0.0+1)

### Pull Request Overview

Desarrollo inicial. Migrado desde genericsuite-mobile

Este es un nuevo submódulo separado del antiguo directorio `flutter_project_template` de `genericsuite-mobile` hacia su propio repositorio de ejemplo de aplicación, dando a la librería Flutter una referencia de implementación dedicada y versionada de forma independiente.

Highlights

- Separación del repositorio desde `genericsuite-mobile` hacia `genericsuite-mobile-exampleapp` [GS-261].
- Establece una aplicación de ejemplo Flutter independiente y versionada.

### CHANGELOG.md

#### [1.0.0+1] - 2026-08-30

##### Added
- Migrado de `genericsuite-mobile` a `genericsuite-mobile-exampleapp`.

## GenericSuite AI Agent Skills

### Package, Pull Request and Tag

* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-skills/pull/1](https://github.com/tomkat-cr/genericsuite-skills/pull/1)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-skills/pull/3](https://github.com/tomkat-cr/genericsuite-skills/pull/3)
* Tag: [https://github.com/tomkat-cr/genericsuite-skills/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-skills/releases/tag/1.0.0)

### Pull Request Overview

Agregar plugin Claude Skills de gs-app-builder-suite [GS-254]

Se introduce el grupo de plugins `gs-app-builder-suite` — un "orchestrator" de habilidades (`gs-app-builder`) más habilidades especializadas de generadores de apps para andamiaje, configuración, JSX, menús, endpoints, Python-FastAPI, IA de código/herramientas, y servidores MCP — junto con un conjunto de evaluaciones y un mecanismo de sincronización de referencias para alinear las habilidades con la documentación del ecosistema GenericSuite.

Highlights

- Nuevo grupo de plugins `gs-app-builder-suite` con un orquestador más 9 habilidades de generadores [GS-254].
- Suite de evals/evals.json para validar la ejecución en tiempo real [GS-254].
- Mecanismo de sincronización de referencias (`make sync-references`) para alinear las habilidades con la documentación de GS [GS-254].
- Habilidad `release-notes` movida fuera al GS Superproject [GS-191].

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Added
- Idea de proyecto y desarrollo inicial (2026-04-12) [GS-254].
- Habilidades de app-builder (`gs-app-builder-suite` grupo de plugins):
  `gs-app-builder` orquestador (detección modo greenfield/brownfield, entrevista breve de la app, flujo con checkpoints), `app-starter`, `config-builder` (actualizado),
  `jsx-code-builder` (actualizado), `menu-builder`, `endpoints-builder`,
  `python-fastapi-code-builder`, `python-ai-code-builder`,
  `python-ai-tools-code-builder`, `jsx-ai-code-builder`, `mcp-builder`.
- Paquetes `evals/evals.json` (todas las habilidades de suite excepto config-builder) con aserciones de validez en tiempo de ejecución, en `playground/` [GS-254].
- Mecanismo de sincronización de referencias: `skills/update-gs-docs` mapa + script, `make sync-references` [GS-254].
- Añadir pruebas SAST [GS-315].

##### Changed
- Marketplace: grupo de plugins de marketplace `code-generation-skills` renombrado a `gs-app-builder-suite`; versión de metadatos 1.1.0 [GS-254].
- Reescritura de README alrededor de la suite de app-builder, instalación y publicación [GS-254].

##### Removed
- Habilidad `release-notes` eliminada del marketplace, y eliminación del SKILL.md (movido al directorio GS Superproject) [GS-191].

##### Security
- Migrar a Python 3.14 [GS-337].
- Subir la versión de Node.js en .nvmrc a 26 [GS-339].

## GenericSuite Security

### Package, Pull Request and Tag

* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-security/pull/4](https://github.com/tomkat-cr/genericsuite-security/pull/3)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-security/pull/4](https://github.com/tomkat-cr/genericsuite-security/pull/4)
* Tag: [https://github.com/tomkat-cr/genericsuite-security/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-security/releases/tag/1.0.0)

### Pull Request Overview

Ideación de proyecto y desarrollo inicial

Nueva submódulo creado en respuesta directa al ataque de la cadena de suministro npm de Keyv/Cacheable el 2026-08-04. Envia cinco habilidades Claude para auditoría de seguridad de la cadena de suministro y lista de producción: escaneo IOC, generador de corpus para toda la organización, escáner de imágenes Docker/contener, escáner de dependencias de GitHub Actions/pinging de dependencias, y analizador de debilidades/preparación para múltiples proyectos — además de un plugin de marketplace registrado.

Highlights

- `supply-chain-ioc-scan` — detectar si un paquete npm/PyPI comprometido o un gusano de la cadena de suministro afecta esta máquina o árbol de repositorios [GS-339].
- `repo-corpus` → `repo-docker-scanner` → `repo-packages-scanner` — escaneo org-wide en tres fases (manifiesto de corpus, referencias de imágenes, detecciones de acciones)
- `project-weakness-analysis` — evaluación de ready-to-run en producción y auditoría de riesgos de seguridad para múltiples proyectos a la vez.
- Cinco modelos de IA evalu — para mantener alineación con la documentación de GS.

##### Changed
- `repo-corpus` y los dos escáneres planificados comparten una única ruta de código, usando un corpus en lugar de enumerar repositorios individualmente.

##### Fixed
- Revisión de reglas de prioridad en `repo-docker-scanner` corregida para usar una leyenda basada en `policy/images.json`.
- Detección de plantillas YAML/CloudFormation como P0 independientemente de su ubicación.
- Corrección de informes y descubrimiento de Dockerfiles; las referencias no resueltas se muestran tal cual.
- Varios ajustes de flujo de tests y preflight para entornos: se simula el entorno de git sin hooks, se desactiva hooks, etc.
- Correcciones de migración a Python 3.14 [GS-337].
- Actualizar Node.js a 26 [GS-339].

##### Security
- Actualizar dependencias para arreglar vulnerabilidades múltiples en LangChain, cryptography, pyjwt, etc. [GS-219].
- Migrar a Python 3.14 [GS-337].
- Añadir rate limiter en documentación y scripts [GS-332].
- Actualizar Node.js a 26 [GS-339].

##### Removed
- Actualizaciones de limpieza de dependencias no utilizadas y herramientas desfasadas.

