# 20241007 - Presentación de estreno de GenericSuite en la UPB Medellín

![GS_Release_2024-10-07_Image_4 - The FynBots.jpg](./images/GS_Release_2024-10-07_Image_4%20-%20The%20FynBots.jpg)

Fecha de lanzamiento: 2024-10-07

## Resumen

El 7 de octubre de 2024 marca un hito con el lanzamiento de la última versión de GenericSuite, una biblioteca de software avanzada diseñada para el desarrollo de aplicaciones tanto en el backend como en el frontend usando Python y React.js. Esta actualización trae una variedad de mejoras y nuevas características que prometen aumentar la eficiencia y potenciar los flujos de trabajo de los desarrolladores.

Entre los aspectos destacados está la incorporación de la abstracción DynamoDb, Flux.1, Groq, interfaces de Amazon Bedrock, Claude 3.5 Sonnet, 100% Tailwind, modo oscuro y un menú lateral configurable, lo que permite una experiencia de usuario más personalizada. También hemos introducido la biblioteca "GsIcons", que reemplaza FontAwesome, para ofrecer una estética más moderna y coherente.

En el ámbito frontend, hemos adoptado por completo Tailwind CSS, eliminando la dependencia de react-bootstrap, lo que optimiza el rendimiento y la personalización de la interfaz de usuario. Además, se han realizado mejoras significativas en la capacidad de respuesta del chatbot, asegurando interacciones más suaves y efectivas.

En el backend, se han mejorado las capacidades de abstracción de la base de datos DynamoDb, y se han introducido nuevas funcionalidades de IA, incluyendo generadores de imágenes y modelos de chat avanzados: generador de imágenes Flux.1, Groq y interfaces de la plataforma Amazon Bedrock, y la implementación del modelo Claude 3.5 Sonnet más reciente.

GenericSuite continúa evolucionando, proporcionando herramientas que facilitan el desarrollo ágil y eficaz de aplicaciones, adaptándose a las necesidades cambiantes del mercado tecnológico. Explora todas las nuevas capacidades y transforma tu enfoque de desarrollo de aplicaciones hoy.

## GenericSuite Frontend Core

### Paquete, pull request y etiqueta

- Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.22](https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.22)
- PR: [https://github.com/tomkat-cr/genericsuite-fe/pull/4](https://github.com/tomkat-cr/genericsuite-fe/pull/4)
- Paquete: [https://www.npmjs.com/package/genericsuite/v/1.0.22](https://www.npmjs.com/package/genericsuite/v/1.0.22)

### Registro de cambios

#### 1.0.22 (2024-10-07)
---

##### Nuevas
- Añadir modo oscuro [GS-63].
- Añadir menú lateral configurable [GS-114].
- Añadir funciones genéricas de localstorage [GS-112].
- Añadir guardar el modo oscuro y el menú lateral en localstorage [GS-112].
- Nueva biblioteca "GsIcons" reemplaza FontAwesome [GS-115].
- Añadir logotipo horizontal en el encabezado de la App [GS-63].
- Añadir el atributo opcional "template" a las entradas de app_main_menu.json para personalizar el diseño de las opciones de menú [GS-112] [GS-129].
- Añadir <NoDesignComponent>> para tener opciones de menú sin el diseño GS FE Core [GS-112] [GS-129].
- Añadir export testHelpersMocks [GS-129].

##### Cambios
- Reemplazar por completo react-bootstrap y usar solo Tailwind CSS [GS-63].
- Eliminar PII de local storage [GS-2]
- Cambiar el comportamiento de las acciones para que aparezcan al hacer clic en la línea de la página de listado de GCE_RFC (editor CRUD genérico) [GS-112].
- Cambiar el color al pasar el cursor sobre la línea en la página de listado de GCE_RFC [GS-112].
- Cambiar las líneas con colores diferentes si son pares/impares en la página de listado de GCE_RFC [GS-112].
- Mejorar la maquetación de la página de datos implementando constantes Tailwind en la GCE_RFC [GS-112].
- Cambiar el tamaño del cuadro de búsqueda que es demasiado pequeño en la página de listado de la GCE_RFC [GS-112].
- <HashRouter> fue reemplazado por <RouterProvider> y createBrowserRouter() [GS-112].
- "/login" reemplazado por "/logout" en la opción Cerrar sesión [GS-112].
- Añadir campos "openai_api_key" y "openai_model" a las configuraciones JSON predeterminadas de usuario y user_profile [FA-200] [FA-201].
- <PrivateRoute/> evita usar getPrefix(true) [GS-112].
- Renombrar "test-helpers/mock-fetch.ts" a "test-helpers/mocks.js" para hacerlo más genérico y cambiar la extensión de ".ts" a ".js" para corregir el error "Parameter 'data' implicitly has an 'any' type | export function mockFetch(data)..." durante el "make publish" [GS-129].

##### Correcciones
- Corregir clases faltantes en el nuevo output.css de Tailwind v3.4.9 [GS-63].
- Corregir el problema de valores de fila en la página de índice que no se muestran [GS-108].
- Corregir el problema de %PUBLIC_URL% en public/index.html al ejecutar la app con webpack [GS-116].
- Corregir Mostrar WaitAnimation() en iterateChildComponents() y EditFormFormik() para que la carga de datos sea evidente en la opción de Perfil de Usuario [GS-112].

##### Rupturas
- Bootstrap CSS ya no se usa [GS-63].
- FontAwesome ya no se usa [GS-115].
- Imágenes SVG eliminadas e incluidas en la biblioteca "GsIcons" [GS-115].
- Eliminar eval() en el GS FrontEnd [GS-127].

## GenericSuite Frontend AI

### Paquete, pull request y etiqueta

- Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.20](https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.20)
- PR: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/4](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/4)
- Paquete: [https://www.npmjs.com/package/genericsuite-ai/v/1.0.20](https://www.npmjs.com/package/genericsuite-ai/v/1.0.20)

### Registro de cambios

#### 1.0.20 (2024-10-07)
---

##### Nuevas
- Nueva biblioteca "GsIcons" reemplaza FontAwesome [GS-115].

##### Cambios
- Actualizar GS FE AI con conversión GS FE Core Tailwind y nuevos contextos [GS-129].
- <HashRouter> fue reemplazado por <RouterProvider> y createBrowserRouter() [GS-112].
- Cambios en las: íconos de cámara, voz y clip del chatbot a tamaño "m" [GS-129].
- Diseño del chatbot mejorado y comportamiento responsive corregido [GS-129].
- El botón de eliminar en la lista de conversaciones del Chatbot solo se muestra cuando el puntero está sobre la conversación [GS-129].

##### Correcciones
- Corregir las clases faltantes en el nuevo output.css de Tailwind v3.4.9 [GS-63].
- Corregir el problema de %PUBLIC_URL% en public/index.html al ejecutar la app con webpack [GS-116].
- Corregir cuando el Chatbot envía un error y se hace clic en Cerrar, que no se muestre más información en el área de mensajes [GS-129].
- Corregir que el clic en un elemento de la lista de conversaciones del Chatbot funcione solo si se hace clic en el texto, no en el área de relleno [GS-129].
- Corregir la ubicación de <UserInput> del Chatbot con el nuevo GS FE Core y Tailwind puro, también debe funcionar cuando se usa la plantilla <NoDesignComponent> [GS-129].
- Corregir todas las pruebas para que sean compatibles con los nuevos contextos y constantes del GS FE Core [GS-112] [GS-129].
- Eliminar todas las referencias de enlaces a "/#" [GS-112].
- Restringir el código fuente exportado a dist en "make publish".
- Versión de Formik fijada a 2.4.5 en package.json para evitar la advertencia de GCE_RFC cuando se hace clic en el botón +New [GS-112].

##### Rupturas
- Bootstrap CSS ya no se usa [GS-63].
- FontAwesome ya no se usa [GS-115].
- Imágenes SVG eliminadas e incluidas en la biblioteca "GsIcons" [GS-115].

## GenericSuite Backend Core

### Paquete, pull request y etiqueta

- Etiqueta: [https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.1.9](https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.1.9)
- PR: [https://github.com/tomkat-cr/genericsuite-be/pull/7](https://github.com/tomkat-cr/genericsuite-be/pull/7)
- Paquete: [https://pypi.org/project/genericsuite/0.1.9/](https://pypi.org/project/genericsuite/0.1.9/)

### Registro de cambios

#### 0.1.9 (2024-10-07)
---

##### Nuevas
- Añadir endpoint "/users/current_user_d" [GS-2].
- Añadir la variable de entorno GS_LOCAL_ENVIR para detectar una base de datos local que se ejecuta en un contenedor Docker [GS-102].

##### Cambios
- Hacer que las tablas DynamoDb con prefijo funcionen con la Abstracción GS DB [GS-102].
- Añadir manejo de errores a todos los métodos de GenericDbHelper [GS-102].
- El método de abstracción DynamoDB "update_one()" maneja update_one, replace_one, $addToSet y operaciones $pull [GS-102].
- El registrador de la app muestra la condición LOCAL y el motor de la base de datos.
- Botocore actualizado a "^1.35.20" [GS-128].
- S3transfer actualizado a "^0.10.0" [GS-128].

## GenericSuite Backend AI

### Paquete, pull request y etiqueta

- Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.10](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.10)
- PR: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/6](https://github.com/tomkat-cr/genericsuite-be-ai/pull/6)
- Paquete: [https://pypi.org/project/genericsuite-ai/0.1.10/](https://pypi.org/project/genericsuite-ai/0.1.10/)

### Registro de cambios

#### 0.1.10 (2024-10-07)
---

##### Nuevas
- Implementar pipelines locales HF (HuggingFace) [GS-59].
- Implementar generador de imágenes HF (HuggingFace) [GS-117].
- Implementar generador de imágenes Flux.1 [GS-117].
- Implementar Anthropic Claude 3.5 Sonnet [GS-33].
- Implementar modelo de chat Groq [GS-92].
- Implementar chat y generador de imágenes de Amazon Bedrock [GS-131].
- Añadir HUGGINGFACE_PIPELINE_DEVICE para configurar el parámetro "device" de pipeline() [FA-233].
- Implementar modelos o1-mini/o1-preview para usar vía AI/ML API aimlapi.com [GS-138].
- Implementar modelo ligero GS Huggingface, identificado por model_types "huggingface_remote" o "gs_huggingface". Los model_types "huggingface" y "huggingface_pipeline" usan la dependencia "langchain_hugginface" que requiere "sentence-transformers", dificultando desplegar el proyecto en AWS Lambda Functions [GS-136].
- Implementar Falcon Mamba con HF [GS-118].
- Implementar Meta Llama 3.1 con HF [GS-119].

##### Cambios
- Actualizar Langchain a "^0.3.0" [GS-131].
- Reemplazar "gpt-3.5-turbo" por "gpt-4o-mini" como modelo OpenAI por defecto [GS-109].
- HUGGINGFACE_ENDPOINT_URL reemplazado por HUGGINGFACE_DEFAULT_CHAT_MODEL [GS-59].
- La clase Config acepta tanto OPENAI_MODEL_NAME como OPENAI_MODEL envvars [GS-128].
- La verificación de facturación en get_model() se moved a get_model_middleware() [GS-128].
- El usuario con plan gratuito solo puede usar el modelo "gpt-4o-mini" con su propia clave API, independientemente de lo configurado en LANGCHAIN_DEFAULT_MODEL [FA-233].

##### Correcciones
- Corregir error de Claude2 de Anthropic API tras cambio de prompts grandes, reemplazando Claude2 por Claude 3.5 Sonnet [GS-33].
- Corregir la advertencia "Warning: deprecated HuggingFaceTextGenInference-use HuggingFaceEnpoint instead" [GS-59].
- Corregir la incompatibilidad de dependencias entre GS BE Core y GS BE AI corrigiendo la versión de "urllib3" a "1.26" (y clarifai a "^10.1.0" en consecuencia) porque el uso de "urllib3" de GS BE Core es menor que "<2" [GS-128].

##### Rupturas
- La dependencia "langchain_hugginface" ya no se incluye en este paquete. Debe importarse en el proyecto de la App [GS-136].

## GS BE Scripts

### Paquete, pull request y etiqueta

- Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.0.12](https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.0.12)
- PR: [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/3/files](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/3/files)
- Paquete: [https://www.npmjs.com/package/genericsuite-be-scripts/v/1.0.12](https://www.npmjs.com/package/genericsuite-be-scripts/v/1.0.12)

### Registro de cambios

#### 1.0.12 (2024-10-07)
---

##### Nuevas
- Añadir archivo ".nvmrc" para establecer la versión predeterminada de Node del repositorio.
- Añadir la base de datos DynamoDB funcionando junto con MongoDB en un contenedor Docker al ejecutar la App en la etapa "dev" [GS-102].
- Añadir generación de tablas DynamoDB locales en "generate_dynamodb_cf.py" [GS-102].
- Añadir contenedor Docker de DynamoDB a "mongodb_stack_for_test.yml" [GS-102].
- Añadir gestor de banco de pruebas DynamoDB local (taydy/dynamodb-manager) a "mongodb_stack_for_test.yml" [GS-102].
- Añadir la variable de entorno DYNAMDB_PREFIX al script "run_aws.sh" con el valor "${APP_NAME_LOWERCASE}_${STAGE}_" [GS-102].
- Añadir GS_LOCAL_ENVIR para detectar una base de datos local en un contenedor Docker [GS-102].
- Añadir "run_mongo_docker.sh" ejecuta "generate_dynamodb_cf.sh create_tables dev" para crear las tablas DynamoDB en el contenedor Docker local [GS-102].
- Añadir "/users/current_user_d" endpoint [GS-2].

##### Cambios
- Hacer que las tablas DynamoDb con prefijo funcionen con la Abstracción GS DB [GS-102].
- Makefile "mongo_docker" ejecuta los contenedores MongoDB y DynamoDB sin llamar a "make run" por defecto [GS-102].

##### Correcciones
- Corregir el error en "run_mongo_docker.sh" al iniciar contenedores cuando Docker Desktop no está en ejecución [GS-102].

## GenericSuite Basecamp

### Pull request y etiqueta

- Etiqueta: [https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/0.0.12](https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/0.0.12)
- PR: [https://github.com/tomkat-cr/genericsuite-basecamp/pull/4](https://github.com/tomkat-cr/genericsuite-basecamp/pull/4)

### Registro de cambios

#### 0.0.12 (2024-10-07)
---

##### Nuevas
- Hacer que las tablas DynamoDb con prefijo funcionen con la Abstracción GS DB [GS-102].
- Implementar HF (HuggingFace) pipelines locales [GS-59].
- Implementar Falcon Mamba con HF [GS-118].
- Implementar Meta Llama 3.1 con HF [GS-119].
- Implementar HF (HuggingFace) generador de imágenes [GS-117].
- Implementar Flux.1 generador de imágenes [GS-117].
- Implementar Claude 3.5 Sonnet de Anthropic [GS-33].
- Implementar Groq modelo de chat [GS-92].
- Añadir documentación LOCALSTACK_AUTH_TOKEN [GS-97].
- Implementar Amazon Bedrock chat y generador de imágenes [GS-131].
- Añadir HUGGINGFACE_PIPELINE_DEVICE para configurar el parámetro "device" de pipeline() [FA-233].
- Implementar o1-mini/o1-preview modelos para usar vía AI/ML API aimlapi.com [GS-138].
- Implementar modelo ligero GS Huggingface, identificado por model_types "huggingface_remote" o "gs_huggingface" [GS-136].

##### Cambios
- Reemplazar react-bootstrap por completo y usar solo Tailwind CSS [GS-63].
- Ya no es necesario "index-template.html" porque se corrigió el problema de %PUBLIC_URL% en public/index.html al ejecutar la app con webpack [GS-116].
- Reemplazar GPT-3.5 con gpt-4o-mini como modelo OpenAI por defecto [GS-109].
- HUGGINGFACE_ENDPOINT_URL reemplazado por HUGGINGFACE_DEFAULT_CHAT_MODEL [GS-59].
- El componente HashRouter fue reemplazado por RouterProvider y createBrowserRouter() [GS-112].

##### Correcciones
- Corregir el problema de %PUBLIC_URL% en public/index.html al ejecutar la app con webpack [GS-116].

##### Rupturas
- Bootstrap CSS ya no se usa [GS-63].
- FontAwesome ya no se usa [GS-115].
- Imágenes SVG eliminadas e incluidas en la biblioteca "GsIcons" [GS-115].
- Eliminar eval() en el GS FrontEnd [GS-127].