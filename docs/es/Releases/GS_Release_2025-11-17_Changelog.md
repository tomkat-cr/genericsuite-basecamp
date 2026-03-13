# 20251117 - La Edición del Servidor MCP

![GS_Release_2025-11-17_Image_1.png](./images/GS_Release_2025-11-17_Image_1.png)

Fecha: 2025-11-17

## Resumen

Estamos encantados de anunciar el lanzamiento de GenericSuite: la Edición del Servidor MCP (2025-11-17). Este lanzamiento representa un gran salto hacia adelante en la arquitectura del backend y la experiencia del desarrollador.

Puntos clave:

- Implementación MCP: Hemos introducido un servidor fundamental del Protocolo de Comunicación entre Microservicios (MCP) en el Núcleo Backend, mejorando la comunicación entre procesos. La ExampleApp ahora cuenta con una implementación de servidor MCP en vivo para herramientas de gestión de nutrición.

- Seguridad mejorada: Hemos fortalecido significativamente nuestra postura de seguridad. La autenticación por clave API se ha movido de archivos temporales a consultas directas en la base de datos para mitigar riesgos. También corregimos vulnerabilidades críticas en dependencias como axios, urllib3 y transformers en toda la pila.

- Pila de desarrollo modernizada: Ahora tratamos uv y poetry como herramientas de primera clase para la gestión de paquetes de Python, junto a pipenv. Además, actualizamos a Node.js 20 y mejoramos la compatibilidad con Linux para nuestros scripts de compilación.

- Evolución de GitOps: Ahora está disponible un nuevo módulo Nginx Router con generación automática de certificados SSL (Let's Encrypt/Mkcert) para optimizar la gestión del tráfico.

Esta actualización garantiza que GenericSuite siga siendo una opción robusta, segura y moderna para una arquitectura de software escalable.

## Núcleo Frontend de GenericSuite

### Paquete, Pull Request y Etiqueta

* Paquete: https://www.npmjs.com/package/genericsuite/v/1.1.0
* Pull Request: https://github.com/tomkat-cr/genericsuite-fe/pull/8
* Etiqueta: https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.1.0

### Visión general de Pull Request

Resumen de cambios

Esta solicitud de extracción proporciona un conjunto exhaustivo de actualizaciones centradas principalmente en fortalecer la postura de seguridad de la aplicación y mejorar su robustez. Aborda vulnerabilidades de seguridad críticas actualizando dependencias clave e implementando medidas de protección como la limitación de tasa. Además, resuelve un error significativo en la creación de claves API y refina el manejo de URL para redirecciones, asegurando una experiencia de usuario más segura y confiable. Los cambios también incluyen varias modernizaciones de código y mejoras en el proceso de compilación.

### Aspectos destacados

- Mejoras de seguridad: Varias dependencias se han actualizado para abordar vulnerabilidades de seguridad, incluida axios (CVE-2025-7783, ataques DoS), postcss (error de análisis de retorno de línea), react-syntax-highlighter (DOM Clobbering) y babel-loader (Denegación de Servicio por Expresión Regular). Además, varias vulnerabilidades identificadas por npm audit fix --force se han resuelto, y se ha implementado una limitación básica de tasa en server.js para mitigar ataques DoS.

- Corrección de creación de API Key: Se resolvió un problema en la creación de la clave API donde un valor vacío en el objeto fieldValues podría provocar un error durante la fusión de 'resultset' en la función reduceAllResponses. La función UsersApiKeyDbPreRead ahora asigna correctamente el access_token generado dentro del objeto resultset.

- Análisis de parámetros de URL y saneamiento de redirección: Se corrigió la función getUrlParams() para analizar correctamente los parámetros de URL, especialmente cuando un parámetro de redirección contiene un hash (#). El componente LoginPage ahora incluye una función sanitizeRedirectUrl para validar y sanear las URL de redirección, previniendo vulnerabilidades de redirección abierta, y se han agregado nuevos casos de prueba para cubrir esta funcionalidad.

- Actualizaciones de configuración de compilación: La configuración de Babel se ha actualizado para reemplazar @babel/plugin-proposal-class-properties por @babel/plugin-transform-class-properties. La configuración de webpack ahora registra condicionalmente opciones y variables de entorno según la detección del entorno local, y el objetivo de limpieza del Makefile se ha actualizado para una limpieza más exhaustiva.

- Modernización y refactorización de código: Varias secciones de código en varios archivos (dist/cjs/index.js, dist/esm/index.js, src/lib/helpers/NavLib.jsx, etc.) se han refactorizado para usar sintaxis moderna de JavaScript, como plantillas de literales para concatenación de cadenas, nullish coalescing (??) para valores por defecto y propagación de objetos (...) para fusionar objetos, mejorando legibilidad y mantenibilidad.

### CHANGELOG.md

#### [1.1.0] - 2025-11-17

##### Añadido
- Añadir casos de prueba para la funcionalidad de redirección en el componente LoginPage [GS-219].

##### Cambiado
- Actualizar el formato de CHANGELOG para que sea más semántico [GS-222].

##### Corregido
- Corregir la fusión de "resultset" cuando los valores siguientes tienen la misma clave pero están vacíos en el objeto "fieldValues" (manejo de funciones específicas de GCE_RFC, función reduceAllResponses) [GS-159].
- Reemplazar el plugin de propiedades de clase por transform-class-properties para corregir la advertencia "npm warn deprecated @babel/plugin-proposal-class-properties@7.18.6: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-class-properties instead." [GS-219].
- Corregir el análisis de parámetros de URL en getUrlParams() para manejar el parámetro de redirección con un hash (#) en el valor [GS-219].
- Mejorar la configuración de webpack para registrar condicionalmente opciones y variables de entorno según la detección del entorno local.
- Corregir: "generic.editor.rfc.specific.func.jsx" para evitar TypeError al fusionar fieldValues en la función "reduceAllResponses" [GS-230].

##### Seguridad
- Actualizar "axios" a ^1.13.0 para corregir la vulnerabilidad de seguridad [GS-219]:
  - "form-data" CWE-343, CVE-2025-7783, CVSS 9.4.
  - "Axios es vulnerable a ataques DoS por falta de verificación del tamaño de datos"
  - "form-data usa función aleatoria insegura en form-data para elegir el boundary"
- Corregir "PostCSS line return parsing error" actualizando "postcss" a "^8.5.6" [GS-219].
- Corrección de limitación de tasa básica para mitigar DoS por operaciones FS costosas en "server.js" [GS-219].
- Mejorar el manejo de redirección en LoginPage con saneamiento de URL [GS-219].
- Actualizar "react-syntax-highlighter" a "^16.1.0" para corregir la vulnerabilidad de seguridad [GS-219]:
  - "Vulnerabilidad de DOM Clobbering de PrismJS"
- Aumentar babel-loader a ^10.0.0 para corregir "@"eslint/plugin-kit es vulnerable a ataques de Denegación de Servicio mediante expresiones regulares" [GS-219].
- Las siguientes vulnerabilidades de seguridad se corrigieron ejecutando "npm audit fix --force" [GS-219]:
  - "Contaminación de prototipo en JSON5 mediante Parse Method"
  - "pbkdf2 devuelve memoria no inicializada/llena de ceros predecible para algoritmos no normalizados o no implementados"
  - "pbkdf2 pasa por alto la entrada Uint8Array, devolviendo claves estáticas"
  - "Contaminación de prototipo en webpack loader-utils"
  - "sha.js carece de comprobaciones de tipo que llevan a un rewind de hash y a datos creados"

...

## GenericSuite Frontend AI

### Paquete, Pull Request y Etiqueta

* Paquete: https://www.npmjs.com/package/genericsuite-ai/v/1.1.0
* Pull Request: https://github.com/tomkat-cr/genericsuite-fe-ai/pull/8
* Etiqueta: https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.1.0

### Visión general de Pull Request

Resumen de cambios

Esta solicitud de extracción ofrece una actualización significativa centrada en fortalecer la seguridad, mejorar la experiencia del usuario del Asistente de IA y modernizar la gestión de dependencias del proyecto. Se han parcheado vulnerabilidades de seguridad clave mediante actualizaciones de dependencias y la introducción de limitación de tasa. El renderizado de bloques de código del Asistente de IA se ha solucionado para mejorar la legibilidad, y el proceso de compilación se ha optimizado actualizando configuraciones de Babel y eliminando herramientas de desarrollo obsoletas. Estos cambios contribuyen a una aplicación más segura, estable y fácil de usar.

Highlights

- Mejoras críticas de seguridad: Se abordaron múltiples vulnerabilidades actualizando dependencias clave como "axios" y "postcss", solucionando problemas como CWE-343, CVE-2025-7783 y "Hugging Face Transformers Regular Expression Denial of Service (ReDoS)". También se introdujo limitación de tasa en "server.js" para prevenir ataques DoS.

- Correcciones UI de IA: Se resolvió un problema donde los bloques de código de chat de IA Assistant carecían de envoltura correcta de palabras y desplazamiento horizontal, mejorando significativamente la legibilidad.

- Modernización de dependencias: Actualizaciones de configuraciones de Babel para usar "@babel/plugin-transform-class-properties" y eliminación de dependencias de desarrollo obsoletas (Vite, Webpack, React-App-Rewired) para agilizar la construcción y publicación.

- Optimización del resaltado de código: El componente "ChatCodeBlock" ahora importa inteligentemente los lenguajes soportados desde "react-syntax-highlighter", haciendo el código más limpio y robusto.

- Mejora del proceso de compilación: Mejora de la configuración de Jest para manejar correctamente módulos ES desde "node_modules" y actualización del "Makefile" para una mejor gestión de dependencias durante la publicación.

### CHANGELOG.md

#### [1.1.0] - 2025-11-17

##### Añadido
- Añadir opciones de protocolo de ejecución local (RUN_PROTOCOL) en .env.example.

##### Cambiado
- Actualizar el formato de CHANGELOG para que sea más semántico.
- Quitar el registro en el componente AudioPlayer para mayor claridad.
- Modificar Makefile para mover dependencias de desarrollo antes de la prepublicación [GS-230].
- Optimizar el componente ChatCodeBlock importando la lista de lenguajes compatibles directamente desde react-syntax-highlighter en lugar de definir una larga lista de lenguajes en getPrismLanguajes() [GS-230].

##### Corregido
- Corregir que la IA Assistant muestre bloques de código de chat con mal formato sin envoltura de palabras ni desplazamiento horizontal [GS-225].
- Quitar Vite, Webpack y React-App-Rewired antes de publicar en NPM.
- Reemplazar el plugin de propiedades de clase por transform-class-properties para corregir la advertencia "npm warn deprecated @babel/plugin-proposal-class-properties@7.18.6" [GS-219].
- Arreglar el error "[!] Only inline sourcemaps are supported when bundling to stdout." al ejecutar "make publish" (específicamente en el comando "rollup -c") debido a que `react-syntax-highlighter` v16+ y sus dependencias ahora usan ES modules de forma exclusiva, y Jest necesita configuración explícita para transformar estos módulos desde `node_modules` (que normalmente se ignoran por defecto) [FA-83].

##### Seguridad
- Actualizar "axios" a ^1.13.0 para corregir la siguiente vulnerabilidad de seguridad [GS-219]:
  - "form-data" CWE-343, CVE-2025-7783, CVSS 9.4.
  - "Axios es vulnerable a ataques DoS por falta de verificación del tamaño de datos"
  - "form-data usa función aleatoria insegura en form-data para elegir el boundary"
- Corregir "PostCSS line return parsing error" actualizando "postcss" a "^8.5.6" [GS-219].
- Limitación básica de tasa para mitigar DoS por operaciones FS costosas en "server.js" [GS-219].
- Actualizar "react-syntax-highlighter" a "^16.1.0" para corregir la vulnerabilidad de seguridad [GS-219]:
  - "Vulnerabilidad de DOM Clobbering de PrismJS"
- Aumentar babel-loader a ^10.0.0 para corregir "@eslint/plugin-kit es vulnerable a Denegación de Servicio mediante expresiones regulares con ConfigCommentParser" [GS-219].
- Se corrigieron las siguientes vulnerabilidades de seguridad ejecutando "npm update" [GS-219]:
  - "Contaminación de prototipo en JSON5 mediante Parse Method"
  - "pbkdf2 devuelve memoria no inicializada/llena de ceros predecible para algoritmos no normalizados o no implementados"
  - "pbkdf2 pasa por alto la entrada Uint8Array, devolviendo claves estáticas"
  - "Contaminación de prototipo en webpack loader-utils"
  - "sha.js carece de comprobaciones de tipo que conducen a rewind de hash y a pasar datos manipulados"

...

## GenericSuite Backend Core

### Paquete, Pull Request y Etiqueta

* Paquete: https://pypi.org/project/genericsuite/0.2.0/
* Pull Request: https://github.com/tomkat-cr/genericsuite-be/pull/13
* Etiqueta: https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.2.0

### Resumen de Pull Request

Resumen de cambios

Esta solicitud de extracción introduce la implementación fundamental de un servidor MCP (Protocolo de Comunicación entre Microservicios), mejorando significativamente las capacidades de microservicios del backend y la comunicación entre procesos. También trae actualizaciones de seguridad cruciales al rediseñar la autenticación de claves API y actualizar varias dependencias centrales para parchear vulnerabilidades conocidas. Los cambios incluyen refactorización sustancial para mejorar la modularidad y mantenibilidad, junto con actualizaciones en configuraciones del entorno de desarrollo y procesos de construcción.

Destacados

- Implementación del servidor MCP: El núcleo de esta solicitud de extracción es la implementación de un servidor MCP (Protocolo de Comunicación entre Microservicios), incluyendo nuevos endpoints para la gestión de usuarios (inicio de sesión, creación de superadmin, datos del usuario actual, generación de archivos de API key) y una capa de abstracción de marco para respaldar MCP.

- Seguridad mejorada: Se han realizado mejoras significativas de seguridad, particularmente al mover la autenticación de claves API desde archivos temporales en /tmp a una consulta directa en la base de datos. Esto mitiga riesgos asociados con el almacenamiento de datos sensibles en directorios de escritura mundial. Además, numerosas actualizaciones de dependencias abordan diversas vulnerabilidades en bibliotecas como urllib3, Werkzeug, cryptography, Requests, fastmcp, mcp y dnspython.

- Refactorización arquitectónica para modularidad: GenericDbHelper se ha refactorizado en GenericDbHelperSuper (una clase base sin contexto de solicitud) y GenericDbHelperWithRequest (una clase consciente de la solicitud). Esta separación de responsabilidades mejora la reutilización y soporta el modelo operativo del nuevo servidor MCP, que no siempre implica un contexto de solicitud web.

- Mejoras de gestión de dependencias y entorno: El proyecto ahora admite Python 3.10+ y Node.js 20. Nuevas variables de entorno (PEM_TOOL, AUTO_RELOAD, RUN_METHOD, etc.) se han introducido para una configuración más flexible de los gestores de paquetes de Python y el desarrollo local. El Makefile se ha actualizado con comandos de ayuda e instalación, y poetry run se utiliza ahora para los pasos de construcción y publicación.

- Calidad de código y mantenibilidad: Varias mejoras de calidad de código incluyen corrección de docstrings, eliminación de código no utilizado, simplificación del manejo de variables de entorno con get_non_empty_value y centralización de la lógica de inicialización del registro en una función auxiliar privada para adherirse a principios DRY.

### CHANGELOG.md

#### [0.2.0] - 2025-11-17

##### Añadido
- Implementar MCP en GS BE Core [GS-189].
- Añadir variable de entorno PEM_TOOL para seleccionar la herramienta de gestión de paquetes y dependencias de Python (uv, pipenv y poetry), por defecto "uv" [GS-77].
- Añadir variable de entorno AUTO_RELOAD a .env.example, para solucionar algunos problemas con la opción "--auto-reload" / "--reload" al ejecutar la app en "run_aws.sh", Turborepo y "uv", por defecto "1" [GS-77].
- Añadir get_non_empty_value para manejar variables de entorno declaradas en docker-composer.yml sin valor.
- Añadir comando "help" al Makefile.
- Añadir comando "install" al Makefile para facilitar la gestión de dependencias.  

##### Cambiado
- Cambiar la versión de Node.js en .nvmrc a 20.
- Actualizar README para claridad y precisión.
- Actualizar el formato de CHANGELOG para ser más semántico, para consistencia, claridad y el estándar "Keep a Changelog".
- Actualizar correo del autor en pyproject.toml y setup.py.
- Modificar pyproject.toml para compatibilidad con Python 3.10 y versiones superiores.
- Añadir .vscode y .idea al archivo .gitignore.
- Usar Poetry para ejecutar comandos de construcción y publicación en Makefile.
- Limpieza de código y cambios de linting.
- Autenticar claves API desde la base de datos [GS-240]
- get_non_empty_value() simplificado con un patrón de Python más idiomático.

##### Corregido
- Actualizar la dependencia urllib3 a la versión 2.5.0 para corregir un error de "make publish".
- Añadir nuevas dependencias de desarrollo "build" y "twine" para corregir un error de "make publish".
- Corregir el conflicto entre "boto3" y "s3transfer" removiendo dependencias "s3transfer" y "botocore" en pyproject.toml, ya que ya están incluidas en "boto3".
- Actualizar manejo de errores en set_tool_context() para obtener un mensaje de error más conciso desde app_context [GS-240].

##### Seguridad
- Actualizar "urllib3" a "^2.5.0" para corregir vulnerabilidades de seguridad [GS-219]:
    * "Catastrophic backtracking en el analizador de autoridad de URL cuando se pasa una URL con muchos @"
    * "`Cookie` HTTP header no se elimina en redirecciones entre orígenes"
    * "Las redirecciones de urllib3 no se desactivan cuando los reintentos están desactivados al instanciar PoolManager"
    * "La cabecera Proxy-Authorization de urllib3 no se elimina durante redirecciones entre orígenes"
    * "El cuerpo de la solicitud de urllib3 no se elimina tras redirección de cambios de método de GET"
    * "Usar SSLContext predeterminado para solicitudes HTTPS en un proxy HTTPS no verifica el nombre de host del certificado para la conexión proxy"
    * "`Cookie` HTTP header no se elimina en redirecciones entre orígenes"
- Actualizar "Werkzeug" a "^3.0.6" para corregir vulnerabilidades [GS-219]:
    * "Potencial agotamiento de recursos en Werkzeug al analizar datos de formulario"
    * "safe_join no seguro en Windows"
- Actualizar "cryptography" a "^44.0.1" para corregir vulnerabilidad [GS-219]:
    * "pyca/cryptography tiene OpenSSL vulnerable incluido en ruedas de cryptography"
- Actualizar "Requests" a "^2.32.4" para corregir vulnerabilidades [GS-219]:
    * "Requests vulnerable a filtración de credenciales .netrc vía URLs maliciosas"
    * "Usar SSLContext predeterminado para HTTPS en un proxy HTTPS no verifica el nombre de host del certificado"
    * "OpenSSL vulnerable incluido en ruedas de cryptography"
- Actualizar "fastmcp" a "^2.13.0" para corregir vulnerabilidades [GS-219]:
    * "Integración de autenticación FastMCP permite suplantación de autoridad"
    * "Authlib es vulnerable a Denegación de Servicio por JOSE segments excesivos"
- Actualizar "mcp" a ">=1.21.0" para corregir vulnerabilidades [GS-219]:
    * "Starlette vulnerable a DoS por combinación de Range header en ``starlette.responses.FileResponse``"
- Actualizar "dnspython" a ">=2.6.1" para corregir vulnerabilidades [GS-219]:
    * "Posible DoS vía el mecanismo Tudoor en eventlet y dnspython"
- Leer los datos del usuario desde la base de datos en "get_api_key_auth()" en lugar de "/tmp/params_[user_id].json" porque almacenar datos sensibles o de configuración en un directorio de escritura mundial como /tmp es un riesgo de seguridad [GS-240].
- Añadir la variable de entorno USER_PARAMS_FILE_ENABLED para habilitar/deshabilitar el archivo de parámetros del usuario "/tmp/params_[user_id].json", por defecto "0" para evitar riesgos de seguridad en entornos de producción [GS-240].

...

## GenericSuite Backend AI

### Paquete, Pull Request y Etiqueta

* Paquete: https://pypi.org/project/genericsuite-ai/0.2.0/
* Pull Request: https://github.com/tomkat-cr/genericsuite-be-ai/pull/11
* Etiqueta: https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.2.0

### Visión general de Pull Request

Resumen de cambios

Esta solicitud de extracción ofrece una actualización significativa centrada en mejorar la seguridad, la mantenibilidad y la experiencia de desarrollo del proyecto. Aborda vulnerabilidades de seguridad críticas mediante actualizaciones de dependencias, facilita la integración de modelos de HuggingFace y refina los procesos de construcción y configuración. Estos cambios buscan mejorar la estabilidad y robustez de la aplicación mientras brindan directrices de desarrollo más claras.

Destacados

- Actualizaciones de seguridad: Varias dependencias, incluidas transformers, urllib3, setuptools, clarifai, pypdf y langchain, se han actualizado para abordar diversas vulnerabilidades, como ReDoS, traversal de rutas y ataques XXE.

- Refactorización de modelos HuggingFace: El manejo de modelos HuggingFace se ha refactorizado. El tipo de modelo huggingface ahora se integra con la API de OpenAI para generación de texto, mientras que el comportamiento anterior se ha trasladado a un nuevo tipo langchain_huggingface. Se han eliminado las clases personalizadas GsHuggingFaceEndpoint y GsChatHuggingFace en favor de llamadas a HuggingFace con OpenAI API.

- Gestión de dependencias y mejoras en el proceso de construcción: El requisito de versión de Python del proyecto se ha actualizado de 3.9 a 3.10. Se han añadido nuevos comandos de instalación al Makefile para facilitar la gestión de dependencias, y los comandos de construcción y publicación ahora utilizan explícitamente poetry run.

- Configuración y variables de entorno: Se han introducido nuevas variables de entorno PEM_TOOL (para gestión de paquetes de Python) y AUTO_RELOAD (para desarrollo local). Las banderas de depuración en varios módulos de IA ahora son configurables mediante variables de entorno (p. ej., AI_CHATBOT_DEBUG, AI_AUDIO_PROCESSING_DEBUG, etc.). El archivo .env.example se ha actualizado para mayor claridad y para reflejar las nuevas opciones de configuración.

- Compatibilidad y limpieza de código con Langchain: Se han migrado importaciones de langchain.* a langchain_classic.* para garantizar compatibilidad con Langchain 1.0.x. Varias banderas DEBUG se han hecho configurables mediante variables de entorno, y se han realizado mejoras de formato de código y docstrings, incluyendo correcciones de errores tipográficos y añadir noqa: E501 para líneas largas.

- Eliminación de dependencias: Se han eliminado las dependencias langchain-together, text-generation y clarifai del proyecto.

### CHANGELOG.md

#### [0.2.0] - 2025-11-17

##### Añadido
- Añadir comando "install" al Makefile para facilitar la gestión de dependencias.
- Añadir PEM_TOOL a .env.example, para seleccionar la herramienta de gestión de paquetes y dependencias de Python (uv, pipenv y poetry), por defecto "uv" [GS-77].
- Añadir AUTO_RELOAD a .env.example, para solucionar algunos problemas con la opción "--auto-reload" / "--reload" ejecutando la app en "run_aws.sh", Turborepo y "uv", por defecto "1" [GS-77].
- Añadir variables DEBUG a todos los módulos de IA para habilitar el registro de depuración, por defecto "0" (deben estar configuradas en el archivo .env) [GS-230].

##### Cambiado
- Actualizar README para claridad y precisión.
- Actualizar formato de CHANGELOG para ser más semántico.
- Actualizar correo del autor en pyproject.toml y setup.py.
- Aumentar urllib3 a 2.5.0 y numpy a 2.0.2 para compatibilidad con GS BE Core.
- Refactorizar importaciones en ai_langchain_models.py para incluir ChatBedrock (AWS Bedrock) y langchain-aws de forma condicional.
- Mejorar funciones de consulta de texto de HuggingFace ("huggingface_remote" model type) para soportar la integración de la API de OpenAI.
- Cambiar el tipo de modelo "huggingface" para usar la API de OpenAI en lugar del HuggingFaceEndpoint de langchain, de modo que no se requiera la dependencia "langchain-huggingface".
- El antiguo tipo de modelo "huggingface" ahora es "langchain_huggingface" y requiere la dependencia "langchain-huggingface", que es opcional por defecto.
- El tipo de modelo "gs_huggingface" es equivalente al tipo "huggingface_remote", llamando a Hugging Face con requests.

##### Corregido
- Arreglar el error de llamada de herramientas de IA debido a un desajuste de tipos de parámetros de pydantic, cambiando la anotación de tipo de Dict a Any.
- Corregir "langchain_community not found" añadiendo la dependencia "langchain-community". Esta adición requirió la actualización de dependencias "langchain" a "0.3.26" y "faiss-cpu" a "^1.11.0.post1".
- Arreglar el streaming de respuestas en funciones de consulta de texto de "huggingface_remote".
- Arreglar los problemas con la migración de imports de langchain 1.0.x a langchain_classic.*.
- Añadir nuevas dependencias de desarrollo incluyendo build y twine para corregir un error de "make publish".
- Usar Poetry para ejecutar comandos de construcción y publicación en Makefile para corregir un error de "make publish".

##### Seguridad
- Actualizar "transformers" a "^4.57.1" para corregir vulnerabilidades [GS-219]:
    * "Regular Expression Denial of Service (ReDoS)", CVE-2025-5197 y CWE-1333
    * "Hugging Face Transformers ReDoS"
    * "Transformers vulnerable a ReDoS en el optimizador AdamWeightDecay"
    * "Hugging Face Transformers tiene Denegación de Servicio por Regex"
    * "Transformers vulnerable a ReDoS a través de su MarianTokenizer"
    * "Transformers vulnerable a ReDoS a través de su clase DonutProcessor"
    * "Vulnerabilidad de validación de entrada de Transformers que puede explotarse mediante inyección de nombres de usuario"
- Actualizar "urllib3" a "^2.5.0" para corregir vulnerabilidades [GS-219]:
    * "Backtracking catastrófico en el analizador de autoridad de URL cuando se pasa una URL con muchos @"
    * "`Cookie` cabecera HTTP no se elimina en redirecciones entre orígenes"
    * "Las redirecciones de urllib3 no se desactivan cuando los reintentos están desactivados en PoolManager"
    * "La cabecera Proxy-Authorization de urllib3 no se elimina durante redirecciones entre orígenes"
    * "El cuerpo de la solicitud de urllib3 no se elimina tras redirección de cambios de método a GET"
    * "Usar SSLContext predeterminado para HTTPS en un proxy HTTPS no verifica el nombre de host del certificado para la conexión del proxy"
    * "`Cookie` cabecera HTTP no se elimina en redirecciones entre orígenes"
- Actualizar "setuptools" a "^78.1.1" para corregir vulnerabilidad [GS-219]:
    * "setuptools tiene una vulnerabilidad de recorrido de ruta en PackageIndex.download que conduce a Escritura Arbitraria de Archivos"
- Eliminar "text-generation" para corregir vulnerabilidad (tampoco se usa en este proyecto) [GS-219]:
    * "Existe una vulnerabilidad de inyección de código en el repositorio huggingface/text-generation-inference"
- Las vulnerabilidades de "llama-index-core" se resuelven al ya no ser dependencia del proyecto (debido a la eliminación de clarifai):
    * "Llama-index-core maneja archivos temporales de forma insegura"
    * "LlamaIndex vulnerable a un DoS por JSONReader"
    * "LlamaIndex vulnerable a Path Traversal por encode_image"
    * "LlamaIndex vulnerable a DoS por parsing recursivo de JSON"
    * "LlamaIndex tiene documentación incompleta sobre la ejecución de programas relacionada con JsonPickleSerializer"
- Instalar "pypdf" última versión "^6.1.3" para corregir vulnerabilidades (era una dependencia de clarifai) [GS-219]:
    * "pypdf puede hacer bucles infinitos al leer imágenes DCT inline sin marcador EOF"
    * "pypdf puede agotar RAM mediante flujos LZWDecode manipulados"
    * "Los flujos FlateDecode manipulados pueden agotar RAM"
- Actualizar todas las dependencias de langchain a las últimas versiones para corregir vulnerabilidades [GS-219]:
    * "LangChain Text Splitters vulnerable a XML External Entity (XXE) por análisis XSLT inseguro"

##### Eliminado
- Eliminar "langchain-together" para permitir la actualización de todas las demás dependencias de langchain y encaminar llamadas de Together AI a través de la API de OpenAI.
- Eliminar "clarifai" para que sea opcional por defecto [GS-219].
- Eliminar las clases GsHuggingFaceEndpoint y GsChatHuggingFace porque fueron reemplazadas por las nuevas llamadas Hugging Face con la API de OpenAI.

...

## GenericSuite Backend Scripts

### Paquete, Pull Request y Etiqueta

* Paquete: https://www.npmjs.com/package/genericsuite-be-scripts/v/1.2.0
* Pull Request: https://github.com/tomkat-cr/genericsuite-be-scripts/pull/11
* Etiqueta: https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.2.0

### Resumen de Pull Request

Resumen de cambios

Esta solicitud de extracción introduce mejoras significativas en la gestión de dependencias del proyecto y en los flujos de desarrollo local. Integra a los gestores de paquetes de Python modernos 'uv' y 'poetry' como herramientas de primer nivel, proporcionando una interfaz unificada a través de un nuevo script 'run_pem.sh'. Los cambios también incluyen una actualización a Node.js 20, configuraciones de auto-reload más flexibles para los servidores de aplicación locales y una amplia refactorización de scripts de shell para mejorar la consistencia y la compatibilidad en Linux. Estas actualizaciones buscan proporcionar a los desarrolladores más opciones y una experiencia más fluida al gestionar dependencias del proyecto y ejecutar servicios locales.

Destacados

- Gestión de paquetes de Python mejorada: Se introdujeron 'uv' y 'poetry' como herramientas alternativas de gestión de paquetes y dependencias de Python, junto a 'pipenv', con 'uv' configurado como predeterminado. Un nuevo script envoltorio, 'run_pem.sh', centraliza todas las operaciones de gestión de paquetes para mantener la consistencia.

- Entorno de desarrollo mejorado: Actualizada la versión de Node.js a 20, refinadas opciones de auto-reload para servidores locales (Chalice, Gunicorn, Uvicorn) y ajustadas políticas de reinicio de MongoDB a 'unless-stopped' para una mejor experiencia de desarrollo local.

- Consistencia de scripts y compatibilidad con Linux: Estandarizada la ejecución de scripts de shell reemplazando 'sh' por 'bash' en numerosos objetivos de Makefile y llamadas a scripts internos, mejorando la compatibilidad y consistencia, especialmente en entornos Linux.

- Mejoras de flujo de gestión de dependencias: Añadidos nuevos objetivos 'make update' y 'make update_dev', y se aseguró que 'npm install' se ejecute antes de las instalaciones de dependencias de Python, optimizando el proceso de mantener las dependencias del proyecto actualizadas.

### CHANGELOG.md

#### [1.2.0] - 2025-11-17

##### Añadido
- Añadir herramientas de gestión de paquetes de Python "uv" y "poetry" [GS-77].
- Añadir PEM_TOOL para seleccionar la herramienta de gestión de paquetes y dependencias (uv, pipenv y poetry), por defecto "uv" [GS-77].
- Añadir AUTO_RELOAD para fix de issues con "--auto-reload" / "--reload" ejecutando la app en "run_aws.sh", Turborepo y "uv", por defecto "1" [GS-77].
- Añadir compatibilidad con Linux: reemplazar "sh" por "bash" en Makefile y archivos package.json para ejecutar en Linux [GS-230].
- Añadir "make update" y "make update_dev" para actualizar las dependencias.

##### Cambiado
- Incrementar versión de Node.js en .nvmrc a 20.
- Modificar el correo del autor en package.json.
- Mejorar README para claridad y precisión.
- Actualizar CHANGELOG para ser más semántico.
- Cambiar la política de reinicio de MongoDB en la pila de pruebas de 'always' a 'unless-stopped'.
- Cambiar "make install" y "make install_dev" para llamar a "sh node_modules/genericsuite-be-scripts/scripts/run_pem.sh install" y "sh node_modules/genericsuite-be-scripts/scripts/run_pem.sh install_dev" respectivamente

##### Corregido
- Cambiar "make install" y "make install_dev" para que "npm install" se llame antes de "sh node_modules/genericsuite-be-scripts/scripts/run_pem.sh" para instalar los GS BE Scripts y evitar el error "Error: Cannot find module 'genericsuite-be-scripts' [GS-77].
- Arreglar "change_local_ip_for_dev.sh" añadiendo verificaciones de $2 y $3 para evitar sobrescribir BACKEND_LOCAL_PORT y FRONTEND_LOCAL_PORT [GS-230].

...

## GenericSuite BaseCamp

### Pull Request y Etiqueta

* Pull Request: 
    - https://github.com/tomkat-cr/genericsuite-basecamp/pull/10
    - https://github.com/tomkat-cr/genericsuite-basecamp/pull/11
    - https://github.com/tomkat-cr/genericsuite-basecamp/pull/12
    - https://github.com/tomkat-cr/genericsuite-basecamp/pull/13
    - https://github.com/tomkat-cr/genericsuite-basecamp/pull/14
* Etiquetas:
    - https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.3.0
    - https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.3.1
    - https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.3.2

### Resumen de Pull Request (Resumen)

Resumen de cambios

Esta actualización mejora significativamente ExampleApp al incorporar un nuevo servidor MCP para la gestión de nutrición. Más allá de las características, hemos modernizado el entorno de desarrollo al cambiar a uv para la gestión de Python y refinar nuestros procesos de construcción pnpm. El lanzamiento también incluye una reestructuración completa de la documentación de GenericSuite y parches de seguridad esenciales para garantizar un ecosistema más robusto y orientado al desarrollo.

Destacados

- Nuevo servidor MCP para ExampleApp: Se ha añadido un nuevo servidor Protocolo de Contexto de Modelo (MCP) a ExampleApp, introduciendo herramientas de gestión de comida y nutrición y convirtiéndose en una cuarta opción de backend junto a FastAPI, Flask y Chalice. Además, se incluyeron nuevos comandos 'make' para simplificar la instalación y actualización de todos los servicios de ExampleApp.

- Entorno Python y gestión de dependencias: El proyecto ExampleApp está migrando a Python 3.12 y adopta 'uv' como la herramienta preferida de gestión de paquetes y dependencias de Python, con documentación detallada para migrar desde 'pipenv'.

- Actualizaciones de documentación: La documentación se ha ampliado y aclarado, cubriendo la configuración detallada de ExampleApp, pautas sobre gestores de paquetes de Python y nuevos indicadores de depuración de módulos de IA.

- Reestructuración y mejora de especificaciones: Los documentos de especificaciones del proyecto han sido reformateados, reemplazando el antiguo GEMINI.md por una suite de archivos de contexto detallados (Resumen del Proyecto, Contexto de Producto, Contexto Activo, Patrones del Sistema, Contexto Técnico). Esto proporciona una visión más estructurada y completa del ecosistema GenericSuite.

- Actualizaciones de dependencias y del sistema de construcción: Archivos clave de dependencias como .gitignore, pnpm-lock.yaml y requirements.txt se han actualizado para reflejar nuevos paquetes, eliminar otros y asegurar una resolución de dependencias coherente. Los scripts de construcción y configuraciones también se han ajustado para soportar el nuevo servidor MCP y mejorar la estabilidad general.

- Mejora de la experiencia del desarrollador: Cambios que incluyen agregar documentación para enlazar bibliotecas de GenericSuite para recarga en caliente, actualizar archivos .env.example para mayor claridad y corregir el script mkdocs_install.sh para la gestión adecuada de dependencias, todo orientado a optimizar el flujo de desarrollo.

- Validación de Pydantic de ExampleApp y generación de prompts de IA: El archivo ai_gpt_fn_app.py ahora incluye validadores de campos de Pydantic para varias unidades y tipos de comida, asegurando la integridad de los datos. También se han añadido nuevas funciones para generar análisis nutricional y prompts de IA para la planificación de comidas.

- Nuevo comando Makefile: Se añadió un nuevo comando update-pnpm en el Makefile de ExampleApp para simplificar la instalación.

- Estandarización del changelog: Los archivos CHANGELOG.md del proyecto se han actualizado para seguir estrictamente el estándar 'Keep a Changelog', asegurando un formato semántico y coherente para las notas de la versión en todos los componentes.

- Actualizaciones de dependencia: Varias dependencias en pnpm-lock.yaml se han actualizado, incluyendo @vitejs/plugin-react, postcss y @rolldown/pluginutils, junto con ajustes a plugins de Babel y dependencias pares.

- Configuración del espacio de trabajo PNPM: Se ha mejorado pnpm-workspace.yaml para especificar onlyBuiltDependencies para una mejor gestión de paquetes.

- Mejoras de seguridad: Se han implementado mejoras clave de seguridad, como actualizar dependencias críticas de paquetes (p. ej., turbo, dotenv, GS BE Core/AI), y deshabilitar el encabezado 'X-Powered-By' en la interfaz para evitar exponer información del marco de trabajo.

### CHANGELOG.md

#### [1.3.2] - 2025-11-19

##### Añadido
- Nuevo comando "lsof" para Makefile para listar puertos TCP abiertos.

##### Cambiado
- Actualizar "build_if_required.sh" para usar "make install" en lugar de comandos npm.
- Mejorar "clean_directory.sh" para también buscar y eliminar archivos ".log" para su eliminación.
- Actualizar el README de ExampleApp para añadir la sección MCP Server y mejorar la documentación.

##### Corregido
- Arreglar el fallo del script "build_if_required.sh" para instalar y construir todas las aplicaciones de ExampleApp si alguna de ellas no tiene el directorio node_modules.

#### [1.3.1] - 2025-11-19

##### Añadido
- Nota de lanzamiento para la Edición del Servidor MCP (2025-11-17) [GS-230].
- Mejorar el índice principal de documentación con una nueva sección de Notas de Lanzamiento [GS-230].
- Añadir estructura de directorio detallada en la lectura indicativa genericsuite-configs [GS-230].

##### Cambiado
- Actualizar dependencias en requirements.txt y package-lock.json a versiones más recientes, incluyendo backrefs, certifi y turbo [GS-230].

##### Corregido
- Arreglar el error "npm error code ERR_INVALID_ARG_TYPE npm error The 'from' argument must be of type string. Received undefined" en los comandos "make exampleapp-install-all" y "make exampleapp-update-all" [GS-230].
- Arreglar el error "docs/Sample-Code/exampleapp/apps/ui/public/static not found" en el comando "make publish" [GS-230].
- Arreglos menores de formato en archivos JSON y scripts [GS-230].

#### [1.3.0] - 2025-11-17

##### Añadido
- Añadir el nuevo servidor MCP para ExampleApp con herramientas de comida y gestión de nutrición [GS-189]. 
- Añadir compatibilidad con Linux: reemplazar "sh" por "bash" en Makefile y archivos package.json para ejecutar en Linux [GS-230].
- Añadir PEM_TOOL para seleccionar la herramienta de gestión de paquetes y dependencias de Python (uv, pipenv y poetry), por defecto "uv" [GS-77].
- Añadir AUTO_RELOAD para solucionar algunos problemas con la opción "--auto-reload" / "--reload" ejecutando la app en "run_aws.sh", Turborepo y "uv", por defecto "1" [GS-77].
- Añadir los comandos `make exampleapp-update-all` y `make exampleapp-install-all` para actualizar e instalar todas las apps de ExampleApp.
- Añadir el comando `make link_gs_libs` y documentarlo en los GS BE Scripts.
- Añadir desanexión de activos comunes y solicitar confirmación del usuario antes de limpiar directorios en el comando `make exampleapp-clean`.
- Añadir el comando "clean" en Makefile para la gestión de activos.
- Añadir el nuevo comando `update-pnpm` en See ExampleApp Makefile para una instalación más fluida.
- Añadir las variables de entorno MCP_SERVER_PORT, MCP_SERVER_HOST, MCP_TRANSPORT, GS_USER_NAME, GS_USER_ID y GS_API_KEY al archivo .env.example del servidor MCP de ExampleApp [GS-189].
- Añadir el archivo "mcp_server.log" al directorio del servidor MCP de ExampleApp para facilitar la depuración.
- Añadir la variable de entorno HUGGINGFACE_PROVIDER para configurar el proveedor de inferencia de Hugging Face, por defecto "auto" [GS-241].
- Añadir la opción LANGCHAIN_AGENT_TYPE=lcel en la documentación de GenericSuite AI.
- Añadir variables de depuración (DEBUG) a todos los módulos de IA para habilitar el registro de depuración, por defecto "0" (deben estar configuradas en el archivo .env) [GS-230].

##### Cambiado
- Actualizar .gitignore para incluir configuraciones de IDE y eliminar archivos utilitarios no utilizados.
- Eliminar archivos utilitarios no usados de todas las backends de ExampleApp.
- El archivo "GEMINI.md" se renombró y movió a "specs/productContext.md".
- Actualizar el archivo "productContext.md" para reflejar el nuevo ExampleApp y el servidor MCP.
- Añadir documentos de memoria en el directorio "specs".
- Actualizar el formato del CHANGELOG para ser más semántico.
- Mejorar la documentación de la configuración de ExampleApp, incluyendo: estructura detallada de directorios y diferencias entre backend/frontend.
- Servidor MCP de ExampleApp: usar los cambios de la biblioteca GS BE MCP, mejorar la gestión de variables de entorno en el script de ejecución y actualizar requirements.txt para compatibilidad con las nuevas versiones de la biblioteca.
- Reemplazar la variable de entorno HUGGINGFACE_ENDPOINT_URL por HUGGINGFACE_DEFAULT_CHAT_MODEL y HUGGINGFACE_DEFAULT_IMG_GEN_MODEL en las plantillas de .env.example de ExampleApp.
- Actualizar la versión predeterminada de Python a 3.12 en la documentación y en los archivos .python-version de ExampleApp [GS-230].
- Actualizar la versión mínima de Python a 3.10 en la documentación [GS-230].
- Actualizar todas las dependencias de GenericSuite a las últimas versiones (npm, uv, pipenv) en ExampleApp [GS-230].

##### Corregido
- Arreglar "mkdocs_install.sh" para actualizar las dependencias de mkdocs a la última versión y reconstruir el archivo requirements.txt de forma adecuada.

##### Seguridad
- Actualizar dependencias de paquetes en package.json y pnpm-lock.yaml para actualizar turbo y dotenv [GS-219].
- Interfaz de ExampleApp: Deshabilitar el encabezado X-Powered-By para evitar exponer información del marco en server.js [GS-219].
- Actualizar GS BE Core y las bibliotecas IA en ExampleApp para corregir alertas de dependabot [GS-219].
- Añadir la variable de entorno USER_PARAMS_FILE_ENABLED para habilitar/deshabilitar el archivo de parámetros del usuario "/tmp/params_[user_id].json", por defecto "0" para evitar riesgos de seguridad cuando se ejecuta en un entorno de producción [GS-240].

...

## GenericSuite Gitops

### Pull Request y Etiqueta

* Pull Request: https://github.com/tomkat-cr/genericsuite-gitops/pull/4
* Etiqueta: https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.4.0

### Resumen de Pull Request # 2

Resumen de cambios

Este pull request expande significativamente el kit de herramientas GenericSuite GitOps al introducir un nuevo módulo Nginx Router para una gestión robusta del tráfico web y generación automática de certificados SSL. Estandariza prácticas operativas entre varios servicios como Ollama, N8n, Kubernetes, Docker, GitLab Runner y despliegues en VPS mediante la adición de Makefiles y READMEs completos. Los cambios también se centran en mejorar la robustez de scripts, mejorar la gestión del ciclo de vida de contenedores Docker y proporcionar documentación interna detallada para optimizar los flujos de desarrollo y despliegue.

Destacados

- Módulo Nginx Router: Se introdujo un nuevo módulo de enrutador Nginx, completo con configuraciones de ejemplo, configuración de Docker Compose y objetivos de Makefile para gestionar su ciclo de vida (ejecución, detención, reinicio, registros, generación de certificados SSL).

- Generación automática de certificados SSL: Se añadieron scripts para generar certificados SSL usando Let’s Encrypt (para Debian/Ubuntu y macOS) y certificados autofirmados mediante Mkcert, mejorando la seguridad y la facilidad de configuración para servicios web.

- Documentación y automatización estandarizadas: Se añadieron README.md y archivos Makefile a los directorios ollama, n8n, k8, docker, gitlab_runner, vps y scripts, proporcionando documentación consistente y ejecución automatizada de comandos para cada módulo.

- Mejora de la gestión de Ollama: Se integró la funcionalidad ollama_update en el gestor de Ollama, permitiendo actualizaciones más fáciles del servicio local de LLM.

- Mejora de la configuración de N8n y la integración con Docker: Se añadió un comando init a N8n para la configuración inicial y se incluyeron archivos de configuración de Docker (docker-compose.yml, .env) en .gitignore para prevenir control de versiones accidental.

- Robustez y mejores prácticas para scripts de shell: Se implementó set -euo pipefail en numerosos scripts de shell para un manejo de errores más robusto, junto con la modernización de asignaciones de variables y comprobaciones de comandos.

- Política de reinicio de Docker: Se actualizó la política de reinicio de Docker a unless-stopped para los servicios n8n, postgres y pgadmin, asegurando que los contenedores se reinicien automáticamente después de reinicios del sistema a menos que se detengan explícitamente.

- Documentación interna integral: Se añadieron varios documentos de memoria (activeContext.md, productContext.md, projectBrief.md, systemPatterns.md, techContext.md) al directorio specs, detallando el contexto, la arquitectura y las decisiones técnicas del proyecto.

### CHANGELOG.md

#### [0.4.0] - 2025-11-17

##### Añadido
- Añadir módulo Nginx Router [GS-180] [GS-234].
- Añadir generación de certificados SSL con Let's Encrypt y Mkcert [GS-180].
- Añadir "README.md" y "Makefile" a los directorios "ollama", "n8n", "k8", "docker", "gitlab_runner", "vps" y "scripts" [GS-231].
- Añadir "ollama_update" al gestor de Ollama [GS-229].
- Añadir documentos de memoria en el directorio "specs" [GS-208].
- Mejorar la experiencia del usuario con scripts de ayuda adicionales y comandos, p. ej., Tmux cheatsheet [GS-231].

##### Cambiado
- Actualizar formato de CHANGELOG para ser más semántico [GS-222].
- Scripts en VPS mejorados para implementar mejores prácticas de servidor en Linux [GS-231].
- N8n - añadir comando init y archivos de configuración de Docker en gitignore [GS-141].
- Cambiar la política de reinicio a 'unless-stopped' para n8n, postgres y pgadmin [GS-141].

##### Corregido
- Arreglar comprobaciones de conectividad entre servicios [GS-231]
- Arreglar error en vps/create_server_users_and_groups.sh al añadir un usuario al grupo sudoers [GS-230].

...