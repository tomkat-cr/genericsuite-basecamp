# Unlock Full-Stack Power with Generic Suite (GS)

<table cellpadding="0" cellspacing="0" style="border: 0px white;">
    <tr>
        <td>
            <a href="./genericsuite-core/">
                <img
                    src="images/gs_logo_circle.svg"
                    title="Generic Suite logo by Carlos J. Ramirez"
                />
            </a>
        </td>
        <td>
            <a href="./genericsuite-ai/">
                <img
                    src="images/gs_ai_logo_circle.svg"
                    title="Generic Suite AI logo by Carlos J. Ramirez"
                />
            </a>
        </td>
    </tr>
</table>

Generic Suite (GS) is the ultimate development library designed to streamline both frontend and backend workflows, enabling rapid app development with AI-powered enhancements. Whether you're building robust APIs, scalable databases, or dynamic user interfaces, GS provides the flexibility and efficiency needed to accelerate your projects.

## Why Choose Generic Suite?

* Seamless Full-Stack Integration – Develop applications faster with a unified library for both frontend and backend, reducing redundant code and ensuring consistency.
* AI-Driven Efficiency – Leverage built-in AI capabilities to enhance automation, generate content, and optimize software development.
* Customizable & Scalable – Adapt the framework to your specific needs, with support for multiple programming frameworks, databases, and deployment platforms.
* Accelerated Development Workflow – Pre-built utilities and automation tools save time, letting you focus on innovation instead of repetitive tasks.
* Cross-Platform Compatibility – Whether you're working with FastAPI, Flask, Chalice, DynamoDB, or MongoDB, GS adapts to your tech stack effortlessly.

## Key Features

### Core Framework

* Customizable CRUD editor, menu generator, and login interface.
* Generic database and API endpoint builder to eliminate redundant coding.
* Backend framework abstraction supporting FastAPI, Flask, and Chalice.
* Database abstraction for MongoDB and DynamoDB with a unified query syntax.
* Easy deployment with AWS and other cloud services.

### AI-Powered Development

* AI chatbot endpoint with OpenAI, LangChain, and Hugging Face integrations.
* Computer vision, speech processing, and text-to-speech capabilities.
* Web scraping, translation tools, and vector search for advanced data handling.

### GSAM (Generic Suite App Maker)

* AI-assisted ideation for app development, code generation, and database structuring.
* Image and video generation using cutting-edge AI models.
* AI-powered app presentations, naming suggestions, and prompt engineering.

### ASDT (Agentic Software Development Team)

* Multi-agent AI collaboration for problem-solving and software automation.
* Built on CrewAI, Camel AI, LangGraph, and Smolagent for scalable agentic workflows.

### Effortless DevOps & Deployment

* Pre-configured GitOps scripts for Kubernetes, Docker, and VPS environments.
* Local AI service setups, including OLLAMA, WebUI, Stable Diffusion, and N8N.
* Comprehensive documentation and best practices via Generic Suite Basecamp.

## Get Started

Join the growing community of developers using Generic Suite to supercharge their projects. Explore the repositories and start building today!

* [Why choose Generic Suite?](#why-choose-generic-suite)
* [Key Features](#key-features)
* [What is the Generic Suite for?](#what-is-the-genericsuite-for)
* [The Generic Suite Core](#the-genericsuite-core)
* [The Generic Suite AI](#the-genericsuite-ai)
* [Sample Code](#sample-code)
* [Repositories](#repositories)
* [Releases](#releases)
* [Presentation](#presentation)
* [Post](#posts)
* [Frontend Development](./Frontend-Development/index.md)
* [Backend Development](./Backend-Development/index.md)
* [Configuration Guide](./Configuration-Guide/index.md)
* [History](./history.md)

## What is the Generic Suite for?

The Generic Suite is a frontend and backend set of utilities made with ReactJS and Python to help develop Apps faster.

It's composed by a **Generic Suite Core**, which is the core for all the suite elements, and extensions like the Generic Suite AI.

<img 
    align="right"
    width="100"
    height="100"
    src="images/gs_logo_circle.svg"
    title="Generic Suite logo by Carlos J. Ramirez"
/>

## The Generic Suite Core

Features:

* Customizable CRUD editor, menu generator, customizable login interface, deploy to AWS and a suite of tools to kickstart your frontend development process.
* Generic CRUD database and API endpoints: by having a core Create-Read-Update-Delete code that can be parametrized & extended, there’s no need to rewrite code for each table editor.
* Generic menu and API endpoints builder.
* Database abstractor: The backend can use DynamoDB or MongoDB as the persistent storage. ImplementS DynamoDB access by a MongoDB-styled syntax.
* Framework abstractor: supports various frameworks including FastAPI, Flask and Chalice, making it adaptable to a range of projects.
* [Utilities](./Backend-Development/GenericSuite-Scripts/index.md), and [Configurations](./Configuration-Guide/index.md) necessary to build and deploy scalable and maintainable applications.

Packages:

* :fontawesome-brands-react:{ .react } [GenericSuite Core (frontend version) for React.js](./Frontend-Development/GenericSuite-Core/index.md)
* :fontawesome-brands-python:{ .python } [GenericSuite Core (backend version) for Python](./Backend-Development/GenericSuite-Core/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (backend version)](./Backend-Development/GenericSuite-Scripts/index.md)

<img 
    align="right"
    width="100"
    height="100"
    src="images/gs_ai_logo_circle.svg"
    title="Generic Suite AI logo by Carlos J. Ramirez"
/>

## The Generic Suite AI

The **Generic Suite AI** is an extension to help develop Apps that implements AI.

Features:

* AI Agent endpoint to implement NLP Chatbot-like conversations.
* OpenAI GPT, Google Gemini, Anthropic Claude, Meta Llama, Hugging Face, xAI, IBM WatsonX, and many other models handling.
* OpenAI API, Google API, Anthropic API, Hugging Face, Together AI, OpenRuter, AI/ML API, Ollama, Clarifai and other LLM providers.
* Computer vision (OpenAI GPT4 Vision, Google Gemini Vision, Clarifai Vision).
* Speech-to-text processing (OpenAI Whisper, Clarifai Audio Models).
* Text-to-speech (OpenAI TTS-1, Clarifai Audio Models).
* Image generator (OpenAI DALL-E 3, Google Gemini Image, Clarifai Image Models).
* Vector indexers (FAISS, Chroma, Clarifai, Vectara, Weaviate, MongoDBAtlasVectorSearch).
* Embeddings (OpenAI, Hugging Face, Bedrock, Cohere, Ollama, Clarifai).
* Web search tool.
* Webpage scrapping and analyzing tool.
* JSON, PDF, Git and YouTube readers.
* Language translation tools.
* Chats stored in the Database.
* User Plan, OpenAI API key and model name attributes in the user profile, to allow free plan users to use Models at their own expense.

Packages:

* :fontawesome-brands-react:{ .react } [GenericSuite AI (frontend version) for React.js](./Frontend-Development/GenericSuite-AI/index.md)
* :fontawesome-brands-python:{ .python } [GenericSuite AI (backend version) for Python](./Backend-Development/GenericSuite-AI/index.md)
* :fontawesome-brands-linux:{ .linux } [GenericSuite Scripts (backend version)](./Backend-Development/GenericSuite-Scripts/index.md)

### GSAM: The Generic Suite AI App Maker

The **Generic Suite App Maker (GSAM)** is the AI tool to enhance the software development ideation and test AI models, LLM providers and its features. It also allows to generate descriptions, database structures, images, videos or answers from a text prompt, and kick start code to be used with the Generic Suite library.

Repository:

* :fontawesome-brands-python:{ .python } [GenericSuite App Maker](https://github.com/tomkat-cr/genericsuite-app-maker)

### AI Agentic Software Development Team

The **Generic Suite Agentic Software Development Team (ASDT)** provides a team of autonomous entities designed to solve software development problems using AI to make decisions, learn from interactions, and adapt to changing conditions without human intervention.

Repository:

* :fontawesome-brands-python:{ .python } [GenericSuite Agentic Software Development Team](https://github.com/tomkat-cr/genericsuite-asdt-be)

### Git and Server Operations

The **Generic Suite Gitops** provides the scripts and configurations needed to deploy on various platforms (local development servers, VPS) using orchestration technologies like Kubernetes, and manage artifacts and repositories with Docker and GitHub.

Repository:

* :fontawesome-brands-linux:{ .linux } [GenericSuite Gitops (Local Development Server operations)](https://github.com/tomkat-cr/genericsuite-gitops)

## Repositories

[Click here](./repositories.md) to review the Git repositories, NPMJS and PyPI packages.

## Documentation

* Main: [https://genericsuite.carlosjramirez.com](https://genericsuite.carlosjramirez.com)
* Mirror: [https://genericsuite.readthedocs.io](https://genericsuite.readthedocs.io)

## Sample Code

We have an [ExampleApp](./Sample-Code/exampleapp/README.md) to show you how to use the GenericSuite libraries.

[![ExampleApp Banner](./Sample-Code/exampleapp/assets/exampleapp_banner_01.png)](./Sample-Code/exampleapp/README.md)    

[ExampleApp](./Sample-Code/exampleapp/README.md) is a full-featured example application built as a monorepo using Turborepo and pnpm. This provides a practical, real-world blueprint for developers to learn from and accelerate their own projects. There are a frontend in React and backends in Python, using the 3 main frameworks: FastAPI, Flask and Chalice.

## Releases

You can find the detailed changelog for each release [here](./Releases/index.md).

## Presentation

English:

* [Introduction to Generic Suite](./documents/GS_Presentation_EN_V2.pdf)

Spanish:

* [Introducción a Generic Suite](./documents/GS_Presentation_SP_V2.pdf)

## Posts

X: [@genericsuitelib](https://twitter.com/genericsuitelib)

English:

* [https://www.carlosjramirez.com/genericsuite](https://www.carlosjramirez.com/genericsuite)

Spanish:

* [https://www.carlosjramirez.com/genericsuite-es/](https://www.carlosjramirez.com/genericsuite-es/)

## License

Generic Suite is open-sourced software licensed under the [ISC](https://github.com/tomkat-cr/genericsuite-basecamp/blob/main/LICENSE) license.

## Credits

This project is developed and maintained by [Carlos J. Ramirez](https://www.carlosjramirez.com). For more information or to contribute to the project, visit [GenericSuite on GitHub](https://github.com/stars/tomkat-cr/lists/genericsuite).

Happy Coding!