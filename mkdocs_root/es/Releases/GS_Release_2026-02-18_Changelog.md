# 20260218 - La 2ª Edición de Aniversario

![GS_Release_2026-02-18_Image_1A.png](./images/GS_Release_2026-02-18_Image_1A.png)

Fecha: 2026-02-18

## Resumen

Celebrando 2 años de innovación: GenericSuite Release 2026-02-18 ya está disponible! 🚀

Al alcanzar nuestro segundo aniversario, nos complace anunciar una actualización transformadora del ecosistema GenericSuite. Esta versión se centra en tres pilares: flexibilidad, rendimiento y seguridad.

Beneficios profesionales clave:

* Base de datos y nube agnósticas: Hemos roto los límites. El soporte ahora se extiende a PostgreSQL, MySQL y Supabase, junto con MongoDB y DynamoDB ya existentes.

* Experiencia mejorada para desarrolladores: Con la nueva Plantilla FastAPI, sincronización automática de dependencias para Dockerfiles, el motor de contenedores Podman y el script estándar de inicio del servidor MCP, creación automática de la estructura de tablas de la base de datos local, creación de superusuario y establecimiento de servicios backend robustos es más rápido que nunca.

* Optimización del frontend: Una refactorización completa de nuestro Generic CRUD Editor (GCE_RFC) usando hooks de rendimiento de React reduce significativamente las recargas de componentes, junto con una interfaz moderna "rounded-xl".

* IA y Seguridad: Enmascaramiento de URL de adjuntos de conversación IA y URLs pre-firmadas evitan ataques de sobrefacturación durante interacciones con LLM.

* Capa de abstracción de almacenamiento en la nube: abre la puerta para cambiar entre AWS S3, Azure Blob y Google Cloud Storage (AWS está 100% implementado hasta ahora).

* Validación de datos moderna: La migración a Pydantic garantiza serialización de datos más rápida, más fiable y esquemas estrictamente tipados, reduciendo errores en tiempo de ejecución.

Esta Edición de 2º Aniversario está diseñada para escalar con las necesidades de su negocio, proporcionando la base para aplicaciones de alto rendimiento impulsadas por IA. Consulta el changelog completo para detalles sobre nuestra nueva integración de Cloudflare Tunnel y soporte de Python 3.12.

## Núcleo del Frontend de GenericSuite

### Paquete, Pull Request y Etiqueta

* Paquete: [https://www.npmjs.com/package/genericsuite/v/1.2.0](https://www.npmjs.com/package/genericsuite/v/1.2.0)
* Pull Request: [https://github.com/tomkat-cr/genericsuite-fe/pull/9](https://github.com/tomkat-cr/genericsuite-fe/pull/9)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.2.0](https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.2.0)

### Descripción de la Pull Request

Páginas de formulario de editor genérico con listados de hijos externos, versionado de API y una mejor compatibilidad con monorepos

Esta solicitud de extracción introduce un conjunto completo de mejoras y optimizaciones en la aplicación, centradas principalmente en las capacidades del Editor Genérico CRUD, la gestión de estado y la experiencia del usuario. Refactoriza componentes centrales para aprovechar los hooks de rendimiento de React, estandariza configuraciones de entorno y agiliza los procesos de construcción. Estos cambios buscan proporcionar una base más robusta, con mejor rendimiento y más amigable para los desarrolladores para futuros desarrollos.

Destacados

- Editor genérico CRUD mejorado (GCE_RFC): El Editor genérico CRUD ahora admite tablas externas con subTipo: "table" para listados de hijos, lo que permite relaciones de datos más flexibles. Se han añadido tipos de campo h1 a h6 para una mejor estructura de las páginas de formulario, y el componente SuggestionDropdown se ha mejorado con debounce y el hook useCombobox para un mejor rendimiento y experiencia de usuario. Las llamadas API dentro de GCE_RFC se han optimizado para evitar repeticiones.
- Gestión de claves API y caché de datos de usuario: Las claves API ahora se gestionan en una tabla separada users_api_keys, y la página de perfil de usuario incluye una sección dedicada para claves API. Se ha implementado caché de datos de usuario (getUserDataCache, setUserDataCache) para optimizar la obtención de datos del usuario.
- Mejora de la gestión de estado y rendimiento: Contextos clave (MainSectionContext, UsersContext, AppContext) se han refactorizado para utilizar useCallback, useMemo, useRef y useReducer, reduciendo significativamente las recargas innecesarias de componentes y mejorando el rendimiento general de la aplicación. Se ha introducido un mecanismo de caché (fetchOrCache) en MainSectionProvider para optimizar la obtención de datos.
- Manejo flexible de variables de entorno: Las variables de entorno del frontend se han estandarizado para evitar conflictos en configuraciones de monorepos, permitiendo que las variables con prefijo REACT_APP_ sean reemplazadas por prefijos APP_. Se han añadido nuevas variables como API_VERSION, API_KEYS_PREFIX, USE_CONTAINERS_ENGINE_APP y RUN_PROTOCOL_AND_PORT_REPLACEMENT para mayor flexibilidad de configuración.
- Refinamientos UI/UX: Los botones y campos de entrada en toda la aplicación se han actualizado con un estilo más redondeado rounded-xl. Los mensajes de error en la página de inicio de sesión se han mejorado, y se ha añadido un botón de cierre a los mensajes de índice de GCE_RFC. Las clases de animación se han renombrado para mayor claridad, y se ha añadido un nuevo icono de error a GsIconLib.
- Actualizaciones de Build y herramientas: Las dependencias del proyecto, incluyendo babel-jest, jest y postcss-loader, se han actualizado. Nuevos objetivos de Makefile (tailwind-build) y un nuevo script (link_external_configs.sh) se han agregado para agilizar la reconstrucción de Tailwind CSS y el enlace de configuraciones JSON externas para el desarrollo y pruebas locales.

### CHANGELOG.md

#### [1.2.0] - 2026-02-18

##### Agregado
- Variable de entorno API_VERSION para establecer la versión de la API, por defecto "v1" [GS-245].
- Listados de la página de formulario del editor genérico ahora aceptan tablas externas con el subTipo "table" [GS-159].
- Separador de regla horizontal antes de los elementos secundarios en páginas de formulario genéricas [GS-250].
- Variable de entorno API_KEYS_PREFIX para establecer el prefijo de claves API, por defecto "sk-gsu-" [GS-159].
- Constante WAIT_ANIMATION_MARGIN_TOP_CLASS para añadir margen superior a <WaitAnimation /> en el componente <App /> [GS-246].
- Documentación de UPDATE_SNAPSHOTS=0/1 para ejecutar "make publish" y correr "npm test -- -u" en lugar de "npm run test" [GS-246].
- "UPDATE_SNAPSHOTS=1 make publish" documentación en Makefile [GS-63].
- Tipos de campo h1 a h6 para archivos JSON [GS-250].
- "make tailwind-build" para reconstruir los archivos Tailwind CSS (sin vigilancia de cambios) [GS-63].
- "make tailwind-build" añadido al script de publicación (publish) [GS-63].
- getUserDataCache y setUserDataCache para almacenar en caché los datos del usuario actual, implementado en las funciones específicas de Users.jsx [GS-251].
- Botón de cierre para mensajes emergentes de la página índice de GCE_RFC (p. ej., "X items deleted...") mostrados al regresar desde la página de Datos del Formulario [GS-251].
- Componente de claves API añadido al Perfil de Usuario [GS-159].
- Función "customOnChange()" añadida a <PutOneFormfield /> como parámetro "onChange", también Formik setFieldValue() añadido como parámetro "setValue", para que campos tipo "component" actualicen valores internos de Formik y se almacenen en la base de datos [GS-252].
- Componente ShowAsDisabledField puede renderizar el componente personalizado como un campo deshabilitado simulado (comportamiento actual) o como un Formik Field, personalizable con los nuevos parámetros "showAsField", "isReadOnly", "type", "onChange", "onBlur". OnChange permite almacenar el valor calculado en los valores internos de Formik y por lo tanto guardarlo en la base de datos [GS-252].
- Variable USE_CONTAINERS_ENGINE_APP para controlar si usar la app del motor de contenedores para el entorno de desarrollo local cuando RUN_PROTOCOL="https" [GS-257].
- Variable RUN_PROTOCOL_AND_PORT_REPLACEMENT para controlar la sustitución automática de protocolo y puerto para variables de entorno de desarrollo local APP_FE_URL_DEV y APP_API_URL_DEV [GS-257].
- Script "link_external_configs.sh" para enlazar el directorio de configuraciones JSON externas para que pueda probarse en GenericSuite FE Core [GS-258].
- Cambio de tipo de campo "config_name" a "suggestion_dropdown" en "Admin > Users > User Configurations", para que Suggestion Dropdown pueda probarse en GenericSuite FE Core [GS-258].
- Icono de error añadido a GsIconLib [GS-258].
- Componente <ChatBotButtonGeneric /> para añadir una capa de try-catch a definiciones de campos con "chatbot_popup" establecido en true [GS-258].
- Documentación completa de parámetros para `GenericSelectDataPopulator`.
- Documentación completa para `getUrlParams`.
- Variable VERBOSE_RUN_CONFIG para habilitar registro detallado en run_config.sh.
- Utilidades MD5 [GS-266].
- Generación de ObjectId() tipo BSON a "id.utilities.jsx" [GS-266].
- "UsersUserHistory.jsx" y "users_user_history.json" para depurar listados de hijos con fechas y generación de ObjectId() BSON de MongoDB [GS-266].
- Implementar navegaciones para pruebas [GS-267].
- "generalUtilities" para detectar diferentes tipos de elementos, incluyendo dict y list [GS-251].

##### Cambiado
- Mejorar el mensaje de error en la página de inicio de sesión [GS-246].
- Actualizar class_name_constants.jsx para hacer los botones más redondeados y eliminar comentarios no usados [GS-246].
- Actualizar getFetch() para verificar si la respuesta es OK usando los códigos de estado [200, 201, 202, 204] [GS-245].
- Renombrar constantes de clase de estilo: PAGE_ANIMATION_CLASS a WAIT_ANIMATION_CLASS, SHOW_HIDE_PAGE_ANIMATION_ENABLED_CLASS a WAIT_ANIMATION_ENABLED_CLASS, SHOW_HIDE_PAGE_ANIMATION_DISABLED_CLASS a WAIT_ANIMATION_DISABLED_CLASS [GS-246].
- Renombrar el componente <ShowHidePageAnimation /> a <ShowHideWaitAnimation /> [GS-246].
- El separador de regla horizontal <hr /> ahora es a guiones [GS-250].
- Las claves API ahora están en una tabla separada "users_api_keys", no en un arreglo de la tabla "users" [GS-159].
- Renombrar "parentKeyNames" a "endpointKeyNames" en archivos de configuración JSON [GS-159].
- Mover el atributo "parentUrl" desde "endpointKeyNames" a la raíz de los archivos de configuración JSON [GS-159].
- MainSectionContext, UsersContext y AppContext implementan useCallback, useMemo, useRef y useReducer en lugar de useState, para evitar recargas innecesarias de componentes [GS-251].
- La referencia del README de Configs a la documentación oficial de GenericSuite en lugar de repetir su contenido [GS-251].
- getFieldElementsYupValidations() habilitado para tener validaciones en la página de Datos de Formulario [GS-251].
- Renombrar estado y setState a errorState, setErrorState en AppContext.jsx, App.jsx, generic.editor.rfc.selector.jsx, generic.menu.service.jsx [GS-251].
- Renombrar status y setStatus a errorStatus, setErrorStatus en generic.editor.rfc.formpage.jsx [GS-251].
- Renombrar los parámetros de <FormPage />: mode_par, id_par, y editor_par a mode, id y editor [GS-251].
- Renombrar las variables de entorno del frontend para evitar conflictos con las mismas variables usadas en el backend y poder fusionar los archivos ".env" en un monorepo: GIT_SUBMODULE_LOCAL_PATH a GIT_SUBMODULE_LOCAL_PATH_FRONTEND, y RUN_METHOD a RUN_BUNDLER [GS-243].
- REACT_APP_APP_NAME puede eliminarse y reemplazarse por APP_NAME en monorepos [GS-243].
- REACT_APP_DEBUG puede eliminarse y reemplazarse por APP_DEBUG en monorepos [GS-243].
- Si REACT_APP_API_URL no está configurado, se puede usar APP_API_URL en su lugar [GS-243].
- Si REACT_APP_URI_PREFIX no está configurado, se puede usar URI_PREFIX en su lugar [GS-243].
- Si REACT_APP_X_TOKEN no está configurado, X_TOKEN puede usarse en su lugar [GS-243].
- Si REACT_APP_USE_AXIOS no está configurado, USE_AXIOS puede usarse en su lugar [GS-243].
- Envío de "currentObj" a los tipos de campo "select_component" y "component" ahora reciben "currentObj" como parámetro en getSelectDescription() [GS-258].
- Pasar `dbRow` a los tipos de campo de formulario "select_component" y "component" para un contexto de datos mejorado [GS-37].
- Exportar la utilidad `buildDescription` en "generic.editor.rfc.selector" y mejorar la documentación de "GenericSelectGenerator" [GS-37].
- Pasar `currentObj` como parámetro a `dataPopulator` en getSelectFieldsOptions() [GS-37].
- Centralizar y mejorar la extracción de mensajes de error de API con un nuevo helper `getErrorMsgFromApi` para evitar mensajes como "[object Object]" cuando se usa axios [GS-262].
- Renombrar "idUtilities.getUuidV4" a "uuidUtilities.getUuidV4" [GS-266].
- El diseño de la página de inicio de sesión se ha mejorado aislando el logotipo de la caja de usuario y contraseña.

##### Fijo
- Mensaje de error al usar axios y la sesión expira o las credenciales son inválidas [GS-246].
- API "errorMsg" como arreglo cuando hay errores en la llamada principal a la API o en las llamadas a funciones específicas de la API [GS-251].
- getFileExtension() para eliminar los parámetros de consulta de la URL [GS-72].
- Optimizar las llamadas API del Generic CRUD Editor (GCE_RFC), evitando llamadas repetidas [GS-251].
- Optimizar las llamadas API del Generador de Menú Genérico (GMG), evitando llamadas repetidas [GS-251].
- Botón de inicio de sesión mostrado en cada recarga de página, mientras se cargan los menús [GS-251].
- GMG muestra el mensaje "URL not found..." durante la carga del menú [GS-251].
- GCE_RFC no muestra el mensaje de error cuando la sesión ha expirado [GS-251].
- Suprimir la advertencia en la página de inicio de sesión sobre los atributos de autocompletado de usuario y contraseña (Más info: https://goo.gl/9p2vKq)
- Arreglar el color del campo de entrada en el componente <SuggestionDropdown /> [GS-252].
- Arreglar la inicialización de la caché en el proveedor del Generic CRUD Editor (MainSectionProvider) [GS-252].
- Arreglar el componente SuggestionDropdown: usar debounce para limitar llamadas a la API y reemplazar el legado Downshift por el hook useCombobox [GS-258].
- Mostrar el mensaje de error en la página de inicio de sesión cuando se usa axios y la sesión expira o las credenciales son inválidas [GS-37] [GS-202].
- Implementar renderizado seguro de Markdown para mensajes [GS-262].
  * La función includesAppValidLinks se usa como heurística de seguridad para determinar si un mensaje de error debe renderizarse como HTML. Esta verificación era insuficiente ya que solo verifica si el mensaje contiene un correo o URL 'válidos' incrustados. Un atacante podría evadir esta verificación incluyendo alguna de estas cadenas (p. ej., 'support@exampleapp.com') en una carga útil maliciosa. Si el mensaje de error contiene datos no confiables, como entradas reflejadas de una respuesta de error de la API, esto podría provocar una vulnerabilidad de Cross-Site Scripting (XSS) al renderizar el mensaje en la interfaz.
- Optimizar la obtención de datos de usuario con caché de solicitudes para evitar condiciones de carrera [GS-262].
- "TypeError: stringDate.indexOf is not a function" en addMissingTz cuando la fecha suministrada es un número [GS-194].
- "\"[object Object] EFFF-020\" cuando la API devuelve un error al eliminar/actualizar el ítem en EditFormFormikFinal() [GS-194].
- La fecha no se muestra en listados secundarios de solo lectura: timestampDbPostRead() usa resultset[0] para llamar a processTimestampToDate() porque los campos "date" y "datetime-local" se muestran como "mm/dd/yyyy, --:-- --" [GS-266].
- Usar utilidades MD5 para hashear rowId en formularios cuando no hay row._id o row[editor.primaryKeyName], evitando la advertencia "Encountered two children with the same key, `<table_name>_row_undefined_tr_enclosure`" [GS-266].
- Los parámetros de consulta no se reconocen en getUrlParams() [GS-266].
- Mostrar solo contenido cuando `menu=0` en la página principal [GS-266].
- Deshabilitar el botón de página siguiente y evitar mostrar el mensaje "Page 1 of 0" cuando la tabla no tenga elementos en GCE_RFC [GS-266].
- Arreglar el cierre de menús desplegables cuando se haga clic en cualquier otro elemento [GS-266].
- Evitar avisos de React manejando valores de campos de formulario nulos/indefinidos en getFieldElementsDbValues() [GS-266] [GS-262].

##### Seguridad
- Actualizar Jest y Babel a las últimas versiones para corregir la advertencia "npm warn deprecated inflight@1.0.6..." [GS-219] [GS-267].
- 37 vulnerabilidades de seguridad (incluyendo altas y críticas) encontradas en las dependencias del proyecto fueron resueltas, añadiendo una sección "overrides" en package.json para forzar versiones seguras de dependencias transitivas (elliptic, json5, minimatch, postcss, loader-utils) sin romper la configuración de alto nivel [GS-219] [GS-267].

##### Eliminado
- Se eliminaron las dependencias "boto3" y "pymongo", para que cada proyecto pueda tener sus propias dependencias dependiendo de la base de datos y del proveedor de almacenamiento en la nube seleccionado [GS-245].
- Se eliminó la función save_all_users_params_files() y el endpoint /users/caujf [GS-240] [GS-245].
- Las dependencias "python-dateutil", "marshmallow", "requests", "dnspython", "wheel" fueron eliminadas, ya que no se usan [GS-248].
- Se eliminaron las dependencias "fastmcp" y "mcp" para que cada proyecto pueda instalarlas si es necesario [GS-248].

## GenericSuite Backend AI

### Paquete, Pull Request y Etiqueta

* Paquete: [https://pypi.org/project/genericsuite-ai/0.3.0/](https://pypi.org/project/genericsuite-ai/0.3.0/)
* Pull Request: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/12](https://github.com/tomkat-cr/genericsuite-be-ai/pull/12)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.3.0](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.3.0)

### Descripción de la Pull Request

Agregar create_app() para Flask, try-except a todas las importaciones opcionales para reportar qué dependencia falta y correcciones de seguridad

Esta PR mejora significativamente la flexibilidad, seguridad y mantenibilidad del proyecto. Introduce un patrón estandarizado de creación de aplicaciones para Flask, amplía las capacidades de bases de datos y almacenamiento en la nube, e integra funciones avanzadas de masking de conversaciones de IA. Un enfoque importante es mejorar la gestión de dependencias haciendo muchas bibliotecas opcionales y proporcionando instrucciones de instalación más claras, junto con actualizaciones críticas de seguridad a bibliotecas centrales. Estos cambios, en conjunto, optimizan el desarrollo, reducen la sobrecarga operativa y fortalecen la resiliencia de la aplicación.

Destacados

- Mayor modularidad y soporte de frameworks: Se introdujo una función estandarizada create_app() para aplicaciones Flask e integrado AI Conversation Masking en FastAPI, Flask y Chalice, mejorando la configuración de la aplicación y la consistencia.
- Mejor gestión de dependencias e informes de errores: Se implementaron bloques try-except para todas las importaciones opcionales, proporcionando mensajes de error más claros a los desarrolladores sobre dependencias ausentes y agilizando la instalación. Muchas dependencias fueron eliminadas o hechas opcionales para reducir el tamaño del proyecto.
- Ampliación de capacidades de bases de datos y almacenamiento en la nube: Se añadió soporte para bases de datos PostgreSQL y MySQL y se desarrolló una capa robusta de abstracción de almacenamiento para AWS S3, Azure y Google Cloud Platform, incluyendo el uso de URLs prefirmadas de AWS para acceso seguro y limitado en el tiempo a cubos de S3.
- Actualizaciones de seguridad críticas: Se abordaron múltiples vulnerabilidades de seguridad actualizando dependencias clave como urllib3, langchain-core y langchain a sus versiones más seguras. 
- Configuración y actualizaciones de modelo: Se actualizó el modelo predeterminado de HuggingFace, se ajustaron las URLs base de API para AIMLAPI y Groq, y se corrigió la compatibilidad de la versión de faiss-cpu para implementaciones de AWS Lambda.

### CHANGELOG.md

#### [0.3.0] - 2026-02-18

##### Agregado
- Variable API_VERSION para establecer la versión de la API, por defecto "v1" [GS-245].
- Soporte para Postgres [GS-194].
- Soporte para Supabase [GS-161].
- Soporte para MySQL [GS-249].
- Implementación de la capa de abstracción de almacenamiento para AWS S3, Azure y GCP [GS-72].
- Implementación de AWS generate_presigned_url() para proteger el acceso a buckets S3, configurables para expirar en corto tiempo. Configuración disponible con STORAGE_PRESIGNED_EXPIRATION_SECONDS (predeterminado 5 minutos o 300 segundos) [GS-72].
- Soportes para guardar archivos de OpenAPI (JSON y YAML) en un directorio definido por PATH_TO_SAVE_OPENAPI [GS-245].
- Dependencia "requests-toolbelt" requerida para parse_multipart.py [GS-248].
- Comando "make test" para correr tests [GS-248].
- "pymongo" y "boto3" en dependencias de desarrollo para correr tests [GS-248].
- Variable APP_LOGGER_OPTIONS para configurar opciones de registro, inicialmente para deshabilitar mensaje de inicio cuando "silent" está activo [GS-245].
- Recobro de tokens MCP desde encabezados (Authorization: Bearer <token>) con la función get_access_token() en utilidades mcplib [GS-159].
- Variable MCP_MANDATORY_USER_ID para forzar autenticación MCP con user_id y api_key. Por defecto "0" para permitir autenticación con clave API solamente [GS-159].
- Implementación del endpoint de logs [GS-250].
- Añadir encabezado Message-ID a correos salientes [GS-37].
- Permitir configurar modo de depuración de correo mediante la variable de entorno SEND_EMAIL_DEBUG [GS-37].
- Configuración de db_engine a SqlTable para que métodos como array_fields_management() y array_fields_value() usen las funciones correspondientes [GS-194].
- Implementar operaciones $inc, $push, $addToSet y $pull en la abstracción SQL [GS-194].
- Añadir get_table_structure() y quote_value() en helpers DB genéricos para corregir la ejecución de super_admin_create() ("supad-create" endpoint) en apps con atributos obligatorios de usuario que requieren valores por defecto [GS-125].
- Introducir soporte para $elemMatch en todas las abstracciones de bases de datos. Mejorar el manejo de consultas extrayendo y filtrando condiciones $elemMatch, aumentando la precisión de recuperación de datos [GS-161] [GS-194] [GS-249] [GS-102].

##### Cambiado
- Estandarizar el prefijo de la URL de recuperación de almacenamiento de /asset a /assets en todos los frameworks [GS-245].
- Estandarizar el parámetro de estado status con "http_error" a "status_code" en "utilities.py" y "users.py" [GS-245].
- Mejorar el registro en aws.py para una mejor depuración, incluyendo un mensaje inicial al inicio de la aplicación para mostrar el nivel de registro.
- Ahora STORAGE_URL_SEED es necesario solo si STORAGE_URL_ENCRYPTION está habilitado [GS-72].
- STORAGE_ENCRYPTION renombrado a STORAGE_URL_ENCRYPTION [GS-72].
- Mejorar la máscara de URL de AWS S3 para evitar exponer el nombre del bucket, configurables con STORAGE_URL_ENCRYPTION, STORAGE_URL_SEED, RUN_PROTOCOL, URL_MASK_EXTERNAL_HOSTNAME, URL_MASK_EXTERNAL_PROTOCOL. No compatible con API Gateway; solo en instancias EC2 o VPS [GS-72].
- La variable URL_MASK_EXTERNAL_HOSTNAME reemplaza DEV_MASK_EXT_HOSTNAME, y DEV_MASK_EXT_HOSTNAME aún se usa, pero se da prioridad a URL_MASK_EXTERNAL_HOSTNAME [GS-72].
- Migración de Marshmallow a Pydantic: actualizar schema_verification() para usar Pydantic en lugar de Marshmallow [GS-248].
- Renombrar "parentKeyNames" a "endpointKeyNames" en archivos JSON [GS-159].
- Reimplementar la autenticación por clave API usando la tabla dedicada "users_api_keys" [GS-159].
- Eliminar usuarios_api_keys de ejemplo del contexto de la app.
- Mejorar `send_email.py` para devolver un conjunto de resultados con información de errores cuando ocurra un fallo, validación de parámetros, eliminación de HTML, y hints de tipo [GS-37].

##### Fijo
- Eliminar "/" en el prefijo de la clave para evitar doble "/" en get_bucket_key_from_url() y corregir caracteres codificados en get_s3_presigned_url() [GS-245].
- Limpiar imports y comentarios no usados en create_app.py.
- Actualizar el tipo de retorno de delete_params_file en app_context.py.
- Error de escaneo de objeto de tabla en DyanmoDB abstractor "AttributeError: 'tuple' object has no attribute 'update'" [GS-102].
- Robustecer la conversión ObjectId cuando "_id_" está en like_query_params.
- Permitir objetos Request como entrada para funciones de datos del usuario para hacer que el flujo de onboarding funcione [GS-37].
- Evitar "AssertionError: AuthenticationMiddleware must be installed to access request.user" en get_curr_user_id cuando es una Request normal sin autenticación JWT [GS-37].
- send_email incluye el encabezado "Message-ID" para evitar que Google (y otros) rechacen correos [GS-37].
- Actualizar la abstracción SQL para manejar comparaciones NULL dinámicamente [GS-262].
- "bson.errors.InvalidId" al crear un nuevo usuario con Supabase, asignando `parent_keys["_id"] = ObjectId(parent_keys["id"])` [GS-251].

##### Seguridad
- Actualizar urllib3 a "^2.6.3" para corregir vulnerabilidades de seguridad [GS-219]:
    * "Asignación de recursos sin límites ni throttling": "CWE-770", "CVE-2025-66418", "CVSS 8.9", "SNYK-PYTHON-URLLIB3-14192443"
    * "Manejo inapropiado de datos altamente comprimidos (Data Amplification)": "CWE-409", "CVSS 8.9", "CVE-2025-66471", "CVE-2026-21441", "CWE-409".
- Actualizar werkzeug a "^3.1.6" para corregir vulnerabilidades de seguridad [GS-219]:
    * "Manejo inapropiado de nombres de dispositivos Windows": "CWE-67", "CVSS 6.3", "CVE-2025-66221", "CVE-2026-27199", "CWE-67".
- Actualizar criptografía a "^46.0.5" para corregir vulnerabilidades de seguridad [GS-219]:
    * "Verificación insuficiente de autenticidad de datos": "CVE-2026-26007", "CWE-345".
- Añadir filtros obligatorios a get_item_from_db() y GenericEndpointHelper.generic_crud_main() [GS-262].
- Añadir sanitización al parámetro "message" en el endpoint POST /log [GS-262].

##### Eliminado
- Dependencias "boto3" y "pymongo", para que cada proyecto pueda tener sus propias dependencias según la base de datos y proveedor de almacenamiento en la nube [GS-245].
- Eliminación de endpoints de ejemplo de usuario desde OpenAPI.
- Otros cambios de eliminación de dependencias no utilizados en varias partes del proyecto.

## GenericSuite Backend Scripts

### Paquete, Pull Request y Etiqueta

* Paquete: [https://www.npmjs.com/package/genericsuite-be-scripts/v/1.3.0](https://www.npmjs.com/package/genericsuite-be-scripts/v/1.3.0)
* Pull Request:
    - [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/13](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/13)
    - [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/14](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/14)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.3.0](https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.3.0)

### Descripción de la Pull Request

Sincronización de dependencias, creación de superadmin, soporte Postgres, Supabase, MySQL y Cloudflare Tunnel

Esta Pull Request mejora significativamente el flujo de desarrollo y despliegue mediante la introducción de sincronización automática de dependencias, expansión del soporte de bases de datos para incluir Postgres y MySQL, e integración de Cloudflare Tunnel para acceso seguro al desarrollo local. También trae mejoras importantes para despliegues de AWS Lambda, incluyendo runtime de Python 3.12 y OpenAPI 3.0.1, junto con varias correcciones y optimizaciones para la configuración local y prácticas de seguridad.

Destacados

- Módulo de Sincronización de Dependencias: Se añadió un nuevo módulo scripts/dependency-sync para sincronizar automáticamente dependencias de Python desde archivos pyproject.toml en directorios backend (./server y ./mcp-server) a Dockerfiles, asegurando dependencias actualizadas y consistentes.
- Soporte mejorado de bases de datos: Soporte para Postgres y MySQL; nuevos objetivos de Makefile para generar SQL, crear tablas de desarrollo y desplegar recursos de CloudFormation. La gestión de bases de datos locales ahora usa un directorio unificado local_db.
- Integración de Cloudflare Tunnel: Soporte para Cloudflare Tunnel para permitir acceso HTTPS seguro a entornos de desarrollo locales sin necesidad de Docker o DNS local, haciendo localhost accesible públicamente para pruebas.
- Mejoras de AWS Lambda: Runtime de Lambda actualizado a Python 3.12, API Gateway actualizado a OpenAPI 3.0.1 con CORS, y definiciones de endpoints refactorizadas. Se añadió una opción de despliegue 'zip' para funciones Lambda y nuevas variables de entorno (CICD, USE_EXISTING_ZIP, PATH_TO_SAVE_OPENAPI) para despliegues más flexibles y automatizados.
- Mejoras de entorno de desarrollo local: Estandarización del script del servidor MCP, nuevo objetivo make create-supad para la creación inicial de un super admin, y validación de puertos de backend locales. Mayor compatibilidad con Podman gracias a la refactorización de configuraciones de Docker Compose y del DNS local.
- Seguridad y Mantenimiento: Todos los archivos requirements.txt ahora se ignoran y se recrean cuando se necesitan para asegurar las dependencias más recientes y mitigar vulnerabilidades. Comandos de limpieza en run_aws.sh se comentaron para evitar eliminación accidental de archivos durante la limpieza.

### CHANGELOG.md

#### [1.3.0] - 2026-02-18

##### Agregado
- Módulo de Sincronización de Dependencias ("scripts/dependency-sync") para sincronizar dependencias de Python en Dockerfile desde directorios monorepo de GenericSuite Backend ("./server" y "./mcp-server" con un archivo "pyproject.toml") [GS-243].
- "scripts/run_mcp_server.sh" para estandarizar el script de servidor MCP [GS-243].
- Soporte para Postgres [GS-194].
- Reglas de Make para Postgres:
```
make generate_postgres_dev_sql
make create_postgres_dev_tables
make generate_cf_postgres
make deploy_postgres
```
- Soporte para MySQL [GS-249].
- Reglas de Make para MySQL:
```
make generate_mysql_dev_sql
make create_mysql_dev_tables
make generate_cf_mysql
make deploy_mysql
```
- "make create-supad" para crear el usuario administrador inicial (supad) para el entorno de desarrollo local [GS-125].
- Tipos de campo h1 a h6 a archivos JSON [GS-250].
- Validación de BACKEND_LOCAL_PORT y BACKEND_DEBUG_LOCAL_PORT para ser diferentes en el script "secure_local_server/run.sh".
- Puertos y documentación de UI de bases de datos locales en "scripts/local_db/local_db_stack.yml" [GS-249] [GS-194].
- Opción de zip para despliegue de AWS Lambda [GS-248].
- Variable de entorno AWS_LAMBDA_DEPLOYMENT_TYPE para seleccionar el tipo de despliegue para funciones de AWS Lambda ("zip" o "container", predeterminado "container"). Si el proyecto incluye GS BE AI, no puede ser "zip" debido al límite de tamaño de archivo zip de AWS Lambda de 250 MB [GS-248].
- Variable CICD para "big_lambdas_manager.sh" para evitar confirmaciones en varios pasos y ejecutarlo de forma no interactiva [GS-248].
- Variable USE_EXISTING_ZIP para "big_lambdas_manager.sh" para usar un archivo zip existente en lugar de compilar uno nuevo [GS-248].
- PATH_TO_SAVE_OPENAPI para "run_aws.sh" para guardar los archivos de OpenAPI [GS-245].
- Implementación de Cloudflare Tunnel para acceso https al entorno de desarrollo local sin Docker o DNS local y hacer localhost público para pruebas, p. ej. para acceder a la cámara del PC (sin port forwarding) [GS-257].
- Añadir USE_CONTAINERS_ENGINE_APP para activar/desactivar el uso de la app del motor de contenedores para desarrollo local cuando RUN_PROTOCOL="https" [GS-257].
- Añadir RUN_PROTOCOL_AND_PORT_REPLACEMENT para activar/desactivar la sustitución automática de protocolo y puerto para variables de entorno de desarrollo local APP_CORS_ORIGIN (asignado desde APP_CORS_ORIGIN_{STAGE}), APP_FE_URL (asignado desde APP_FE_URL_{STAGE}) y REACT_APP_API_URL (asignado desde APP_API_URL_{STAGE}), según el valor de RUN_PROTOCOL [GS-257].
- Configurar uvicorn para procesar encabezados de proxy y IPs reenviadas en el script `run_aws.sh` [GS-37].

##### Cambiado
- Permitir fusionar archivos ".env" entre los backends de GenericSuite monorepo ("./server" y "./mcp-server"), renombrar APP_MAIN_FILE y APP_DIR envvars a MCP_APP_MAIN_FILE_DEV y MCP_APP_DIR_DEV en run_mcp_server.sh [GS-243].
- Renombrar valores de APP_DB_ENGINE "MONGO_DB" y "DYNAMO_DB" a "MONGODB" y "DYNAMODB" [GS-194].
- Se añadieron perfiles a "local_db_stack.yml" para que solo el APP_DB_ENGINE seleccionado esté habilitado [GS-194].
- Eliminar secciones "link", "depends_on" y "healthcheck" de "local_db_stack.yml" para compatibilidad con Podman [GS-215] [GS-194].
- STORAGE_URL_SEED envvar requerido solo si STORAGE_URL_ENCRYPTION está activado [GS-72].
- Renombrar carpetas "mongo" y "postgres" a nombres más apropiados: "mongo" ahora es "local_db" e incluye containers locales para MongoDB, DynamoDB, Postgres y MySQL. "postgres" ahora es "sql_db" porque funciona para Postgres y MySQL [GS-249].
```
/postgres -> /sql_db
/postgres/generate_postgres_cf -> /sql_db/generate_sql_db_cf
/postgres/generate_postgres_cf/run-postgres-deploy.sh -> /sql_db/generate_sql_db_cf/run_sql_db_deploy.sh

/mongo/run_mongo_docker.sh -> /local_db/run_local_db_docker.sh
/mongo/mongodb_stack_for_test.yml -> /local_db/local_db_stack.yml

make mongo_docker -> make local-db-up
make mongo_docker_down -> make local-db-down
make mongo_logs -> make local-db-logs
set_chalice_cnf.sh mongo_docker -> set_chalice_cnf.sh local_db_docker
```
- Renombrar HUGGINGFACE_TEXT_TO_IMAGE_ENDPOINT a HUGGINGFACE_DEFAULT_CHAT_MODEL [GS-59].
- Subir la versión de Python a 3.12 en despliegues de Lambda de AWS, EC2 ELB y Dockerfiles del servidor local [GS-248].
- El Dockerfile de Lambda grande de Python 3.11 está en el archivo "Dockerfile-big-lambda-AL2-python3.11" [GS-248].
- Añadir "v1" a los endpoints definidos en "aws_big_lambda/template-sam-endpoint-entry.yml" [GS-245].
- Añadir depuración adicional en "run-cf-deployment.sh" y "aws_secrets_manager.sh" [GS-248].
- Renombrar "dns/docker-compose.yml" a "dns/docker-compose-template.yml" [GS-215].
- Debido a la eliminación de dependencias "fastmcp" y "mcp", run_mcp_server.sh ahora verifica si ambos están instalados [GS-248].
- Actualizar a Lambda runtime a Python 3.12, actualizar API Gateway a OpenAPI 3.0.1 con CORS y refactor de definiciones de endpoints en "aws_big_lambda/template-sam.yml" [GS-245].

##### Fijo
- Comentar comandos de limpieza en "run_aws.sh" para evitar eliminación accidental de archivos importantes durante la operación de limpieza.
- Renombrar CONTAINER_ENGINE a CONTAINERS_ENGINE [GS-215].
- Arreglar "secure_local_server/run.sh" para que funcione con Podman creando un volumen nombrado para montar archivos de configuración en el directorio de nginx "/etc/nginx/conf.d" (lectura sola) que Podman no permite montar directorios de solo lectura de la misma forma que Docker. Ahora GS es compatible con Podman [GS-215].
- Local_dns funciona con Podman [GS-215].
- APP_VERSION eliminado de CORE_ENVS en "aws_secrets/aws_secrets_manager.sh", separado del resto de variables de entorno que se envían a AWS Secrets Manager y se incluyen en la plantilla CloudFormation de AWS Lambda "aws_big_lambda/template-sam.yml".

##### Seguridad
- Todos los archivos "requirements.txt" son ahora ignorados y recreados a demanda para evitar reposts de vulnerabilidades y contar con las últimas dependencias [GS-219].

## GenericSuite BaseCamp

### Pull Request y Etiqueta

* Pull Request:
    - [https://github.com/tomkat-cr/genericsuite-basecamp/pull/15](https://github.com/tomkat-cr/genericsuite-basecamp/pull/15)
    - [https://github.com/tomkat-cr/genericsuite-basecamp/pull/17](https://github.com/tomkat-cr/genericsuite-basecamp/pull/17)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.5.0](https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.5.0)

### Descripción de la Pull Request

Aplicación Plantilla FastAPI, soporte multilingüe, creación avanzada de Apps, archivos de configuración JSON, editor CRUD y documentación de variables de entorno

Esta Pull Request introduce la Plantilla FastAPI, mejorando la experiencia de desarrollo para aplicaciones de plantilla, y, de forma significativa, mejora la infraestructura de documentación del proyecto al introducir soporte multilingüe, reestructurar contenido para una mejor organización y actualizar enlaces externos para mayor fiabilidad. También simplifica el flujo de desarrollo añadiendo nuevas herramientas para la gestión de Cloudflare Tunnel y refinando la configuración de variables de entorno, haciendo el proyecto más accesible y fácil de desarrollar. Las actualizaciones se centran en mejorar la exactitud de la documentación, estandarizar convenciones de nombres de variables de entorno para evitar conflictos y fortalecer diversas herramientas de construcción y scripts de limpieza.

Destacados

- Aplicación plantilla FastAPI.
- Documentación multilingüe: Soporte multilingüe para la documentación, comenzando con español e inglés, y añadida la capacidad de traducción automática futura usando OpenAI.
- Reestructuración de la documentación: Renombramiento de múltiples archivos y directorios, consolidación de código de ejemplo bajo una nueva ruta 'docs/code' y eliminación de archivos de índice antiguos.
- Soporte para Postgres, MySQL y Supabase.
- Documentación extensa para configuraciones de CRUD Editor, Modelos de preámbulo IA, y nuevos tipos de campo.
- Variable de entorno API_VERSION
- Refinamientos de documentación: Varias secciones de documentación han sido actualizadas y corregidas para mayor claridad.
- Estandarización de variables de entorno: Renombrar RUN_METHOD a RUN_BUNDLER y GIT_SUBMODULE_LOCAL_PATH a GIT_SUBMODULE_LOCAL_PATH_FRONTEND para evitar conflictos en monorepos.
- Mejoras de variables de entorno: Nuevas variables para guardar archivos de OpenAPI, controlar el uso del motor de contenedores para desarrollo local y gestionar sustitución automática de protocolo/puerto para URLs frontend.
- Actualización de changelog y notas de versión para versiones recientes (1.3.1 y 1.3.2) aplicables a todo el proyecto, incluidas plantillas de aplicaciones.
- Mejoras y limpieza de scripts de backend para Chalice, FastAPI, Flask y MCP Server.
- Enlaces de documentación actualizados para ser relativos en lugar de URL absolutas.
- Corregidas instrucciones de instalación para uv y poetry.
- Procesos de construcción mejorados con nuevos objetivos "prepare_docs" y "generate_openapi".
- "make serve" ahora se vincula a localhost:8015.
- Imágenes de documentación convertidas de SVG a PNG.
- Varias instrucciones de instalación y descripciones de variables de entorno aclaradas o ampliadas, incluyendo una nueva sección de modelos de preámbulo para IA.
- Varias correcciones para problemas con Podman, limpieza de npm, enlaces de documentación rotos y error FileNotFoundError para activos UI estáticos.
- Actualizaciones de enlaces: se reemplazaron enlaces relativos a archivos .pdf y código de ejemplo por URL directas de GS Basecamp en GitHub.
- Lógica común de Chatbot y otras lógicas comunes movidas de api-chalice a api-fastapi en ExampleApp.
- Cloudflare Tunnel: Añadidos objetivos de Makefile para administrar túneles de Cloudflare en tanto el proyecto de ExampleApp como fastapitemplate, junto con documentación relacionada.
- También se incluye una actualización de seguridad para urllib3.

### CHANGELOG.md

#### [1.5.0] - 2026-02-18

##### Agregado
- Documentación multilingüe, empezando por español e inglés (gracias a @otobonh por la idea) [GS-252].
- Documentación en español, usando Google Translate y OpenAI gpt-5-nano [GS-252].
- Objetivos de Makefile para túnel Cloudflare en exampleapp y fastapitemplate [GS-257].
- Variable PATH_TO_SAVE_OPENAPI al Makefile principal para guardar los archivos de OpenAPI [GS-245].
- Variable USE_CONTAINERS_ENGINE_APP para encender/apagar el motor de contenedores para desarrollo local cuando RUN_PROTOCOL="https" [GS-257].
- Documentación de RUN_PROTOCOL_AND_PORT_REPLACEMENT para activar/desactivar la sustitución automática de protocolo y puerto para variables APP_CORS_ORIGIN (asignadas desde APP_CORS_ORIGIN_{STAGE}), APP_FE_URL (asignadas desde APP_FE_URL_{STAGE}) y REACT_APP_API_URL (asignadas desde APP_API_URL_{STAGE}), dependiendo del RUN_PROTOCOL [GS-257].
- OpenAI_API_KEY, OPENAI_MODEL, OPENAI_TEMPERATURE para preparar futura documentación automática [GS-252].
- Añadir el changelog de la 2ª aniversario [GS-262].

##### Cambiado
- Reemplazar enlaces relativos a archivos .pdf con enlaces crudos de GS Basecamp en GitHub [GS-252].
- Reemplazar enlaces de código fuente de exampleapp y fastapitemplate con URLs de GS Basecamp [GS-252].
- "docs_prepare.py" filtra ciertos nombres de archivos no deseados [GS-252].
- Implementar documentación de Cloudflare Tunnel [GS-257].
- Refactorizar archivos .env.example para variables comunes y ampliar documentación sobre fastapitemplate y exampleapp [GS-252].
- Actualizar documentación de configuración [GS-252].
- Renombrar "docs/Sample-Code" a "docs/code" [GS-252].

##### Fijo
- Añadir PyGithub a "mkdocs_install.sh" porque "mkdocs-git-committers-plugin" lo requiere [GS-262].
- Arreglar claves primarias de users_api_keys (_id) [GS-262].

#### [1.4.0] - 2026-01-21

##### Agregado
- Plantilla FastAPI [GS-243].
- Soporte para base de datos Postgres [GS-194].
- Soporte para base de datos MySQL [GS-249].
- Supabase [GS-161].
- API_VERSION envvar para establecer la versión de la API, por defecto "v1" [GS-245].
- Página principal de documentación de código de ejemplo.
- Archivo de historial de cambios de GS Release 20251117: "docs/Releases/GS_Release_2025-11-17_Changelog.md".
- Enlaces a modelos específicos de IA en configuraciones genéricas de "ai_conversation_masking" para ExampleApp y FastAPI Template.
- Documentación de tipos de campo "array" y ejemplos de "specific_function" en la Documentación de Configuración del Editor Genérico CRUD.
- Documentación y ejemplos de Modelos de Preámbulo (usualmente necesarios para configurar LLMs de IA) en la documentación de GenericSuite AI.
- Tipos de campo h1 a h6 a archivos JSON [GS-250].
- API_VERSION envvar para establecer la versión de la API, por defecto "v1" [GS-245].
- Soporte para OpenAPI/Swagger y generación de OpenAPI desde "make generate_openapi" para salvar esquemas (JSON y YAML) y ser incluidos en el proceso de transferencia y construcción (make build, make serve, make transfer_debug, make transfer_cicd) [GS-245].
- Documentación para las nuevas bases de datos soportadas.
- Dependencias opcionales para proyectos de ejemplo (boto3, pymongo).
- Crear documentación de Super Admin.
- Documentación de pila de base de datos local y operaciones.
- Clases Python e interfaces TypeScript para validación de configuraciones JSON de CRUD Editor y guía correspondiente [GS-172].
- Cómo crear tablas y formularios (docs) [GS-172].
- Cómo establecer relaciones 1-a-muchos entre tablas [GS-172].
- Claves API en Perfil de Usuario en exampleapp y fastapitemplate [GS-251].
- Política de privacidad [GS-252].
- Introducción de scripts de preparación de documentación para reducir el tiempo de transferencia FTP [GS-252].
- Comando "make translate_uncommitted" para traducir cambios no publicados en el directorio "docs" antes de publicar [GS-252].
- Comando "make sample_code_prepare" para preparar código de muestra (exampleapp y fastapitemplate) para usar las últimas dependencias antes de publicar [GS-262].

##### Cambiado
- Mejorar "exampleapp/apps/mcp-server/run_mcp_server.sh" separando las variables de entorno SCRIPT_DIR y BASE_DIR.
- Renombrar variables de entorno del frontend para evitar conflictos con las mismas variables usadas en el backend y poder fusionar ".env": GIT_SUBMODULE_LOCAL_PATH a GIT_SUBMODULE_LOCAL_PATH_FRONTEND, RUN_METHOD a RUN_BUNDLER [GS-243].
- Limpiar documentación y código de exampleapp relacionado con la antigua "authenticationService".
- Añadir "-PRESENT" a todos los archivos LICENSE.
- Cambiar el orden de opciones de la barra superior de la documentación.
- Mejorar la documentación de STORAGE_URL_ENCRYPTION y STORAGE_URL_SEED.
- STORAGE_URL_SEED necesario solo si STORAGE_URL_ENCRYPTION está en 1 [GS-72].
- 'Special Installation' y './Other/special-installs.md' renombrados a 'Installation' y './Other/installation.md' respectivamente.
- docs: Mejorar la guía de configuración del backend con estructuras de monorepo, gestión detallada de dependencias y nuevas secciones de instalación para bases de datos y servicios en la nube, añadiendo `psycopg2-binary`.
- Actualizar todos los .env.example con nuevas bases de datos soportadas.
- Reemplazar "/mongo" por "/local_db" y "mongo_docker" por "local_db_docker" en archivos Makefile. 
- Debido a la eliminación de dependencias "fastmcp" y "mcp", run_mcp_server.sh ahora verifica que ambas estén instaladas [GS-248].
- Evitar pedir confirmaciones al limpiar directorios durante el proceso de construcción de "make publish".
- Actualizar "mkdocs_transfer_site.sh" para desactivar el modo de depuración a menos que se especifique.
- Quitar advertencias de Podman en la documentación de Desarrollo Backend.
- Los scripts de instalación de MkDocs eliminan el directorio .venv para incluir la última versión de dependencias.
- Servir y ejecutar en el Makefile principal cambiado: "make run" realiza una limpieza completa y recompilación; "make serve" solo ejecuta "mkdocs serve".
- Actualizar runtime de Lambda a Python 3.12, actualizar API Gateway a OpenAPI 3.0.1 con CORS y refactor de definiciones de endpoints en "aws_big_lambda/template-sam.yml" [GS-245].
- Renombrar "parentKeyNames" a "endpointKeyNames" en archivos JSON [GS-159].
- Mover atributo "parentUrl" desde "endpointKeyNames" a la raíz de los archivos JSON [GS-159].
- Renombrar el chatbot IA de "GPT functions" a "AI Tools" en comentarios de exampleapp.
- Vincular mkdocs serve a localhost:8015 para evitar conflictos con otras APIs GS [GS-172].
- Todos los logos .svg ahora están incrustados como .png en todos los archivos .md, para que se muestren en GitHub y en la app móvil de documentación [GS-252].
- EjemploApp: archivos comunes de la biblioteca movidos de "exampleapp/apps/api-chalice" a "exampleapp/apps/api-fastapi".

##### Fijo
- Arreglar problemas del motor "podman" con el comando `podman composer`.
- Arreglar instrucciones de instalación de uv y poetry en la documentación de Gestores de Paquetes de Python.
- Arreglar "npm clean" para la raíz y todos los workspaces.
- Arreglar los enlaces de configuración en la documentación, ya que apuntaban a "https://github.com/tomkat-cr/genericsuite-fe/tree/main/src/configs".
- Arreglar "FileNotFoundError: [Errno 2] No such file or directory: 'docs/Sample-Code/exampleapp/ui/public/static'" añadiendo "remove_ui_public_static" a clean_directory.sh.
- La etiqueta "create-ssl-certs" en el Makefile de exampleapp estaba definida incorrectamente.
- Afinar enlaces rotos de la documentación.
- APP_VERSION eliminado de CORE_ENVS en "aws_secrets/aws_secrets_manager.sh", separado del resto de variables de entorno que se envían a AWS Secrets Manager y se incluyen en la plantilla CloudFormation de AWS Lambda "aws_big_lambda/template-sam.yml".
- Renombrar "CONTAINER_ENGINE" a "CONTAINERS_ENGINE" en archivos .env.example [GS-252].
- Arreglar: añadir ".venv" a los scripts de limpieza.
- Reducir el tiempo de transferencia FTP construyendo un directorio temporal "docs_for_ftp", copiando allí solo los archivos necesarios y usándolo como fuente para MkDocs.

##### Seguridad
- Actualizar "urllib3" a "^2.6.2" en el archivo principal requirements.txt para corregir vulnerabilidades [GS-219]:
    * "Asignación de recursos sin límites o throttling": "CWE-770", "CVE-2025-66418", "CVSS 8.9", "SNYK-PYTHON-URLLIB3-14192443"
    * "Manejo inapropiado de datos altamente comprimidos ( Data Amplification )": "CWE-409", "CVSS 8.9", "CVE-2025-66471", "SNYK-PYTHON-URLLIB3-14192442".
##### Eliminado
- Eliminado el variable AWS_API_GATEWAY_STAGE de todos los archivos .env.example.
- Dependencias boto3 y pymongo, para que cada proyecto tenga sus propias dependencias según la base de datos y el proveedor de almacenamiento en la nube [GS-245].
- Eliminados endpoints genéricos de OpenAPI no utilizados.

## GenericSuite Backend Scripts AI

### Paquete, Pull Request y Etiqueta

* Paquete: [https://pypi.org/project/genericsuite-ai/0.3.0/](https://pypi.org/project/genericsuite-ai/0.3.0/)
* Pull Request: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/12](https://github.com/tomkat-cr/genericsuite-be-ai/pull/12)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.3.0](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.3.0)

### Descripción de la Pull Request

Agregar create_app() para Flask, pruebas try-except para todas las importaciones opcionales para reportar dependencias faltantes y arreglos de seguridad

Esta PR mejora significativamente la flexibilidad, seguridad y mantenibilidad del proyecto. Introduce un patrón estandarizado de creación de aplicaciones para Flask, amplía capacidades de bases de datos y almacenamiento en la nube, e integra masking de conversaciones de IA. Un gran enfoque está puesto en mejorar la gestión de dependencias haciendo que muchos paquetes sean opcionales y proporcionando instrucciones de instalación más claras, junto con actualizaciones críticas de seguridad a bibliotecas centrales. Estos cambios, en conjunto, optimizan el desarrollo, reducen la sobrecarga operativa y fortalecen la resiliencia de la aplicación.

Destacados

- Mayor modularidad y soporte de frameworks: Se introdujo una función create_app() estandarizada para aplicaciones Flask e integrado AI Conversation Masking en FastAPI, Flask y Chalice, mejorando la configuración y consistencia de la aplicación.
- Mejor gestión de dependencias e informes de errores: Se implementaron bloques try-except para todas las importaciones opcionales, proporcionando mensajes de error más claros a los desarrolladores sobre dependencias faltantes y simplificando la instalación. Muchas dependencias fueron eliminadas o hechas opcionales para reducir el tamaño del proyecto.
- Ampliación de bases de datos y capacidades de almacenamiento en la nube: Se añadió soporte para PostgreSQL y MySQL y se desarrolló una capa de abstracción de almacenamiento para AWS S3, Azure y Google Cloud Platform, incluyendo el uso de URLs prefirmadas de AWS para acceso seguro y limitado en el tiempo a cubos de S3.
- Actualizaciones de seguridad críticas: Se abordaron múltiples vulnerabilidades de seguridad actualizando dependencias clave como urllib3, langchain-core y langchain a sus versiones más seguras.
- Configuración y actualizaciones de modelos: Se actualizó el modelo predeterminado de HuggingFace, se ajustaron las URL base de AIMLAPI y Groq, y se corrigió la compatibilidad de faiss-cpu para implementaciones en AWS Lambda.

### CHANGELOG.md

#### [0.3.0] - 2026-02-18

##### Agregado
- API_VERSION envvar para establecer la versión de la API, por defecto "v1" [GS-245].
- Postgres [GS-194].
- Supabase [GS-161].
- MySQL [GS-249].
- Capa de abstracción de almacenamiento para AWS S3, Azure y GCP [GS-72].
- AWS generate_presigned_url() para proteger el acceso a S3, configurable para expirar pronto; STORAGE_PRESIGNED_EXPIRATION_SECONDS (predeterminado 5 minutos) [GS-72].
- Guardar archivos de OpenAPI (JSON y YAML) en PATH_TO_SAVE_OPENAPI [GS-245].
- Dependencia "requests-toolbelt" para parse_multipart.py [GS-248].
- Comando "make test" para ejecutar tests [GS-248].
- "pymongo" y "boto3" en dev dependencies para tests [GS-248].
- APP_LOGGER_OPTIONS para configurar logging, inicialmente para deshabilitar mensaje al inicio si "silent" está activo [GS-245].
- Obtención de token MCP desde encabezados (Authorization: Bearer <token>) con get_access_token() en mcplib [GS-159].
- MCP_MANDATORY_USER_ID para forzar autenticación MCP con user_id y api_key. Por defecto "0" para permitir solo autenticación con clave API [GS-159].
- Implementación del endpoint de logs [GS-250].
- Añadir header Message-ID a correos salientes [GS-37].
- Permitir configurar modo de depuración de correo vía SEND_EMAIL_DEBUG [GS-37].
- Configuración db_engine a SqlTable para que métodos como array_fields_management() y array_fields_value() usen las funciones correspondientes [GS-194].
- Implementar operaciones $inc, $push, $addToSet y $pull en la abstracción SQL [GS-194].
- Añadir get_table_structure() y quote_value() en helpers genéricos para arreglar la ejecución de super_admin_create() [GS-125].
- Soporte de $elemMatch en todas las abstracciones de bases de datos. Mejorar manejo de consultas para mayor precisión [GS-161] [GS-194] [GS-249] [GS-102].

##### Cambiado
- Standardización de prefijo de recuperación de almacenamiento de /asset a /assets en todos los frameworks [GS-245].
- Estándar de retorno status_code en lugar de http_error en "utilities.py" y "users.py" [GS-245].
- Mejoras de logging en aws.py para depuración, con mensaje inicial al inicio de la app.
- STORAGE_URL_SEED ahora requerido solo si STORAGE_URL_ENCRYPTION está activo [GS-72].
- STORAGE_ENCRYPTION renombrado a STORAGE_URL_ENCRYPTION [GS-72].
- Mejora de máscara de URL S3 para no exponer el nombre del bucket; configurables mediante STORAGE_URL_ENCRYPTION, STORAGE_URL_SEED, RUN_PROTOCOL, URL_MASK_EXTERNAL_HOSTNAME, URL_MASK_EXTERNAL_PROTOCOL. No compatible con API Gateway; solo EC2 o VPS [GS-72].
- Migración de Marshmallow a Pydantic: actualizar schema_verification() para usar Pydantic [GS-248].
- Renombrar "parentKeyNames" a "endpointKeyNames" [GS-159].
- Reimplementar autenticación por clave API usando "users_api_keys" [GS-159].
- Eliminar claves API de ejemplo del contexto de la app.
- Mejorar `send_email.py` para devolver un conjunto de resultados con información de errores, validación de parámetros, limpieza de HTML y hints de tipo [GS-37].

##### Fijo
- Remover "/" de prefijo de clave para evitar doble "/" en get_bucket_key_from_url() y corregir caracteres codificados en get_s3_presigned_url() [GS-245].
- Limpiar imports no usados y comentarios en create_app.py.
- Actualizar tipo de retorno de delete_params_file en app_context.py.
- Error de escaneo de tabla en DynamoDB abstractor "AttributeError: 'tuple' object has no attribute 'update'" [GS-102].
- Robustecer conversión de ObjectId cuando "_id_" está en like_query_params.
- Permitir objetos Request como entradas para funciones de datos de usuario para que el flujo de onboarding funcione [GS-37].
- Evitar "AssertionError: AuthenticationMiddleware must be installed to access request.user" en get_curr_user_id.
- send_email incluye encabezado "Message-ID" para evitar bloqueos de Google [GS-37].
- Actualizar abstracción SQL para manejar NULL dinámicamente [GS-262].
- Error "bson.errors.InvalidId" al crear nuevo usuario con Supabase, asignando `parent_keys["_id"] = ObjectId(parent_keys["id"])` [GS-251].

##### Seguridad
- Actualizar "urllib3" a "^2.6.3" para corregir vulnerabilidades [GS-219].
- Actualizar "werkzeug" a "^3.1.6" para corregir vulnerabilidades [GS-219].
- Actualizar "cryptography" a "^46.0.5" para corregir vulnerabilidades [GS-219].
- Añadir filtros obligatorios para get_item_from_db() y GenericEndpointHelper.generic_crud_main() [GS-262].
- Añadir sanitización al parámetro "message" en el endpoint /log [GS-262].

##### Eliminado
- Eliminadas dependencias "boto3" y "pymongo", para que cada proyecto pueda tener sus propias dependencias según el backend elegido [GS-245].
- Eliminados endpoints de ejemplo de usuario y otros para reducir dependencias no utilizadas.