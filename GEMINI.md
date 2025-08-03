# Genericsuite Basecamp

This repository is the starting point and documentation for GenericSuite-based project development.

In this repository you will find:

- The [Configuration Guide](./docs/Configuration-Guide/index.md)
- The [Generic CRUD Editor Configuration](./docs/Configuration-Guide/Generic-CRUD-Editor-Configuration.md)
- The [App Frontend](./docs/Frontend-Development/index.md)
- The [App Backend](./docs/Backend-Development/index.md)
- The [Code examples](./docs/Sample-Code/exampleapp/README.md) for your App development.
- The [Releases](./docs/Releases/index.md) of the GenericSuite library.
- The [Basecamp Changelog](./CHANGELOG.md) for the GenericSuite Basecamp repository.
- The [GenericSuite Core](./docs/Backend-Development/GenericSuite-Core/index.md)
- The [GenericSuite AI](./docs/Backend-Development/GenericSuite-AI/index.md)

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
2. **Review the sample code:** The `docs/Sample-Code/` directory provides examples for different backend and frontend frameworks.
3. **Use the scripts:** The `scripts/` directory contains useful scripts for managing the documentation site.

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

- **Development Tools**:

  - pnpm for package management
  - TurboRepo for monorepo management
  - Environment-based configuration

### Running the Example App

The following `make` commands are available to manage the `exampleapp`:

- `make exampleapp-install`: Installs all dependencies for the monorepo.
- `make exampleapp-run`: Starts the application.
- `make exampleapp-update`: Updates the dependencies.
- `make exampleapp-clean`: Removes all installed dependencies and build artifacts.

## Repositories

A full list of GenericSuite repositories can be found in the [docs/repositories.md](docs/repositories.md) file.
