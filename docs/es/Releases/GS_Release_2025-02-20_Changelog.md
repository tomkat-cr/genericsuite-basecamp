# 20250220 - El Lanzamiento del 1er Aniversario

![GS_Release_2025-07-05_Image_3B.png](./images/GS_Release_2025-07-05_Image_3B.png)

Fecha de lanzamiento: 2025-02-20

## Resumen

Nos complace anunciar el 1er Lanzamiento del Aniversario de GenericSuite, un hito significativo que trae una serie de potentes nuevas funciones y mejoras para desarrolladores y empresas. Este lanzamiento subraya nuestro compromiso de proporcionar un conjunto completo y de vanguardia de herramientas para el desarrollo de software moderno.

Los puntos clave de este lanzamiento incluyen:

- Capacidades de IA mejoradas: Hemos integrado funcionalidades de IA avanzadas, incluida la generación de imágenes y vídeos dentro del Generador de Aplicaciones GenericSuite (GSAM). Nuestro backend de IA ahora admite una gama más amplia de proveedores, como Together AI, xAI (Grok), IBM WatsonX y Nvidia, ofreciendo mayor flexibilidad y potencia para tus aplicaciones impulsadas por IA.

- Introducción del Equipo de Desarrollo de Software Basado en Agentes (ASDT): Una incorporación innovadora, el ASDT es un equipo de agentes de IA diseñados para automatizar y optimizar el ciclo de vida del desarrollo de software. Desde la ideación y planificación hasta la codificación y las pruebas, el ASDT está listo para revolucionar la forma en que construyes software.

- Desarrollo e implementación mejorados: Hemos avanzado significativamente en nuestra GitOps e infraestructura de backend. La introducción de un servidor Ollama, un servidor n8n y la implementación de claves API en el GS BE Core mejora la seguridad y la escalabilidad. El Generador Genérico de Endpoints para Flask simplifica la creación de API, mientras que las correcciones en nuestros componentes de frontend y backend aseguran una experiencia de desarrollo más estable y robusta.

Este lanzamiento de aniversario es mucho más que una simple actualización; es un salto hacia adelante en nuestra misión de empoderar a los desarrolladores con las herramientas que necesitan para construir el futuro del software. Te invitamos a explorar las nuevas funciones y a ver cómo GenericSuite puede acelerar tu proceso de desarrollo.

## GSAM (GenericSuite App Maker)

### Pull Request y Etiqueta 0.5.0

* Etiqueta: [https://github.com/tomkat-cr/genericsuite-app-maker/releases/tag/0.5.0](https://github.com/tomkat-cr/genericsuite-app-maker/releases/tag/0.5.0)
* PR: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/4](https://github.com/tomkat-cr/genericsuite-app-maker/pull/4)
* PR: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/5](https://github.com/tomkat-cr/genericsuite-app-maker/pull/5)
* PR: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/6](https://github.com/tomkat-cr/genericsuite-app-maker/pull/6)
* PR: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/7](https://github.com/tomkat-cr/genericsuite-app-maker/pull/7)
* PR: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/8](https://github.com/tomkat-cr/genericsuite-app-maker/pull/8)
* PR: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/9](https://github.com/tomkat-cr/genericsuite-app-maker/pull/9)
* PR: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/10](https://github.com/tomkat-cr/genericsuite-app-maker/pull/10)
* PR: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/11](https://github.com/tomkat-cr/genericsuite-app-maker/pull/11)
* PR: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/12](https://github.com/tomkat-cr/genericsuite-app-maker/pull/12)

### Registro de cambios

#### 0.5.0 (2025-02-17)
--

##### Nuevo
- Agregar capacidades de generación de imágenes y vídeos al GSAM Agent compatible con Live Agent Studio [GS-166].
- Agregar el botón y la acción "new_prompt" para vaciar el campo de entrada de preguntas [GS-55].
- Agregar el uso del modelo genérico para la gsam_agent_lib [GS-55].

##### Cambios
- Ollama habilitado [GS-55].
- Control de uso del modelo genérico para la gsam_agent_lib con la constante SIMPLE_PAI_AGENT. Cuando es True, solo están disponibles los proveedores OpenAI u Openrouter; False (por defecto) ofrece todos los proveedores en el archivo "app_config.json" [GS-55].

##### Correcciones
- Arreglar el error de tiempo de ejecución en la interfaz de usuario de Streamlit en producción [GS-55].
- Se corrigieron errores de tiempo de ejecución de Ollama y todas las configuraciones pasan al subelemento "options" [GS-55].

## ASDT (Equipo de Desarrollo de Software Basado en Agentes de GenericSuite)

### Pull Request y Etiqueta 0.1.0

* Etiqueta: [https://github.com/tomkat-cr/genericsuite-asdt-be/releases/tag/0.1.0](https://github.com/tomkat-cr/genericsuite-asdt-be/releases/tag/0.1.0)
* PR: [https://github.com/tomkat-cr/genericsuite-asdt-be/pull/1](https://github.com/tomkat-cr/genericsuite-asdt-be/pull/1)
* PR: [https://github.com/tomkat-cr/genericsuite-asdt-be/pull/2](https://github.com/tomkat-cr/genericsuite-asdt-be/pull/2)
* PR: [https://github.com/tomkat-cr/genericsuite-asdt-be/pull/3](https://github.com/tomkat-cr/genericsuite-asdt-be/pull/3)
* PR: [https://github.com/tomkat-cr/genericsuite-asdt-be/pull/4](https://github.com/tomkat-cr/genericsuite-asdt-be/pull/4)
* PR: [https://github.com/tomkat-cr/genericsuite-asdt-be/pull/5](https://github.com/tomkat-cr/genericsuite-asdt-be/pull/5)

### Registro de cambios

#### 0.1.0 (2025-02-17)
---

##### Nuevo
- Añadir selección y configuración de LLM utilizando variables de entorno, e incluyendo OpenAI, Google, Ollama, Anthropic, Hugging Face, Groq, NVIDIA, X AI, Together AI, API de IA/ML y OpenRouter [GS-128].
- Añadir la tarea de ideación para generar ideas para el hackathon "AIstronauts-Space Agents on a mission" desde lablab.ai [GS-55].
- Añadir distintas variables de entorno para llms y modelos de codificación, razonamiento, planificación y gestión, para que los agentes normales, el agente gestor y el agente de planificación puedan usarlas [GS-128].
- Añadir el agente de planificación, para que las acciones de generación de código se disparen e iteren [GS-128].
- Añadir la herramienta de monitoreo "openlit" [GS-128].
- Añadir la herramienta de monitoreo "agentops" [GS-128].
- Añadir generación de archivos de salida en cada tarea [GS-128].
- Añadir generación automática del equipo, agentes y tareas directamente desde los archivos yaml sin envoltorios (clase y métodos decorados) [GS-128].
- Añadir "allow_code_execution" a los agentes de desarrollo y de pruebas automatizadas [GS-128].
- Añadir la lectura desde archivo a las entradas `project` y `topic` (el contenido entre corchetes indica una ruta de archivo) [GS-128].
- Añadir "examples/instructions.md" para construir la entrada `project` como un archivo PRD (Documento de Requisitos del Producto) [GS-128].
- Añadir la sociedad Camel-AI de agentes a las bibliotecas de agentes.

##### Cambios
- Cambio: eliminar la dependencia de GenericSuite.

##### Correcciones
- Corregir los prompts de agentes y tareas para que funcionen efectivamente como un equipo [GS-128].

## GenericSuite Gitops

### Pull Request y Etiqueta 0.2.0

* Etiqueta: [https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.2.0](https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.2.0)
* PR: [https://github.com/tomkat-cr/genericsuite-gitops/pull/1](https://github.com/tomkat-cr/genericsuite-gitops/pull/1)

### Registro de cambios

#### 0.2.0 (2024-02-18)
---

##### Nuevo
- Abstract y añadir al proyecto Genericsuite [GS-141].
- Implementar servidor ollama [GS-139].
- Implementar servidor n8n [GS-165].

#### 0.1.2 (2022-03-16)
---

##### Cambios
- FA-58: "restart: unless-stopped" a la configuración de docker compose del VPS, para mantener los contenedores activos durante reinicios del servidor.
- FA-31: Bases de datos separadas para prod, staging y desarrollo.
- Aumentar la versión de las imágenes Docker del VPS.

##### Nuevo
- Añadir scripts Python para obtener IP y escanear la red.
- Crear este repositorio `version.txt`, `README.md` y `CHANGELOG.md` archivos.

#### 0.1.11 (2022-03-10)
---

##### Nuevo
- Vista previa con el despliegue inicial del BE (Backend) y FE (Frontend) de Fynapp webapp.
Notas de la versión:
- FA-3: Crear una pipeline para construir y desplegar el backend en un contenedor Docker en un VPS Linux.
- FA-13: Crear una rama de desarrollo y empezar a usarla con buenas prácticas de SDLC.
- FA-18: Crear una pipeline para construir y desplegar BE & FE en Heroku.
- FA-21: Recuperar el servidor local I5 y/o Celeron y instalar Centos 7.
- FA-22: Instalar y configurar Kubernetes en el servidor local y realizar un spike para evaluar el uso de esta tecnología.
- FA-23: Construir una imagen Docker en una pipeline de Gitlab instalando un runner de Gitlab.

## GenericSuite Backend Scripts

### Paquete, Pull Request y Etiqueta 1.0.13

* Paquete: [https://www.npmjs.com/package/genericsuite-be-scripts/v/1.0.13](https://www.npmjs.com/package/genericsuite-be-scripts/v/1.0.13)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.0.13](https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.0.13)
* PR: [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/4](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/4)
* PR: [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/5](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/5)

### Registro de cambios

#### 1.0.13 (2025-02-18)
---

##### Cambios
- La opción "--loglevel debug" se añadió al servidor gunicorn para Generic Endpoint Builder para Flask [GS-15].

##### Correcciones
- Arreglar el error de tiempo de ejecución de flask run con gunicorn cuando la máquina local está ejecutando una VPN, obteniendo la dirección IP local, que es la primera reportada por el comando "ifconfig" [GS-15].

## GenericSuite Backend Core

### Paquete, Pull Request y Etiqueta 0.1.10

* Paquete: [https://pypi.org/project/genericsuite/0.1.10/](https://pypi.org/project/genericsuite/0.1.10/)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.1.10](https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.1.10)
* PR: [https://github.com/tomkat-cr/genericsuite-be/pull/8](https://github.com/tomkat-cr/genericsuite-be/pull/8)
* PR: [https://github.com/tomkat-cr/genericsuite-be/pull/9](https://github.com/tomkat-cr/genericsuite-be/pull/9)

### Registro de cambios

#### 0.1.10 (2025-02-19)

##### Nuevo
- Implementar claves API para GS BE Core [GS-159].
- Implementar el endpoint "CAUJF" para construir todos los parámetros del usuario en archivos JSON locales [GS-159].
- Generador Genérico de Endpoints para Flask [GS-15].

##### Cambios
- FastAPI get_current_user() ahora obtiene los encabezados desde el objeto de solicitud (requerido por la implementación de claves API) [GS-159].
- La clase GenericDbHelperSuper asigna valor por defecto None a Request y Blueprint, y {} a query_params y request_body, para que pueda ser utilizada por save_all_users_params_files() u otras funciones que no dispongan de esos objetos en un momento dado [GS-159].
- La clase GenericDbHelperSuper evita llamar a specific_func_name() cuando blueprint es None [GS-159].
- Limpieza general del código y cambios de linting.

##### Correcciones
- Arreglar el error de Poetry 2.x "The option --no-update does not exist" [FA-84].
- Faltaban las propiedades "context" y "event_dict", eventos "to_dict" y "to_original_event" fueron añadidos a la clase FastAPI Request.
- Arreglar "'License :: OSI Approved :: ISC License' no es un clasificador válido" al intentar subir con "python3 -m twine upload dist/*" [FA-84].

## GenericSuite Backend AI

### Paquete, pull request y Etiqueta 0.1.12

* Paquete: [https://pypi.org/project/genericsuite-ai/0.1.12/](https://pypi.org/project/genericsuite-ai/0.1.12/)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.12](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.12)
* PR: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/8](https://github.com/tomkat-cr/genericsuite-be-ai/pull/8)

### Registro de cambios

#### 0.1.12 (2025-02-19)
---

##### Nuevo
- Implementar el proveedor y modelos Together AI [GS-158].
- Implementar el modelo xAI Grok [GS-157].
- Implementar el proveedor IBM watsonx [GS-155].
- Implementar la interfaz abstracta de Langchain para modelos genéricos [GS-155].
- Implementar API de Nvidia / NIM / Nemotron [GS-93].
- Implementar el modelo de chat Rhymes.ai Aria [GS-152].
- Implementar el modelo de generación de vídeo Rhymes.ai Allegro (solo configuración) [GS-153].
- Añadir la variable de entorno AI_STREAMING para configurar el método de respuesta en streaming [GS-32].
- Añadir NVIDIA_API_KEY, NVIDIA_MODEL_NAME, NVIDIA_TEMPERATURE, NVIDIA_MAX_TOKENS, NVIDIA_TOP_P y NVIDIA_BASE_URL como variables de entorno [GS-93].
- Añadir RHYMES_CHAT_API_KEY, RHYMES_CHAT_MODEL_NAME, RHYMES_CHAT_TEMPERATURE, RHYMES_CHAT_MAX_TOKENS, RHYMES_CHAT_TOP_P, RHYMES_CHAT_BASE_URL, RHYMES_VIDEO_API_KEY, RHYMES_VIDEO_MODEL_NAME, RHYMES_VIDEO_BASE_URL, RHYMES_VIDEO_NUM_STEP y RHYMES_VIDEO_CFG_SCALE como variables de entorno [GS-152].
- Añadir AIMLAPI_TOP_P para configurar el parámetro top_p en API de IA/ML [GS-138].
- Añadir OPENAI_TOP_P para configurar el parámetro top_p en el modelo de chat de OpenAI.
- Añadir la clase abstract CustomLLM para LangChain para implementar nuevos proveedores de LLM que aún no están implementados en LangChain [GS-155].

##### Cambios
- Cambiar el modelo de generación de imágenes "black-forest-labs/FLUX.1-schnell" por defecto.
- Cambiar OPENAI_MAX_TOKENS y AIMLAPI_MAX_TOKENS para que tengan '' por defecto para obtener el máximo de tokens posible [GS-157].
- Cambiar "grok-beta" a "grok-2" como modelo predeterminado para xAI [GS-157].
- Cambiar "openai" en lugar de "openai_chat" para obtener el proveedor predeterminado de OpenAI en el parámetro LANGCHAIN_DEFAULT_MODEL.
- Se añadió la función "get_openai_api()" para estandarizar la creación del cliente LLM para proveedores compatibles con la API de completions de OpenAI [GS-157].

##### Correcciones
- Arreglar el error "ValueError: invalid literal for int() with base 10: ''" en get_vision_response() cuando OPENAI_MAX_TOKENS está vacío [GS-152].
- Arreglar el mensaje de error de Poetry 2.x "The option --no-update does not exist" [FA-84].
- Arreglar el error "'License :: OSI Approved :: ISC License' no es un clasificador válido" al ejecutar "python3 -m twine upload dist/*" [FA-84].

## GenericSuite Frontend Core

### Paquete, Pull Request y Etiqueta 1.0.24

* Paquete: [https://www.npmjs.com/package/genericsuite/v/1.0.24](https://www.npmjs.com/package/genericsuite/v/1.0.24)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.24](https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.24)
* PR: [https://github.com/tomkat-cr/genericsuite-fe/pull/6](https://github.com/tomkat-cr/genericsuite-fe/pull/6)

### Registro de cambios

#### 1.0.24 (2025-02-19)
---

##### Nuevo
- Implementar claves API para GS BE Core [GS-159].
- Añadir nuevas características y corregir cosas descubiertas durante la implementación de IBM Watson X [GS-155].
- Añadir el parámetro "description_fields" en selectOptions() para tener un atributo/columna compuesto(a) para las descripciones de los menús desplegables. Si no se especifica, usará ["name"] (como antes) [GS-155].

##### Correcciones
- Arreglar el error de passcode no definido en la actualización de usuarios que llama al backend después de crear un usuario dejando la contraseña vacía (UsersPasswordValidations) [GS-155].
- Arreglar un fallo al llamar a funciones específicas asignando el objeto "fieldValues", porque genericFuncArrayDefaultValue() le asignaba un atributo "resultset" recursivo infinito, evitando la asignación de valores predeterminados en la llamada "dbPreRead" (creación).

## GenericSuite Frontend AI

### Paquete, Pull Request y Etiqueta 1.0.22

* Paquete: [https://www.npmjs.com/package/genericsuite-ai/v/1.0.22](https://www.npmjs.com/package/genericsuite-ai/v/1.0.22)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.22](https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.22)
* PR: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/6](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/6)

### Registro de cambios

#### 1.0.22 (2025-02-19)
---

##### Cambios
- Núcleo FE de GenericSuite actualizado a v1.0.24.