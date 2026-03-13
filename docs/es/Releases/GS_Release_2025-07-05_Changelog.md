# 20250705 - La Edición Monorepo de ExampleApp

![GS_Release_2025-07-05_Image_4B.png](./images/GS_Release_2025-07-05_Image_4B.png)

Fecha de lanzamiento: 2025-07-12

## Resumen

Lanzamiento GenericSuite del 5 de julio de 2025: Un gran salto en modernización y experiencia del desarrollador

Estamos emocionados de anunciar el lanzamiento de GenericSuite para el 5 de julio de 2025, una actualización significativa centrada en modernizar la pila de desarrollo y aumentar la productividad de los desarrolladores. Este lanzamiento, "La Edición Monorepo de ExampleApp", introduce una gran cantidad de nuevas características, integraciones y mejoras en toda la suite.

Los puntos clave de este lanzamiento incluyen:

* Herramientas Frontend modernizadas: Hemos integrado Vite como alternativa a Webpack, ofreciendo una experiencia de desarrollo más rápida y eficiente. El núcleo frontend ahora también admite oficialmente Axios para una recuperación de datos más robusta, junto con importantes actualizaciones de dependencias a React Router v7 y Tailwind CSS v4.

* Mayor flexibilidad del Backend: En el backend, los tiempos de expiración de JWT ahora son configurables mediante variables de entorno, proporcionando un mayor control sobre las políticas de seguridad. El manejo de solicitudes para Flask y FastAPI también ha sido refactorizado para una mayor consistencia.

* Capacidades de IA ampliadas: Ampliamos nuestro soporte de integración de IA con la incorporación de nuevos proveedores, incluidos Google Vertex AI y OpenRouter. Esto permite a los desarrolladores aprovechar una gama más amplia de modelos potentes para sus aplicaciones.

* Introducción del monorepo "ExampleApp": Una piedra angular de este lanzamiento es una nueva aplicación de ejemplo completamente funcional construida como monorepo usando Turborepo y pnpm. Esto proporciona un plano práctico y del mundo real para que los desarrolladores aprendan y aceleren sus propios proyectos.

* Mejora de la experiencia del desarrollador: Hemos introducido varias mejoras de calidad de vida, como un nuevo script para enlazar en vivo bibliotecas locales para ciclos de desarrollo más rápidos y una mejor gestión de certificados SSL locales con mkcert.

Este lanzamiento subraya nuestro compromiso de proporcionar un ecosistema poderoso, flexible y orientado al desarrollador. Te invitamos a explorar las notas de la versión detalladas y a profundizar en el nuevo ExampleApp para ver estas mejoras en acción.

## Núcleo Frontend de GenericSuite

### Paquete, Pull Request y Etiqueta 1.0.25

- Paquete: [https://www.npmjs.com/package/genericsuite/v/1.0.25](https://www.npmjs.com/package/genericsuite/v/1.0.25)
- Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.25](https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.25)
- PR: [https://github.com/tomkat-cr/genericsuite-fe/pull/7](https://github.com/tomkat-cr/genericsuite-fe/pull/7)

### Resumen del Pull Request # 1

Este PR implementa Axios como alternativa a Fetch mientras también actualiza dependencias y añade soporte para Vite como método de ejecución.

- Extrae y renombra la importación del componente App en index.tsx.
- Añade nuevos scripts y actualiza los existentes para gestionar enlaces simbólicos, configuraciones de módulos, certificados SSL y dependencias del método de ejecución.
- Actualiza las versiones de paquetes (p. ej. react-router-dom, Tailwind CSS) y ajusta las configuraciones de herramientas de compilación.

### Resumen del Pull Request # 2

Implementa la gestión de claves API, mejora el componente de selección genérico con descripciones de multi‑campo y corrige la clonación de valores por defecto y la lógica de validación de contraseñas.

- Introduce el componente UsersApiKey, registra sus configuraciones frontend/backend y su endpoint (GS-159).
- Extiende GenericSelectGenerator con un parámetro description_fields para etiquetas de opciones compuestas (GS-155).
- Corrige la clonación de valores por defecto en genericFuncArrayDefaultValue y refuerza UsersPasswordValidations para evitar filtrado accidental.

### Resumen del Pull Request # 3

Este PR integra Axios como alternativa a fetch, centraliza definiciones de variables de entorno para Webpack y Vite, y amplía utilidades de configuración local.

- Introduce GSFetch wrapper que delega a Axios o Fetch según REACT_APP_USE_AXIOS
- Refactoriza dbApiService para usar gsFetch y añade opcional Access-Control-Expose-Headers
- Actualiza configuraciones de Webpack y Vite para un proceso.env unificado, soporte HTTPS y salida de depuración

### Changelog

#### 1.0.25 (2025-07-08)

---

##### Nuevo
- Implementar axios como alternativa a fetch [GS-202] [GS-15].
- Añadir envvar REACT_APP_USE_AXIOS para usar axios en lugar de fetch por defecto.
- Añadir Vite como alternativa a webpack [GS-195].
- Añadir: "run_method_dependency_manager.sh" para unificar la instalación o desinstalación de dependencias del método de ejecución [GS-195].
- Añadir getAdditionalHeaders() en la clase dbApiService para enviar el encabezado 'Access-Control-Expose-Headers': 'Content-Disposition' y recibir nombres de archivos desde el backend [GS-15].
- Añadir envvar REACT_APP_USE_EXPOSE_HEADERS para añadir el encabezado 'Access-Control-Expose-Headers' al llamar al backend (por defecto desactivado) [GS-15].
- Configurar líneas por página en el editor CRUD: guardar y restaurar desde LocalStorage. Por defecto 30 (anteriormente 5) [GS-185].
- Añadir configuraciones GCE_RFC a buildConfigData() de local-config [GS-185].
- Añadir nueva función "getLocalConfigItem" a local-config para obtener un ítem de configuración desde la variable de configuración del almacenamiento local [GS-185].
- Añadir envvar REACT_APP_GCE_ACTIONS_ALLOW_MOUSE_OVER para permitir MouseOver en acciones GCE_RFC [GS-185].
- Añadir envvar REACT_APP_GCE_ACTIONS_ALLOW_MAGIC_BUTTON para permitir el Botón Mágico (3 puntos) en acciones GCE_RFC [GS-185].
- Añadir función getErrorDetail() para obtener los detalles del error desde el objeto de error [GS-15].
- Añadir función getUuidV4() para generar un UUID v4 [GS-15].
- Añadir función getContentTypeFromHeadersOrFilename() para obtener el tipo de contenido desde los encabezados o el nombre de archivo [GS-15].
- Añadir objetivo Makefile copy_ssl_certs para copiar los certificados SSL generados en el backend al frontend [GS-198].
- Añadir setupTests.js para arreglar pruebas de jest con "react-router-dom" a v7 [GS-199].
- Añadir setupTests.js y jest.config.cjs a la entrada "files" de package.json, para que estén disponibles en node_modules [GS-199].
- Añadir "@types/node" para resolver rutas sin errores usando el prefijo "@/" [GS-112].
- Implementar RUN_PROTOCOL envvar para que el protocolo http/https se configure automáticamente en la ejecución local de la app, sin intervención del usuario, como parte de la iniciativa Turborepo [GS-188].
- Añadir los parámetros "TARGET_DIR" (predeterminado "public") y "BASE_DIR" (predeterminado ".") al script "build_copy_images.sh" para copiar las imágenes al directorio "public" [GS-188].
- Añadir el script "run_method_build.sh" para ejecutar el proceso de construcción usando el método de ejecución especificado [GS-188].

##### Cambios
- Limpieza de código GCE_RFC y class_name_constants.
- convertId() movido de db.service.jsx a id.utilities.jsx [GS-185].
- fixBlob() recibe el parámetro de encabezados para obtener el tipo de contenido desde los encabezados, intenta con un try-catch para manejar errores en URL.createObjectURL(), si el error es 'Overload resolution failed', inténtalo usando binaryData.push(blobObj) [GS-15].
- isBinaryFileType() recibe un parámetro adicional contentType para obtener el tipo de contenido desde los encabezados o nombre de archivo [GS-15].
- getFilenameFromContentDisposition() verifica si el encabezado Content-Disposition contiene un filename con o sin comillas [GS-15].
- Instalar vite, webpack o react-app-rewired dependencias ejecutando run_app_frontend.sh según la variable RUN_METHOD [GS-198].
- Eliminar dependencias de vite, webpack y react-app-rewired ejecutando npm_publish.sh [GS-198].
- Implementar RUN_METHOD en aws_deploy_to_s3.sh y build_prod_test.sh, para que use vite, webpack o react-app-rewired [GS-199].
- React Router actualizado de "^v6.18.0" a "^v7.5.3" [GS-199].
- Versión predeterminada de Node actualizada a 20 en ".nvmrc" [GS-199].
- Tailwind CSS actualizado de "^v3.4.9" a "^v4.1.5" [GS-112].
- Añadir *.ts, *.tsx y ./index.html a tailwind.config.js [GS-112].
- Todos los flags de depuración desactivados.

##### Correcciones
- Arreglar el error net:ERR_CERT_AUTHORITY_INVALID en GenericSuite FE/BE usando el protocolo https [GS-198].
- Arreglar el objetivo Makefile copy_ssl_certs para que llame efectivamente a la creación de certificados SSL de respaldo del backend al frontend [GS-198].
- Arreglar la advertencia Future Flag de React Router v7 actualizando "react-router-dom" a v7 [GS-199].
- Arreglar el mensaje "‘assert’ is deprecated in import statements and support will be removed in a future version; use 'with' instead" al ejecutar "make publish" y rollup.connfig.mjs.
- Arreglar el problema de color de fondo de entradas y textareas de Tailwind 4 añadiendo gs_core.css en index.html [GS-112].
- Arreglar la mutación de objetos en llamadas Object.assign añadiendo un objeto vacío como primer parámetro
- Actualizar "webpack.config.js" para solucionar el error "Error: Can't resolve 'process/browser'" y eliminar la variable de entorno NODE_TLS_REJECT_UNAUTHORIZED [GS-199] [GS-198] [GS-195].

## Núcleo de GenericSuite Frontend AI

### Paquete, Pull Request y Etiqueta 1.0.23

- Paquete: [https://www.npmjs.com/package/genericsuite-ai/v/1.0.23](https://www.npmjs.com/package/genericsuite-ai/v/1.0.23)
- Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.23](https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.23)
- PR: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/7](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/7)

### Resumen del Pull Request # 1

Esta PR prepara el lanzamiento v1.0.23 actualizando dependencias centrales, añadiendo soporte para Vite junto a Webpack, actualizando Tailwind CSS e introduciendo una nueva prop de logotipo de cabecera.

- Añadir la propiedad appLogoHeader al componente App principal y actualizar archivos de cambios/versión.
- Integrar la configuración de Vite como alternativa a la configuración existente de Webpack.
- Actualizar Tailwind CSS a v4.x, mover definiciones de entorno a objetos compartidos y corregir el entorno de Jest.

### Changelog

#### 1.0.23 (2025-07-08)
---

##### Nuevo
- Añadir logotipo de paisaje al encabezado de la App (appLogoHeader) [GS-63].

##### Cambios
- Núcleo de GenericSuite FE actualizado a v1.0.25.
- función convertId() movida de db.service.jsx a id.utilities.jsx en GenericSuite FE [GS-185].
- Implementar axios en todas las llamadas a API para manejar la recuperación de archivos del backend Flask con todos los encabezados requeridos [GS-15].
- Añadir Vite como alternativa a webpack [GS-195].
- Tailwind CSS actualizado de "^v3.4.9" a "^v4.1.5" [GS-112].
- Añadir setupTests.js para arreglar pruebas de jest con "react-router-dom" a v7 [GS-199].
- Versión de Node predeterminada actualizada a 20 en ".nvmrc" [GS-199].
- Añadir "@types/node" para resolver rutas sin error usando el prefijo "@/" [GS-112] [PC-2].

##### Correcciones
- Arreglar el error net:ERR_CERT_AUTHORITY_INVALID en GenericSuite FE/BE usando el protocolo https [GS-198].
- Arreglar la advertencia futura de React Router v7 actualizando "react-router-dom" a v7 [GS-199].
- Arreglar la advertencia: "Warning: Each child in a list should have a unique 'key' prop..." en el render de `ChatCodeBlock`.
- Actualizar "webpack.config.js" para solucionar el error "Error: Can't resolve 'process/browser'" y eliminar la variable NODE_TLS_REJECT_UNAUTHORIZED [GS-199] [GS-198] [GS-195].

## Núcleo de GenericSuite Backend Core

### Paquete, Pull Request y Etiqueta 1.0.11

- Paquete: [https://pypi.org/project/genericsuite/0.1.11/](https://pypi.org/project/genericsuite/0.1.11/)
- Etiqueta: [https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.1.11](https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.1.11)
- PR: [https://github.com/tomkat-cr/genericsuite-be/pull/10](https://github.com/tomkat-cr/genericsuite-be/pull/10)

### Resumen del Pull Request # 1

Este PR avanza el proyecto a v0.1.11, hace que la expiración de JWT sea configurable y mejora el manejo de solicitudes en los constructores de endpoints de Flask y FastAPI.

- Aumentar la versión del paquete a 0.1.11 en setup.py y pyproject.toml
- Leer EXPIRATION_MINUTES desde el entorno en el módulo jwt
- Refactorizar la abstracción de solicitudes y el análisis de parámetros de consulta para Flask y FastAPI

### Changelog

#### 0.1.11 (2025-07-08)

##### Nuevo
- Añadir documentación de SSL_CERT_GEN_METHOD, BASE_DEVELOPMENT_PATH y SAM_BUILD_CONTAINER al archivo .env.example.
- Añadir expiración de JWT configurable con la variable de entorno EXPIRATION_MINUTES [GS-200].
- Añadir documentación RUN_PROTOCOL al archivo .env.example [GS-137].

##### Cambios
- Refactorizar el análisis de parámetros de consulta para FastAPI [GS-200].
- Refactorizar la abstracción de solicitudes para Flask [GS-15].
- Añadir 'Access-Control-Expose-Headers' a las cabeceras de respuesta de Flask [GS-15].

##### Correcciones
- Arreglar error "AttributeError: 'Request' object has no attribute 'to_dict'" en get_query_params() cuando se usa Flask en generic_array_crud() [GS-15].
- Arreglar la presentación de errores en modify_item_in_db() que no mostraba el contenido de la variable "json_file" [GS-196].
- Arreglar el problema de filtrado en el editor CRUD usando FastAPI [GS-200].
- Cambios de linting.

## Núcleo de GenericSuite Backend AI

### Paquete, Pull Request y Etiqueta 1.0.13

- Paquete: [https://pypi.org/project/genericsuite-ai/0.1.13/](https://pypi.org/project/genericsuite-ai/0.1.13/)
- Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.13](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.13)
- PR: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/9](https://github.com/tomkat-cr/genericsuite-be-ai/pull/9)

### Resumen del Pull Request # 1

Esta versión incrementa a 0.1.13, añade nuevos proveedores de IA (OpenRouter, Vertex AI), endpoints de Flask y soporte simulado para TTS de audio, mientras mejora la configurabilidad de IBM WatsonX y actualiza los defaults de búsqueda web.

- Aumentar la versión del paquete y actualizar dependencias (langchain, duckduckgo-search, faiss-cpu)
- Introducir nuevos proveedores de IA: OpenRouter y Google Vertex AI, además de endpoints REST de Flask
- Añadir GET_MOCKS_DEBUG para pruebas de audio y unificar parámetros impulsados por entorno para IBM WatsonX

### Changelog

#### 0.1.13 (2025-07-08)
---

##### Nuevo
- Implementar proveedor y modelos de IA OpenRouter [GS-182].
- Implementar proveedor y modelos de Vertex AI [GS-183].
- Añadir Endpoints de IA para Flask [GS-15].
- Añadir envvar GET_MOCKS_DEBUG para probar la herramienta text_to_audio_generator y ahorrar en facturación de IA de audio usando archivos de audio ya generados en /tmp (GET_MOCKS_DEBUG="1") o una ruta de archivo específica (GET_MOCKS_DEBUG="/path/to/file.mp3") [GS-185].

##### Cambios
- La función web_search() actualizada para usar DEFAULT_MAX_RESULTS=30 [GS-87].
- Añadir envvars para configurar varios parámetros del proveedor IBM WatsonX (IBM_WATSONX_REGION, IBM_WATSONX_TEMPERATURE, IBM_WATSONX_REPETITION_PENALTY, IBM_WATSONX_MAX_NEW_TOKENS, IBM_WATSONX_MIN_NEW_TOKENS, IBM_WATSONX_DECODING_METHOD, IBM_WATSONX_MODERATION_HAP_THRESHOLD) [GS-184].
- Implementar llamadas a AppContext.get_env_var() cuando AppContext se pasa a la clase CustomLLM, de lo contrario llama a os.environ.get() [GD-184].
- Cambiar "web_search.py" para usar min() en lugar de max() para garantizar un mínimo entre DEFAULT_MAX_RESULTS y el número de resultados solicitados por el usuario/modelo. Si la solicitud es mayor que DEFAULT_MAX_RESULTS, se usará ese valor.
- Cambiar "ADDITIONAL GUIDELINES:\n" a "REQUIREMENTS:\n" y añadir "* " (viñetas) a cada línea en build_gs_prompt (ai_chatbot_main_langchain) para obtener un mejor prompt del sistema para el modelo de IA.
- Cambiar "DEBUG" para usar Config().DEBUG == "1" en web_search [GS-185].

##### Correcciones
- Arreglar el error "ERROR: Failed building wheel for pyreqwest-impersonate" al ejecutar "sam build" (con "make deploy_run_local_qa") cuando "duckduckgo-search" se actualizó a la versión "6.1.1" [GS-87].
- Arreglar la generación de texto-a-archivo con text_to_audio_response() porque a veces con algunos modelos nunca genera un nuevo audio.
- Arreglar el parámetro model_name que falta al llamar get_openai_api().
- Establecer DUCKDUCKGO_MAX_RESULTS a 5 para evitar el error "error: https://lite.duckduckgo.com/lite/ 202 Ratelimit" [GS-87].
- Establecer DUCKDUCKGO_RATE_LIMIT_TOKEN para comprobar el "202 Ratelimit" y cambiar a búsqueda en Google si WEBSEARCH_DEFAULT_PROVIDER no es "ddg" o "google" [GS-87].

### Paquete, Pull Request y Etiqueta 1.0.14

- Paquete: [https://pypi.org/project/genericsuite-ai/0.1.14/](https://pypi.org/project/genericsuite-ai/0.1.14/)
- Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.14](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.14)
- PR: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/10](https://github.com/tomkat-cr/genericsuite-be-ai/pull/10)

### Resumen del Pull Request # 2

Este PR corrige problemas de limitación de tasa de DuckDuckGo y errores de bloqueo de referer con la API de Búsqueda Personalizada de Google, mientras actualiza la versión del paquete.

- Subir la versión a 0.1.14 y actualizar el correo del autor en setup.py y pyproject.toml
- Cambia la integración con DuckDuckGo para usar la biblioteca ddgs y añade un método de búsqueda configurable
- Añade una implementación de búsqueda paginada de Google, actualiza la sanitización de resultados y actualiza el changelog
- Actualiza la versión de Node en .nvmrc de 18 a 20

### Changelog

#### 0.1.14 (2025-07-12)
---

##### Correcciones
- Arreglar el error de "202 Ratelimit" en DuckDuckGo Search [GS-224].
- Arreglar las solicitudes de Google Search cuando el referer está vacío y se bloquea [GS-223].

## GenericSuite Backend Scripts

### Paquete, Pull Request y Etiqueta 1.0.14

- Paquete: [https://www.npmjs.com/package/genericsuite-be-scripts/v/1.0.14](https://www.npmjs.com/package/genericsuite-be-scripts/v/1.0.14)
- Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.0.14](https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.0.14)
- PR: [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/8](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/8)

### Resumen del Pull Request # 1

Este PR refactoriza el scripting para desarrollo local y CI/CD introduciendo una abstracción de motor de contenedor (Docker/Podman), mejorando los flujos de SSL y reorganizando la configuración de Nginx.

- Centralizar el manejo del motor de contenedores con container_engine_manager.sh y reemplazar llamadas directas a docker en todos los scripts por DOCKER_CMD/DOCKER_COMPOSE_CMD
- Añadir soporte de mkcert para la generación de certificados SSL locales en local_ssl_certs_creation.sh
- Reestructurar la configuración de Nginx en conf.d/ y añadir opción de reinicio en secure_local_server/run.sh

### Resumen del Pull Request # 2

Este PR estandariza comandos de motor de contenedores en todos los scripts con un nuevo gestor, añade soporte para Podman, mejora la gestión de certificados SSL vía mkcert, introduce un script de enlazado para desarrollo y actualiza versiones y objetivos de Makefile.

- Centralizar la invocación de Docker/Podman usando container_engine_manager.sh y variables DOCKER_CMD
- Generar certificados SSL por defecto con mkcert, unificar conf de nginx en conf.d y mejorar opciones del servidor local seguro
- Añadir link_gs_libs_for_dev.sh y objetivos de Makefile para el enlazado en vivo de las bibliotecas GenericSuite

### Changelog

#### 1.0.14 (2025-07-08)
---

##### Nuevo
- Añadir el script "link_gs_libs_for_dev.sh" para enlazar bibliotecas locales de GenericSuite y disparar la recarga de uvicorn/gunicorn sin necesidad de ejecutar "pipenv update". Añadir al Makefile y ejecutar con `make link_gs_libs` [FA-84].
- Añadir la variable de entorno BASE_DEVELOPMENT_PATH para especificar la ruta base de desarrollo de GS (directorio padre de repos genericsuite-be*) para habilitar "make link_gs_libs_for_dev" [FA-84].
- Añadir la variable SAM_BUILD_CONTAINER para forzar "sam build --use-container --debug" cuando se ejecute "make deploy_run_local_qa" [GS-87].
- Añadir el método "mkcert" para mejorar la creación de certificados SSL autofirmados para el entorno de desarrollo local usando "https" (anteriormente usaba "office-addin-dev-certs" por defecto) [GS-198].
- Añadir la variable de entorno SSL_CERT_GEN_METHOD para seleccionar el método de generación de certificados SSL [GS-198].
- Añadir opción de reinicio a "secure_local_server/run.sh", para que el contenedor de desarrollo del backend no se reconstruya si no es necesario [GS-198].
- Añadir logs de errores y de acceso al nginx de secure_local_server [GS-198].
- Añadir claves de API para varios servicios a EXTENSION_SECRETS en aws_secrets_manager.sh [GS-198].
- Implementar RUN_PROTOCOL para que el protocolo http/https se configure automáticamente en la ejecución local de la app, como parte de la iniciativa Turborepo [GS-188].
- Implementar Podman como alternativa a Docker [GS-215].
- Añadir CONTAINER_ENGINE y OPEN_CONTAINERS_ENGINE_APP en GenericSuite BE Core [GS-215].
- Añadir puertos de backend configurables usando BACKEND_LOCAL_PORT y BACKEND_DEBUG_LOCAL_PORT al "sls" (servidor local seguro) [GS-137].

##### Cambios
- Eliminar "make lock_pip_file" y reemplazarlo por "make requirements". Añadir "make lock" y "make npm_lock" [FA-84] [GS-15].
- "run_aws.sh" valida que CURRENT_FRAMEWORK sea Chalice para los comandos "run", "deploy", "create_stack", "describe_stack", "delete_app", "delete_stack", y ejecuta "set_chalice_cnf.sh" para todos esos comandos cuando es Chalice [GS-15].

##### Correcciones
- Arreglar el error poetry 2.x "The option --no-update does not exist" al construir el entorno dev dev (sls-backend) cuando se actualizó "duckduckgo-search" a la versión "6.1.1" [FA-84].
- Arreglar la generación de audio a partir de texto con text_to_audio_response() cuando algunos modelos no generan audio nuevo.
- Arreglar el parámetro model_name que falta al llamar get_openai_api().
- Establecer DUCKDUCKGO_MAX_RESULTS en 5 para evitar el error "202 Ratelimit" [GS-87].
- Establecer DUCKDUCKGO_RATE_LIMIT_TOKEN para detectar el "202 Ratelimit" y cambiar a búsqueda en Google si WEBSEARCH_DEFAULT_PROVIDER no es "ddg" ni "google" [GS-87].

## GenericSuite BaseCamp

### Pull Request y Etiqueta 1.0.0

- Etiqueta: [https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.0.0)
- PR: [https://github.com/tomkat-cr/genericsuite-basecamp/pull/7](https://github.com/tomkat-cr/genericsuite-basecamp/pull/7)

### Resumen del Pull Request # 1

Este PR actualiza y expande la documentación de GenericSuite, proporcionando instrucciones más claras sobre herramientas de construcción, opciones de despliegue y comandos de instalación. Cambios clave:

- Corrección de lenguaje (singular vs plural) en la descripción del endpoint del chatbot de IA.
- Adición de nuevos ejemplos de código para instalaciones especiales y configuraciones detalladas de herramientas de compilación.
- Mejoras en las instrucciones de despliegue a través de servicios de AWS y actualizaciones en el changelog.

### Resumen del Pull Request # 2

Este PR mejora el script de despliegue de mkdocs con validaciones, valores por defecto, pasos de limpieza y una lógica robusta de instalación de lftp; corrige un pequeño issue de gramática en Markdown; actualiza el runtime de AWS SAM en la plantilla; y añade un scaffold frontend completo de “ExampleApp” bajo docs/Sample-Code/exampleapp.

- Validación de parámetros, valores por defecto, limpieza de directorios y instalación multi-plataforma de lftp en mkdocs_transfer_site.sh.
- Afinación de una viñeta en docs/index.md para gramática de endpoints singular y actualización del runtime de Python en template-sam.yml.
- Introducción de un completo ejemplo de Turborepo basado en ExampleApp, incluyendo generadores, scripts, configs y presets.

### Resumen del Pull Request # 3

Una actualización concisa para incluir nuevos repos y fortalecer la introducción del proyecto a través de la documentación.

- Nuevos repos IA (GSAM, ASDT) y listados de repositorios actualizados con prefijos consistentes “GS”.
- Ampliación del índice de documentación con secciones “Why Choose” y “Key Features” para enfatizar el valor del proyecto.
- Registro de cambios en CHANGELOG para una versión no publicada.

### Changelog

#### 1.1.0 (2025-07-12)
---

##### Nuevo
- Agregar el enlace al código fuente en el archivo Basecamp README.md [GS-137].
- Añadir documentación para WEBSEARCH_DEFAULT_PROVIDER y WEBSEARCH_DUCKDUCKGO_METHOD [GS-223] [GS-224].

##### Cambios
- Cambiar "libraries" por "packages" cuando se hace referencia a paquetes frontend y backend de GenericSuite.
- Actualizar la versión predeterminada de Node a 20+ para cumplir con los requisitos de tailwindcss v4 y Shadcn v2+.
- Cambiar "make transfer" para que se ejecute en modo CI/CD por defecto.
- Cambiar redacción en history.md y README.md de exampleapp.
- Cambiar build_if_required.sh para usar arrays de bash.

##### Correcciones
- Arreglar el error "Error: Cannot find module 'dotenv'" añadiendo el directorio raíz de exampleapp al script "build_if_required.sh".
- Arreglar el error "Failed to send compressed multipart ingest: langsmith.utils.LangSmithError" al ejecutar consultas hacia el Asistente IA comentando las variables de entorno LANGCHAIN_API_KEY y LANGCHAIN_PROJECT en los archivos "exampleapp/apps/**/.env.example". 

### Pull Request y Etiqueta 1.1.0

- Etiqueta: [https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.1.0](https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.1.0)
- PR: [https://github.com/tomkat-cr/genericsuite-basecamp/pull/8](https://github.com/tomkat-cr/genericsuite-basecamp/pull/8)

### Resumen del Pull Request # 4

Este PR actualiza la documentación y corrige temas de compilación/ejecución como parte de la versión 1.1.0.

- Renombrar referencias de "libraries" a "packages" y elevar requisito de Node a ≥20 en toda la documentación
- Añadir enlace al código fuente en README de la Example App y mejorar la docs de variables de entorno
- Arreglar el script de construcción para incluir el directorio raíz y comentar variables problemáticas de Langchain

### Changelog

#### 1.0.0 (2025-07-08)
---

##### Nuevo
- Añadir monorepo de código de ejemplo [GS-137].
- Añadir comandos "make exampleapp-run", "make exampleapp-install", "make exampleapp-update" y "make exampleapp-clean" para gestionar el monorepo de ExampleApp [GS-137].
- Añadir comandos EC2, KMS, Secrets Manager y DynamoDB [GS-96].
- Añadir el script "link_gs_libs_for_dev.sh" para enlazar bibliotecas locales de GenericSuite y activar la recarga de uvicorn/gunicorn sin necesidad de ejecutar "pipenv update". Añadir al Makefile y ejecutar con `make link_gs_libs` [FA-84].
- Añadir la variable BASE_DEVELOPMENT_PATH para especificar la ruta base de desarrollo de GS (directorio padre de los repos genericsuite-be*) para habilitar "make link_gs_libs_for_dev" [FA-84].
- Añadir la variable SAM_BUILD_CONTAINER para forzar "sam build --use-container --debug" cuando se ejecuta "make deploy_run_local_qa" [GS-87].
- Añadir visión general del proyecto para Gemini CLI (o Claude Code).
- Implementar Turborepo en el monorepo de ExampleApp [GS-188].
- Implementar Pnpm en el monorepo de ExampleApp [GS-187].
- Implementar RUN_PROTOCOL para que el protocolo http/https se configure automáticamente en la ejecución local de la app, sin intervención del usuario [GS-188].
- Añadir los parámetros "TARGET_DIR" (predeterminado "public") y "BASE_DIR" (predeterminado ".") al script "build_copy_images.sh" para copiar las imágenes en el directorio "public" [GS-188].
- Añadir el script "run_method_build.sh" para ejecutar el proceso de construcción con el método de ejecución especificado [GS-188].
- Añadir documentación de "make test-run-build".
- Implementar Podman como alternativa a Docker [GS-215].
- Añadir CONTAINER_ENGINE y OPEN_CONTAINERS_ENGINE_APP en GenericSuite BE Core [GS-215].
- Añadir documentación de la variable de entorno WEBSEARCH_DEFAULT_PROVIDER a GenericSuite AI [GS-87].
- Añadir puerto de depuración configurable de backend usando BACKEND_DEBUG_LOCAL_PORT al "sls" (servidor local seguro) [GS-137].

##### Cambios
- Añadir nuevos repos a README, índice de repos y documentación general [GS-1].
- Mejorar la introducción del índice de documentación para resaltar la importancia del proyecto [GS-1].
- Eliminar "make lock_pip_file" y reemplazarlo por "make requirements". Añadir "make lock" y "make npm_lock" [FA-84] [GS-15].
- Ajustes de redacción e instrucciones en la guía de configuración
- Hacer que "mkdocs_transfer_site.sh" funcione tanto en macOS como en Linux
- Cambiar "vite.config.js" a "vite.config.mjs"
- Cambiar "fynapp_gitops" a "genericsuite-gitops"

##### Correcciones
- Corregir plantilla de configuración chalice en la documentación.

## GenericSuite Gitops

### Pull Request y Etiqueta 0.3.0

- Etiqueta: [https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.3.0](https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.3.0)
- PR: [https://github.com/tomkat-cr/genericsuite-gitops/pull/2](https://github.com/tomkat-cr/genericsuite-gitops/pull/2)

### Resumen del Pull Request # 1

Este PR mejora el script de WebUI gestionando centralizadamente inicio/parada/ejecución, añade un flujo de trabajo de "update" y actualiza el archivo Docker Compose de n8n para usar la etiqueta de imagen más reciente.

- Reestructurar y extraer lógica común en run_webui, run_help y run_done en run_webui.sh
- Introducir acciones update y update_wo para extraer y redeployar el contenedor Open-WebUI
- Cambiar el servicio de n8n en docker-compose.yml para usar la imagen latest por defecto

### Resumen del Pull Request # 2

Este PR añade un nuevo flujo de actualización para el contenedor open-webui y cambia n8n para que use su última imagen por defecto.

- Introduce comandos update y update_watchtower en run_webui.sh para manejar actualizaciones de imagen y reinicios de contenedores.
- Modifica n8n/docker-compose.yml para usar la imagen untagged/latest de n8n y comenta la versión fijada anterior.
- Actualiza CHANGELOG.md a la versión 0.3.0, documentando la nueva función de actualización webUI y el cambio de versión de n8n.

### Changelog

#### 0.3.0 (2025-07-07)
---

##### Nuevo
- Añadir documentación para reemplazar nombres de exampleapp y otros nombres de ejemplo por los nombres específicos de la app [GS-141].
- Añadir actualización de WebUI con el script `run_webui.sh update`.

##### Cambios
- Variable SECRET_GROUP movida de apply_secrets.sh a .env [GS-141].
- Correcciones de errores tipográficos, notas adicionales, eliminar IDs hard-codeados en varios archivos.
- Cambiar para ejecutar "scripts/get_os_name_type.sh" con fuente o "." en el gestor de firewall. [GS-141]
- Cambiar para obtener la última versión de n8n en el archivo de composición de Docker.

