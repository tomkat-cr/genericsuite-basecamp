# 20260830 - v1.0.0

![GS_Release_2026-08-30_Image_1A.png](./images/GS_Release_2026-08-30_Image_1A.jpeg)

Fecha: 2026-08-30

## Resumen

Presentamos v1.0.0: ¡El Superproyecto GenericSuite está en vivo! 🚀

Este lanzamiento marca un hito fundamental para el ecosistema: se introduce un **paquete de desarrollo de aplicaciones móviles en Flutter**, **habilidades de generación de código**, **herramientas y políticas de seguridad**, y una **aplicación móvil de documentación**. También GenericSuite ahora se distribuye como un único **Superproyecto**, reuniendo los 16 paquetes como submódulos de git bajo un monorepo, con automatización compartida y contexto de IA-agente que guía a cada paquete por igual. Es el mayor lanzamiento estructural en la historia de GenericSuite, y va acompañado de una amplia fase de endurecimiento y expansión en todos los frentes.

Beneficios profesionales clave:

- **Nuevos Paquetes**: `genericsuite-mobile`, `genericsuite-mobile-exampleapp` (para desarrollo de apps móviles con Flutter), `genericsuite-basecamp-app` (aplicación móvil de documentación), `genericsuite-skills` (habilidades de generación de aplicaciones), `genericsuite-security` (herramientas y políticas de seguridad), y `genericsuite-fe-scripts` (scripts comunes de frontend), todos debutan en este ciclo, además de una nueva ruta de despliegue OpenTofu (Terraform).

- **Un Ecosistema, un Hogar**: El nuevo Superproyecto orquesta todos los paquetes de GenericSuite — frontend, backend, móvil, scripts, docs, y ahora seguridad — desde una única raíz, con archivos de contexto `AGENTS.md`/`GEMINI.md`/`CLAUDE.md` enlazados a través de cada paquete para asistentes de Codificación IA.

- **Seguridad, en Todas Partes**: Python 3.14 y Node.js 26 en todo el conjunto, ecosistema con licencia MIT, decenas de correcciones CVE (axios, LangChain/aiohttp, Vite, Forge), límites de tasa en FastAPI/Flask, y una nueva **GenericSuite Security Suite** — cinco habilidades Claude nacidas directamente de la respuesta al gusano de la cadena de suministro npm de Shai-Hulud.

- **Relaciones 1-1 y 1-N, en Todas Partes**: El nuevo tipo de campo `select_table` llega a los editores CRUD de React y Flutter, uniéndose al soporte de `childComponents` de Flutter para relaciones 1-N.

- **Almacenamiento y Secretos Multinube**: GCP Cloud Storage y Azure Blob Storage se unen a AWS S3, además de GCP Secret Manager y Azure Key Vault como backends de secretos — genericsuite-be empieza a comunicarse con las tres grandes nubes.

- **Despliegues en AWS con OpenTofu**: la nueva ruta OpenTofu (Terraform) de despliegue, junto con CloudFormation para despliegues en AWS.

Consulta el registro completo de cambios para todos los detalles en los 16 paquetes.

## Superproyecto GenericSuite

### Paquete, Pull Request y Etiqueta

* Pull Request: [https://github.com/tomkat-cr/genericsuite/pull/2](https://github.com/tomkat-cr/genericsuite/pull/2)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite/releases/tag/1.0.0)

### Resumen de Pull Request

Presentando la estructura del superproyecto GenericSuite

Esta pull request establece la estructura del Superproyecto GenericSuite como una capa de orquestación de un monorepo, reuniendo los 16 paquetes de GenericSuite como submódulos de git bajo un único repositorio. Añade scripts de automatización para sincronizar y gestionar paquetes, documentación a nivel de proyecto y archivos de contexto de IA para Asistentes de Codificación IA, sentando las bases para lanzamientos coordinados a nivel de todo el ecosistema como este.

Destacados

- Capa de orquestación de monorepo: todos los paquetes de GenericSuite (`genericsuite-fe`, `genericsuite-be`, `genericsuite-be-ai`, `genericsuite-fe-ai`, `genericsuite-basecamp`, y más) se gestionan ahora como submódulos de git bajo `packages/`, con `make update-packages` para sincronizarlos.
- Contexto del Asistente de Codificación IA: `AGENTS.md`, `GEMINI.md`, y `CLAUDE.md` brindan a Claude Code, Gemini CLI, Cursor, Antigravity y otros asistentes directrices consistentes a lo largo de todo el ecosistema.
- Nueva habilidad de IA `release-notes`: automatiza la recopilación de changelogs, PRs y etiquetas en todos los paquetes para producir este propio changelog de release y sus resúmenes en redes sociales.

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Añadido
- Añadir: Presentar la estructura del superproyecto GenericSuite con submódulos de git, scripts de automatización y documentación del proyecto, para facilitar la gestión, el cambio y el despliegue del proyecto en su conjunto [GS-319].
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes de Codificación IA [GS-303].
- Añadir la habilidad `release-notes` al directorio `.ai./skills`, para generar notas de lanzamiento y resúmenes para redes sociales del proyecto [GS-191].

##### Cambiado
- Licencia cambiada a MIT [FA-244].
- Rename AWS_S3_BUCKET_NAME to AWS_S3_BUCKET_NAME_FE en el archivo .env y scripts [GS-328].
- `webpack.config.js` y `config-overrides.js`: se comentaron los polyfills del módulo central de Node.js `resolve.fallback` (`os`, `url`, `crypto`, `stream`, `assert`, `vm`, `tty`, `constants`) ya que nada en la base de código los necesita y Vite ya funciona sin ellos; se añaden notas `npm install --save-dev ...` sobre cada uno para que puedan reactivarse si el gráfico de dependencias de un consumidor lo necesita [GS-338].
- Actualizar .npmignore para incluir archivos y directorios adicionales para Claude Code, AI Agents y OpenTofu [GS-327].
- Actualizar versión a 1.0.0 en package.json, package-lock.json y version.txt para reflejar el último lanzamiento [GS-327].

##### Fixeado
- getFieldElementsYupValidations() no funcionaba con action=CREATION; se desactivaron las validaciones de Yup por ahora [GS-251].
- Versión del paquete `bson` fijada a 7.2.0 para corregir el error "Uncaught TypeError: globalThis?.process?.getBuiltinModule is not a function" tras actualizar vite a la versión 8 [GS-268].
- `tsconfig.json` carecía de un `exclude` para `*.test.tsx`, por lo que cada archivo de prueba recibía su propio stub `.d.ts` durante la construcción de Rollup. Dado que `dist` está incluido en el paquete npm publicado, se generaron ~24 archivos de declaración inútiles en cada lanzamiento [GS-338].
- `rollup.config.mjs`: añadido `bson` y `js-md5` al arreglo `external`. Ambos son dependencias pares reales usadas en `src/lib/services/id.utilities.jsx` y `md5.utilities.jsx`, pero faltaban en `external`, por lo que Rollup los empacaba directamente en `dist` en lugar de tratarlos como dependencias pares de los consumidores [GS-338].
- Eliminada una entrada `with` del config de Webpack `resolve.fallback` — `with` no es un módulo central de Node.js, por lo que el fallback nunca hacía nada [GS-338].
- "config-overrides.js" actualizado para corregir errores al ejecutar la app con RUN_BUNDLER="react-scripts" [GS-338] y refactorizado para usar fileURLToPath para resolución de rutas y limpieza de logs de depuración no usados [GS-327].
- Documentación de instalación de la dependencia "process" en el archivo "webpack.config.js" para corregir errores al ejecutar la app [GS-338].
- "generic.editor.rfc.common.jsx" y "generic.editor.rfc.service.jsx" corregidos para mostrar errores de configuración eventual en listados de hijos, y actualizados para mostrar el nombre del editor en los mensajes de error [GS-327].
- "vite.config.mjs" actualizado para corregir el aviso "(!) Your Vite config uses features that are unsupported by `configLoader: 'native'` ..." tras actualizar vite a la versión 8 [GS-268].

##### Seguridad
- Actualización de dependencias a la última versión: crypto-browserify@^3.12.1, downshift@^9.4.0, react-icons@^5.7.0, react-markdown@^10.1.0, react-syntax-highlighter@^16.1.1 [GS-219] [GS-214].
- Actualización de axios@^1.19.0 para corregir vulnerabilidades [GS-219]:
  - SSRF, inyección de información sensible, modificaciones inseguras de atributos, etc. (descritos en la lista original) [GS-219].
- Actualización de yup@^1.7.1 para corregir vulnerabilidades [GS-219]:
  - Inyección de código arbitrario y otros vectores asociados [GS-219].
- Actualización de react-router-dom@^7.18.2 para corregir vulnerabilidad de seguridad [GS-219]:
  - Varios vectores de CSRF y otros problemas de seguridad relacionados con rutas.
- "react" y "react-dom" ahora tienen dependencias pares con "^18.2.0" (esto no afecta este código, ya que solamente se usan rutas de navegador); será actualizado a 19 en la próxima versión para corregir la vulnerabilidad mencionada [GS-219].
- Aumento de la versión de Node.js en .nvmrc a 26 [GS-339].
- Los archivos de configuración de usuario `users_user_history.json`, `users_config.json` y `users_api_keys.json` ahora usan el parámetro "mandatoryFilters" para asegurar que el historial de usuarios, la configuración y las claves API estén forzados al usuario actual [GS-327].
- Los archivos de configuración `users_user_history_admin.json`, `users_config_admin.json` y `users_api_keys_admin.json` no usan "mandatoryFilters" para permitir que el superusuario vea todo el historial de usuarios, configuraciones y claves API al editar usuarios [GS-327].
- Actualizar @babel/core a ^7.29.7 para corregir vulnerabilidad de lectura de archivos a través de un comentario de sourceMappingURL ([CVE-2026-49356]) [GS-219].

##### Eliminado
- El directorio `scripts/` se movió a la [biblioteca de scripts frontend](https://github.com/tomkat-cr/genericsuite-fe-scripts) [GS-107].
- Dependencias pares no usadas: `react-icons`, `web-vitals`, `fs`, `json-loader`, `with`, `constants-browserify`, `crypto-browserify`, `os-browserify`, `stream-browserify`, `tty-browserify`, `url`, `vm-browserify`. Ninguna se importa en `src/`, y los shims de módulos centrales de Node se usaban solo en las configuraciones de desarrollo opcionales de webpack/`react-app-rewired` [GS-338].
- DevDependencies no usadas: `@babel/cli` (nadie invoca el binario Babel), `@babel/preset-stage-0` (no referenciado), `@rollup/plugin-typescript` (superado por `rollup-plugin-typescript2`), `@testing-library/user-event` (uso en pruebas presente), `file-loader` y `url-loader` (los SVGs usan el `asset/resource` de webpack 5), `path` (todas las llamadas `require('path')` resuelven al núcleo de Node), etc. [GS-338].
- Atributo `id="copyButton"` quitado del componente <CopyButton /> [GS-327].

## GenericSuite Frontend AI

### Paquete, Pull Request y Etiqueta

* Paquete: [https://www.npmjs.com/package/genericsuite-ai/v/1.3.0](https://www.npmjs.com/package/genericsuite-ai/v/1.3.0)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/11](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/11)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/12](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/12)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.3.0](https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.3.0)

### Resumen de Pull Request

Documentación de agentes IA, scripts movidos a GS FE Scripts, licencia MIT y actualizaciones de seguridad

Refleja el lanzamiento central de FE: documentación de IA agents, relicensing con MIT y movimiento del directorio de scripts a `genericsuite-fe-scripts`. Añade pulido de la interfaz de ChatBot UI (botón de copiar con icono, mejor renderizado de bloques de código) y corrige un error de resolución de dependencias de Formik que afectaba a consumidores de ExampleApp/FastApiTemplate, junto con la misma gran limpieza de dependencias de seguridad que FE Core, además de actualizaciones de Jest/Rollup-Plugin-Typescript.

Destacados

- Fijado: error “Could not resolve dependency: formik@2.4.5” que afectaba a consumidores de ExampleApp/FastApiTemplate [GS-254].
- Bloques de código de conversación de ChatBot: botón de copiar con icono y mejoras de renderizado [GS-214].
- `scripts/` movido a `genericsuite-fe-scripts`; Licencia cambiada a MIT [GS-107] [FA-244].
- Seguridad: actualizaciones de axios, yup, react-router-dom, jest, rollup-plugin-typescript2/typescript, y @babel/core para corregir numerosas vulnerabilidades de alta/criticalidad, incluyendo vectores de RCE y DoS [GS-219].
- Limpieza de construcción/dependencias: se eliminaron dependencias pares/dev no usadas (css-loader, postcss-loader, gh-pages, etc.) [GS-338].

### CHANGELOG.md

#### [1.3.0] - 2026-08-30

##### Añadido
- AGENTS.md, GEMINI.md, y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes de Codificación IA [GS-303].
- Añadir pruebas SAST [GS-315].
- Añadir biblioteca de scripts de frontend [GS-107].

##### Cambiado
- Licencia cambiada a MIT [FA-244].
- Renombrar AWS_S3_BUCKET_NAME a AWS_S3_BUCKET_NAME_FE en el archivo .env [GS-328].
- Bloques de código de conversación de ChatBot: mejoras de bloques y diseño [GS-214].
- Añadir script "tailwind-build" para deploy_* y run_* en Makefile [GS-214].
- `webpack.config.js` y `config-overrides.js`: se comentaron polyfills del módulo central de Node `resolve.fallback` (`os`, `url`, `crypto`, `stream`, `assert`, `vm`, `tty`, `constants`, `zlib`, `https`, `http`, `util`) ya que nada en la base de código los necesita y Vite ya funciona sin ellos; se añaden notas `npm install --save-dev ...` para reactivarlos si el grafo de dependencias del usuario lo requiere [GS-338].
- Actualizar versión a 1.3.0 en package.json, package-lock.json y version.txt para reflejar el último lanzamiento [GS-327].

##### Fixeado
- Error "Could not resolve dependency: formik@2.4.5" en `ExampleApp`, `FastApiTemplate` y todas las apps que usan `genericsuite-fe-ai` como dependencia [GS-254].
- Error "installHook.js:1 TypeError: JY.default.includes is not a function" cuando ciertas conversaciones de ChatBot se hacen clic y la página queda vacía [GS-214].
- `tsconfig.json` tenía falta de `exclude` para `*.test.tsx`, emitiéndose ~14 archivos de declaración en `dist/esm` y `dist/cjs` durante la construcción de Rollup. Estos archivos ya estaban en el repo y se publican con cada npm publish [GS-338].
- Eliminar entrada ilegítima `"with"` de la configuración `config-overrides.js` `resolve.fallback` — `with` no es un módulo central de Node.js, por lo que el fallback nunca hizo nada [GS-338].
- Actualizar `config-overrides.js` para corregir errores al ejecutar la app con RUN_BUNDLER="react-scripts" [GS-338], y refactor para usar fileURLToPath para resolución de rutas y limpieza de logs de depuración no usados [GS-327].
- Documentación de instalación de la dependencia "process" en `webpack.config.js` para corregir errores al ejecutar la app [GS-338].
- Correcciones en `generic.editor.rfc.*.jsx` para mostrar errores de configuración en listados de hijos y mostrar el nombre del editor en los mensajes de error [GS-327].
- Actualización de `vite.config.mjs` para corregir el mensaje de compatibilidad tras actualizar vite a la versión 8 [GS-268].

##### Seguridad
- Actualización de dependencias a versiones más recientes para corregir múltiples vulnerabilidades [GS-219].
- Actualización de axios, yup, react-router-dom y otras dependencias para corregir vulnerabilidades de seguridad listadas [GS-219].
- Actualizar Node.js a 26 en .nvmrc [GS-339].
- Otras mejoras de seguridad y migraciones a Python 3.14 [GS-337].

##### Eliminado
- El directorio `scripts/` movido a la biblioteca de scripts frontend [GS-107].
- Eliminación de varias dependencias y devDependencies no usadas y rutas obsoletas descritas en la lista de Eliminados [GS-338].
- Eliminación del atributo `id="copyButton"` del componente <ChatCopyButton /> [GS-327].

## GenericSuite Frontend Scripts

### Paquete, Pull Request y Etiqueta

* Paquete: [https://www.npmjs.com/package/genericsuite-fe-scripts/v/1.0.0](https://www.npmjs.com/package/genericsuite-fe-scripts/v/1.0.0)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/2](https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/2)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/3](https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/3)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe-scripts/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-fe-scripts/releases/tag/1.0.0)

### Resumen de Pull Request

Crear la biblioteca de scripts GS FE, despliegue frontend expandido para uso en páginas de aterrizaje, prueba SAST, OpenTofu para despliegue FE

El lanzamiento de debut de la biblioteca de scripts frontend de GenericSuite — separada del directorio `scripts/` de `genericsuite-fe` en su propio paquete independiente y reutilizable. Expande el despliegue frontend de S3 para soportar páginas de aterrizaje (no solo la app principal) y añade una tubería de despliegue completa basada en OpenTofu (S3 privado + CloudFront con Origin Access Control, enrutamiento SPA, TLS 1.2 y estado remoto S3) paralela al despliegue de scripts en bash existente.

Destacados

- Nueva biblioteca independiente de scripts frontend, extraída de `genericsuite-fe` [GS-107].
- Nuevo módulo OpenTofu `frontend-hosting`: S3 privado + CloudFront (OAC, TLSv1.2_2021, enrutamiento SPA) con pipeline completo `aws_tf_deploy_to_s3.sh` [GS-334].
- Despliegue FE S3 expandido para soportar páginas de aterrizaje, no solo la app principal [GS-328].

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Añadido
- Crear la biblioteca de scripts frontend [GS-107].
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes de Codificación IA [GS-303].
- Despliegue de infraestructura OpenTofu (IaC) compatible con Terraform en `scripts/aws_tf`: módulo `frontend-hosting` (S3 privado + CloudFront con Origin Access Control, redirección a https, TLSv1.2_2021, enrutamiento SPA) y tubería completa `aws_tf_deploy_to_s3.sh` (tofu apply + build + S3 sync + CloudFront invalidation), con estado remoto S3 — paralelo al existente `aws_deploy_to_s3.sh`, que permanece sin cambios [GS-334].

##### Cambiado
- Cambiar despliegue FE S3 para usarlo en Páginas de Aterrizaje [GS-328].
- Renombrar AWS_S3_BUCKET_NAME a AWS_S3_BUCKET_NAME_FE en el archivo .env y scripts [GS-328].
- Mejorar `aws_deploy_to_s3.sh`: establecer valores por defecto para RUN_BUNDLER, UPDATE_BUILD y BUILD_DIR si no se especifican; mejorar manejo de nombres de bucket y verificación de distribución CloudFront. Actualizar la página de inicio en package.json durante el despliegue y restaurarla solo si RUN_BUNDLER != none. Usar BUILD_DIR para establecer el directorio de build, de modo que el despliegue móvil (que no es react-vite) pueda hacerse.
- Actualizar .npmignore para incluir archivos y directorios adicionales para Claude Code, AI Agents y OpenTofu [GS-327].

##### Seguridad
- Aumento de la versión de Node.js en .nvmrc a 26 [GS-339].

## GenericSuite Backend Core

### Paquete, Pull Request y Etiqueta

* Paquete: [https://pypi.org/project/genericsuite/0.4.0/](https://pypi.org/project/genericsuite/0.4.0/)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-be/pull/16](https://github.com/tomkat-cr/genericsuite-be/pull/16)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-be/pull/16](https://github.com/tomkat-cr/genericsuite-be/pull/19)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.4.0](https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.4.0)

### Resumen de Pull Request

OPENSPEC, mejorar documentación de IA, mejorar medidas de seguridad, licencia MIT y pruebas unitarias

Este lanzamiento añade implementaciones completas de abstracción de almacenamiento en GCP Cloud Storage y Azure Blob Storage (coincidiendo con el soporte existente de AWS S3), además de backends de secretos GCP Secret Manager y Azure Key Vault — expandiendo el diseño independiente de la nube a dos proveedores más. También añade rate limiting con FastAPI/Flask, cobertura de pruebas unitarias general, un resolver de relaciones 1-1 `select_table` en todos los motores de DB, relicensado MIT y una pasada de seguridad (pyjwt, cryptography, urllib3) más una corrección de path traversal en `app_context.py`.

Destacados

- Soporte completo para GCP Cloud Storage y Azure Blob Storage (subir/eliminar/URL prefirmada/revisión) [GS-318] [GS-317].
- Backends `get_secrets()` para GCP Secret Manager y Azure Key Vault [GS-318] [GS-317].
- Tipo de campo `select_table`: resolver de relación 1-1 independiente del motor (Rápidas rutas en DynamoDB BatchGetItem / MongoDB `$lookup`) [GS-259].
- Rate limiting (`slowapi`) integrado en endpoints de FastAPI y Flask [GS-332].
- Seguridad: actualizaciones de pyjwt, cryptography, urllib3; corrección de vulnerabilidad de path traversal en `app_context.py`; migración a Python 3.14 [GS-219] [GS-337].

### CHANGELOG.md

#### [0.4.0] - 2026-08-30

##### Añadido
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes de Codificación IA [GS-303].
- Pruebas SAST [GS-315].
- Pruebas unitarias generales [GS-21].
- Variable de entorno AWS_SSL_CERTIFICATE_ARN_BE añadida al archivo `.env.example` [GS-328].
- Soporte de almacenamiento GCS (GCS) de objetos: implementación completa de `upload_file_to_storage`, `remove_from_storage`, `get_gcs_presigned_url`, `storage_retieval`, y `prepare_asset_url` en `genericsuite/util/gcp.py` [GS-318].
- Soporte de almacenamiento de Azure Blob: implementación completa de `upload_file_to_storage`, `remove_from_storage`, `get_blob_presigned_url` (tokens SAS), `storage_retieval`, y `prepare_asset_url` en `genericsuite/util/azure.py` [GS-317].
- Soporte de GCP Secret Manager: implementación real de `get_secrets()` en `genericsuite/util/gcp_secrets.py` usando el SDK `google-cloud-secret-manager`; requiere la variable de entorno `GCP_PROJECT_ID` [GS-318].
- Soporte de Azure Key Vault: implementación real de `get_secrets()` en `genericsuite/util/azure_secrets.py` usando los SDKs `azure-keyvault-secrets` + `azure-identity`; requiere `AZURE_KEYVAULT_URL` [GS-317].
- Grupos de dependencias opcionales `gcp` y `azure` en `pyproject.toml` para instalación diferida de SDKs [GS-317] [GS-318].
- Nuevas variables de entorno documentadas en `.env.example`: `GCP_PROJECT_ID`, `GCS_CHATBOT_ATTACHMENTS_BUCKET_*`, `AZURE_STORAGE_ACCOUNT_NAME`, `AZURE_STORAGE_ACCOUNT_KEY`, `AZURE_CHATBOT_ATTACHMENTS_CONTAINER_*`, `AZURE_KEYVAULT_URL`, `CLOUD_STORAGE_PRESIGNED_EXPIRY`, `CLOUD_STORAGE_PRESIGNED_ACTIVE` [GS-317] [GS-318].
- Pruebas unitarias para almacenamiento GCS (`tests/test_gcp_storage.py`), Azure Blob storage (`tests/test_azure_storage.py`), GCP Secret Manager (`tests/test_util_gcp_secrets.py`), y Azure Key Vault (`tests/test_util_azure_secrets.py`) [GS-317] [GS-318].
- Introducir la variable de entorno `DEBUG_CORS` en FastAPI `create_app.py` para registrar orígenes CORS durante el desarrollo. Esto mejora la capacidad de depuración de la configuración CORS [GS-329].
- `slowapi` para rate limiting en FastAPI [GS-332].
- Integración de rate limiting en endpoints de FastAPI y Flask [GS-332].
- Tipo de campo `select_table`: resolución 1-1 en listados y lecturas. Nuevos atributos JSON `related_table`, `local_field`, `related_key`, `description_fields`, `description_separator`, `related_filter`; filas ahora incluyen `{field}_description`. Buscador `$in` independiente del motor para todos los DB, con rutas rápidas en DynamoDB BatchGetItem y MongoDB `$lookup` [GS-259].

##### Fixed
- Encabezados de cabeceras de API Key MCP y autenticación de clave API: modificar get_access_token para incluir todas las cabeceras, actualizar mcp_authenticate_api_key para requerir user_id solo según MCP_MANDATORY_USER_ID, ajustar la asignación de user_id cuando solo se proporciona la Clave API. Ajustar verify_app_context para señalar un error más descriptivo ante credenciales de usuario faltantes [GS-243].

##### Changed
- Licencia cambiada a MIT [FA-244].
- Actualizar configuración de CORS en `framework_abstraction.py` para que `Access-Control-Allow-Origin` sea `*` para múltiples orígenes, ya que FastAPI gestiona la separación de orígenes internamente [GS-329].
- Eliminar autenticación de solicitudes por flexibilidad [GS-329].
- Añadir limitación de tasa en `logs.py` para el endpoint `/logs` [GS-332].
- Mejora de comentarios sobre cómo especificar condicionantes de lint C0301 y E501 en `config.py`.
- Reemplazo de revisión de código de Gemini de Github por SonarQube y Claude [GS-336].
- Modificar Makefile para permitir argumentos opcionales para la subida de twine durante la publicación de producción, p. ej. "--verbosity" [GS-327].
- Actualizar versión a 0.4.0 en package.json, pyproject.toml y setup.py [GS-327].

##### Seguridad
- Actualizar "pyjwt" a "^2.13.0" para corregir vulnerabilidades [GS-219].
    * PyJWKClient: lista de esquemas permitidos ausente permite SSRF y falsificación de tokens
    * PyJWKClient: peticiones JWKS sin límite de endpoint (DoS)
- Actualizar cryptography a "^50.0.0" para corregir vulnerabilidades [GS-219].
    * Intermediarios autofirmados duplicados pueden causar problemas
- Evitar caracteres no permitidos en nombres de archivos basados en user_id u ObjectId en `app_context.py` [GS-219].
- Actualizar "urllib3" a "^2.7.0" para corregir vulnerabilidades [GS-219].
- Corregir flujo de entrada no saneada desde encabezados HTTP hacia json.dump en app_context.py [GS-219].
- Migrar a Python 3.14 [GS-337].
- Aumentar versión de Node.js en .nvmrc a 26 [GS-339].

## GenericSuite Backend AI

### Paquete, Pull Request y Etiqueta

* Paquete: [https://pypi.org/project/genericsuite-ai/0.4.0/](https://pypi.org/project/genericsuite-ai/0.4.0/)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/14](https://github.com/tomkat-cr/genericsuite-be-ai/pull/14)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/15](https://github.com/tomkat-cr/genericsuite-be-ai/pull/15)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.4.0](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.4.0)

### Resumen de Pull Request

Documentación de IA y vulnerabilidades de seguridad

Una versión enfocada en seguridad e higiene: onboarding de IA-agent, pruebas SAST, relicensing MIT y revisión de código movida de GitHub Gemini a SonarQube + Claude. El grueso del cambio es una pasada de actualización de dependencias de seguridad a lo largo de la pila LangChain (langchain, langchain-openai, langchain-core, langchain-community) que corrige vulnerabilidades de recorrido de directorios, SSRF, DoS y deserialización, junto con actualizaciones de pytest/twine/fastapi/aiohttp/cryptography/pyjwt y una migración a Python 3.14.

Destacados

- Actualización de la pila LangChain (langchain, langchain-openai, langchain-core, langchain-community) corrigiendo vulnerabilidades de alto, incluyendo recorrido de directorios, SSRF, DoS y deserialización insegura [GS-219].
- Actualización de cryptography y pyjwt para corregir problemas de construcción de rutas y SSRF/falsificación de tokens [GS-219].
- Licencia MIT; revisión de código movida a SonarQube + Claude [FA-244] [GS-336].
- Migración a Python 3.14; actualizaciones de Node.js en `.nvmrc` [GS-337] [GS-339].

### CHANGELOG.md

#### [0.4.0] - 2026-08-30

##### Añadido
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes de Codificación IA [GS-303].
- Pruebas SAST [GS-315].
- Pruebas unitarias generales [GS-21].
- Variable de entorno AWS_SSL_CERTIFICATE_ARN_BE añadida al `.env.example` [GS-328].

##### Cambiado
- Eliminar referencias a fynapp en `ai_conversations_conversion.py`
- Mejorar comentarios sobre cómo especificar condiciones de lint C0301 y E501 en `config.py`
- Licencia cambió a MIT [FA-244].
- Reemplazar revisión de código de Github Gemini por SonarQube y Claude [GS-336].
- Modificar Makefile para permitir argumentos opcionales para la subida de twine durante la publicación de producción [GS-327].
- Actualizar versión a 0.4.0 en package.json, pyproject.toml y setup.py [GS-327].

##### Seguridad
- Actualizar LangChain a "^1.3.14", LangChain-OpenAI a "^1.4.1", LangChain-Core a "^1.5.2", LangChain-Community a "^0.4.2" para corregir vulnerabilidades [GS-219].
- Actualizar dependencias principales (cryptography, crypto-browserify, downshift, react-icons, react-markdown, react-syntax-highlighter, react-router-dom, yup) para corregir vulnerabilidades de seguridad [GS-219].
- Otras actualizaciones de seguridad y migraciones a Python 3.14 [GS-337].

##### Eliminado
- Entrada de referencia a GeminI/Markdown y otros elementos de limpieza no utilizados descritos en la sección de Eliminados [GS-338].

## GenericSuite Mobile

### Paquete, Pull Request y Etiqueta

* Pull Request: [https://github.com/tomkat-cr/genericsuite-mobile/pull/2](https://github.com/tomkat-cr/genericsuite-mobile/pull/2)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-mobile/releases/tag/0.5.0](https://github.com/tomkat-cr/genericsuite-mobile/releases/tag/0.5.0)

### Resumen de Pull Request

Desarrollo inicial de GenericSuite Mobile

Esta release trae soporte de relaciones 1-N `childComponents` en el Editor CRUD de Flutter (secciones tocables de hijos, edición a pantalla completa, subtipos `array`/`table` que coinciden con el comportamiento de genericsuite-fe), un sistema de temas Apple-clean basado en `shadcn_ui` y una gran batería de mejoras defensivas de errores en el editor CRUD, formularios, manejo de autenticación/sesión y navegación — además de pruebas SAST y el tipo de campo `select_table` heredado de 0.4.2.

Destacados

- Soporte `childComponents` (1-N) en el Editor CRUD de Flutter, a la par con genericsuite-fe [GS-261].
- Nuevo tema Apple-clean basado en `shadcn_ui` con un contrato de fusión `defaultThemeParams` [GS-261].
- Ampliación de correcciones de errores generales: decodificación JWT, filtrado y sincronización de llamadas API, etc. [GS-327].
- Campo `select_table` con resolución de descripciones de registros relacionados, heredado de 0.4.2 [GS-259].

### CHANGELOG.md

#### [0.5.0] - 2026-08-30

##### Añadido
- Soporte de `childComponents` (relaciones 1-N) en el Editor CRUD de Flutter: los componentes secundarios declarados en la configuración JSON del frontend se muestran como secciones táctiles en el formulario de edición, se abren a pantalla completa con el registro padre como `parentData`, y soportan ediciones de `child_listing` con subtipos `array` y `table` (incluyendo payloads de escritura `<array_name>`/`<array_name>_old`), igual que el comportamiento del CRUD Editor de genericsuite-fe [GS-261].
- Tokens de tema estilo Apple en `theme_config_defaults.dart` (`accentColor`, `borderRadius` 12px, `fontFamily`/`textTheme` con Inter vía google_fonts, texto casi negro, colores semánticos iOS) + contrato de fusión `defaultThemeParams` para que las apps sobrescriban solo las claves que necesiten [GS-261].
- `shadcn_ui` (port de flutter-shadcn-ui) ahora gestiona la raíz del árbol de widgets vía `ShadApp.custom`; `CreateGsApp` genera el tema MaterialApp a partir de los tokens de GenericSuite; los botones Save/Cancel del formulario usan ShadButton [GS-261].
- `buildGsShadTheme()` genera `ShadThemeData` a partir de los tokens de tema de GenericSuite; nuevo parámetro de tema `shadColorSchemeName` que selecciona el esquema base de shadcn (`green` por defecto; cualquier valor válido de `ShadColorScheme.fromName`), con `accentColor` que anula `primary`/`ring` y tokens de superficie/texto/errores de GS aplicados vía `copyWith` [GS-261].
- Comandos de "lint" y "test" para Makefile.
- Cobertura de pruebas para el proyecto [GS-327].

##### Cambiado
- Color de acento por defecto cambiado de azul a verde; la barra de herramientas y el cajón por defecto se vuelven superficies blancas con texto casi negro; versión de genericsuite_flutter actualizada a 0.5.0 [GS-261].
- Instrucciones detalladas de configuración de README movidas a la documentación de GS Basecamp [GS-261].

##### Fixeado
- http_service.dart [GS-327]:
  1. getJwtPayload usa ascii.decode(...) en lugar de utf8.decode(...) para decodificar la carga útil del JWT. Cualquier reclamación con caracteres no ASCII provoca FormatException.
  2. Sin `.timeout(...)` en llamadas http.get/post/put/delete/patch (a diferencia de ip_address_service.dart) — por lo que una conexión colgada puede bloquear al llamante indefinidamente.
  3. La ruta de éxito 200/201 con json.decode(response.body) no tiene try/catch, a diferencia de la rama de error. Flags de depuración imprimirían JWTs/claves si se activaran (actualmente false).
  4. Añadir anotaciones de tipo a bToA(str).
- create_gs_app.dart: payload["exp"] * 1000 no tiene verificación de null; un token sin exp o malformado puede lanzar en build(), bloqueando el inicio de la app.
- crud_editor.dart [GS-327]:
  1. _saveItem: si es creación y editorConfig['createReenter'] es true tras un guardado exitoso, el método retorna sin llamar a setState(); _isLoading se establece a true con setState pero se resetea con asignación simple, pudiendo dejar el spinner cargando.
  2. Sin comprobaciones de mounted tras await antes de llamadas a setState/_setStateAndShowMessages; navegar fuera durante la solicitud puede lanzar "setState() called after dispose()".
  3. json.decode(localApiResp['resultset']) en _loadSelectedItem sin try/catch; int.parse(...['rows_affected']) sin protección.
  4. _getSelectFieldsOptions — await secuencial en un bucle en lugar de Future.wait, haciendo llamadas de red en serie innecesariamente.
- crud_editor_commons.dart [GS-327]:
  1. (buildChildRowToSave): índices en `parentData` sin verificación de null.
  2. Puede haber `parentData` vacío/faltante (p. ej., `_setEndpointFilter` hace no-ops), por lo que guardar/eliminar en un editor `child_listing` puede lanzar NoSuchMethodError.
- form_field_service.dart [GS-327]:
  1. Casos de `select` y `select_component` configuran `DropdownButtonFormField.initialValue` sin verificar si el valor existe entre los elementos; a diferencia del caso `select_table` que sí verifica con `containsKey(...) ? value : null`.
  2. Datos obsoletos/edición provocan fallos al abrir el formulario; los campos numéricos llaman a `double.parse`/`int.parse` en cada pulsación; borrar el campo o escribir caracteres provoca `FormatException` no capturada.
  3. `TextEditingController(text: ...)` creado inline en `build()` para la mayoría de tipos de campo y nunca eliminado; cada reconstrucción provoca fuga de controladores y restablece el cursor/foco.
- app_drawer.dart [GS-327]:
  1. `Icon(item['callable']['icon'])` lanza si `item['element']` no existe en `callables`; no hay fallback.
  2. `_loadConfig().then(...)` no tiene manejo de errores; las excepciones se vuelven errores asíncronos no manejados.
- error_reporter_widget.dart: `ScaffoldMessenger.of(context).showSnackBar(...)` se llama de forma sincrónica dentro de `build()` — anti-patrón conocido en Flutter que debe diferirse con `addPostFrameCallback`, como se hace en `homepage.dart`.
- login.dart [GS-327]:
  1. `_usernameController`/`_passwordController` se crean pero el widget no tiene `dispose()` para liberarlos.
  2. `apiResponse['resultset']['token']` se accede sin verificación de null en `resultset`. El campo "password" carece de autocorrección: false / enableSuggestions: false.
- current_user_service.dart: si (data['error'] == 'Not Found') nunca puede ser verdadero porque `http_service.dart` siempre devuelve un booleano; este ramo es código muerto [GS-327].
- logout_service.dart: llamadas `storage.delete(...)` para jwt/api_key/user_data no esperan a que se complete antes de navegar; el cierre de la app tras el logout puede dejar credenciales obsoletas en almacenamiento seguro [GS-327].
- routing_services.dart: se añadió `item['callable']['type'] = 'async'` (predeterminado) | 'sync' para permitir llamadas síncronas/asíncronas y manejar cambios de código en `logout_service.dart` [GS-327].
- locator_service.dart: `registerLazySingleton` no tiene guardia `isRegistered`; volver a configurar mediante hot restart, remount o tests lanza duplicación de registro [GS-327].
- timestamp_utilities.dart: la formateación de 12 horas no maneja medianoche correctamente; la hora 0 se muestra como "0:MM AM" en lugar de "12:MM AM" [GS-327].
- homepage.dart: `loadHomeData(true)` se llama directamente como el futuro del `FutureBuilder`: al reconstruirse, vuelve a llamar a la API en cada render antes de tener datos [GS-327].
- deviceid_service.dart: dependencia implícita de orden en `setupStorageLocator()` para ejecutarse primero [GS-327].
- back_button.dart: `Navigator.of(context, rootNavigator: true).pop(context)` pasa `context` como resultado de la operación de pop, lo que parece no intencional [GS-327].
- CRUD Editor guarda y detiene el spinner, y sustituyó la escritura por `CircularProgressIndicator`; mejorado para que el formulario/listado permanezca montado bajo una superposición de carga, y el botón "Save" de AppBar pase por `DataFormBody.submit()` para que las filas hijas persistan sus valores [GS-261].
- `suggestion_dropdown`: el texto ingresado se guarda en la fila en memoria (`selectedItem`) al cambiar y al guardar, y al seleccionar una sugerencia se copian campos de API relacionados, manteniendo el nombre del campo de formulario [GS-261].
- `suggestion_dropdown`: las filas de sugerencias se leen de la misma manera que las listas CRUD decodifican `resultset` (lista ya decodificada, cadena JSON, o `{resultset: [...]}`), para mostrar opciones cuando la API devuelve filas [GS-261].
- `suggestion_dropdown`: elegir una sugerencia ya no copia claves de tablas relacionadas (`_id`, `name`, …) en la fila guardada. Solo se escribe el campo del formulario y `autocomplete_fields`, en línea con genericsuite-fe [GS-261].
- El campo de contraseña muestra hash SHA-256 en lugar de texto plano. La contraseña inicial debe estar en blanco [GS-261].

##### Eliminado
- Directorio `flutter_project_template`. Usar [genericsuite-mobile-exampleapp](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp) en su lugar [GS-261].

#### [0.4.2] - 2026-04-20

##### Añadido
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes de Codificación IA [GS-303].
- Añadir pruebas SAST [GS-315].
- `select_table` field type en el editor CRUD de Flutter: listado y formulario de solo lectura muestran la descripción del registro relacionado (backend `{field}_description` con fallback en caché del cliente); crear/editar renderiza un dropdown poblado a partir de la tabla relacionada [GS-259].

##### Cambiado
- Pequeños fixes en archivos README.md
- Licencia cambiada a MIT [FA-244].
- Actualización de `.gitignore` para incluir directorios de IA agents [GS-303].

##### Fixeado
- Mejorar manejo de errores en `create_gs_app.dart` y `ip_address_service.dart` para mayor estabilidad y bootstrap de Flutter web [GS-252].

## GenericSuite Mobile ExampleApp

### Paquete, Pull Request y Etiqueta

* Pull Request: [https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/pull/2](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/pull/2)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/releases/tag/1.0.0+1](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/releases/tag/1.0.0+1)

### Resumen de Pull Request

Desarrollo inicial. Pasó de genericsuite-mobile

Esta es una nueva submódulo desprendida del antiguo directorio `flutter_project_template` de `genericsuite-mobile` y ahora en su propio repositorio de ejemplo de aplicación independiente, dando a la librería Flutter una implementación de referencia dedicada y versionada de forma independiente.

Destacados

- Separación del repositorio de `genericsuite-mobile` desde `flutter_project_template` [GS-261].
- Establece una aplicación de ejemplo Flutter independiente y versionada.

### CHANGELOG.md

#### [1.0.0+1] - 2026-08-30

##### Añadido
- Pasó de `genericsuite-mobile` a `genericsuite-mobile-exampleapp`.

## GenericSuite AI Agent Skills

### Paquete, Pull Request y Etiqueta

* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-skills/pull/1](https://github.com/tomkat-cr/genericsuite-skills/pull/1)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-skills/pull/3](https://github.com/tomkat-cr/genericsuite-skills/pull/3)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-skills/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-skills/releases/tag/1.0.0)

### Resumen de Pull Request

Añadir el plugin de Claude Skills para gs-app-builder-suite [GS-254]

Introduce el grupo de plugins `gs-app-builder-suite` — un skill orquestador (`gs-app-builder`) más habilidades especializadas para el andamiaje de apps, configuración, JSX, menús, endpoints, FastAPI, herramientas de IA y servidores MCP — junto con un conjunto de evaluaciones y un mecanismo de sincronización de referencias para mantener alineados los docs de skills con la documentación del ecosistema GenericSuite.

Destacados

- Nuevo grupo de plugins `gs-app-builder-suite` con un orquestador y 9 habilidades de construcción especializadas [GS-254].
- Conjunto `evals/evals.json` con aserciones de validez en tiempo de ejecución [GS-254].
- Mecanismo de sincronización de referencias (`make sync-references`) para mantener las habilidades alineadas con los docs de GS [GS-254].
- Habilidad `release-notes` movida al Superproyecto GS [GS-191].

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Añadido
- Proyecto de ideación y desarrollo inicial (2026-04-12) [GS-254].
- Conjunto de habilidades de app-builder (`gs-app-builder-suite`) [GS-254]:
  `gs-app-builder` orquestador (detección modo verde/archivo, entrevista breve de app, flujo con checkpoints), `app-starter`, `config-builder` (actualizado), `jsx-code-builder` (actualizado), `menu-builder`, `endpoints-builder`, `python-fastapi-code-builder`, `python-ai-code-builder`, `python-ai-tools-code-builder`, `jsx-ai-code-builder`, `mcp-builder`.
- Series `evals/evals.json` (todas las habilidades de la suite excepto `config-builder`) con aserciones de validez en tiempo de ejecución, ejercidas en `playground/` [GS-254].
- Mecanismo de sincronización de referencias: `skills/update-gs-docs` mapa + script, `make sync-references` [GS-254].
- Añadir pruebas SAST [GS-315].

##### Cambiado
- Grupo de plugins de marketplace de código de distribución cambiado a `gs-app-builder-suite`; versión de metadatos 1.1.0 [GS-254].
- Reescritura de README alrededor del paquete app-builder-suite, instalación y publicación [GS-254].

##### Eliminado
- Habilidad `release-notes` eliminada del marketplace (moved to GS Superproject directory) [GS-191].

##### Seguridad
- Migrar a Python 3.14 [GS-337].
- Aumento de la versión de Node.js en .nvmrc a 26 [GS-339].

## GenericSuite Security

### Paquete, Pull Request y Etiqueta

* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-security/pull/4](https://github.com/tomkat-cr/genericsuite-security/pull/3)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-security/pull/4](https://github.com/tomkat-cr/genericsuite-security/pull/4)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-security/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-security/releases/tag/1.0.0)

### Resumen de Pull Request

Ideación y desarrollo inicial

Nueva submódulo creada en respuesta directa al ataque de la cadena de suministro npm de Keyv/Cacheable del 2026-08-04. Envía cinco habilidades Claude para auditoría de cadena de suministro y listos para producción: escaneo IOC, un generador de corpus de la organización, un escáner de contenedores Docker, un escáner de dependencias de acciones de GitHub y un analizador de debilidades/preparación cruzada — además de un plugin de marketplace registrado.

Destacados

- `supply-chain-ioc-scan` — detectar si un paquete npm/PyPI comprometido afecta esta máquina o árbol de repositorios [GS-339].
- `repo-corpus` → `repo-docker-scanner` → `repo-packages-scanner` — escaneo organizacional en tres fases (manifiesto de corpus, referencias a imágenes, dependencias de acciones no fijadas a SHA; etc.).
- `project-weakness-analysis` — preparación para producción y evaluación de riesgos de seguridad a través de múltiples proyectos a la vez.
- Salidas en `./insights`: `WEAKNESS-REPORT.md`, `insights.json`, `insights-table.json`/`insights-table.csv`, `security-audit.json`, `projects/<slug>.json`, y `findings.sarif`.
- Plugin de Claude Marketplace registra las nuevas habilidades: `supply-chain-security`, `repo-corpus`, `repo-docker-scanner`, `repo-packages-scanner`, y `project-weakness-analysis`.

##### Cambiado
- `repo-corpus` y los dos escáneres planificados consumen un corpus en lugar de enumerar repositorios por sí mismos, de modo que el modo de una sola repo y la auditoría a nivel de org comparten una única ruta de código.

##### Fixeado
- Se corrigieron descripciones de reglas en `repo-docker-scanner` para reflejar la leyenda correcta obtenida de `policy/images.json`.
- `repo-docker-scanner` detecta plantillas de infraestructura como código P0 por contenido (CloudFormation) sin depender de la ruta.
- Corrección de minúsculas en referencias de plantillas en `repo-docker-scanner` para informes verídicos.
- Corrección de descubrimiento de Dockerfile en `repo-docker-scanner` y regla de prioridad `**/Dockerfile*` para evitar omisiones silenciosas.
- `run_corpus.sh` no falla en macOS bash 3.2; ahora usa parámetros posicionales y reporta resultados de corpus solo si hay un manifiesto.
- Los repos de pruebas se clonan con una configuración que evita dependencias de git no deseadas.
- Correcciones en rutas de prueba y nombres de archivos en la autoevaluación.
- La ruta de marketplace `.claude-plugin/marketplace.json` fue corregida para apuntar a la ruta existente de habilidades.

##### Seguridad
- El `build_corpus.py` advierte cuando la lista de repos puede cortarse; una lista acotada es la única que puede expresarse en un manifiesto.
- La auto-prueba es hermética respecto a la configuración de git del desarrollador; deshabilita ganchos, LFS y prompts de credenciales interactivos al clonar.
- Clonar repos se maneja como entrada hostil: deshabilitar hooks, LFS, prompts de credenciales; validar nombres de repos como rutas; recorrer directorios sin seguir symlinks fuera del root.
- Migrate a Python 3.14 [GS-337].
- Aumentar Node.js a 26 en .nvmrc [GS-339].

## GenericSuite BaseCamp

### Paquete, Pull Request y Etiqueta

* Pull Request: [https://github.com/tomkat-cr/genericsuite-basecamp/pull/19](https://github.com/tomkat-cr/genericsuite-basecamp/pull/19)
* Pull Request: [https://github.com/tomkat-cr/genericsuite-basecamp/pull/22](https://github.com/tomkat-cr/genericsuite-basecamp/pull/22)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.6.0](https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.6.0)

### Resumen de Pull Request

Renombrar docs a mkdocs_root + etc.

Esta solicitud de extracción es una actualización amplia de documentación y herramientas que abarca todo el ecosistema GenericSuite: el sitio de docs se reorganizó (`docs/` → `mkdocs_root/`, `specs/` → `docs/`), se añadió nueva documentación para Desarrollo Móvil, Habilidades IA, GS FE Scripts y una guía de despliegue OpenTofu, el proyecto cambió a licencia MIT, se aplicaron pruebas SAST y correcciones de vulnerabilidades dependencias en ExampleApp y FastApiTemplate, y el puntero del repositorio principal se cambió de GS Basecamp al nuevo GS Superproject.

Destacados

- Reorganización del sitio de documentación: `docs/` renombrado a `mkdocs_root/`, nuevas páginas para Desarrollo Móvil, Habilidades IA, GS FE Scripts y OpenTofu; el repositorio principal apunta ahora al GS Superproject.
- Seguridad y cumplimiento: pruebas SAST integradas, actualizaciones de dependencias (cryptography, crypto-browserify, correcciones CVE de `@babel/core`), migración a Python 3.14, licencia MIT y aplicación de `mandatoryFilters` para historial de usuarios/tabla de configuraciones/ claves API.
- Herramientas para desarrolladores: scripts de scaffolding `new-project-from-template.sh` y `rename-app.sh`, refactorización de Makefile para usar `genericsuite-fe-scripts`, y tres nuevas habilidades IA (`add-doc`, `sample-code-update`, `translate-docs`).
- CRUD Editor y configuración: tipo de campo `select_table` y documentación de `SelectElementItem` para opciones inline en la configuración del editor CRUD.

### CHANGELOG.md

#### [1.6.0] - 2026-08-30

##### Añadido
- Nueva imagen de arquitectura para la página de índice de documentación [GS-327].
- Nueva página de documentación de Habilidades IA [GS-254].
- Nueva página de Habilidades de Seguridad [GS-339].
- Documentación de GS FE Scripts [GS-107].
- Sección de Desarrollo Móvil: instalación de GenericSuite Flutter, CRUD driven por JSON, childComponents (1-N), tokens de tema de Apple-clean, y tokens de tematización para iOS [GS-261].
- Guía de despliegue OpenTofu (`mkdocs_root/en/Deployment-Guide/opentofu.md`) cubriendo los stacks IaC de genericsuite-fe-scripts y genericsuite-be-scripts, con entrada de navegación en `mkdocs.yml` [GS-334].
- Superproyecto GS, Seguridad y GS FE Scripts en la página repositories.md [GS-319].
- Pruebas SAST [GS-315].
- Documentación de tipo `select_table` para añadir soporte a relaciones 1-1 en listas y páginas de datos [GS-259].
- Navegación en español para la sección de documentación de Desarrollo Móvil [GS-261].
- Introducción del modelo `SelectElementItem` para opciones inline en la configuración del editor CRUD. Actualización de `select_elements` para soportar IDs predefinidos y objetos inline {title, value} [GS-254].
- Variables de entorno AWS_SSL_CERTIFICATE_ARN_FE y AWS_SSL_CERTIFICATE_ARN_BE [GS-328].
- Soporte de múltiples orígenes CORS para FastAPI en `aws_big_lambda/template-sam.yml` [GS-329].
- `make create-supad` para el servidor exampleapp/fastapitemplate [GS-306].
- Nuevos definiciones de habilidades IA (`.ai/skills/`): add-doc, sample-code-update, translate-docs
- Dependencia `zipp` añadida a los requisitos principales para abordar una vulnerabilidad recomendada por Snyk [GS-219].

##### Cambiado
- Renombrar `docs/` a `mkdocs_root/` [GS-208].
- Renombrar `specs/` a `docs/` [GS-208].
- Añadido `.venv/` a `.gitignore` y `.dockerignore`.
- `run_translate_uncommitted.sh` crea y elimina entornos virtuales `.venv` [GS-316].
- Licencia cambiada a MIT [FA-244].
- Mejoras en documentación de ARN de certificado SSL para claridad de uso de `AWS_SSL_CERTIFICATE_ARN_FE` y `AWS_SSL_CERTIFICATE_ARN_BE` entre backend y scripts frontend [GS-328].
- Inicializar variable APP_ENVS en `update_additional_envvars.sh` para ejemplos de variables de entorno de la app [GS-329].
- Actualizar Makefile de FastApiTemplate con nuevos objetivos utilitarios, reemplazo de "tomkat-cr" por "github-username" en `.env.example` [GS-306]
- Separar estructura de directorios de CLAUDE.md para hacerla más pequeña [GS-303].
- Actualizar guía de configuración de FastAPI Template para usar `new-project-from-template.sh` con `curl` [GS-306].
- Añadir referencia de FastApiTemplate a la guía de configuración principal [GS-254]
- FastApiTemplate: Refactor de renombrado de componentes UI `_components` > `components`, `_images` > `images`, y `_constants` > `constants` [GS-306].
- Actualizar servidor de exampleap/fastapitemplate y scripts de desarrollo mcp-server para gestión dinámica de entornos, para que stage pueda ejecutarse con `STAGE=dev make dev` (package.json ahora usa la variable STAGE en "dev": "make run_${STAGE:-qa}") [GS-306].
- Archivos `.env.example` de FastApiTemplate para usar valores predeterminados para menos cambios del usuario al iniciar el proyecto [GS-306].
- Mejoras en AGENTS.md, GEMINI.md y CLAUDE.md para ofrecer mejor contexto e instrucciones a los Asistentes de Codificación IA [GS-303].
- Incluir directorios `.claude`, `.agents`, `.codex`, `.cursor`, y `.gemini` para compartir habilidades/comandos desde el directorio `.ai` [GS-254]
- Renombrar `.claude` a `.ai`
- Corregir visualización de gráficos de directorios
- Modificar la documentación de `food_moment_in_user` para claridad sobre referencias de usuario; mejorar documentación de operaciones de momentos de comida [GS-254].
- ExampleApp: manejo de excepciones amplio en el endpoint FDA de comida [GS-254].
- `mkdocs.yml` — una línea de navegación ('AI Skills'), verificar `build-safe` contra la convención de carpeta i18n [GS-254].
- ExampleApp: actualizar dependencias en `package.json` y `pnpm-lock.yaml` para dotenv y turbo [GS-254]
- ExampleApp: actualizar versiones de `aiohappyeyeballs` y `aiohttp` en archivos uv.lock para apps API [GS-219].

##### Fixeado
- Corregir_ENV vars no pasados a MCP server: CLOUD_PROVIDER, APP_NAME, AWS_REGION, STORAGE_URL_SEED, APP_SUPERADMIN_EMAIL, GIT_SUBMODULE_LOCAL_PATH, GET_SECRETS_ENABLED, GET_SECRETS_CRITICAL y GET_SECRETS_ENVVARS [GS-243].
- Corregir errores de `pnpm install` que llamaban al comando de release y trataban el script `publish` como hook de npm en dependencias git-hosted; renombrado a `npm-publish` y `npm-pre-publish` [GS-339].

##### Seguridad
- Migrar a Python 3.14 [GS-337].
- Limpiar salidas en `run_mcp_server.sh` eliminando declaraciones de eco innecesarias [GS-243].
- Suprimir aviso de servidor MCP en `run_mcp_server.sh` estableciendo la variable de entorno `MCP_DISABLE_NOTICE` a true [GS-243].
- Aumentar versión de Node.js en .nvmrc a 26 [GS-339].
- Eliminar "office-addin-dev-certs" de dependencias de package.json para que el usuario decida instalarlo si es necesario, y corregir vulnerabilidades de seguridad [GS-219].
   * Forge tiene falsificación de firma en Ed25519 por fallo S > L
   * Forge tiene falsificación de firma en RSA-PKCS por campo ASN.1 adicional
   * Forge tiene bypass de validación de código en su verificación de cadena de certificados
   * uuid: verificación de límites de búfer ausente en v3/v5/v6

## GenericSuite BaseCamp App

### Paquete, Pull Request y Etiqueta

* Pull Request: [https://github.com/tomkat-cr/genericsuite-basecamp-app/pull/2](https://github.com/tomkat-cr/genericsuite-basecamp-app/pull/2)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-basecamp-app/releases/tag/1.0.0+4](https://github.com/tomkat-cr/genericsuite-basecamp-app/releases/tag/1.0.0+4)

### Resumen de Pull Request

Desarrollo inicial

Esta release ("GS Doc", la app móvil de visión de documentación Flutter) añade archivos de contexto IA, pruebas SAST y un conjunto de objetivos Makefile para abrir emuladores de iOS/Android, mientras se completa la migración desde el antiguo submódulo `genericsuite-basecamp` en favor de la obtención de docs vía `GS_BASECAMP_PATH`.

Destacados

- Nueva variable de entorno `GS_BASECAMP_PATH` y `run_docs_converter.sh` actualizado para clonar o reutilizar una comprobación local de GenericSuite Basecamp
- Nuevos objetivos `make open-ios-simulator` / `open-android-emulator` para desarrollo local
- El submódulo `genericsuite-basecamp` como dependencia fue eliminada a favor del flujo dirigido por `GS_BASECAMP_PATH`
- Licencia cambiada a MIT [FA-244]; arreglos de imágenes que no aparecían tras el cambio de ruta con prefijo de idioma [GS-252]

### CHANGELOG.md

#### [1.0.0+4] - 2026-08-30

##### Añadido
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes de Codificación IA [GS-303].
- Añadir pruebas SAST [GS-315].
- Variable de entorno `GS_BASECAMP_PATH` para especificar la ruta al repositorio GenericSuite Basecamp.
- Contenido de `README.md` con prerrequisitos, instalación y uso [GS-303].
- `make open-ios-simulator` para abrir el simulador Apple iOS.
- `open-android-emulator` y el script `open-android-emulator.sh`.

##### Cambiado
- Renombrar `assets/docs/` a `assets/mkdocs_root/` [GS-208].
- `run_docs_converter.sh` clona el repositorio GenericSuite Basecamp en `./genericsuite-basecamp` si `GS_BASECAMP_PATH` está vacío; de lo contrario, usa la ruta especificada.
- Licencia cambiada a MIT [FA-244].

##### Fixeado
- Las imágenes se muestran correctamente tras añadir el prefijo de idioma a la ruta [GS-252].

##### Eliminado
- Submódulo Git `genericsuite-basecamp`.

## GenericSuite Gitops

### Paquete, Pull Request y Etiqueta

* Pull Request: [https://github.com/tomkat-cr/genericsuite-gitops/pull/6](https://github.com/tomkat-cr/genericsuite-gitops/pull/6)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.5.0](https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.5.0)

### Resumen de Pull Request

Mejora de documentación de IA y estructura de directorios

Una versión de mantenimiento enfocada: archivos de contexto de IA, pruebas SAST, cambio de estructura de directorio (`docs/` → `help/`, `specs/` → `docs/`), y migración a licencia MIT.

Destacados

- AGENTS.md, GEMINI.md y CLAUDE.md añadidos [GS-303]
- Pruebas SAST añadidas [GS-315]
- Estructura de directorios unificada: `docs/` renombrado a `help/`, `specs/` renombrado a `docs/` [GS-303]
- Licencia cambiada a MIT [FA-244]

### CHANGELOG.md

#### [0.5.0] - 2026-08-30

##### Añadido
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes IA [GS-303].
- Añadir pruebas SAST [GS-315].

##### Cambiado
- Renombrar directorios `docs/` a `help/` [GS-303].
- Renombrar directorios `specs/` a `docs/` [GS-303].
- Licencia cambiada a MIT en archivos README.md [FA-244].

## GenericSuite App Maker (GSAM)

### Paquete, Pull Request y Etiqueta

* Pull Request: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/15](https://github.com/tomkat-cr/genericsuite-app-maker/pull/15)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-app-maker/releases/tag/0.6.0](https://github.com/tomkat-cr/genericsuite-app-maker/releases/tag/0.6.0)

### Resumen de Pull Request

IA Agent docs + pruebas SAST + correcciones de vulnerabilidades + errores tipográficos en README

Esta versión añade documentación de IA para agentes y SAST, limpia el texto del README y actualiza dependencias en `requirements.txt` a sus últimas versiones para cerrar vulnerabilidades conocidas.

Destacados

- Se añaden archivos de contexto IA (`AGENTS.md`, `GEMINI.md`, `CLAUDE.md`) y pruebas SAST [GS-303] [GS-315]
- Objetivos Makefile de "upgrade" y "update" para el mantenimiento de dependencias [GS-219]
- Dependencias actualizadas en `requirements.txt` para corregir vulnerabilidades [GS-219]
- Se regeneró el lockfile, eliminando paquetes transitorios no usados [GS-219]

### CHANGELOG.md

#### [0.6.0] - 2026-08-30

##### Añadido
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes IA [GS-303].
- Añadir pruebas SAST [GS-315].
- Objetivos de Makefile de `upgrade` y `update` para mantenimiento de dependencias [GS-219].

##### Cambiado
- Errores de redacción en README
- Licencia cambiada a MIT [FA-244].

##### Seguridad
- Actualizar dependencias a versiones más nuevas [GS-219].
- Migrar a Python 3.14 [GS-337]
- `.github` usa Python 3.14 [GS-337]

##### Eliminado
- Regenerado lockfile elimina paquetes que no estaban antes [GS-219].

## GenericSuite ASDT

### Paquete, Pull Request y Etiqueta

* Pull Request: [https://github.com/tomkat-cr/genericsuite-asdt-be/pull/6](https://github.com/tomkat-cr/genericsuite-asdt-be/pull/6)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-asdt-be/releases/tag/0.3.0](https://github.com/tomkat-cr/genericsuite-asdt-be/releases/tag/0.3.0)

### Resumen de Pull Request

IA Agents docs + pruebas SAST + vulnerabilidades y MIT

Esta versión añade documentación de IA para agentes, pruebas SAST, migración a Python 3.14, y documenta que LangGraph y Smolagents siguen pendientes (no soportados aún) junto con la implementación principal CrewAI.

Destacados

- Nuevo comando de Makefile `make upgrade`, `make crewai_upgrade`, `make camelai_upgrade` para mantener dependencias actualizadas y corregir vulnerabilidades [GS-219]
- Documentación indica que LangGraph y Smolagents están planificados, no soportados aún [GS-327]
- Seguridad: migración a Python 3.14 [GS-337]
- Licencia cambiada a MIT [FA-244]

### CHANGELOG.md

#### [0.3.0] - 2026-08-30

##### Añadido
- AGENTS.md, GEMINI.md y CLAUDE.md para proporcionar contexto e instrucciones a los Asistentes IA [GS-303].
- Añadir pruebas SAST [GS-315].
- `make upgrade`, `make crewai_upgrade`, y `make camelai_upgrade` para actualizar dependencias y corregir vulnerabilidades [GS-219].

##### Cambiado
- Licencia cambiada a MIT [FA-244].
- Documentación sobre LangGraph y Smolagents como planificados, no aún soportados [GS-327].
- Mejora de Makefile y scripts para gestión de versión de Python y comandos de actualización [GS-219].
- Actualizar dependencias en todos los proyectos Python (pyproject.toml y poetry.lock) para mejorar compatibilidad y arreglos de seguridad [GS-219].

##### Seguridad
- Migrar a Python 3.14 [GS-337].

##### Eliminado
- Eliminar archivo requirements.txt obsoleto [GS-219].

## GenericSuite Mobile

### Paquete, Pull Request y Etiqueta

* Pull Request: [https://github.com/tomkat-cr/genericsuite-mobile/pull/2](https://github.com/tomkat-cr/genericsuite-mobile/pull/2)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-mobile/releases/tag/0.5.0](https://github.com/tomkat-cr/genericsuite-mobile/releases/tag/0.5.0)

### Resumen de Pull Request

Desarrollo inicial de GenericSuite Mobile

Esta versión trae soporte 1-N `childComponents` en el Editor CRUD de Flutter (secciones táctiles de hijos, edición a pantalla completa, subtipos `array`/`table` que coinciden con el comportamiento de genericsuite-fe), un sistema de tema Apple-clean basado en `shadcn_ui`, y un gran lote de correcciones defensivas de bugs en el editor CRUD, formularios, manejo de autenticación/sesión y navegación — además de pruebas SAST y el tipo de campo `select_table` heredado de 0.4.2.

Destacados

- Soporte `childComponents` (1-N) en el Editor CRUD de Flutter, a la par con genericsuite-fe [GS-261].
- Nuevo sistema de temas `shadcn_ui` con fusión `defaultThemeParams` [GS-261].
- Ampliación de correcciones de errores: decodificación JWT, fugas de dispose/mounted, comprobaciones nulas faltantes, timeouts, llamadas API sincrónicas, etc. [GS-327].
- Campo `select_table` con resolución de descripciones de registros relacionados, heredado de 0.4.2 [GS-259].

### CHANGELOG.md

#### [0.5.0] - 2026-08-30

##### Añadido
- Soporte de `childComponents` (relaciones 1-N) en el Editor CRUD de Flutter: componentes secundarios declarados en la configuración JSON se renderizan como secciones táctiles en el formulario de edición, se abren a pantalla completa con el registro padre como `parentData`, y soportan editores de `child_listing` con subtipos `array` y `table` (incluyendo payloads de escritura `<array_name>`/`<array_name>_old`), coincidiendo con el comportamiento del Editor CRUD de genericsuite-fe [GS-261].
- Tokens de tema Apple-clean en `theme_config_defaults.dart` (`accentColor`, `borderRadius` 12px, `fontFamily`/`textTheme` con Inter vía google_fonts, texto casi negro, colores semánticos de iOS) + contrato de fusión `defaultThemeParams` para que las apps solo sobrescriban las claves que necesiten [GS-261].
- `shadcn_ui` (port de flutter-shadcn-ui) ahora gestiona la raíz del árbol de widgets vía `ShadApp.custom`; `CreateGsApp` construye el tema MaterialApp a partir de los tokens de GenericSuite; los botones de guardar/cancelar usan ShadButton [GS-261].
- `buildGsShadTheme()` construye `ShadThemeData` a partir de los tokens de tema de GenericSuite; nuevo parámetro `shadColorSchemeName` para seleccionar el esquema base de shadcn (`green` por defecto; cualquier valor de `ShadColorScheme.fromName`) con `accentColor` que sobrescribe `primary`/`ring` y los tokens de superficie/texto/errores de GS aplicados mediante `copyWith` [GS-261].
- Comandos de "lint" y "test" para Makefile.
- Cobertura de pruebas para el proyecto [GS-327].

##### Cambiado
- Color de acento por defecto cambiado de azul a verde; la barra de herramientas y el cajón se vuelven superficies blancas con texto casi negro; la versión de genericsuite_flutter se actualiza a 0.5.0 [GS-261].
- Instrucciones de configuración detalladas de README migradas a la documentación de GS Basecamp [GS-261].

##### Fixed
- http_service.dart [GS-327]:
  1. getJwtPayload ahora usa ascii.decode(...) en lugar de utf8.decode(...) para decodificar la carga útil JWT.
  2. No hay `.timeout(...)` en llamadas http.get/post/put/delete/patch.
  3. La ruta de éxito 200/201 con json.decode(response.body) sin manejo de errores.
  4. Añadir tipado a `bToA(str)`.
- create_gs_app.dart: payload exp sin verificación de null puede lanzar en build.
- crud_editor.dart [GS-327]: mejoras en guardado, manejo de estado y lectura de `resultset`.
- crud_editor_commons.dart [GS-327]: manejo de `parentData` y errores en guardado.
- form_field_service.dart [GS-327]: manejo de valores iniciales y validaciones de inputs.
- app_drawer.dart [GS-327]: manejo seguro de iconos y errores.
- error_reporter_widget.dart: demorar `SnackBar` para evitar patrón anti recomendado.
- login.dart [GS-327]: liberación de recursos y verificación de rutas de token.
- current_user_service.dart: rama de error muerta removida.
- logout_service.dart: asegurar cierre correcto y limpieza de credenciales.
- routing_services.dart: manejo de llamadas asíncronas.
- locator_service.dart: evitar duplicación de registro.
- timestamp_utilities.dart: corrección de formato de 12 horas.
- homepage.dart: evitar llamada repetida en cada render.
- deviceid_service.dart: dependencia de orden de inicialización.
- back_button.dart: manejo correcto de pop.
- Otros ajustes de seguridad y migraciones a Python 3.14 y Node 26 [GS-337] [GS-339].

##### Seguridad
- Actualizaciones de dependencias relacionadas con seguridad en varias capas [GS-219].
- Migraciones a Python 3.14 y ajustes de Node 26 [GS-337] [GS-339].

##### Eliminado
- Varios paquetes y dependencias no utilizados listados en la sección de Eliminados.

Este documento conserva la estructura Markdown original y adapta el texto al español manteniendo los nombres técnicos y vínculos.