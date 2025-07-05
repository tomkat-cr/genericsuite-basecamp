# The GenericSuite for Python
<img 
    align="right"
    width="100"
    height="100"
    src="../../images/gs_logo_circle.svg"
    title="GenericSuite logo by Carlos J. Ramirez"
/>

[GenericSuite (backend version)](https://github.com/tomkat-cr/genericsuite-be) is a versatile backend solution, designed to provide a comprehensive suite of features for Python APIs. It supports various frameworks including FastAPI, Flask and Chalice, making it adaptable to a range of projects. This repository contains the backend logic, utilities, and configurations necessary to build and deploy scalable and maintainable applications.

## Features

- **Framework Agnostic**: Supports FastAPI, Flask, and Chalice frameworks.
- **Database Support**: Includes abstracted database operations for both MongoDB and DynamoDB, offering flexibility in choosing the database.
- **Authentication**: Implements JWT-based authentication, providing secure access to endpoints.
- **Dynamic Endpoint Creation**: Allows for defining endpoints dynamically through JSON configurations.
- **Utilities**: A collection of utilities for tasks such as sending emails, parsing multipart data, handling passwords, and more.
- **Billing Utilities**: Tools for managing billing plans and user subscriptions.
- **Menu Options**: Functionality to manage and retrieve authorized menu options based on user roles.

## Pre-requisites

- [Python](https://www.python.org/downloads/) >= 3.9 and < 4.0
- [Git](https://www.atlassian.com/git/tutorials/install-git)
- Make: [Mac](https://formulae.brew.sh/formula/make) | [Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
- Node version 18+, installed via [NVM (Node Package Manager)](https://nodejs.org/en/download/package-manager) or [NPM and Node](https://nodejs.org/en/download) install.
* [Docker and Docker Composer](https://www.docker.com/products/docker-desktop)

### AWS account and credentials

If you plan to deploy the App in the AWS Cloud:

* AWS account, see [free tier](https://aws.amazon.com/free).
* AWS Token, see [Access Keys](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/security_credentials?section=IAM_credentials).
* AWS Command-line interface, see [awscli](https://formulae.brew.sh/formula/awscli).
* API Framework and Serverless Deployment, see [Chalice](https://github.com/aws/chalice).

## Getting Started

To get started with [GenericSuite](../../index.md), follow these steps:

### Initiate your project

To create the project directory for the App's backend API. E.g. `exampleapp_backend`, instrctions will depend on the dependency management of your preference:

```bash
# Pip
mkdir -p exampleapp_backend/exampleapp_backend
cd exampleapp_backend
python3 -m venv venv
source venv/bin/activate
```

```bash
# Pipenv
# https://docs.pipenv.org/basics/
mkdir -p exampleapp_backend/exampleapp_backend
cd exampleapp_backend
pipenv install
```

```bash
# Poetry
# https://python-poetry.org/docs/basic-usage/
poetry start exampleapp_backend
cd exampleapp_backend
```

## Installation

To use [GenericSuite](../../index.md) in your project, install it with the following command(s):

### From PyPi

Pip
```bash
pip install genericsuite
```

Pipenv
```bash
pipenv install genericsuite
```

Poetry
```bash
poetry add genericsuite
```

**NOTE**: in the following instructions we'll only show `pip install ...`.<BR/>
If you'll use `Pipenv`, change it with `pipenv install ...`.<BR/>
If you'll use `Poetry`, change it with `poetry add ...`.<BR/>

### From Git or Local Directory

Check [this documentation](../../Other/special-installs.md) to install from a Git repository/branch or a Local Directory.


## Framework installation

Install the desired framework: [FastAPI](https://fastapi.tiangolo.com/), [Flask](https://flask.palletsprojects.com/) or [Chalice](https://aws.github.io/chalice/quickstart.html):

#### FastAPI
```bash
pip install fastapi fastapi-cors "uvicorn[standard]" python-multipart mangum
```

#### Flask
```bash
pip install flask flask_cors gunicorn
```

#### Chalice
```bash
pip install chalice
```

For more information:

* [FastAPI installation](https://fastapi.tiangolo.com/#installation)
* [Flask installation](https://flask.palletsprojects.com/en/2.3.x/installation/)
* [Chalice installation](https://aws.github.io/chalice/quickstart.html)

### Test dependencies

To execute the unit and integration test, install `pytest` and `coverage`:

```bash
pip install pytest coverage
```

### Development scripts installation

[The GenericSuite backend development scripts](https://github.com/tomkat-cr/genericsuite-be-scripts?tab=readme-ov-file#the-genericsuite-scripts-backend-version) contains utilities to build and deploy APIs made by The GenericSuite.

```bash
npm install -D genericsuite-be-scripts
```

## Available options

1. **Select Your Framework**: Depending on your project, choose between [FastAPI](https://fastapi.tiangolo.com/), [Flask](https://flask.palletsprojects.com/) or [Chalice](https://aws.github.io/chalice/quickstart.html).
2. **Select Your Database of choice**: Implement database operations using the provided abstracted functions for [MongoDB](https://www.mongodb.com/) and [DynamoDB](https://aws.amazon.com/pm/dynamodb/).
3. **Included Authentication**: Your endpoints will be secured with [JWT](https://jwt.io/libraries)-based authentication.
4. **Define Endpoints**: Utilize the dynamic endpoint creation feature by defining your endpoints in a JSON configuration file. Visit the [Generic Suite Configuration Guide](https://github.com/tomkat-cr/genericsuite-fe/tree/main/src/configs) for more information.
5. **Define Menu Options**: Utilize the dynamic menu creation feature by defining your menu and option access security in a JSON configuration file. Visit the [Generic Suite Configuration Guide](https://github.com/tomkat-cr/genericsuite-fe/tree/main/src/configs) for guidance.
6. **Define Table structures**: Utilize the dynamic table creation feature by defining your CRUD editors in JSON configuration files. Visit the [Generic Suite Configuration Guide](https://github.com/tomkat-cr/genericsuite-fe/tree/main/src/configs) for sample code and files.

## Configuration

Configure your application by setting up the necessary environment variables. Refer to the [.env.example](https://github.com/tomkat-cr/genericsuite-be/blob/main/.env.example) and [config.py](https://github.com/tomkat-cr/genericsuite-be/blob/main/genericsuite/config/config.py) files for the available options.

* Aplicacion name
```env
APP_NAME=ExampleApp
```

* Aplicacion domain
```env
APP_DOMAIN_NAME=exampleapp.com
```

* Application default language
```env
DEFAULT_LANG=en
```

* Stage and Debug flag
```env
# DEV
# Application debug (0,1)
APP_DEBUG=1
# Application environment: dev, qa, staging, prod
# APP_STAGE=dev
```
```env
# QA
APP_DEBUG=1
# APP_STAGE=qa
```
```env
# PROD
APP_DEBUG=0
# APP_STAGE=prod
```

* Application secret keys
```env
# Application secret key (to be used in password encryption)
APP_SECRET_KEY=xxxx
```
```env
# Storage seed: to be used in storage URL encryption -e.g. AWS S3-
# Generate a new one with: `make generate_seed`
STORAGE_URL_SEED="yyyy"
```

* Application super administrator Email
```env
APP_SUPERADMIN_EMAIL=xxxx
```

* Database configuration

1. For AWS DynamoDB<BR/>
[https://console.aws.amazon.com](https://console.aws.amazon.com)
```env
# DEV: docker
APP_DB_ENGINE_DEV=DYNAMO_DB
DYNAMDB_PREFIX_DEV=
APP_DB_URI_DEV=http://127.0.0.1:8000
```
```env
# QA: AWS DynamoDB
APP_DB_ENGINE_QA=DYNAMO_DB
DYNAMDB_PREFIX_QA=
APP_DB_URI_QA=
```
```env
# PROD: AWS DynamoDB
APP_DB_ENGINE_PROD=DYNAMO_DB
DYNAMDB_PREFIX_PROD=
APP_DB_URI_PROD=
```
```env
# # DEMO: AWS DynamoDB
# APP_DB_ENGINE_DEMO=DYNAMO_DB
# DYNAMDB_PREFIX_DEMO=
# APP_DB_URI_DEMO=
```

**NOTE**: set `DYNAMDB_PREFIX_*` empty and it'll be defaulted to `<APP_NAME_LOWERCASE>_<STAGE>_`.

2. For MongoDB<BR/>
[https://www.mongodb.com/](https://www.mongodb.com/)
```env
# DEV: Docker container
APP_DB_ENGINE_DEV=MONGO_DB
APP_DB_NAME_DEV=mongo
APP_DB_URI_DEV=mongodb://root:example@app.exampleapp.local:27017/
```
```env
# QA: MongoDB Atlas
APP_DB_ENGINE_QA=MONGO_DB
APP_DB_NAME_QA=xxxx
APP_DB_URI_QA=mongodb+srv://<user>:<password>@<cluster>.mongodb.net
```
```env
# Staging: MongoDB Atlas
APP_DB_ENGINE_STAGING=MONGO_DB
APP_DB_NAME_STAGING=xxxx
APP_DB_URI_STAGING=mongodb+srv://<user>:<password>@<cluster>.mongodb.net
```
```env
# PROD: MongoDB Atlas
APP_DB_ENGINE_PROD=MONGO_DB
APP_DB_NAME_PROD=xxxx
APP_DB_URI_PROD=mongodb+srv://<user>:<password>@<cluster>.mongodb.net
```
```env
# DEMO: MongoDB Atlas
APP_DB_ENGINE_DEMO=MONGO_DB
APP_DB_NAME_DEMO=xxxx
APP_DB_URI_DEMO=mongodb+srv://<user>:<password>@<cluster>.mongodb.net
```

* CORS Origin
```env
# DEV
APP_CORS_ORIGIN_DEV=*
```
```env
# QA
APP_CORS_ORIGIN_QA=*
APP_CORS_ORIGIN_QA_CLOUD=https://app-qa.exampleapp.com
APP_CORS_ORIGIN_QA_LOCAL=http://localhost:3000
```
```env
# Staging
APP_CORS_ORIGIN_STAGING=https://app-qa.exampleapp.com
```
```env
# PROD
APP_CORS_ORIGIN_PROD=https://app.exampleapp.com
```
```env
# DEMO
APP_CORS_ORIGIN_DEMO=https://app-demo.exampleapp.com
```

* Current framework options: chalice, flask, fastapi
```env
CURRENT_FRAMEWORK=chalice
```

* JSON configuration files location and git URL
```env
GIT_SUBMODULE_LOCAL_PATH=lib/config_dbdef
GIT_SUBMODULE_URL=git://github.com/username/exampleapp_configs.git
```

* Frontend application path (to copy version file during big lambdas deployment)
```env
FRONTEND_PATH=../exampleapp_frontend
```

* Local python version
```env
PYTHON_VERSION=3.11.5
# PYTHON_VERSION=3.10.12
# PYTHON_VERSION=3.9.17
```

* IAAS Cloud provider
```env
# IAAS Cloud provider
# Available options: `aws`, `gcp`, `azure`
CLOUD_PROVIDER=aws
```

* Enable/disable Cloud Provider secrets
```env
# Enable/disable Cloud Provider secrets (instead of environment variables).
# Available options: `1` to enable, `0` to disable. Defaults to: 1
# GET_SECRETS_ENABLED=0
#
# Fine grained Cloud Provider secrets management:
#
# Enable/disable Cloud Provider envvars.
# Available options: `1` to enable, `0` to disable. Defaults to: 1
# Set to "0" in local development environment so envvars like APP_CORS_ORIGIN can be
# set by the scripts and .env file and access QA resources from DEV.
# GET_SECRETS_ENVVARS=0
#
# Enable/disable Cloud Provider critical secrets.
# Available options: `1` to enable, `0` to disable. Defaults to: 1
# Set to "0" in local development environment so envvars like APP_DB_URI can be
# set by the scripts and .env file and access QA resources from DEV.
# GET_SECRETS_CRITICAL=0
```

* AWS Configuration<BR/>
[https://console.aws.amazon.com](https://console.aws.amazon.com)

```env
# AWS S3 bucket name (used by set_fe_cloudfront_domain.sh to set the CloudFront domain name in the frontend for the CORS config)
AWS_S3_BUCKET_NAME_FE=exampleapp-frontend-website-[STAGE]
```
```env
# Region for this App all AWS services
AWS_REGION=aws-region
```
```env
# AWS base name for Lambda Functions, API Gateway, EC2, ELB, etc.
AWS_LAMBDA_FUNCTION_NAME=exampleapp-backend
```
```env
# AWS Lambda function role:
# These variables are used only if deploy without AWS SAM (deploy_without_sam) in big_lambdas_manager.sh. SAM generates this role automatically
AWS_LAMBDA_FUNCTION_ROLE_QA=exampleapp-api_handler-role-qa
AWS_LAMBDA_FUNCTION_ROLE_STAGING=exampleapp-api_handler-role-staging
AWS_LAMBDA_FUNCTION_ROLE_DEMO=exampleapp-api_handler-role-demo
AWS_LAMBDA_FUNCTION_ROLE_PROD=exampleapp-api_handler-role-prod
```
```env
# AWS SSL certificate ARN (used by big_lambdas_manager.sh)
AWS_SSL_CERTIFICATE_ARN=arn:aws:acm:AWS-REGION:AWS-ACCOUNT:certificate/AWS-CERTIFICATE-UUID
```

```env
# AWS Deployment type
# Available options: `lambda`, `fargate`, `ec2`. Defaults to: lambda
AWS_DEPLOYMENT_TYPE=lambda
```

* Assests URL masking external hostname
```env
# For features like AI Vision, only in development environment, used by the storage URL encryption.
# E.g. app-dev.exampleapp.com
# Leave blank to use the same URL stored, for example in the AI Assistant conversarions.
URL_MASK_EXTERNAL_HOSTNAME=
```

* SMTP Mail configuration
```env
SMTP_SERVER=smtp_server
SMTP_PORT=smtp_port
SMTP_USER=smtp_user
SMTP_PASSWORD=smtp_password
SMTP_DEFAULT_SENDER=sender_email
```

* Docker configuration
```env
DOCKER_ACCOUNT=docker_account_username
```

* Local development environment run configuration
```env
# Options are: uvicorn, gunicorn, chalice, chalice_docker
# RUN_METHOD="uvicorn"
# RUN_METHOD="gunicorn"
# Chalice case: "chalice" to use http (running without docker) or "chalice_docker" to use https (with docker)
# http:
# RUN_METHOD="chalice"
# https:
RUN_METHOD="chalice_docker"
```

* Local run http/https protocol, to have it automatically on the application local running, no user intervention.
```env
# RUN_PROTOCOL="http"
# RUN_PROTOCOL="https"
#
# Leave blank to let the user select the protocol when the local dev environment run starts.
# RUN_PROTOCOL=""
```

* Tests configuration
```env
# Testing endpoint
TEST_APP_URL=http://app.exampleapp.local:5001
```

* Run methods and framework App directory and entry point
```env
#
# Default App main code directory
# for Chalice:
# https://aws.github.io/chalice/topics/packaging.html
# APP_DIR='.'
# for FastAPI:
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=directory+structure#an-example-file-structure
# APP_DIR='app'
# for Flask:
# https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/
# APP_DIR='flaskr'
#
# Default App entry point code file
# for Chalice:
# https://aws.github.io/chalice/topics/packaging.html
# APP_MAIN_FILE='app'
# for FastAPI:
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=directory+structure#an-example-file-structure
# APP_MAIN_FILE='main'
# for Flask:
# https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/
# APP_MAIN_FILE='__init__'
#
```env

* App local ports
```env
# Local frontend port (defaults to 3000)
FRONTEND_LOCAL_PORT=3000
#
# Local backend API port (defaults to 5001)
BACKEND_LOCAL_PORT=5001
```

* Disable local services<BR/>
  (useful when running the local dev environment on the road, offline, over a smartphone internet connection)
```env
# Disable local DNS server startup during app run
LOCAL_DNS_DISABLED=1
# Disable bridge proxy startup during app run
BRIDGE_PROXY_DISABLED=1
```

* Flask configuration
```env
FLASK_APP=__init__.py
```

* Localstack<BR/>
[https://www.localstack.cloud/](https://www.localstack.cloud/)

```env
# Localstack configuration
# LOCALSTACK_AUTH_TOKEN=""
# (Set LOCALSTACK_AUTH_TOKEN empty when working offline, and assign the Auth Token to make services like EC2 to work correctly)
```

## App structure

Suggested directory structure by framework:

* [FastAPI directory structure](https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=directory+structure#an-example-file-structure)
* [Flask directory structure](https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/)
* [Chalice directory structure](https://aws.github.io/chalice/topics/packaging.html)

This is a suggested App development repository structure for a FastAPI project:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
├── logs
│   └── .gitignore
├── .env
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── Makefile
├── Pipfile
├── Pipfile.lock
├── README.md
├── package-lock.json
├── package.json
├── requirements.txt
├── tests
│   ├── .env.for_test
│   ├── __init__.py
│   ├── assets
│   ├── conftest.py
│   └── pytest.ini
└── version.txt
```

This is a suggested App development repository structure for a Flask project:

```
.
├── flaskr/
│   ├── __init__.py
│   ├── items.py
│   ├── users.py
│   ├── admin.py
│   └── index.py
├── logs
│   └── .gitignore
├── package-lock.json
├── package.json
├── requirements.txt
├── tests
│   ├── .env.for_test
│   ├── __init__.py
│   ├── assets
│   ├── conftest.py
│   └── pytest.ini
├── .env
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── Makefile
├── Pipfile
├── Pipfile.lock
├── README.md
└── version.txt
```

This is a suggested App development repository structure for a Chalice project:

```
.
├── .chalice
│   ├── config-example.json
│   ├── config.json
│   ├── deployed
│   │   ├── dev.json
│   │   ├── qa.json
│   │   └── prod.json
│   ├── deployment
│   │   ├── deployment.zip
│   │   └── sam.json
│   ├── deployments
│   ├── dynamodb_cf_template.yaml
│   └── policy-qa.json
├── chalicelib
│   └── endpoints
│       ├── items.py
│       ├── users.py
│       ├── admin.py
│       └── __init__.py
├── lib
│   ├── .gitignore
│   ├── config
│   │   ├── __init__.py
│   │   └── config.py
│   ├── config_dbdef
│   │   ├── .gitignore
│   │   ├── CHANGELOG.md
│   │   ├── README.md
│   │   ├── backend
│   │   └── frontend
│   └── models
│       ├── __init__.py
│       ├── ai_chatbot
│       │   ├── __init__.py
│       │   └── ai_gpt_fn_index.py
│       ├── external_apis
│       │   └── __init__.py
│       └── utilities
├── logs
│   └── .gitignore
├── tests
│   ├── .env.for_test
│   ├── __init__.py
│   ├── assets
│   ├── conftest.py
│   └── pytest.ini
├── .env
├── .env.example
├── .gitignore
├── app.py
├── CHANGELOG.md
├── LICENSE
├── Makefile
├── package-lock.json
├── package.json
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
└── version.txt

```

## Code examples and JSON configuration files

The main menu, API endpoints and CRUD editor configurations are defined in the JSON configuration files.

You can find examples about configurations and how to code an App in the [GenericSuite App Creation and Configuration guide](../../Configuration-Guide/index.md).

## Usage

Check the [The GenericSuite backend development scripts](../GenericSuite-Scripts/index.md) for more details.

## License

This project is licensed under the ISC License - see the [LICENSE](https://github.com/tomkat-cr/genericsuite-be/blob/main/LICENSE) file for details.

## Credits

This project is developed and maintained by Carlos J. Ramirez. For more information or to contribute to the project, visit [GenericSuite on GitHub](https://github.com/tomkat-cr/genericsuite-be).

Happy Coding!
