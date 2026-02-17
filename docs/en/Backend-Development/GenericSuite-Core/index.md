# The GenericSuite for Python

![gs_logo_circle.png](../../../assets/images/gs_logo_circle.png)

[GenericSuite (backend version)](https://github.com/tomkat-cr/genericsuite-be) is a versatile backend solution, designed to provide a comprehensive suite of features for Python APIs. It supports various frameworks including FastAPI, Flask and Chalice, making it adaptable to a range of projects. This repository contains the backend logic, utilities, and configurations necessary to build and deploy scalable and maintainable applications.

## Features

- **Framework Agnostic**: Supports FastAPI, Flask, and Chalice frameworks.
- **Database Support**: Includes abstracted database operations for MongoDB, DynamoDB, Postgres, MySQL, or Supabase, offering flexibility in choosing the database.
- **Authentication**: Implements JWT-based authentication, providing secure access to endpoints.
- **Dynamic Endpoint Creation**: Allows for defining endpoints dynamically through JSON configurations.
- **Utilities**: A collection of utilities for tasks such as sending emails, parsing multipart data, handling passwords, and more.
- **Billing Utilities**: Tools for managing billing plans and user subscriptions.
- **Menu Options**: Functionality to manage and retrieve authorized menu options based on user roles.

## Pre-requisites

- Python version >= 3.10 and < 4.0 (install with [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) preferably. Versions specified in `.python-version` files)
- [Git](https://www.atlassian.com/git/tutorials/install-git)
- Make: [Mac](https://formulae.brew.sh/formula/make) | [Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
- Node version 20+, installed via [NVM (Node Package Manager)](https://nodejs.org/en/download/package-manager) or [NPM and Node](https://nodejs.org/en/download) install.
- [Docker and Docker Composer](https://www.docker.com/products/docker-desktop)
- [uv](https://docs.astral.sh/uv/getting-started/installation/), [pipenv](https://pipenv.pypa.io/en/latest/), or [poetry](https://python-poetry.org/docs/) (for Python dependency management)

### AWS account and credentials

If you plan to deploy the App in the AWS Cloud, use DynamoDB or RDS for the database:

* AWS account, see [free tier](https://aws.amazon.com/free).
* AWS Token, see [Access Keys](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/security_credentials?section=IAM_credentials).
* AWS Command-line interface, see [awscli](https://formulae.brew.sh/formula/awscli).

### MongoDB

If you plan to use MongoDB for the database:

* Install de python package `pymongo`
* See [Community MongoDB](https://www.mongodb.com/try/download/community) or [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

### Postgres

If you plan to use Postgres for the database:

* Install de python package `psycopg2-binary`
* See [Postgres](https://www.postgresql.org/).

### Supabase

If you plan to use Supabase for the database:

* Install de python package `supabase`
* Go to [Supabase](https://supabase.com/), create an account and a project.

### MySQL

If you plan to use MySQL for the database:

* Install de python package `mysql-connector-python`
* See [MySQL](https://www.mysql.com/).

### MCP Server

If you plan to develop an MCP Server:

* Install python packages `mcp` and `fastmcp`

## Getting Started

To get started with [GenericSuite](../../index.md), follow these steps:

### Initiate your project

To create the project directory for the App's backend API. E.g. `your_app_name_backend` when you want to have separated the backend and frontend code. For a project strture as follows:

```
your_app_name_backend/
└── src/                 # API application
    └── config_dbdef/    # Configuration database definitions
```

Create the project directory for the App's backend API as follows:

```bash
mkdir -p your_app_name_backend/src
cd your_app_name_backend/src
```

For a monorepo (e.g. [exampleapp](../../../code/exampleapp/README.md) and [fastapitemplate](../../../code/fastapitemplate/README.md)), you can have a directory structure as follows:

```
your_app_name/
├── config_dbdef/                 # Configuration database definitions
├── deployment/                   # App deployment files (Docker/Podman)
├── server/                       # Server application
├── ui/                           # User interface
└── mcp-server/                   # MCP server
```

Check the [App Structure](#app-structure) section to have the frontend and backend in differenten repos.

Create the project directory for the App's backend API as follows:

```bash
mkdir -p your_app_name/server
cd your_app_name/server
```

### Dependency manager setup

The following instructions will depend on the dependency management of your preference:

```bash
# Pip
python3 -m venv venv
source venv/bin/activate
```

```bash
# Uv
# https://docs.astral.sh/uv/getting-started
uv init
uv venv
```

```bash
# Poetry
# https://python-poetry.org/docs/basic-usage/
poetry init
```

```bash
# Pipenv
# https://docs.pipenv.org/basics/
pipenv install
pipenv shell
```

## GenericSuite installation

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

Uv
```bash
uv add genericsuite
```

**NOTE**: in the following instructions we'll only show `pip install ...`.<br>
If you'll use `pipenv`, change it with `pipenv install ...`.<br>
If you'll use `poetry`, change it with `poetry add ...`.<br>
If you'll use `uv`, change it with `uv add ...`.<br>

Check [this documentation](../../Other/python-package-managers.md) to use the different Python package and dependency management tools.

### From Git or Local Directory

Check [this documentation](../../Other/installation.md) to install from a Git repository/branch or a Local Directory.


### Framework installation

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

### Development scripts installation

[The GenericSuite backend development scripts](https://github.com/tomkat-cr/genericsuite-be-scripts?tab=readme-ov-file#the-genericsuite-scripts-backend-version) contains utilities to build and deploy APIs made by The GenericSuite.

```bash
npm install -D genericsuite-be-scripts
```

### Database installation

Depending on the database you'll use, install the required dependencies:

#### MongoDB
```bash
pip install pymongo
```

#### DynamoDB
```bash
pip install boto3
```

#### PostgreSQL
```bash
pip install psycopg2-binary
```

#### Supabase
```bash
pip install supabase
```

#### MySQL
```bash
pip install mysql-connector-python
```

### Cloud services

Depending on the cloud service you'll use, install the required dependencies:

#### AWS
```bash
pip install boto3
```

### Test dependencies

To execute the unit and integration test, install `pytest` and `coverage`:

```bash
pip install pytest coverage
```

## Available options

1. **Select Your Framework**: Depending on your project, choose between [FastAPI](https://fastapi.tiangolo.com/), [Flask](https://flask.palletsprojects.com/) or [Chalice](https://aws.github.io/chalice/quickstart.html).
2. **Select Your Database of choice**: Implement database operations using the provided abstracted functions for [MongoDB](https://www.mongodb.com/), [Postgres](https://www.postgresql.org/), [MySQL](https://www.mysql.com/), [Supabase](https://supabase.com/), and [DynamoDB](https://aws.amazon.com/pm/dynamodb/).
3. **Included Authentication**: Your endpoints will be secured with [JWT](https://jwt.io/libraries)-based authentication.
4. **Define Endpoints**: Utilize the dynamic endpoint creation feature by defining your endpoints in a JSON configuration file. Visit the [Generic Suite Configuration Guide](./../../Configuration-Guide/index.md) for more information.
5. **Define Menu Options**: Utilize the dynamic menu creation feature by defining your menu and option access security in a JSON configuration file. Visit the [Generic Suite Configuration Guide](./../../Configuration-Guide/index.md) for guidance.
6. **Define Table structures**: Utilize the dynamic table creation feature by defining your CRUD editors in JSON configuration files. Visit the [Generic Suite Configuration Guide](./../../Configuration-Guide/index.md) for sample code and files.

## Configuration

Configure your application by setting up the necessary environment variables.

Refer to the [.env.example](https://github.com/tomkat-cr/genericsuite-be/blob/main/.env.example) and [config.py](https://github.com/tomkat-cr/genericsuite-be/blob/main/genericsuite/config/config.py) files for the available options.

First copy the `.env.example` template to your `.env` file:

```bash
curl https://raw.githubusercontent.com/tomkat-cr/genericsuite-be/main/.env.example > .env
```

Then, edit the `.env` file to set the desired values:

```bash
vi .env
```

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

* API version (default to "v1")
```env
API_VERSION=v1
```

* Stage and Debug flag
```env
# Application debug APP_DEBUG (0,1)
# Application environment APP_STAGE: dev, qa, staging, prod
# # DEV
APP_DEBUG=1
# APP_STAGE=dev
```
```env
# # QA
APP_DEBUG=1
# APP_STAGE=qa
```
```env
# # PROD
APP_DEBUG=0
# APP_STAGE=prod
```

* Application secret keys
```env
# Application secret key (to be used in password encryption)
APP_SECRET_KEY=xxxx
```

* Application super administrator Email
```env
APP_SUPERADMIN_EMAIL=xxxx
```

* Database configuration

1. For MongoDB<br>
[https://www.mongodb.com/](https://www.mongodb.com/)
```env
# DEV: Docker container
APP_DB_ENGINE_DEV=MONGODB
APP_DB_NAME_DEV=mongo
APP_DB_URI_DEV=mongodb://root:example@app.exampleapp.local:27017/
```
```env
# QA: MongoDB Atlas
APP_DB_ENGINE_QA=MONGODB
APP_DB_NAME_QA=xxxx
APP_DB_URI_QA=mongodb+srv://<user>:<password>@<cluster>.mongodb.net
```
```env
# Staging: MongoDB Atlas
APP_DB_ENGINE_STAGING=MONGODB
APP_DB_NAME_STAGING=xxxx
APP_DB_URI_STAGING=mongodb+srv://<user>:<password>@<cluster>.mongodb.net
```
```env
# PROD: MongoDB Atlas
APP_DB_ENGINE_PROD=MONGODB
APP_DB_NAME_PROD=xxxx
APP_DB_URI_PROD=mongodb+srv://<user>:<password>@<cluster>.mongodb.net
```
```env
# DEMO: MongoDB Atlas
APP_DB_ENGINE_DEMO=MONGODB
APP_DB_NAME_DEMO=xxxx
APP_DB_URI_DEMO=mongodb+srv://<user>:<password>@<cluster>.mongodb.net
```

2. For AWS DynamoDB<br>
[https://console.aws.amazon.com](https://console.aws.amazon.com)
```env
# DEV: docker
APP_DB_ENGINE_DEV=DYNAMODB
DYNAMDB_PREFIX_DEV=
APP_DB_URI_DEV=http://127.0.0.1:8000
```
```env
# QA: AWS DynamoDB
APP_DB_ENGINE_QA=DYNAMODB
DYNAMDB_PREFIX_QA=
APP_DB_URI_QA=
```
```env
# PROD: AWS DynamoDB
APP_DB_ENGINE_PROD=DYNAMODB
DYNAMDB_PREFIX_PROD=
APP_DB_URI_PROD=
```
```env
# # DEMO: AWS DynamoDB
# APP_DB_ENGINE_DEMO=DYNAMODB
# DYNAMDB_PREFIX_DEMO=
# APP_DB_URI_DEMO=
```

**NOTE**: set `DYNAMDB_PREFIX_*` empty and it'll be defaulted to `<APP_NAME_LOWERCASE>_<STAGE>_`.

3. For PostgreSQL<br>
[https://www.postgresql.org/](https://www.postgresql.org/)<br>
[https://www.supabase.com/](https://www.supabase.com/)<br>
[https://console.aws.amazon.com](https://console.aws.amazon.com)
```env
# # DEV: docker
# APP_DB_ENGINE_DEV=POSTGRES
# APP_DB_URI_DEV=postgresql://user:pass@localhost:5432
# APP_DB_NAME_DEV=db

# # QA:
# APP_DB_ENGINE_QA=POSTGRES
# APP_DB_URI_QA=postgresql://user:pass@hostname:5432
# APP_DB_NAME_QA=db

# # PROD:
# APP_DB_ENGINE_PROD=POSTGRES
# APP_DB_URI_PROD=postgresql://user:pass@hostname:5432
# APP_DB_NAME_PROD=db

# # DEMO:
# APP_DB_ENGINE_DEMO=POSTGRES
# APP_DB_URI_DEMO=postgresql://user:pass@hostname:5432
# APP_DB_NAME_DEMO=db
```


4. For Supabase<br>
[https://www.supabase.com/](https://www.supabase.com/)

```env
SUPABASE_KEY=
```

```env
# # DEV: docker
# APP_DB_ENGINE_DEV=SUPABASE
# APP_DB_URI_DEV=https://xxxx.supabase.co
# APP_DB_NAME_DEV=db
#
# # QA:
# APP_DB_ENGINE_QA=SUPABASE
# APP_DB_URI_QA=https://xxxx.supabase.co
# APP_DB_NAME_QA=db
#
# # PROD:
# APP_DB_ENGINE_PROD=SUPABASE
# APP_DB_URI_PROD=https://xxxx.supabase.co
# APP_DB_NAME_PROD=db
#
# # DEMO:
# APP_DB_ENGINE_DEMO=SUPABASE
# APP_DB_URI_DEMO=https://xxxx.supabase.co
# APP_DB_NAME_DEMO=db
```

**NOTES**:
- To configure Supabase with Postgres, form example on the QA environment, set:
```env
APP_DB_ENGINE_QA=POSTGRES
APP_DB_URI_QA=postgresql://postgres:[YOUR_PASSWORD]@db.[SUPABASE_SERVER_SUBDOMAIN].supabase.co:5432
APP_DB_NAME_QA=postgres
```
- `YOUR_PASSWORD` is not the supabase user password, it is a password requested when the Supabase account was created. In case you need to reset that password, go to "Database > Settings > Database password > [Reset database password]".
- `SUPABASE_SERVER_SUBDOMAIN` is the subdomain of the Supabase server. You can find it in the "Supabase Dashboard > Connect > Connection string" option.
- For this to work, you must purchase the **IPv4 add-on** in the Supabase dashboard, otherwise you will get a connection error:
```
Could not translate host name "db.xxxxxx.supabase.co" to address: Name or service not known
```

5. For MySQL<br>
[https://www.mysql.com](https://www.mysql.com)

```env
# # DEV: docker
# APP_DB_ENGINE_DEV=MYSQL
# APP_DB_URI_DEV=mysql://user:pass@localhost:3306
# APP_DB_NAME_DEV=db
#
# # QA:
# APP_DB_ENGINE_QA=MYSQL
# APP_DB_URI_QA=mysql://user:pass@hostname:3306
# APP_DB_NAME_QA=db
#
# # PROD:
# APP_DB_ENGINE_PROD=MYSQL
# APP_DB_URI_PROD=mysql://user:pass@hostname:3306
# APP_DB_NAME_PROD=db
#
# # DEMO:
# APP_DB_ENGINE_DEMO=MYSQL
# APP_DB_URI_DEMO=mysql://user:pass@hostname:3306
# APP_DB_NAME_DEMO=db
```

* CORS Origin
```env
# DEV
APP_CORS_ORIGIN_DEV="*"
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

* Python package and dependency management tool

```env
# Python package and dependency management tool (uv, pipenv, and poetry), default to "uv"
# PEM_TOOL=pipenv
# PEM_TOOL=uv
# PEM_TOOL=poetry
```

* Current framework options: chalice, flask, fastapi
```env
CURRENT_FRAMEWORK=fastapi
# CURRENT_FRAMEWORK=flask
# CURRENT_FRAMEWORK=chalice
```

* Local development environment run configuration
```env
# Options are: uvicorn, gunicorn, chalice, chalice_docker
# FastAPI case:
RUN_METHOD=uvicorn
# Flask case:
# RUN_METHOD=gunicorn
# Chalice case: "chalice" to use http (running without docker) or "chalice_docker" to use https (with docker)
# http:
# RUN_METHOD=chalice
# https:
# RUN_METHOD=chalice_docker
```

* Run methods and framework App directory and entry point
```env
#
# Default App main code directory
# for Chalice:
# https://aws.github.io/chalice/topics/packaging.html
# APP_DIR="."
# for FastAPI:
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=directory+structure#an-example-file-structure
# APP_DIR=app
# for Flask:
# https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/
# APP_DIR=flaskr
#
# Default App entry point code file
# for Chalice:
# https://aws.github.io/chalice/topics/packaging.html
# APP_MAIN_FILE=app
# for FastAPI:
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=directory+structure#an-example-file-structure
# APP_MAIN_FILE=main
# for Flask:
# https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/
# APP_MAIN_FILE="__init__"
#
```

* Local run http/https protocol, to have it automatically on the application local running, no user intervention.
```env
# RUN_PROTOCOL=http
# RUN_PROTOCOL=https
#
# Leave blank to let the user select the protocol when the local dev environment run starts.
# RUN_PROTOCOL=""
```

* Auto-reload configuration: sometimes the auto-reload feature doesn't work correctly, for example running Chalice with Turborepo and the "uv" package manager. In this case, set `AUTO_RELOAD=0` to disable the auto-reload feature and make it work.
```env
# Auto-reload configuration for the local development environment.
# Available options: `1` to enable, `0` to disable, and `-` to remove the auto-reload parameter from the command line. Defaults to: 1
# AUTO_RELOAD=1
# AUTO_RELOAD=0
# AUTO_RELOAD="-"
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
PYTHON_VERSION=3.12
# PYTHON_VERSION=3.11.5
# PYTHON_VERSION=3.10.12
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

* AWS Configuration<br>
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

* Deployment options

```env
# AWS Deployment type
# Available options: `lambda`, `ec2`, `fargate`. Defaults to: lambda
AWS_DEPLOYMENT_TYPE=lambda
```

```env
# AWS Lambda Deployment type
# Available options: `zip`, `container`. Defaults to: zip
AWS_LAMBDA_DEPLOYMENT_TYPE=zip
```

* Storage URL encryption (to mask the AWS S3 bucket name and key)
```env
# Storage URL encryption
#
# Storage URL encryption (default to 0)
# STORAGE_URL_ENCRYPTION=1
#
# Storage seed (to set storage URL encryption -e.g. AWS S3-)
# Generate a new one with: `make generate_seed`
# STORAGE_URL_SEED=yyy
#
# Development URL masking external hostname
#   For features like AI Vision, to send the image URL masked.
#   It's recommended to set only in development environment.
#   E.g. URL_MASK_EXTERNAL_HOSTNAME=app-dev.exampleapp.com
#   Leave blank to use the same URL stored -for example- in the AI Assistant conversarions.
# URL_MASK_EXTERNAL_HOSTNAME=
#
# URL masking external protocol (http or https, defaults to RUN_PROTOCOL or https)
# URL_MASK_EXTERNAL_PROTOCOL=http
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
# Docker account username: used by the docker login command to push images (e.g. when using Kubernetes)
DOCKER_ACCOUNT=docker_account_username
```

* Container engine configuration
```env
# Container engine: used by the docker run command to run the container
# Available options: `docker`, `podman`. Defaults to: docker
# CONTAINERS_ENGINE=docker
# CONTAINERS_ENGINE=podman

# Open containers engine app
# Available options: `1` to enable, `0` to disable. Defaults to: 1
# OPEN_CONTAINERS_ENGINE_APP=1
# OPEN_CONTAINERS_ENGINE_APP=0
```

* Tests configuration
```env
# Backend debug local port
# For http (default)
# BACKEND_DEBUG_LOCAL_PORT=5001
# For https
# WARNING: this port must be different than the BACKEND_LOCAL_PORT, otherwise it will throw
# the "Port already in use" error trying to start the sls-nginx container.
# BACKEND_DEBUG_LOCAL_PORT=5002

# Testing endpoint
# For http
# (defaults to "http://localhost:5001")
# TEST_APP_URL=http://app.exampleapp.local:5001
# For https
# TEST_APP_URL=https://app.exampleapp.local:5002
```

* App local ports
```env
# Local frontend port (defaults to 3000)
FRONTEND_LOCAL_PORT=3000
#
# Local backend API port (defaults to 5001)
BACKEND_LOCAL_PORT=5001
```

* Local self-generated SSL certificate creation method (used when running the local dev environment with https or SLS-Secure Local Server)
```env
# Local self-generated SSL certificate creation method
# (used by "scripts/local_ssl_certs_creation.sh", defaults to "mkcert")
#
# SSL_CERT_GEN_METHOD="mkcert"
# SSL_CERT_GEN_METHOD="office-addin-dev-certs"
# SSL_CERT_GEN_METHOD="openssl"
```

* Disable local services<br>
  (useful when running the local dev environment on the road, offline, over a smartphone internet connection)
```env
# Disable local DNS server startup during app run
LOCAL_DNS_DISABLED=1
# Disable bridge proxy startup during app run
BRIDGE_PROXY_DISABLED=1
```

* Localstack<br>
[https://www.localstack.cloud/](https://www.localstack.cloud/)

```env
# Localstack configuration
# LOCALSTACK_AUTH_TOKEN=""
# (Set LOCALSTACK_AUTH_TOKEN empty when working offline, and assign the Auth Token to make services like EC2 to work correctly)
```

* General parameters file
```env
# Enable/disable general parameters file creation in "/tmp/params_general.json"
# Available options: `1` to enable, `0` to disable. Defaults to: 1
# PARAMS_FILE_ENABLED=0
# PARAMS_FILE_ENABLED=1
```

* User's parameters file
```env
# Enable/disable user's parameters file creation in "/tmp/params_[user_id].json"
# Recommended to enable it in local development environment to make it run faster
# Defaults to "0" to avoid security risks when running in a production environment
# Available options: `1` to enable, `0` to disable.
# USER_PARAMS_FILE_ENABLED=0
# USER_PARAMS_FILE_ENABLED=1
```

* Flask configuration
```env
# Flask app entry point
FLASK_APP=__init__.py
# Flask secret key
FLASK_SECRET_KEY=xxxx
```

## SLS-Secure Local Server

To use resources that only work using the secure socket layer protocol in the browser (e.g. the camera) in the local development environment, the https protocol is required in both the bacjend and frontend servers. There are two options:

1. Using Docker/Podman
2. Using Cloudflare Tunnel

### Using Docker/Podman

With this method, a secure local server is created using local Docker/Podman containers and self-generated SSL certificates.

To implement SLS-Secure Local Server using Docker/Podman, set the following variables in the ".env" files (backend and frontend, or monorepo):

1. `RUN_PROTOCOL="https"` (to turn on https mode)

2. `USE_CONTAINERS_ENGINE_APP=1` (to turn on Docker/Podman completely, so it starts the SLS-Secure Local Server when `RUN_PROTOCOL="https"`)

3. `RUN_PROTOCOL_AND_PORT_REPLACEMENT=1` (to turn on automatic protocol and port replacement for local development environment variables `APP_CORS_ORIGIN` (taken from `APP_CORS_ORIGIN_{STAGE}`), and `REACT_APP_API_URL` (taken from `APP_API_URL_{STAGE}`) depending on `RUN_PROTOCOL` value)

4. Set the following envvars:

* Backend:
  `APP_CORS_ORIGIN_DEV`: the local https hostname for the frontend using local DEV database
  `APP_CORS_ORIGIN_QA_LOCAL`: the local https hostname for the frontend using QA database

* Frontend:
  `APP_API_URL_DEV`: the local https hostname for the backend API
  `APP_FE_URL_DEV`: the local https hostname for the frontend

* Both:
  `APP_NAME`: The name of the app
  `FRONTEND_LOCAL_PORT`: The port of the frontend
  `BACKEND_LOCAL_PORT`: The port of the backend

Example:

For an app called "ExampleApp" and local domain "app.exampleapp.local":

- The frontend hostname will be: `https://app.exampleapp.local:3000`
- The backend API hostname will be: `https://app.exampleapp.local:5000`

There must be an entry in the `/etc/hosts` file for `app.exampleapp.local` pointing to `127.0.0.1`.

```
127.0.0.1      app.exampleapp.local
```

Then the backend and frontend (or monorepo) ".env" files should have the following variables and values:

* Backend:

```env
APP_CORS_ORIGIN_DEV=https://app.exampleapp.local:3000
APP_CORS_ORIGIN_QA_LOCAL=https://app.exampleapp.local:3000
```

* Frontend:

```env
APP_API_URL_DEV=https://app.exampleapp.local:5000
APP_FE_URL_DEV=https://app.exampleapp.local:3000
```

* Both:

```env
APP_NAME="ExampleApp"
FRONTEND_LOCAL_PORT=3000
BACKEND_LOCAL_PORT=5000
RUN_PROTOCOL=https
USE_CONTAINERS_ENGINE_APP=1
RUN_PROTOCOL_AND_PORT_REPLACEMENT=1
```

#### Run the containers and app

Running the app with the following command(s) will automatically start the containers (backend app, nginx and local DNS) and create the SSL self-signed certificates:

```bash
# Monorepoo:
make dev

# Or separate repos:
# make run
# make run_qa
```


### Using Cloudflare Tunnel

Cloudflare Tunnel provides you with a secure way to connect your local resources to Cloudflare without a publicly routable IP address. With Tunnel, you do not send traffic to an external IP — instead, a lightweight daemon in your infrastructure (`cloudflared`) creates outbound-only connections to Cloudflare's global network. Cloudflare Tunnel can connect HTTP web servers, SSH servers, remote desktops, and other protocols safely to Cloudflare. This way, your origins can serve traffic through Cloudflare without being vulnerable to attacks that bypass Cloudflare.

[Official Cloudflare Documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/)

To implement Cloudflare Tunnel, set the following variables in the ".env" files (backend and frontend, or monorepo):

1. `RUN_PROTOCOL="https"` (to turn on https mode)

2. `USE_CONTAINERS_ENGINE_APP=0` (to turn off Docker/Podman completely, so it doesn't start the SLS-Secure Local Server when `RUN_PROTOCOL="https"`)

3. `RUN_PROTOCOL_AND_PORT_REPLACEMENT=0` (to turn off automatic protocol and port replacement for local development environment variables `APP_CORS_ORIGIN` (taken from `APP_CORS_ORIGIN_{STAGE}`), and `REACT_APP_API_URL` (taken from `APP_API_URL_{STAGE}`) depending on `RUN_PROTOCOL` value)

4. Set the following envvars:
  `APP_NAME`: The name of the app
  `FRONTEND_LOCAL_PORT`: The port of the frontend
  `BACKEND_LOCAL_PORT`: The port of the backend
  `CF_HOSTING_DOMAIN`: The domain of the Cloudflare account
  `CF_CONFIG_FILE` (optional): The path to the config file. Default: `${HOME}/.cloudflared/config-${CF_FRONTEND_SUBDOMAIN}.yml`

The subdomains will be:
  `${APP_NAME in lowercase}-dev`
  `${APP_NAME in lowercase}-dev-api`

Example: 

For an app called "ExampleApp" and the Cloudflare domain "exampledomain.com":

- The frontend hostname will be: `https://exampleapp-dev.exampledomain.com`
- The backend API hostname will be: `https://exampleapp-dev-api.exampledomain.com`

The backend and frontend (or monorepo) ".env" files should have the following variables and values:

* Backend:

```env
APP_CORS_ORIGIN_DEV=https://exampleapp-dev.exampledomain.com
APP_CORS_ORIGIN_QA_LOCAL=https://exampleapp-dev.exampledomain.com
CF_HOSTING_DOMAIN=exampledomain.com
```

* Frontend:

```env
APP_API_URL_DEV=https://exampleapp-dev-api.exampledomain.com
APP_FE_URL_DEV=https://exampleapp-dev.exampledomain.com
```

* Both:

```env
APP_NAME="ExampleApp"
FRONTEND_LOCAL_PORT=3000
BACKEND_LOCAL_PORT=5000
RUN_PROTOCOL=https
USE_CONTAINERS_ENGINE_APP=0
RUN_PROTOCOL_AND_PORT_REPLACEMENT=0
```

#### Create the tunnel

To install the `cloudfared` CLI and create the Cloudfare tunnel:
```bash
make cf-tunnel-create
```

#### Run the tunnel and app

To run the Cloudfare tunnel (must be in a different terminal than backend and frontend servers):
```bash
make cf-tunnel-run
```

To stop the Cloudfare tunnel, press `Ctrl-C`.

Then the app can be run locally:

```bash
# Monorepoo:
make dev

# Or separate repos:
# make run
# make run_qa
```

#### Other tunnel commands

To list the installed Cloudfare tunnel:
```bash
make cf-tunnel-list
```

To check the Cloudfare tunnel (it must be running):
```bash
make cf-tunnel-check
```

To remove the Cloudfare tunnel:
```bash
make cf-tunnel-delete
```


## App structure

You can have the frontend and backend in differentent repos or in the same repo.

In case you need to have the frontend and backend in differenten repos, here are some suggested directory structures by framework:

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

## API Specification

The API specification is available in the [FastApiTemplate/server](../../../code/fastapitemplate/server/README.md) directory:

* Swagger JSON: [fastapitemplate-backend_openapi.json](../../../code/fastapitemplate/server/fastapitemplate-backend_openapi.json) 
* Swagger YAML: [fastapitemplate-backend_openapi.yaml](../../../code/fastapitemplate/server/fastapitemplate-backend_openapi.yaml) 

## License

This project is licensed under the ISC License - see the [LICENSE](https://github.com/tomkat-cr/genericsuite-be/blob/main/LICENSE) file for details.

## Credits

This project is developed and maintained by Carlos J. Ramirez. For more information or to contribute to the project, visit [GenericSuite on GitHub](https://github.com/tomkat-cr/genericsuite-be).

Happy Coding!
