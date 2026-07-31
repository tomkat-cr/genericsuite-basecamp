# Desata el poder full-stack con Generic Suite (GS)

![Logotipo de GenericSuite IA](../assets/images/gs_ai_logo_circle.png){ .center }

¿Alguna vez te has encontrado copiando el mismo código común y útil de una aplicación a otra una y otra vez?

¿No crees que construir una aplicación full-stack es demasiado compleja?

GenericSuite (GS) es un framework de código abierto para construir aplicaciones con mejoras potenciadas por IA. Define tu aplicación en archivos JSON. Obtén servicios web, móviles, API de backend y MCP listos para desplegar y escalar.

[![Diagrama de GenericSuite](../assets/images/genericsuite-architecture.png)](https://genericsuite.carlosjramirez.com/assets/images/genericsuite-architecture.png)

Se basa en el paradigma de programación genérica (Principio DRY) y permite definir la estructura de menús de la aplicación, esquemas de bases de datos, formularios de entrada de datos, endpoints de API, autenticación y autorización de usuarios utilizando archivos de configuración JSON.

El resultado es una aplicación completa lista para desplegar y escalar:

- El frontend web está construido con ReactJs
- Las aplicaciones móviles están construidas con Flutter (compatibles con iOS, Android, Windows, macOS y web)
- Las APIs de backend están construidas con Python y el framework de tu elección (FastAPI, Flask o Chalice)
- El servidor MCP está construido con Python y FastMCP
- Soporta los principales proveedores de nube para despliegue (AWS, GCP, Azure)
- Soporta los principales motores de bases de datos (MongoDB, DynamoDB, PostgreSQL, MySQL y Supabase)
- Las funciones de IA pueden ser impulsadas por Claude, OpenAI, Gemini, AWS Bedrock, Google Vertex AI, Hugging Face, Ollama, etc.

Ya sea que estés construyendo APIs robustas, bases de datos escalables o interfaces de usuario dinámicas, GS ofrece la flexibilidad y la eficiencia necesarias para acelerar tus proyectos.

Únete a la creciente comunidad de desarrolladores que utilizan Generic Suite para potenciar sus proyectos. Explora los repositorios y empieza a construir hoy mismo!

[Notas de la versión](./Releases/index.md) | [Código de ejemplo](./Sample-Code/index.md) | [Repositorios](./repositories.md)

## Empezar

* [Características Clave](#características-Clave)
* [¿Por qué elegir Generic Suite?](#por-qué-elegir-generic-suite)
* [¿Para qué sirve Generic Suite?](#para-qué-sirve-generic-suite)
* [El Núcleo de Generic Suite](#el-núcleo-de-generic-suite)
* [La IA de Generic Suite](#la-ia-de-generic-suite)
* [Código de ejemplo](#código-de-ejemplo)
* [Repositorios](#repositorios)
* [Lanzamientos](#lanzamientos)
* [Presentación](#presentación)
* [Publicaciones](#publicaciones)
* [Desarrollo Frontend](./Frontend-Development/index.md)
* [Desarrollo Backend](./Backend-Development/index.md)
* [Desarrollo Móvil](./Mobile-Development/index.md)
* [Guía de Configuración](./Configuration-Guide/index.md)
* [Historia](./historia.md)

## Características Clave

### Núcleo del Framework

* Editor CRUD personalizable, generador de menús y una interfaz de inicio de sesión personalizable.
* Generador genérico de bases de datos y endpoints de API para eliminar código redundante.
* Abstracción del framework de backend que admite FastAPI, Flask y Chalice.
* Abstracción de bases de datos para MongoDB, DynamoDB, PostgreSQL, MySQL y Supabase con una sintaxis de consulta unificada.
* Despliegue sencillo con AWS y otros servicios en la nube.

### Desarrollo impulsado por IA

* Servidor MCP para abrir las aplicaciones desarrolladas a Agentes IA.
* Endpoint de chatbot de IA con integraciones de OpenAI, LangChain y Hugging Face.
* Visión por computadora, procesamiento de voz y conversión de texto a voz.
* Extracción de datos web, herramientas de traducción y búsqueda vectorial para un manejo avanzado de datos.

### Habilidades IA

* Conjunto Claude Skills: un conjunto de habilidades de agentes IA que construyen una aplicación completa de GenericSuite — frontend React, backend FastAPI, CRUD impulsado por JSON, asistente de IA y servidor MCP — a partir de una conversación.

### DevOps & Despliegue sin esfuerzo

* Despliegues a producción, QA, Staging y demo con OpenTofu (IaC) y CloudFormation (AWS).
* Soporte para múltiples plataformas de despliegue en la nube: AWS, Azure, GCP.
* Scripts GitOps preconfigurados para Kubernetes, Docker y entornos VPS.
* Configuraciones de servicio de IA locales, incluyendo OLLAMA, WebUI, Stable Diffusion y N8N.
* Documentación completa y buenas prácticas a través de Generic Suite Basecamp.

### GSAM (Generador de Aplicaciones Generic Suite)

* Ideación asistida por IA para el desarrollo de aplicaciones, generación de código y estructuración de bases de datos.
* Generación de imágenes y videos utilizando modelos de IA de vanguardia.
* Presentaciones de aplicaciones impulsadas por IA, sugerencias de nombres y ingeniería de prompts.

## ¿Por qué elegir Generic Suite?

* Integración full-stack sin fisuras: Desarrolla aplicaciones más rápido con una biblioteca unificada para frontend y backend, reduciendo código redundante y asegurando consistencia.
* Eficiencia impulsada por IA: Aprovecha las capacidades de IA integradas para mejorar la automatización, generar contenido y optimizar el desarrollo de software.
* Personalizable y escalable: adapta el framework a tus necesidades específicas, con soporte para múltiples frameworks de programación, bases de datos y plataformas de despliegue.
* Flujo de desarrollo acelerado: utilidades preconstruidas y herramientas de automatización ahorran tiempo, permitiéndote centrarte en la innovación en lugar de tareas repetitivas.
* Compatibilidad multiplataforma: Ya sea que estés trabajando con FastAPI, Flask, Chalice, MongoDB, DynamoDB, PostgreSQL, MySQL, Supabase, GS se adapta a tu pila tecnológica sin esfuerzo.

## ¿Para qué sirve Generic Suite?

GenericSuite es una biblioteca de desarrollo diseñada para agilizar flujos de trabajo de frontend, backend, móvil e IA, habilitando un desarrollo rápido de aplicaciones con mejoras potenciadas por IA. Cuenta con un conjunto de utilidades hechas con ReactJS, Flutter y Python.

Se compone de un [Núcleo de Generic Suite](#the-generic-suite-core), que es el núcleo de todos los elementos de la suite, extensiones como [La IA de Generic Suite](#the-generic-suite-ai), [Generic Suite Móvil](#the-generic-suite-mobile), y herramientas auxiliares como [Generic Suite Gitops](#server-operations), [Habilidades de Agentes IA de Generic Suite](#genericsuite-ai-agent-skills), y [GSAM - Generador de Aplicaciones de Generic Suite](#gsam-the-generic-suite-ai-app-maker).

![gs_logo_circle.png](../assets/images/gs_logo_circle.png){ .center }

## La IA de Generic Suite

**La IA de Generic Suite** es una extensión para ayudar a desarrollar aplicaciones que implementan IA.

Características:

* Endpoint de Agente IA para implementar conversaciones tipo chatbot basadas en PLN.
* OpenAI GPT, Google Gemini, Anthropic Claude, Meta Llama, Hugging Face, xAI, IBM WatsonX y muchos otros modelos compatibles.
* API de OpenAI, API de Google, API de Anthropic, Hugging Face, Together AI, OpenRuter, API de IA/ML, Ollama, Clarifai y otros proveedores de LLM.
* Visión por computadora (OpenAI GPT-4 Vision, Google Gemini Vision, Clarifai Vision).
* Procesamiento de voz a texto (OpenAI Whisper, Clarifai Audio Models).
* Texto a voz (OpenAI TTS-1, Clarifai Audio Models).
* Generador de imágenes (OpenAI DALL-E 3, Google Gemini Image, Clarifai Image Models).
* Indexadores vectoriales (FAISS, Chroma, Clarifai, Vectara, Weaviate, MongoDBAtlasVectorSearch).
* Embeddings (OpenAI, Hugging Face, Bedrock, Cohere, Ollama, Clarifai).
* Herramienta de búsqueda en la web.
* Rastreo y análisis de páginas web.
* Lectores de JSON, PDF, Git y YouTube.
* Herramientas de traducción de idiomas.
* Chats almacenados en la base de datos.
* Plan de usuario, clave API de OpenAI y atributos de nombre de modelo en el perfil de usuario, para permitir que los usuarios del plan gratuito utilicen los modelos a su propio costo.

Paquetes:

* [GenericSuite IA (versión frontend) para React.js](./Frontend-Development/GenericSuite-AI/index.md)
* [GenericSuite IA (versión backend) para Python](./Backend-Development/GenericSuite-AI/index.md)
* [GenericSuite Scripts (versión backend)](./Backend-Development/GenericSuite-Scripts/index.md)

### Generic Suite Móvil

Características:

* Las mismas que [el Núcleo de Generic Suite](#the-generic-suite-core), pero para el constructor de apps móviles.
* Desarrollado con Flutter para iOS, Android, Windows, macOS y web.

Paquetes:

* [GenericSuite Mobile para Flutter](./Mobile-Development/index.md)

### Habilidades de Agentes IA de Generic Suite

Las **Habilidades de Agentes IA de GenericSuite** es una colección de plugins Claude Skills para el ecosistema de GenericSuite. Su pieza central es la **suite de constructor de aplicaciones** (`gs-app-builder-suite`): un conjunto de habilidades de agentes IA que construyen una aplicación completa de GenericSuite — frontend React, backend FastAPI, CRUD impulsado por JSON, asistente de IA y servidor MCP — a partir de una conversación.

Repositorio:

* [Habilidades de Agentes IA de GenericSuite](https://github.com/tomkat-cr/genericsuite-skills)

### GSAM: El Generador de Aplicaciones de Generic Suite

La herramienta de IA **Generic Suite App Maker (GSAM)** es la herramienta para mejorar la ideación en el desarrollo de software, probar modelos de IA, proveedores de LLM y sus características. También permite generar descripciones, estructuras de bases de datos, imágenes, videos o respuestas a partir de un prompt de texto, y dar inicio al código para usar con la biblioteca Generic Suite.

Repositorio:

* [Generador de Aplicaciones de Generic Suite](https://github.com/tomkat-cr/genericsuite-app-maker)

<!--
### Equipo de Desarrollo de Software con IA

El **Equipo de Desarrollo de Software con IA de Generic Suite (ASDT)** ofrece un equipo de entidades autónomas diseñadas para resolver problemas de desarrollo de software utilizando IA para tomar decisiones, aprender de las interacciones y adaptarse a condiciones cambiantes sin intervención humana.

Repositorio:

* [Habilidades de Agentes IA de GenericSuite](https://github.com/tomkat-cr/genericsuite-asdt-be)
-->

## Operaciones del servidor

El **Generic Suite Gitops** ofrece los scripts y configuraciones necesarios para desplegar en varias plataformas (servidores de desarrollo locales, VPS) utilizando tecnologías de orquestación como Kubernetes, y gestionar artefactos y repositorios con Docker y GitHub.

Repositorio:

* [GenericSuite Gitops (Operaciones del servidor de desarrollo local)](https://github.com/tomkat-cr/genericsuite-gitops)
* Guía de Despliegue: OpenTofu (IaC) Guía de Despliegue

## Repositorios

[Haz clic aquí](./repositories.md) para revisar los repositorios de Git, paquetes NPMJS y PyPI.

## Documentación

* Principal: [https://genericsuite.carlosjramirez.com](https://genericsuite.carlosjramirez.com)
* Espejo: [https://genericsuite.readthedocs.io](https://genericsuite.readthedocs.io)

## Código de ejemplo

Tenemos un [ExampleApp](../code/exampleapp/README.md) para mostrarte cómo usar las bibliotecas de GenericSuite.

[Banner de ExampleApp](../code/exampleapp/assets/exampleapp_banner_01.png)](../code/exampleapp/README.md)

[ExampleApp](../code/exampleapp/README.md) es una aplicación de ejemplo con todas las funciones construida como un monorepo usando Turborepo y pnpm. Esto proporciona un plano práctico y real para que los desarrolladores aprendan y aceleren sus propios proyectos. Hay un frontend en React y backends en Python, utilizando los 3 marcos principales: FastAPI, Flask y Chalice.

[Banner de Plantilla FastAPI](../code/fastapitemplate/assets/fastapitemplate_banner_01.png)](../code/fastapitemplate/README.md)

También tenemos una [Plantilla FastAPI](../code/fastapitemplate/README.md) para ayudarte a empezar con backends basados en FastAPI.

Consulta la sección [Código de ejemplo](./Sample-Code/index.md) para más información.

## Lanzamientos

Puedes encontrar el registro de cambios detallado para cada versión [aquí](./Releases/index.md).

[Imagen de lanzamiento de GenericSuite 2026-02-18 - 2ª Edición del Aniversario](./Releases/images/GS_Release_2026-02-18_Image_1A.png)](./Releases/GS_Release_2026-02-18_Changelog.md)
Nos enorgullece anunciar el [Lanzamiento de GenericSuite 2026-02-18 - 2ª Edición del Aniversario](./Releases/GS_Release_2026-02-18_Changelog.md)

## Presentación

Inglés:

* [Introduction to Generic Suite](https://raw.githubusercontent.com/tomkat-cr/genericsuite-basecamp/main/mkdocs_root/en/documents/GS_Presentation_EN_V2.pdf)

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