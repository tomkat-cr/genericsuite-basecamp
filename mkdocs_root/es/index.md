# Desata el poder Full-Stack con Generic Suite (GS)

![gs_logo_circle.png](../assets/images/gs_logo_circle.png)

Generic Suite (GS) es la biblioteca de desarrollo definitiva diseñada para simplificar los flujos de trabajo de frontend y backend, permitiendo el desarrollo rápido de aplicaciones con mejoras impulsadas por IA. Ya estés construyendo APIs robustas, bases de datos escalables o interfaces de usuario dinámicas, GS ofrece la flexibilidad y la eficiencia necesarias para acelerar tus proyectos.

[Notas de la versión](./Releases/index.md) | [Código de muestra](./Sample-Code/index.md) | [Repositorios](./repositories.md)

<!--
[![GenericSuite 20260218 Release - The 2nd Anniversary Edition](./Releases/images/GS_Release_2026-02-18_Image_1A.png)](./Releases/GS_Release_2026-02-18_Changelog.md)

Nos enorgullece anunciar la [Versión GenericSuite 20260218 - La 2ª Edición del Aniversario](./Releases/GS_Release_2026-02-18_Changelog.md)
-->

## Get Started

Únete a la creciente comunidad de desarrolladores que utilizan Generic Suite para potenciar sus proyectos. Explora los repositorios y ¡empieza a construir hoy mismo!

* [¿Por qué elegir Generic Suite?](#why-choose-generic-suite)
* [Funciones clave](#key-features)
* [¿Para qué sirve Generic Suite?](#what-is-the-generic-suite-for)
* [El Núcleo de Generic Suite](#the-generic-suite-core)
* [La IA de Generic Suite](#the-generic-suite-ai)
* [Código de muestra](#sample-code)
* [Repositorios](#repositories)
* [Lanzamientos](#releases)
* [Presentación](#presentation)
* [Entradas](#posts)
* [Desarrollo Frontend](./Frontend-Development/index.md)
* [Desarrollo Backend](./Backend-Development/index.md)
* [Guía de Configuración](./Configuration-Guide/index.md)
* [Historial](./history.md)

## Why Choose Generic Suite?

* Integración Seamless Full-Stack – Desarrolla aplicaciones más rápido con una biblioteca unificada tanto para frontend como para backend, reduciendo código redundante y asegurando consistencia.
* Eficiencia impulsada por IA – Aprovecha las capacidades de IA integradas para mejorar la automatización, generar contenido y optimizar el desarrollo de software.
* Personalizable y escalable – Adapta el marco a tus necesidades específicas, con soporte para múltiples frameworks, bases de datos y plataformas de despliegue.
* Flujo de desarrollo acelerado – Utilidades preconstruidas y herramientas de automatización ahorran tiempo, permitiéndote centrarte en la innovación en lugar de tareas repetitivas.
* Compatibilidad entre plataformas – Ya estés trabajando con FastAPI, Flask, Chalice, MongoDB, DynamoDB, Postgres, MySQL, Supabase, GS se adapta a tu stack tecnológico sin esfuerzo.

## Key Features

### Core Framework

* Editor CRUD personalizable, generador de menús e interfaz de inicio de sesión.
* Constructor genérico de bases de datos y endpoints de API para eliminar código redundante.
* Abstracción de framework backend que soporta FastAPI, Flask y Chalice.
* Abstractor de base de datos: el backend puede usar MongoDB, DynamoDB, Postgres, MySQL o Supabase como almacenamiento persistente, implementando una sintaxis de consultas unificada.
* Despliegue fácil con AWS y otros servicios en la nube.

### IA en desarrollo

* Endpoint de agente IA para implementar conversaciones tipo chatbot NLP.
* Capacidades de visión por computadora, procesamiento de voz y conversión de texto a voz.
* Web scraping, herramientas de traducción y búsqueda vectorial para un manejo de datos avanzado.

### Habilidades IA

* Conjunto de plugins Claude Skills para el ecosistema GenericSuite.
* Un conjunto de habilidades de agentes IA que construyen una aplicación completa de GenericSuite — frontend en React, backend en FastAPI, CRUD impulsado por JSON, asistente IA y servidor MCP — a partir de una conversación.

### GSAM (Generador de Aplicaciones Generic Suite)

* Ideación asistida por IA para el desarrollo de aplicaciones, generación de código y estructuración de bases de datos.
* Generación de imágenes y videos usando modelos de IA de última generación.
* Presentaciones de apps impulsadas por IA, sugerencias de nombres y ingeniería de prompts.

### ASDT (Equipo de Desarrollo de Software Agentico)

* Colaboración IA de múltiples agentes para resolver problemas y automatizar software.
* Construido sobre CrewAI y Camel AI (LangGraph y Smolagent planificados) para flujos de trabajo agenticos escalables.

### DevOps y despliegue sin esfuerzos

* Despliegues a producción, QA, Staging y demo con OpenTofu (IaC) y CloudFormation (AWS).
* Scripts GitOps preconfigurados para entornos Kubernetes, Docker y VPS.
* Configuraciones de servicios de IA locales, incluyendo OLLAMA, WebUI, Stable Diffusion y N8N.
* Documentación integral y mejores prácticas a través de Generic Suite Basecamp.

## ¿Para qué sirve la Generic Suite?

La Generic Suite es un conjunto de utilidades de frontend y backend hechas con ReactJS y Python para ayudar a desarrollar Apps más rápido.

Está compuesto por un **Núcleo de Generic Suite**, que es el núcleo de todos los elementos de la suite, y extensiones como la Generic Suite AI.

![gs_logo_circle.png](../assets/images/gs_logo_circle.png)

## El Núcleo de Generic Suite

Funciones:

* Editor CRUD personalizable, generador de menús e interfaz de inicio de sesión personalizable, despliegue a AWS y una suite de herramientas para impulsar tu proceso de desarrollo frontend.
* CRUD genérico de bases de datos y endpoints de API: al contar con un código central Create-Read-Update-Delete que puede ser parametrizado y extendido, no es necesario reescribir código para cada editor de tablas.
* Constructor genérico de menús y endpoints de API.
* Abstractor de bases de datos: el backend puede usar MongoDB, DynamoDB, Postgres, MySQL o Supabase como almacenamiento persistente, implementando una sintaxis similar a MongoDB.
* Abstractor de frameworks: admite varios frameworks, incluyendo FastAPI, Flask y Chalice, lo que lo hace adaptable a una variedad de proyectos.
* [Utilidades](./Backend-Development/GenericSuite-Scripts/index.md), y [Configuraciones](./Configuration-Guide/index.md) necesarias para construir y desplegar aplicaciones escalables y mantenibles.

Paquetes:

* :fontawesome-brands-react:{ .react } [GenericSuite Core (versión frontend) para React.js](./Frontend-Development/GenericSuite-Core/index.md)
* :fontawesome-brands-python:{ .python } [GenericSuite Core (versión backend) para Python](./Backend-Development/GenericSuite-Core/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (versión frontend)](./Frontend-Development/GenericSuite-Scripts/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (versión backend)](./Backend-Development/GenericSuite-Scripts/index.md)

![gs_ai_logo_circle.png](../assets/images/gs_ai_logo_circle.png)

## La IA de Generic Suite

La **IA de Generic Suite** es una extensión para ayudar a desarrollar Apps que implementan IA.

Funciones:

* Endpoint de agente IA para implementar conversaciones tipo chatbot NLP.
* OpenAI GPT, Google Gemini, Anthropic Claude, Meta Llama, Hugging Face, xAI, IBM WatsonX y muchos otros modelos compatibles.
* API de OpenAI, API de Google, API de Anthropic, Hugging Face, Together AI, OpenRuter, API de IA/ML, Ollama, Clarifai y otros proveedores de LLM.
* Visión por computadora (OpenAI GPT4 Vision, Google Gemini Vision, Clarifai Vision).
* Procesamiento de voz a texto (OpenAI Whisper, Clarifai Audio Models).
* Texto a voz (OpenAI TTS-1, Clarifai Audio Models).
* Generador de imágenes (OpenAI DALL-E 3, Google Gemini Image, Clarifai Image Models).
* Indexadores vectoriales (FAISS, Chroma, Clarifai, Vectara, Weaviate, MongoDBAtlasVectorSearch).
* Embeddings (OpenAI, Hugging Face, Bedrock, Cohere, Ollama, Clarifai).
* Herramienta de búsqueda web.
* Herramienta de raspado y análisis de páginas web.
* Lectores de JSON, PDF, Git y YouTube.
* Herramientas de traducción de idiomas.
* Conversaciones almacenadas en la base de datos.
* Plan de usuario, clave de API de OpenAI y atributos de nombre de modelo en el perfil del usuario, para permitir que los usuarios del plan gratuito usen modelos a su propio costo.

Paquetes:

* :fontawesome-brands-react:{ .react } [IA de GenericSuite (versión frontend) para React.js](./Frontend-Development/GenericSuite-AI/index.md)
* :fontawesome-brands-python:{ .python } [IA de GenericSuite (versión backend) para Python](./Backend-Development/GenericSuite-AI/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (versión backend)](./Backend-Development/GenericSuite-Scripts/index.md)

### Habilidades de Agente IA de GenericSuite

Las **Habilidades de Agente IA de GenericSuite** son una colección de plugins Claude Skills para el ecosistema GenericSuite. Su pieza central es el **app-builder suite** (`gs-app-builder-suite`): un conjunto de habilidades de agente IA que construyen una aplicación completa de GenericSuite — frontend en React, backend en FastAPI, CRUD impulsado por JSON, asistente IA y servidor MCP — a partir de una conversación.

Repositorio:

* :fontawesome-brands-python:{ .python } [Habilidades de Agente IA de GenericSuite](https://github.com/tomkat-cr/genericsuite-skills)

### GSAM: El Generador de Aplicaciones de Generic Suite IA

El **GSAM (Generador de Aplicaciones de Generic Suite IA)** es la herramienta de IA para mejorar la ideación del desarrollo de software, probar modelos de IA, proveedores de LLM y sus características. También permite generar descripciones, estructuras de bases de datos, imágenes, videos o respuestas a partir de un texto y crear código inicial para usar con la biblioteca Generic Suite.

Repositorio:

* :fontawesome-brands-python:{ .python } [Generador de Aplicaciones GenericSuite](https://github.com/tomkat-cr/genericsuite-app-maker)

### Equipo de Desarrollo de Software Agentico de Generic Suite

El **Equipo de Desarrollo de Software Agentico de Generic Suite (ASDT)** ofrece un equipo de entidades autónomas diseñadas para resolver problemas de desarrollo de software utilizando IA para tomar decisiones, aprender de las interacciones y adaptarse a condiciones cambiantes sin intervención humana.

Repositorio:

* :fontawesome-brands-python:{ .python } [Equipo de Desarrollo de Software Agentico de GenericSuite](https://github.com/tomkat-cr/genericsuite-asdt-be)

## Operaciones del Servidor

Las operaciones de Gitops de Generic Suite proporcionan los scripts y configuraciones necesarios para desplegar en diversas plataformas (servidores de desarrollo locales, VPS) utilizando tecnologías de orquestación como Kubernetes y gestionar artefactos y repositorios con Docker y GitHub.

Repositorio:

* :fontawesome-brands-linux:{ .linux } [GenericSuite Gitops (Operaciones de Servidor de Desarrollo Local)](https://github.com/tomkat-cr/genericsuite-gitops)
* Guía de Despliegue: [Guía de Despliegue de OpenTofu (IaC)](./Deployment-Guide/opentofu.md)

## Repositories

[Haz clic aquí](./repositories.md) para revisar los repositorios de Git, paquetes NPMJS y PyPI.

## Documentation

* Principal: [https://genericsuite.carlosjramirez.com](https://genericsuite.carlosjramirez.com)
* Espejo: [https://genericsuite.readthedocs.io](https://genericsuite.readthedocs.io)

## Sample Code

Tenemos un [ExampleApp](../code/exampleapp/README.md) para mostrarte cómo usar las bibliotecas de GenericSuite.

![Banner de ExampleApp](../code/exampleapp/assets/exampleapp_banner_01.png)](../code/exampleapp/README.md)    

[ExampleApp](../code/exampleapp/README.md) es una aplicación de ejemplo completa construida como un monorepo usando Turborepo y pnpm. Esto proporciona un plano práctico y del mundo real para que los desarrolladores aprendan y aceleren sus propios proyectos. Hay un frontend en React y backends en Python, usando los 3 marcos de trabajo principales: FastAPI, Flask y Chalice.

![Banner de Plantilla FastAPI](../code/fastapitemplate/assets/fastapitemplate_banner_01.png)

También tenemos una [Plantilla FastAPI](../code/fastapitemplate/README.md) para ayudarte a empezar con backends basados en FastAPI.

Consulta la sección [Código de muestra](./Sample-Code/index.md) para obtener más información.

## Releases

Puedes encontrar el registro de cambios detallado de cada versión [aquí](./Releases/index.md).

## Presentación

Inglés:

* [Introduction to Generic Suite](https://raw.githubusercontent.com/tomkat-cr/genericsuite-basecamp/main/mkdocs_root/en/documents/GS_Presentation_EN_V2.pdf)

Español:

* [Introducción a Generic Suite](https://raw.githubusercontent.com/tomkat-cr/genericsuite-basecamp/main/mkdocs_root/es/documents/GS_Presentation_SP_V2.pdf)

## Posts

X: [@genericsuitelib](https://twitter.com/genericsuitelib)

Inglés:

* [https://www.carlosjramirez.com/en/genericsuite/](https://www.carlosjramirez.com/en/genericsuite/)

Español:

* [https://www.carlosjramirez.com/genericsuite-es/](https://www.carlosjramirez.com/genericsuite-es/)

## License

Generic Suite es software de código abierto licenciado bajo la licencia [MIT](https://github.com/tomkat-cr/genericsuite-basecamp/blob/main/LICENSE).

## Credits

Este proyecto es desarrollado y mantenido por [Carlos Ramirez](https://www.carlosjramirez.com). Para obtener más información o contribuir al proyecto, visita [GenericSuite en GitHub](https://github.com/stars/tomkat-cr/lists/genericsuite).

## Privacy Policy

[Haz clic aquí](./privacy-policy.md) para revisar la política de privacidad.

¡Feliz codificación!