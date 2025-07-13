# GenericSuite Example Application

![ExampleApp Banner](./assets/exampleapp_banner_01.png)

**ExampleApp** is a full-stack example application demonstrating a modern webapp architecture with multiple backend services and a React-based frontend implementing GenericSuite.

It is inspired by the principles of Caloric Deficit. The purpose is to achieve weight loss goals and maintain a better lifestyle, based on proper nutrition. 

**ExampleApp** let users:

- Record their preferred food ingredients, recipes, and daily meals
- Keep track their calorie consumption
- AI-powered experiences to the users by letting them to communicate by voice, text, or image uploads to a specialized assistant called ExampleApp Bot, which is based on large language models, speech-to-text, text to image and image to text technologies.

You can view the [Source Code here](https://github.com/tomkat-cr/genericsuite-basecamp/tree/main/docs/Sample-Code/exampleapp).

The application is structured as a monorepo using [TurboRepo](https://turborepo.com/docs) and [pnpm](https://pnpm.io).

## 🚀 Features

- **Frontend**: Modern React application with Vite

- **Backend Options**:

  - FastAPI (Python)
  - Flask (Python)
  - Chalice (Python)

- **Development Tools**:

  - pnpm for package management
  - TurboRepo for monorepo management
  - Environment-based configuration

## 🛠️ Prerequisites

### Software
- [Git](https://www.atlassian.com/git/tutorials/install-git)
- Node version 20+, installed via [NVM (Node Package Manager)](https://nodejs.org/en/download/package-manager) or [NPM and Node](https://nodejs.org/en/download) install (version specified in `.nvmrc`).
- [pnpm](https://pnpm.io/installation) (version 10.12.4 or compatible)
- [Python](https://www.python.org/downloads/) >= 3.9 and < 4.0 (version specified in `.python-version`)
- [Pipenv](https://pipenv.pypa.io/en/latest/) (for Python dependency management)
- Make: [Mac](https://formulae.brew.sh/formula/make) | [Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)

### Services

#### Database

If you plan to use MongoDB:

* MongoDB Atlas account, see [free tier](https://www.mongodb.com/cloud/atlas/register).
* MongoDB community, see [self-hosted MongoDB](https://www.mongodb.com/try/download/community).

#### AWS account and credentials

If you plan to deploy the App in the AWS Cloud and/or use DynamoDB:

* AWS account, see [free tier](https://aws.amazon.com/free).
* AWS Token, see [Access Keys](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/security_credentials?section=IAM_credentials).
* AWS Command-line interface, see [awscli](https://formulae.brew.sh/formula/awscli).
* API Framework and Serverless Deployment, see [Chalice](https://github.com/aws/chalice).

## 🚀 Getting Started

### Installation

1. Clone the repository:

```bash
git clone https://github.com/tomkat-cr/genericsuite-basecamp.git
cd genericsuite-basecamp
```

2. Install dependencies:

```bash
# Install pnpm if not already installed
npm install -g pnpm
```

### Configuration

1. Copy environment files:

```bash
# Automatically copy environment files
make exampleapp-init-env-files

# Manually copy environment files
# cp apps/ui/.env.example apps/ui/.env
# cp apps/api-fastapi/.env.example apps/api-fastapi/.env
# Repeat for other services as needed (api-flask, api-chalice)
```

2. Update the environment variables in each `.env` file according to your setup.

    * [ui configuration](../../Frontend-Development/index.md).
    * [api core configuration](../../Backend-Development/GenericSuite-Core/index.md#configuration).
    * [api AI configuration](../../Backend-Development/GenericSuite-AI/index.md#configuration).

3. To select the backend implementation (FastAPI, Flask, Chalice), in the `apps/ui/.env` file set the `BACKEND_LOCAL_PORT` variable to the port of the API you want to use.

```bash
# Chalice API
BACKEND_LOCAL_PORT=5001
# FastAPI API
# BACKEND_LOCAL_PORT=5011
# Flask API
# BACKEND_LOCAL_PORT=5021
```

**Note:** Once changed the `BACKEND_LOCAL_PORT` variable, press Ctrl-C to stop the development servers and run `make exampleapp-run` again.

4. Use **https**: by default the application will use http (non-secure), if you want to use https:
    - Set the `RUN_PROTOCOL` variable to `https` in the `apps/ui/.env`, `apps/api-fastapi/.env`, `apps/api-flask/.env`, `apps/api-chalice/.env` files.
    - Generate a self-signed certificate and keys (only once):

```bash
make exampleapp-create-ssl-certs
```
    
**Note:** Once changed the `RUN_PROTOCOL` variable, press Ctrl-C to stop the development servers and run `make exampleapp-run` again.

5. Use "webpack": by default the application will use "vite", if you want to use "webpack":
    - Uncomment the line `RUN_METHOD="webpack"` in the `apps/ui/.env`.
    
**Note:** Once changed the `RUN_METHOD` variable, press Ctrl-C to stop the development servers and run `make exampleapp-run` again.

## 🏃‍♂️ Running the Application

### Development Mode

Start the development servers:

```bash
make exampleapp-run
```

### Start a new GenericSuite project

In the following instructions, we will create a new GenericSuite project using the GenericSuite Basecamp repository as a template. Let's say we want to create a new project called "myapp" and the base directory is "~/dev".

1. Start a new project directory. E.g. "myapp":

```bash
mkdir ~/dev/myapp
cd ~/dev/myapp
git init
npm init -y
# or pnpm init -y
```

2. Clone the GenericSuite Basecamp repository:

```bash
cd ~/dev
git clone https://github.com/tomkat-cr/genericsuite-basecamp.git
cd genericsuite-basecamp
```

3. Copy the sample app:

```bash
cp -r genericsuite-basecamp/docs/Sample-Code/exampleapp ~/dev/myapp
```

4. Install dependencies:

```bash
cd ~/dev/myapp
make install
```

5. Configure the environment variables following the instructions in the [Configuration](#configuration) section.

6. Run the application:

```bash
make run
```

<!--

### Building for Production

```bash
# Build all applications
pnpm build

# Or build a specific application
cd apps/ui
pnpm build
```

-->

## 📂 Project Structure

The `exampleapp` directory is located in the Basecamp `docs/Sample-Code` directory. It contains the following structure:
```
exampleapp/
├── apps/
│   ├── api-chalice/      # AWS Chalice backend API
│   ├── api-fastapi/      # FastAPI backend API
│   ├── api-flask/        # Flask backend API
│   ├── config_dbdef/     # Database configuration
│   └── ui/               # React frontend application
├── packages/             # Shared packages
├── scripts/              # Utility scripts
├── .gitignore
├── package.json
├── pnpm-lock.yaml
└── turbo.json
```

## 🤝 Contributing

1. Fork the [GenericSuite Basecamp](https://github.com/tomkat-cr/genericsuite-basecamp) repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the terms of the [MIT](./LICENSE) license.

## 👏 Acknowledgements

- [GenericSuite](https://genericsuite.carlosjramirez.com) - Core framework
- [React](https://react.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Flask](https://flask.palletsprojects.com/)
- [Chalice](https://aws.github.io/chalice)
- [Vite](https://vite.dev/)
- [TurboRepo](https://turborepo.com/docs)

## Credits

This project is developed and maintained by [Carlos J. Ramirez](https://www.carlosjramirez.com). For more information or to contribute to the project, visit [GenericSuite on GitHub](https://github.com/tomkat-cr/genericsuite-basecamp).

Happy Coding!