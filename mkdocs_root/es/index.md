# Desbloquea el poder Full-Stack con Generic Suite (GS)

![gs_logo_circle.png](../assets/images/gs_logo_circle.png)

Generic Suite (GS) es la biblioteca de desarrollo definitiva diseñada para agilizar los flujos de trabajo de frontend y backend, posibilitando un desarrollo de aplicaciones rápido con mejoras impulsadas por IA. Ya sea que estés construyendo APIs robustas, bases de datos escalables o interfaces de usuario dinámicas, GS ofrece la flexibilidad y eficiencia necesarias para acelerar tus proyectos.

[Notas de liberación](./Releases/index.md) | [Código de muestra](./Sample-Code/index.md) | [Repositorios](./repositories.md)

<!-->
[![GenericSuite 20260218 Release - The 2nd Anniversary Edition](./Releases/images/GS_Release_2026-02-18_Image_1A.png)](./Releases/GS_Release_2026-02-18_Changelog.md)

Nos enorgullece anunciar la [Lanzamiento de GenericSuite 20260218 - La 2.ª Edición Conmemorativa](./Releases/GS_Release_2026-02-18_Changelog.md)
-->

## Comienza

Únete a la creciente comunidad de desarrolladores que utilizan Generic Suite para acelerar sus proyectos. Explora los repositorios y ¡empieza a construir hoy mismo!

- [¿Por qué elegir Generic Suite?](#why-choose-generic-suite)
- [Características Clave](#key-features)
- [¿Para qué sirve Generic Suite?](#what-is-the-generic-suite-for)
- [El Núcleo de Generic Suite](#the-generic-suite-core)
- [La IA de Generic Suite](#the-generic-suite-ai)
- [Código de muestra](#sample-code)
- [Repositorios](#repositories)
- [Lanzamientos](#releases)
- [Presentación](#presentation)
- [Publicaciones](#posts)
- [Desarrollo Frontend](./Frontend-Development/index.md)
- [Desarrollo Backend](./Backend-Development/index.md)
- [Guía de configuración](./Configuration-Guide/index.md)
- [Historial](./history.md)

## ¿Por qué elegir Generic Suite?

* Integración Full-Stack sin fisuras: desarrolla aplicaciones más rápido con una biblioteca unificada para frontend y backend, reduciendo código redundante y asegurando consistencia.
* Eficiencia impulsada por IA: aprovecha las capacidades de IA integradas para mejorar la automatización, generar contenido y optimizar el desarrollo de software.
* Personalizable y escalable: adapta el marco a tus necesidades específicas, con soporte para múltiples marcos de programación, bases de datos y plataformas de despliegue.
* Flujo de desarrollo acelerado: utilidades preconstruidas y herramientas de automatización ahorran tiempo, permitiéndote centrarte en la innovación en lugar de tareas repetitivas.
* Compatibilidad multiplataforma: ya sea que trabajes con FastAPI, Flask, Chalice, MongoDB, DynamoDB, Postgres, MySQL, Supabase, GS se adapta a tu pila tecnológica sin esfuerzo.

## Características Clave

### Núcleo del Framework

* Editor CRUD personalizable, generador de menús e interfaz de inicio de sesión personalizable.
* Creador genérico de bases de datos y endpoints de API para eliminar código redundante.
* Abstracción del backend que soporta FastAPI, Flask y Chalice.
* Abstracción de bases de datos para MongoDB, DynamoDB, Postgres, MySQL y Supabase con una sintaxis de consulta unificada.
* Despliegue sencillo con AWS y otros servicios en la nube.

### Desarrollo Potenciado por IA

* Endpoint de Agente IA con integraciones de OpenAI, LangChain y Hugging Face.
* Visión por computadora, procesamiento de voz y texto a voz.
* Extracción web, herramientas de traducción y búsqueda vectorial para un manejo avanzado de datos de forma.

### Habilidades de IA

* Colección de plugins Claude Skills para el ecosistema GenericSuite.
* Un conjunto de habilidades de agentes IA que construyen una aplicación completa de GenericSuite — frontend en React, backend en FastAPI, CRUD impulsado por JSON, asistente IA y servidor MCP — a partir de una conversación.

### GSAM (Generador de Apps de Generic Suite)

* Ideación asistida por IA para el desarrollo de aplicaciones, generación de código y estructuración de bases de datos.
* Generación de imágenes y videos usando modelos de IA de vanguardia.
* Presentaciones de apps impulsadas por IA, sugerencias de nombres e ingeniería de prompts.

### ASDT (Equipo de Desarrollo de Software Agentico)

* Colaboración IA multiagente para resolver problemas y automatizar software.
* Construido sobre CrewAI, Camel AI, LangGraph y Smolagent para flujos de trabajo agentizados escalables.

### DevOps y Despliegue sin Esfuerzo

* Scripts GitOps preconfigurados para Kubernetes, Docker y entornos VPS.
* Configuraciones de servicios IA locales, incluyendo OLLAMA, WebUI, Stable Diffusion y N8N.
* Documentación completa y buenas prácticas vía Generic Suite Basecamp.

## ¿Para qué sirve Generic Suite?

El Generic Suite es un conjunto de utilidades frontend y backend hechas con ReactJS y Python para ayudar a desarrollar Apps más rápido.

Está compuesto por un **Núcleo de Generic Suite**, que es el núcleo para todos los elementos de la suite, y extensiones como la Generic Suite AI.

![gs_logo_circle.png](../assets/images/gs_logo_circle.png)

## El Núcleo de Generic Suite

Características:

* Editor CRUD personalizable, generador de menús, interfaz de inicio de sesión personalizable, despliegue a AWS y un conjunto de herramientas para acelerar el desarrollo frontend.
* Base de datos CRUD genérica y endpoints de API: al disponer de un código central de Crear-Leer-Actualizar-Eliminar que puede parametrizarse y ampliarse, no es necesario reescribir código para cada editor de tablas.
* Creador genérico de menús y endpoints de API.
* Abstracción de bases de datos: el backend puede usar MongoDB, DynamoDB, Postgres, MySQL o Supabase como almacenamiento persistente, implementando una sintaxis estilo MongoDB.
* Abstracción de frameworks: admite varios frameworks, incluyendo FastAPI, Flask y Chalice, haciéndolo adaptable a una variedad de proyectos.
* [Utilidades](./Backend-Development/GenericSuite-Scripts/index.md), y [Configuraciones](./Configuration-Guide/index.md) necesarias para construir y desplegar aplicaciones escalables y mantenibles.

Paquetes:

* :fontawesome-brands-react:{ .react } [GenericSuite Core (frontend version) para React.js](./Frontend-Development/GenericSuite-Core/index.md)
* :fontawesome-brands-python:{ .python } [GenericSuite Core (backend version) para Python](./Backend-Development/GenericSuite-Core/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (backend version)](./Backend-Development/GenericSuite-Scripts/index.md)

![gs_ai_logo_circle.png](../assets/images/gs_ai_logo_circle.png)

## La IA de Generic Suite

La **IA de Generic Suite** es una extensión para ayudar a desarrollar Apps que implementan IA.

Características:

* Endpoint de Agente IA para implementar conversaciones tipo chatbot de PLN.
* OpenAI GPT, Google Gemini, Anthropic Claude, Meta Llama, Hugging Face, xAI, IBM WatsonX, y muchos otros modelos compatibles.
* OpenAI API, Google API, Anthropic API, Hugging Face, Together AI, OpenRuter, API de IA/ML, Ollama, Clarifai y otros proveedores de LLM.
* Visión por computadora (OpenAI GPT4 Vision, Google Gemini Vision, Clarifai Vision).
* Procesamiento de voz a texto (OpenAI Whisper, Clarifai Audio Models).
* Texto a voz (OpenAI TTS-1, Clarifai Audio Models).
* Generador de imágenes (OpenAI DALL-E 3, Google Gemini Image, Clarifai Image Models).
* Indexadores vectoriales (FAISS, Chroma, Clarifai, Vectara, Weaviate, MongoDBAtlasVectorSearch).
* Embeddings (OpenAI, Hugging Face, Bedrock, Cohere, Ollama, Clarifai).
* Herramienta de búsqueda web.
* Herramienta de extracción y análisis de páginas web.
* Lectores de JSON, PDF, Git y YouTube.
* Herramientas de traducción de idiomas.
* Chats almacenados en la base de datos.
* Plan de usuario, clave de API de OpenAI y nombre de modelo en el perfil del usuario, para permitir que los usuarios con plan gratuito utilicen los modelos a su propio costo.

Paquetes:

* :fontawesome-brands-react:{ .react } [GenericSuite AI (versión frontend) para React.js](./Frontend-Development/GenericSuite-AI/index.md)
* :fontawesome-brands-python:{ .python } [GenericSuite AI (versión backend) para Python](./Backend-Development/GenericSuite-AI/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (versión backend)](./Backend-Development/GenericSuite-Scripts/index.md)

### Habilidades de Agente IA de GenericSuite

La colección de Claude Skills para el ecosistema GenericSuite es la colección de habilidades de Agente IA de Claude para GenericSuite. Su pieza central es la suite de construcción de apps (`gs-app-builder-suite`): un conjunto de habilidades de agentes IA que construyen una aplicación completa de GenericSuite — frontend en React, backend en FastAPI, CRUD impulsado por JSON, asistente IA y servidor MCP — a partir de una conversación.

Repositorio:

* :fontawesome-brands-python:{ .python } [Habilidades de Agente IA de GenericSuite](https://github.com/tomkat-cr/genericsuite-skills)

### GSAM: El Generador de Apps de Generic Suite

El **Generador de Apps de Generic Suite (GSAM)** es la herramienta de IA para mejorar la ideación de desarrollo de software y probar modelos de IA, proveedores de LLM y sus características. También permite generar descripciones, estructuras de bases de datos, imágenes, videos o respuestas a partir de un prompt de texto, y generar código de inicio para utilizar con la biblioteca Generic Suite.

Repositorio:

* :fontawesome-brands-python:{ .python } [Generador de Apps de Generic Suite](https://github.com/tomkat-cr/genericsuite-app-maker)

### Equipo de Desarrollo de Software Agentico de Generic Suite

El **Equipo de Desarrollo de Software Agentico de Generic Suite (ASDT)** proporciona un equipo de entidades autónomas diseñadas para resolver problemas de desarrollo de software usando IA para tomar decisiones, aprender de las interacciones y adaptarse a condiciones cambiantes sin intervención humana.

Repositorio:

* :fontawesome-brands-python:{ .python } [Equipo de Desarrollo de Software Agentico de Generic Suite](https://github.com/tomkat-cr/genericsuite-asdt-be)

## Operaciones del Servidor

El **Gitops de Generic Suite** proporciona los scripts y configuraciones necesarios para desplegarse en diversas plataformas (servidores de desarrollo locales, VPS) usando tecnologías de orquestación como Kubernetes, y gestionar artefactos y repositorios con Docker y GitHub.

Repositorio:

* :fontawesome-brands-linux:{ .linux } [Gitops de GenericSuite (Operaciones de servidor de desarrollo local)](https://github.com/tomkat-cr/genericsuite-gitops)

## Repositorios

[Haz clic aquí](./repositories.md) para revisar los repositorios de Git, paquetes de NPMJS y PyPI.

## Documentación

* Principal: [https://genericsuite.carlosjramirez.com](https://genericsuite.carlosjramirez.com)
* Espejo: [https://genericsuite.readthedocs.io](https://genericsuite.readthedocs.io)

## Código de muestra

Tenemos un [ExampleApp](../code/exampleapp/README.md) para mostrarte cómo usar las bibliotecas de GenericSuite.

[![ExampleApp Banner](../code/exampleapp/assets/exampleapp_banner_01.png)](../code/exampleapp/README.md)    

[ExampleApp](../code/exampleapp/README.md) es una aplicación de ejemplo completa construida como un monorepo usando Turborepo y pnpm. Esto proporciona un plano práctico y del mundo real para que los desarrolladores aprendan y aceleren sus propios proyectos. Hay un frontend en React y backends en Python, usando los 3 marcos principales: FastAPI, Flask y Chalice.

[![FastAPI Template Banner](../code/fastapitemplate/assets/fastapitemplate_banner_01.png)](../code/fastapitemplate/README.md)    

También tenemos una [Plantilla FastAPI](../code/fastapitemplate/README.md) para ayudarte a empezar con backends basados en FastAPI.

Consulta la sección [Código de muestra](./Sample-Code/index.md) para más información.

## Lanzamientos

Puedes encontrar el registro de cambios detallado de cada versión [aquí](./Releases/index.md).

## Presentación

Inglés:

* [Introduction to Generic Suite](https://raw.githubusercontent.com/tomkat-cr/genericsuite-basecamp/main/mkdocs_root/en/documents/GS_Presentation_EN_V2.pdf)

Español:

* [Introducción a Generic Suite](https://raw.githubusercontent.com/tomkat-cr/genericsuite-basecamp/main/mkdocs_root/es/documents/GS_Presentation_SP_V2.pdf)

## Publicaciones

X: [@genericsuitelib](https://twitter.com/genericsuitelib)

Inglés:

* [https://www.carlosjramirez.com/genericsuite](https://www.carlosjramirez.com/genericsuite)

Español:

* [https://www.carlosjramirez.com/genericsuite-es/](https://www.carlosjramirez.com/genericsuite-es/)

## Licencia

Generic Suite es un software de código abierto licenciado bajo la licencia [MIT](https://github.com/tomkat-cr/genericsuite-basecamp/blob/main/LICENSE).

## Créditos

Este proyecto es desarrollado y mantenido por [Carlos Ramirez](https://www.carlosjramirez.com). Para más información o contribuir al proyecto, visita [GenericSuite en GitHub](https://github.com/stars/tomkat-cr/lists/genericsuite).

## Política de Privacidad

[Haz clic aquí](./privacy-policy.md) para revisar la política de privacidad.

¡Feliz codificación!