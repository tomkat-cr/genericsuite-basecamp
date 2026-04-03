# Genericsuite Basecamp

This repository is the starting point and documentation for GenericSuite-based project development.

In this repository you will find:

- The [Main Documentation Page](../docs/en/index.md)
- The [App Frontend](../docs/en/Frontend-Development/index.md)
- The [App Backend](../docs/en/Backend-Development/index.md)
- The [GenericSuite Core](../docs/en/Backend-Development/GenericSuite-Core/index.md)
- The [GenericSuite AI](../docs/en/Backend-Development/GenericSuite-AI/index.md)
- The [Configuration Guide](../docs/en/Configuration-Guide/index.md)
- The [Generic CRUD Editor Configuration](../docs/en/Configuration-Guide/Generic-CRUD-Editor-Configuration.md)
- The Code examples: [ExampleApp monorepo with TurboRepo](../docs/code/exampleapp/README.md) and [FastAPI Template monorepo with NPM Workspaces](../docs/code/fastapitemplate/README.md) for your App development.
- The [Releases](../docs/en/Releases/index.md) of the GenericSuite library.
- The [Basecamp Changelog](../CHANGELOG.md) for the GenericSuite Basecamp repository.

## About GenericSuite

GenericSuite is a collection of packages designed to improve software developer productivity and streamline workflows. It consists of a Core set of tools and several extensions, including an AI-powered extension.

### Key Features

- **Full-Stack Integration:** Unified library for frontend and backend development.
- **AI-Driven Efficiency:** Built-in AI capabilities for automation and content generation.
- **Customizable and Scalable:** Adaptable to various frameworks, databases, and deployment platforms.
- **Accelerated Workflow:** Pre-built utilities and automation tools to save time.
- **Cross-Platform Compatibility:** Supports FastAPI, Flask, Chalice, DynamoDB, and MongoDB.

### Core Components

- **GenericSuite Core:**
  - Customizable CRUD editor, menu generator, and login interface.
  - Generic database and API endpoint builder.
  - Backend framework abstraction (FastAPI, Flask, Chalice).
  - Database abstraction (MongoDB, DynamoDB).
- **GenericSuite AI:**
  - AI chatbot endpoint with integrations for OpenAI, LangChain, and Hugging Face.
  - Computer vision, speech processing, and text-to-speech capabilities.
  - Web scraping, translation tools, and vector search.
- **GSAM (Generic Suite App Maker):**
  - AI-assisted app development, code generation, and database structuring.
- **ASDT (Agentic Software Development Team):**
  - Multi-agent AI collaboration for software automation.
- **GitOps:**
  - Pre-configured scripts for Kubernetes, Docker, and VPS environments.

## Project Structure

The GenericSuite Basecamp project is organized into the following main directories:

- `docs/`: Contains the documentation for the project, including guides for backend and frontend development, configuration, and sample code.
- `scripts/`: Includes various shell scripts for tasks such as installing MkDocs, running the documentation server, and transferring the site.
- `overrides/`: Contains files to override the default MkDocs theme.

## Getting Started

1. **Explore the documentation:** The `docs/` directory contains detailed information about the GenericSuite ecosystem.
2. **Review the sample code:** The `docs/code/` directory provides examples for different backend and frontend frameworks.
3. **Use the scripts:** The `scripts/` directory contains useful scripts for managing the documentation site.
4. **Start the mkdocs local server:** The `scripts/mkdocs_run.sh` script can be used to start the mkdocs local server. You can run it using the `make serve` command to build and serve the documentation or `make run` to only serve the documentation.
5. **Translate from english to other languages:** The `scripts/translation` directory contains the scripts to translate the documentation from english to other languages (e.g. spanish), checking the documents under `docs/en` directory modified after its counterparts under `docs/en` directory. You can run `make translate_uncommitted` script to run the translation process.

## Example Application

GenericSuite Basecamp includes a full-stack `exampleapp` to demonstrate a real-world implementation of the suite's capabilities. This application is structured as a monorepo and showcases how to integrate frontend and backend components efficiently.

**ExampleApp** is a full-stack application to manage food ingredients, recipes, and daily meals, demonstrating a modern web app architecture with multiple backend services and a React-based frontend implementing GenericSuite.

It is inspired by the principles of Caloric Deficit. The purpose is to achieve weight loss goals and maintain a better lifestyle, based on proper nutrition. 

**ExampleApp** let users:

- Record their preferred food ingredients, recipes, and daily meals
- Keep track their calorie consumption
- AI-powered experiences to the users by letting them to communicate by voice, text, or image uploads to a specialized assistant called ExampleApp Bot, which is based on large language models, speech-to-text, text to image and image to text technologies.

### Key Features of the Example App

- **Monorepo Structure:** Managed with **PNPM** and **Turborepo** to streamline package management and build processes.

- **Frontend**: Modern React application with Vite

- **Backend Options**:

  - FastAPI (Python)
  - Flask (Python)
  - Chalice (Python)
  - MCP Server (Python)

- **Database Options**:

  - DynamoDB (AWS)
  - MongoDB (MongoDB Atlas or self-hosted)
  - Postgres (PostgreSQL or AWS RDS)
  - MySQL (MySQL or AWS RDS)
  - Supabase

- **Development Tools**:

  - pnpm for package management
  - TurboRepo for monorepo management
  - Environment-based configuration

### Running the Example App

The following `make` commands are available to manage the `exampleapp`:

- `make exampleapp-install`: Installs all dependencies for the monorepo.
- `make exampleapp-update`: Updates the dependencies.
- `make exampleapp-run`: Starts the application.
- `make exampleapp-clean`: Removes all installed dependencies and build artifacts.

## FastAPI Template Application

GenericSuite Basecamp includes a full-stack `fastapitemplate` to demonstrate a real-world implementation of the suite's capabilities. This application is structured as a monorepo and showcases how to integrate frontend and backend components efficiently.

**FastAPITemplate** is a full-stack application with no specific purpose, demonstrating a modern web app architecture with FastAPI based backend services and a React-based frontend implementing GenericSuite.

**FastAPITemplate** let developers:

- To have a template as a starting point to build their own applications
- Pre-packed AI-powered experiences by letting application users to communicate by voice, text, or image uploads to a specialized assistant called AI Assistant, which is based on large language models, speech-to-text, text to image and image to text technologies.

### Key Features of the FastAPITemplate App

- **Monorepo Structure:** Managed with **NPM Workspaces** to streamline package management and build processes.

- **Frontend**: Modern React application with Vite

- **Backend Options**:

  - FastAPI (Python)
  - MCP Server (Python)

- **Database Options**:

  - DynamoDB (AWS)
  - MongoDB (MongoDB Atlas or self-hosted)
  - Postgres (PostgreSQL or AWS RDS)
  - MySQL (MySQL or AWS RDS)
  - Supabase

- **Development Tools**:

  - npm for package management and monorepo management
  - Environment-based configuration

### Running the FastAPITemplate App

The following `make` commands are available to manage the `fastapitemplate`:

- `make fastapitemplate-install`: Installs dependencies for the monorepo.
- `make fastapitemplate-install-all`: Installs dependencies for all the services in the monorepo.
- `make fastapitemplate-update`: Updates the dependencies.
- `make fastapitemplate-create-ssl-certs`: Creates SSL self-signed certificates for the application.
- `make fastapitemplate-run`: Starts the application.
- `make fastapitemplate-clean`: Removes all installed dependencies and build artifacts.

## Repositories

A full list of GenericSuite repositories can be found in the [docs/repositories.md](../docs/en/repositories.md) file.
