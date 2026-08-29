# Desbloquea el poder full-stack con Generic Suite (GS)

![Logo de GenericSuite IA](../assets/images/gs_ai_logo_circle.png){ .center }

¿Alguna vez te has visto copiando el mismo código útil y común de una app a otra una y otra vez?

¿No crees que construir una aplicación full-stack es demasiado complejo?

GenericSuite (GS) es un framework de código abierto para crear aplicaciones con mejoras potenciadas por IA. Define tu aplicación en archivos JSON. Obtén web, móvil, API de backend y servicios MCP listos para desplegar y escalar.

[![Diagrama de GenericSuite](../assets/images/genericsuite-architecture.png)](https://genericsuite.carlosjramirez.com/assets/images/genericsuite-architecture.png)

Se basa en el paradigma de programación genérica (principio DRY), y permite definir la estructura del menú de la aplicación, esquemas de bases de datos, formularios de entrada de datos, endpoints de API, autenticación y autorización de usuarios mediante archivos de configuración JSON.

El resultado es una aplicación completa lista para desplegarse y escalarse:

- El frontend web está construido con ReactJs
- Las apps móviles están construidas con Flutter (soportando iOS, Android, Windows, macOS y web)
- Las APIs de backend están construidas con Python y el framework de tu elección (FastAPI, Flask o Chalice)
- El Servidor MCP está construido con Python y FastMCP
- Soporta los principales proveedores de nube para despliegue (AWS, GCP, Azure)
- Soporta los principales motores de bases de datos (MongoDB, DynamoDB, PostgreSQL, MySQL, Supabase)
- Las funciones de IA pueden ser impulsadas por Claude, OpenAI, Gemini, AWS Bedrock, Google Vertex AI, Hugging Face, Ollama, etc.

Ya sea que estés construyendo APIs robustas, bases de datos escalables o interfaces de usuario dinámicas, GS ofrece la flexibilidad y eficiencia necesarias para acelerar tus proyectos.

Únete a la creciente comunidad de desarrolladores que utilizan Generic Suite para impulsar sus proyectos. Explora los repositorios y empieza a construir hoy mismo.

[Notas de Lanzamiento](./Releases/index.md) | [Código de Ejemplo](./Sample-Code/index.md) | [Repositorios](./repositories.md)

## Cómo Empezar

* [Características Clave](#caracteristicas-clave)
* [¿Por qué elegir Generic Suite?](#por-que-elegir-generic-suite)
* [¿Para qué sirve Generic Suite?](#para-que-sirve-generic-suite)
* [El Núcleo de Generic Suite](#el-nucleo-de-generic-suite)
* [La IA de Generic Suite](#la-ia-de-generic-suite)
* [Código de Ejemplo](#codigo-de-ejemplo)
* [Repositorios](#repositorios)
* [Lanzamientos](#lanzamientos)
* [Presentación](#presentacion)
* [Publicaciones](#publicaciones)
* [Desarrollo Frontend](./Frontend-Development/index.md)
* [Desarrollo Backend](./Backend-Development/index.md)
* [Desarrollo Móvil](./Mobile-Development/index.md)
* [Guía de Configuración](./Configuration-Guide/index.md)
* [Historia](./history.md)

## Características Clave

### Núcleo del Framework

* Editor CRUD personalizable, generador de menús e interfaz de inicio de sesión personalizable, desplegable a AWS y un conjunto de herramientas para impulsar el desarrollo de frontend.
* Base de datos CRUD genérica y endpoints de API: al contar con un núcleo Create-Read-Update-Delete (CRUD) que puede parametrizarse y ampliarse, no es necesario reescribir código para cada editor de tablas.
* Constructor genérico de menús y endpoints de API.
* Abstracción de bases de datos: el backend puede usar MongoDB, DynamoDB, PostgreSQL, MySQL o Supabase como almacenamiento persistente, implementando una sintaxis similar a MongoDB.
* Abstracción de frameworks: admite varios frameworks, incluyendo FastAPI, Flask y Chalice, lo que lo hace adaptable a una variedad de proyectos.
* Utilidades ([Utilities](./Backend-Development/GenericSuite-Scripts/index.md)) y [Configuraciones](./Configuration-Guide/index.md) necesarias para construir y desplegar aplicaciones escalables y mantenibles.

Documentación y repositorios:

* :fontawesome-brands-react:{ .react } [GenericSuite Core (frontend version) for React.js](./Frontend-Development/GenericSuite-Core/index.md)
* :fontawesome-brands-python:{ .python } [GenericSuite Core (backend version) for Python](./Backend-Development/GenericSuite-Core/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (frontend version)](./Frontend-Development/GenericSuite-Scripts/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (backend version)](./Backend-Development/GenericSuite-Scripts/index.md)
* Repositorios: [Superproyecto](./repositories.md#superproject), [Frontend](./repositories.md#frontend), [Backend](./repositories.md#backend)
* Paquetes: [PyPI y NPMJS](./repositories.md#published-packages)

![Logo de GenericSuite](../assets/images/gs_ai_logo_circle.png){ .center }

## La IA de Generic Suite

La **Generic Suite AI** es una extensión para ayudar a desarrollar Apps que implementan IA.

Características:

* Endpoints de Agentes IA para implementar conversaciones tipo chatbot NLP.
* OpenAI GPT, Google Gemini, Anthropic Claude, Meta Llama, Hugging Face, xAI, IBM WatsonX y muchos otros modelos manejados.
* OpenAI API, Google API, Anthropic API, Hugging Face, Together AI, OpenRuter, API de IA/ML, Ollama, Clarifai y otros proveedores de LLM.
* Visión por computadora (OpenAI GPT4 Vision, Google Gemini Vision, Clarifai Vision).
* Procesamiento de voz a texto (OpenAI Whisper, Clarifai Audio Models).
* Texto a voz (OpenAI TTS-1, Clarifai Audio Models).
* Generador de imágenes (OpenAI DALL-E 3, Google Gemini Image, Clarifai Image Models).
* Indexadores vectoriales (FAISS, Chroma, Clarifai, Vectara, Weaviate, MongoDBAtlasVectorSearch).
* Embeddings (OpenAI, Hugging Face, Bedrock, Cohere, Ollama, Clarifai).
* Herramienta de búsqueda web.
* Herramienta de raspeo y análisis de páginas web.
* Lectores de JSON, PDF, Git y YouTube.
* Herramientas de traducción de idiomas.
* Chats almacenados en la Base de Datos.
* Atributos de Plan de Usuario, clave API de OpenAI y nombre de modelo en el perfil del usuario, para permitir a usuarios con plan gratuito usar Modelos con su propio costo.

Documentación y repositorios:

* :fontawesome-brands-react:{ .react } [GenericSuite AI (frontend version) for React.js](./Frontend-Development/GenericSuite-AI/index.md)
* :fontawesome-brands-python:{ .python } [GenericSuite AI (backend version) for Python](./Backend-Development/GenericSuite-AI/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (backend version)](./Backend-Development/GenericSuite-Scripts/index.md)
* Repositorios: [Frontend](./repositories.md#frontend), [Backend](./repositories.md#backend)
* Paquetes: [PyPI y NPMJS](./repositories.md#published-packages)

### Generic Suite Móvil

Características:

* Igual que [el Núcleo de Generic Suite](#el-nucleo-de-generic-suite) pero para el constructor de apps móviles.
* Hecho con Flutter para iOS, Android, Windows, macOS y web.

Documentación y repositorios:

* :fontawesome-brands-flutter:{ .flutter } [GenericSuite Mobile para Flutter](./Mobile-Development/index.md)
* Repositorios: [Móvil](./repositories.md#mobile)

### Habilidades de IA de GenericSuite

La **Colección de Habilidades de Agente IA de GenericSuite** es una colección de habilidades de IA tipo Claude para el ecosistema GenericSuite. Su pieza central es la **suite de creación de apps** (`gs-app-builder-suite`): un conjunto de habilidades de agente IA que construyen una aplicación completa de GenericSuite — frontend en React, backend en FastAPI, CRUD impulsado por JSON, asistente IA y servidor MCP — a partir de una conversación.

Documentación y repositorios:

* :fontawesome-brands-openai:{ .openai } [Habilidades de IA de GenericSuite](/ai-skills.md)
* [Repositorios](./repositories.md#ai)

### GSAM: El Generador de Aplicaciones de Generic Suite

La **Generador de Aplicaciones de Generic Suite (GSAM)** es la herramienta de IA para mejorar la ideación del desarrollo de software y probar modelos de IA, proveedores de LLM y sus características. También permite generar descripciones, estructuras de bases de datos, imágenes, videos o respuestas a partir de una indicación de texto, y dar un impulso inicial al código para usar con la biblioteca de Generic Suite.

Repositorio:

* :fontawesome-brands-python:{ .python } [Generador de Aplicaciones GenericSuite](https://github.com/tomkat-cr/genericsuite-app-maker)

<!--
### Equipo de Desarrollo de Software Asalariado por IA

El **Equipo de Desarrollo de Software Asalariado por IA de Generic Suite (ASDT)** ofrece un equipo de entidades autónomas diseñadas para resolver problemas de desarrollo de software usando IA para tomar decisiones, aprender de las interacciones y adaptarse a condiciones cambiantes sin intervención humana.

Repositorio:

* :fontawesome-brands-python:{ .python } [Equipo de Desarrollo de Software Asalariado por IA de GenericSuite](https://github.com/tomkat-cr/genericsuite-asdt-be)
-->

## Seguridad

**`Genericsuite Security Suite`** es una suite de auditoría de seguridad y preparación para producción para repositorios de software y entornos de desarrollo. Proporciona **5 habilidades especializadas de agente IA** respaldadas por scripts de la biblioteca estándar de Python 3 sin dependencias.

Ya sea usado de forma interactiva a través de asistentes de codificación IA (**Claude Code**, **Google Antigravity**, **Cursor**, **Windsurf**, etc.) o directamente como herramientas CLI independientes en pipelines CI/CD, este paquete ayuda a los desarrolladores a auditar dependencias de la cadena de suministro, fijar referencias de contenedores, eliminar GitHub Actions sin pin, y verificar la preparación del proyecto antes del despliegue en producción.

Documentación y repositorios:

* :fontawesome-brands-openai:{ .openai } [GenericSuite Security Skills](./security.md)
* [Repositorios](./repositories.md#security)

## Operaciones del Servidor

**Generic Suite Gitops** proporciona los scripts y configuraciones necesarios para desplegar en varias plataformas (servidores de desarrollo locales, VPS) utilizando tecnologías de orquestación como Kubernetes, y gestionar artefactos y repositorios con Docker y GitHub.

Documentación y repositorios:

* Guía de Despliegue: [OpenTofu (IaC) Deployment Guide](./Deployment-Guide/opentofu.md)
* [Repositorios](./repositories.md#platform)

## Repositories

[Haz clic aquí](./repositories.md) para revisar los repositorios de Git, paquetes de NPMJS y PyPI.

## Documentación

* Principal: [https://genericsuite.carlosjramirez.com](https://genericsuite.carlosjramirez.com)
* Espejo: [https://genericsuite.readthedocs.io](https://genericsuite.readthedocs.io)
* App móvil (únete al flight de prueba para probarla): [Google Play Store](https://play.google.com/apps/internaltest/4701425955610073424)

## Código de Ejemplo

Tenemos una [ExampleApp](../code/exampleapp/README.md) para mostrarte cómo usar las bibliotecas de GenericSuite.

[![Banner de ExampleApp](../code/exampleapp/assets/exampleapp_banner_01.png)](../code/exampleapp/README.md)

[ExampleApp](../code/exampleapp/README.md) es una aplicación de ejemplo completa construida como un monorepo usando Turborepo y pnpm. Esto proporciona una guía práctica y del mundo real para que los desarrolladores aprendan y aceleren sus propios proyectos. Hay un frontend en React y backends en Python, usando los 3 marcos principales: FastAPI, Flask y Chalice.

[![Banner de Plantilla de FastAPI](../code/fastapitemplate/assets/fastapitemplate_banner_01.png)](../code/fastapitemplate/README.md)

También contamos con una [Plantilla de FastAPI](../code/fastapitemplate/README.md) para ayudarte a empezar con backends basados en FastAPI.

Consulta la sección [Código de Ejemplo](./Sample-Code/index.md) para más información.

## Lanzamientos

Puedes encontrar el registro de cambios detallado para cada versión [aquí](./Releases/index.md).

[![Lanzamiento GenericSuite 20260218 - La Segunda Edición Aniversario](./Releases/images/GS_Release_2026-02-18_Image_1A.png)](./Releases/GS_Release_2026-02-18_Changelog.md)
Estamos orgullosos de presentar el [Lanzamiento GenericSuite 20260218 - La Segunda Edición Aniversario](./Releases/GS_Release_2026-02-18_Changelog.md)

## Presentación

Inglés:

* [Introducción a Generic Suite](https://raw.githubusercontent.com/tomkat-cr/genericsuite-basecamp/main/mkdocs_root/en/documents/GS_Presentation_EN_V2.pdf)

Español:

* [Introducción a Generic Suite](https://raw.githubusercontent.com/tomkat-cr/genericsuite-basecamp/main/mkdocs_root/es/documents/GS_Presentation_SP_V2.pdf)

## Publicaciones

X: [@genericsuitelib](https://twitter.com/genericsuitelib)

Inglés:

* [https://www.carlosjramirez.com/en/genericsuite/](https://www.carlosjramirez.com/en/genericsuite/)

Español:

* [https://www.carlosjramirez.com/genericsuite-es/](https://www.carlosjramirez.com/genericsuite-es/)

## Licencia

Generic Suite es software de código abierto con licencia MIT.

## Créditos

Este proyecto es desarrollado y mantenido por [Carlos Ramirez](https://www.carlosjramirez.com). Para más información o para contribuir al proyecto, visita [GenericSuite en GitHub](https://github.com/stars/tomkat-cr/lists/genericsuite).

## Política de Privacidad

[Haz clic aquí](./privacy-policy.md) para revisar la política de privacidad.

¡Feliz codificación!