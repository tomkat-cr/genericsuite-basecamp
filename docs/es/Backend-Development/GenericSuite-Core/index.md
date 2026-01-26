# GenericSuite para Python

![gs_logo_circle.png](../../../assets/images/gs_logo_circle.png)

[GenericSuite (versión de backend)](https://github.com/tomkat-cr/genericsuite-be) es una solución de backend versátil, diseñada para proporcionar un conjunto completo de características para APIs de Python. Soporta varios frameworks incluyendo FastAPI, Flask y Chalice, haciéndola adaptable a una variedad de proyectos. Este repositorio contiene la lógica de backend, utilidades y configuraciones necesarias para construir y desplegar aplicaciones escalables y mantenibles.

## Características

- **Independiente del framework**: Soporta FastAPI, Flask y Chalice.
- **Soporte de base de datos**: Incluye operaciones de base de datos abstraídas para MongoDB, DynamoDB, Postgres, MySQL o Supabase, ofreciendo flexibilidad en la elección de la base de datos.
- **Autenticación**: Implementa autenticación basada en JWT, proporcionando acceso seguro a endpoints.
- **Creación dinámica de endpoints**: Permite definir endpoints de forma dinámica mediante configuraciones en JSON.
- **Utilidades**: Una colección de utilidades para tareas como enviar correos, analizar datos multipart, manejar contraseñas, y más.
- **Utilidades de facturación**: Herramientas para gestionar planes de facturación y suscripciones de usuarios.
- **Opciones de menú**: Funcionalidad para gestionar y recuperar opciones de menú autorizadas según roles de usuario.

## Requisitos previos

- Versión de Python >= 3.10 y < 4.0 (instalar con [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) preferiblemente. Las versiones se especifican en los archivos `.python-version`)
- [Git](https://www.atlassian.com/git/tutorials/install-git)
- Make: [Mac](https://formulae.brew.sh/formula/make) | [Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
- Node version 20+, instalado vía [NVM (Node Package Manager)](https://nodejs.org/en/download/package-manager) o [NPM y Node](https://nodejs.org/en/download) instalación.
- [Docker y Docker Composer](https://www.docker.com/products/docker-desktop)
- [uv](https://docs.astral.sh/uv/getting-started/installation/), [pipenv](https://pipenv.pypa.io/en/latest/), o [poetry](https://python-poetry.org/docs/) (para la gestión de dependencias de Python)

### Cuenta de AWS y credenciales

Si planeas desplegar la App en la nube de AWS, usa DynamoDB o RDS para la base de datos:

* Cuenta de AWS, ver [nivel gratuito](https://aws.amazon.com/free).
* Token de AWS, ver [Claves de acceso](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/security_credentials?section=IAM_credentials).
* Interfaz de línea de comandos de AWS, ver [AWS CLI](https://formulae.brew.sh/formula/awscli).

### MongoDB

Si planeas usar MongoDB para la base de datos:

* Instalar el paquete de Python `pymongo`
* Ver [MongoDB Comunidad](https://www.mongodb.com/try/download/community) o [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

### Postgres

Si planeas usar Postgres para la base de datos:

* Instalar el paquete de Python `psycopg2-binary`
* Ver [PostgreSQL](https://www.postgresql.org/).

### Supabase

Si planeas usar Supabase para la base de datos:

* Instalar el paquete de Python `supabase`
* Ir a [Supabase](https://www.supabase.com/), crear una cuenta y un proyecto.

### MySQL

Si planeas usar MySQL para la base de datos:

* Instalar el paquete de Python `mysql-connector-python`
* Ver [MySQL](https://www.mysql.com/).

### MCP Server

Si planeas desarrollar un MCP Server:

* Instalar paquetes de Python `mcp` y `fastmcp`

## Cómo empezar

Para empezar con [GenericSuite](../../index.md), sigue estos pasos:

### Iniciar tu proyecto

Para crear el directorio del proyecto para la API de backend de la App. Por ejemplo, `your_app_name_backend` cuando quieras separar el backend y el frontend. Para una estructura de proyecto como la siguiente:

```
your_app_name_backend/
└── src/                 # API application
    └── config_dbdef/    # Configuration database definitions
```

Crea el directorio del proyecto para la API de backend de la App como sigue:

```bash
mkdir -p your_app_name_backend/src
cd your_app_name_backend/src
```

Para un monorepo (p. ej. [exampleapp](../../../code/exampleapp/README.md) y [fastapitemplate](../../../code/fastapitemplate/README.md)), puedes tener una estructura de directorios como la siguiente:

```
your_app_name/
├── config_dbdef/                 # Configuration database definitions
├── server/                       # Server application
├── ui/                           # User interface
└── mcp-server/                   # MCP server
```

Crea el directorio del proyecto para la API de backend de la App como sigue:

```bash
mkdir -p your_app_name/server
cd your_app_name/server
```

### Configuración del gestor de dependencias

Las siguientes instrucciones dependerán de la gestión de dependencias de tu preferencia:

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

## Instalación de GenericSuite

Para usar [GenericSuite](../../index.md) en tu proyecto, instálalo con los siguientes comandos:

### Desde PyPi

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

**NOTA**: en las siguientes instrucciones solo mostraremos `pip install ...`.<br>
Si usarás `pipenv`, cámbialo por `pipenv install ...`.<br>
Si usarás `poetry`, cámbialo por `poetry add ...`.<br>
Si usarás `uv`, cámbialo por `uv add ...`.<br>

Consulta [esta documentación](../../Other/python-package-managers.md) para usar las distintas herramientas de gestión de paquetes y dependencias de Python.

### Desde Git o Directorio Local

Consulta [esta documentación](../../Other/installation.md) para instalar desde un repositorio/branch de Git o desde un Directorio Local.


### Instalación del framework

Instala el framework deseado: [FastAPI](https://fastapi.tiangolo.com/), [Flask](https://flask.palletsprojects.com/) o [Chalice](https://aws.github.io/chalice/quickstart.html):

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

Para más información:

* [Instalación de FastAPI](https://fastapi.tiangolo.com/#installation)
* [Instalación de Flask](https://flask.palletsprojects.com/en/2.3.x/installation/)
* [Instalación de Chalice](https://aws.github.io/chalice/quickstart.html)

### Instalación de scripts de desarrollo

[Los scripts de desarrollo del backend de GenericSuite](https://github.com/tomkat-cr/genericsuite-be-scripts?tab=readme-ov-file#the-genericsuite-scripts-backend-version) contienen utilidades para construir y desplegar APIs creadas por The GenericSuite.

```bash
npm install -D genericsuite-be-scripts
```

### Instalación de la base de datos

Dependiendo de la base de datos que uses, instala las dependencias requeridas:

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

### Servicios en la nube

Dependiendo del servicio de nube que uses, instala las dependencias requeridas:

#### AWS
```bash
pip install boto3
```

### Dependencias de pruebas

Para ejecutar las pruebas unitarias e de integración, instala `pytest` y `coverage`:

```bash
pip install pytest coverage
```

## Opciones disponibles

1. **Selecciona tu Framework**: Dependiendo de tu proyecto, elige entre [FastAPI](https://fastapi.tiangolo.com/), [Flask](https://flask.palletsprojects.com/) o [Chalice](https://aws.github.io/chalice/quickstart.html).
2. **Selecciona tu base de datos**: Implementa operaciones de base de datos usando las funciones abstraídas proporcionadas para [MongoDB](https://www.mongodb.com/), [Postgres](https://www.postgresql.org/), [MySQL](https://www.mysql.com/), [Supabase](https://supabase.com/), y [DynamoDB](https://aws.amazon.com/pm/dynamodb/).
3. **Autenticación incluida**: Tus endpoints estarán asegurados con autenticación basada en [JWT](https://jwt.io/libraries).
4. **Define Endpoints**: Utiliza la característica de creación dinámica de endpoints definiendo tus endpoints en un archivo de configuración JSON. Consulta la [Guía de Configuración de Generic Suite](./../../Configuration-Guide/index.md) para más información.
5. **Define Opciones de Menú**: Utiliza la característica de creación dinámica de menús definiendo tu menú y el acceso a opciones en un archivo de configuración JSON. Consulta la [Guía de Configuración de Generic Suite](./../../Configuration-Guide/index.md) para orientación.
6. **Define estructuras de tablas**: Utiliza la característica de creación dinámica de tablas definiendo tus editores CRUD en archivos de configuración JSON. Consulta la [Guía de Configuración de Generic Suite](./../../Configuration-Guide/index.md) para código de ejemplo y archivos.

## Configuración

Configura tu aplicación configurando las variables de entorno necesarias. Consulta los archivos [.env.example](https://github.com/tomkat-cr/genericsuite-be/blob/main/.env.example) y [config.py](https://github.com/tomkat-cr/genericsuite-be/blob/main/genericsuite/config/config.py) para las opciones disponibles.

* Nombre de la aplicación
```env
APP_NAME=ExampleApp
```

* Dominio de la aplicación
```env
APP_DOMAIN_NAME=exampleapp.com
```

* Idioma predeterminado de la aplicación
```env
DEFAULT_LANG=en
```

* Versión de la API (predeterminada a "v1")
```env
API_VERSION=v1
```

* Bandera de Stage y Debug
```env
# Aplicación en modo debug APP_DEBUG (0,1)
# Entorno de la aplicación APP_STAGE: dev, qa, staging, prod
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

* Claves secretas de la aplicación
```env
# Application secret key (to be used in password encryption)
APP_SECRET_KEY=xxxx
```

* Correo electrónico del superadministrador de la aplicación
```env
APP_SUPERADMIN_EMAIL=xxxx
```

* Configuración de la base de datos

1. Para MongoDB<br>
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

2. Para AWS DynamoDB<br>
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

**NOTA**: pon `DYNAMDB_PREFIX_*` vacío y se dejará por defecto a `<NOMBRE_APP_MINÚSCULAS>_<ETAPA>`.

3. Para PostgreSQL<br>
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

4. Para Supabase<br>
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

**NOTAS**:
- Para configurar Supabase con Postgres, como ejemplo en el entorno QA, establece:
```env
APP_DB_ENGINE_QA=POSTGRES
APP_DB_URI_QA=postgresql://postgres:[YOUR_PASSWORD]@db.[SUPABASE_SERVER_SUBDOMAIN].supabase.co:5432
APP_DB_NAME_QA=postgres
```
- `YOUR_PASSWORD` no es la contraseña del usuario de Supabase, es una contraseña solicitada cuando se creó la cuenta de Supabase. Si necesitas restablecerla, ve a "Base de datos > Configuración > Contraseña de base de datos > [Restablecer contraseña de base de datos]".
- `SUPABASE_SERVER_SUBDOMAIN` es el subdominio del servidor Supabase. Puedes encontrarlo en la opción "Panel de Supabase > Conectar > Cadena de conexión".
- Para que esto funcione, debes adquirir el complemento **IPv4** en el panel de Supabase; de lo contrario recibirás un error de conexión:
```
Could not translate host name "db.xxxxxx.supabase.co" to address: Name or service not known
```

5. Para MySQL<br>
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

* Origen CORS
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

* Herramienta de gestión de paquetes y dependencias de Python (uv, pipenv y poetry), por defecto a "uv"
```env
# Python package and dependency management tool (uv, pipenv, and poetry), default to "uv"
# PEM_TOOL=pipenv
# PEM_TOOL=uv
# PEM_TOOL=poetry
```

* Opciones actuales de framework: chalice, flask, fastapi
```env
CURRENT_FRAMEWORK=fastapi
# CURRENT_FRAMEWORK=flask
# CURRENT_FRAMEWORK=chalice
```

* Configuración de ejecución del entorno de desarrollo local
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

* Métodos de ejecución y directorio de la App y punto de entrada
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

* Protocolo de ejecución local http/https para que aparezca automáticamente en la ejecución local de la aplicación, sin intervención del usuario.
```env
# RUN_PROTOCOL=http
# RUN_PROTOCOL=https
#
# Deja vacío para permitir que el usuario seleccione el protocolo cuando inicie el entorno de desarrollo local.
# RUN_PROTOCOL=""
```

* Configuración de recarga automática: a veces la característica de recarga automática no funciona correctamente, por ejemplo al ejecutar Chalice con Turborepo y la gestión de paquetes "uv". En este caso, pon `AUTO_RELOAD=0` para deshabilitar la recarga automática y hacer que funcione.
```env
# Configuración de recarga automática para el entorno de desarrollo local.
# Opciones disponibles: `1` para habilitar, `0` para deshabilitar, y `-` para eliminar el parámetro de recarga de la línea de comandos. Por defecto es: 1
# AUTO_RELOAD=1
# AUTO_RELOAD=0
# AUTO_RELOAD="-"
```

* Ubicación de archivos de configuración JSON y URL de git
```env
GIT_SUBMODULE_LOCAL_PATH=lib/config_dbdef
GIT_SUBMODULE_URL=git://github.com/username/exampleapp_configs.git
```

* Ruta de la aplicación frontend (para copiar el archivo de versión durante el despliegue de grandes lambdas)
```env
FRONTEND_PATH=../exampleapp_frontend
```

* Versión local de Python
```env
PYTHON_VERSION=3.12
# PYTHON_VERSION=3.11.5
# PYTHON_VERSION=3.10.12
```

* Proveedor de nube IAAS
```env
# IAAS Cloud provider
# Available options: `aws`, `gcp`, `azure`
CLOUD_PROVIDER=aws
```

* Habilitar/deshabilitar secretos del Proveedor de Nube (en lugar de variables de entorno).
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

* Configuración de correo SMTP
```env
SMTP_SERVER=smtp_server
SMTP_PORT=smtp_port
SMTP_USER=smtp_user
SMTP_PASSWORD=smtp_password
SMTP_DEFAULT_SENDER=sender_email
```

* Configuración de Docker
```env
# Docker account username: used by the docker login command to push images (e.g. when using Kubernetes)
DOCKER_ACCOUNT=docker_account_username
```

* Configuración del motor de contenedores
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

* Configuración de pruebas
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

* Puertos locales de la App
```env
# Local frontend port (defaults to 3000)
FRONTEND_LOCAL_PORT=3000
#
# Local backend API port (defaults to 5001)
BACKEND_LOCAL_PORT=5001
```

* Método de creación de certificado SSL auto-generado local (utilizado cuando se ejecuta el entorno de desarrollo local con https)
```env
# Local self-generated SSL certificate creation method
# (used by "scripts/local_ssl_certs_creation.sh", defaults to "mkcert")
#
# SSL_CERT_GEN_METHOD="mkcert"
# SSL_CERT_GEN_METHOD="office-addin-dev-certs"
# SSL_CERT_GEN_METHOD="openssl"
```

* Desactivar servicios locales
  (útil cuando se ejecuta el entorno de desarrollo local en la carretera, sin conexión, mediante la internet de un teléfono)
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

* Archivo de parámetros general
```env
# Enable/disable general parameters file creation in "/tmp/params_general.json"
# Available options: `1` to enable, `0` to disable. Defaults to: 1
# PARAMS_FILE_ENABLED=0
# PARAMS_FILE_ENABLED=1
```

* Archivo de parámetros del usuario
```env
# Enable/disable user's parameters file creation in "/tmp/params_[user_id].json"
# Recommended to enable it in local development environment to make it run faster
# Defaults to "0" to avoid security risks when running in a production environment
# Available options: `1` to enable, `0` to disable.
# USER_PARAMS_FILE_ENABLED=0
# USER_PARAMS_FILE_ENABLED=1
```

* Configuración de Flask
```env
# Flask app entry point
FLASK_APP=__init__.py
# Flask secret key
FLASK_SECRET_KEY=xxxx
```

## Estructura de la App

Estructura de directorios sugerida por framework:

* [Estructura de directorio de FastAPI](https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=directory+structure#an-example-file-structure)
* [Estructura de directorio de Flask](https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/)
* [Estructura de directorio de Chalice](https://aws.github.io/chalice/topics/packaging.html)

Este es un repositorio de desarrollo de la App sugerido para un proyecto FastAPI:

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

Este es un repositorio de desarrollo de la App sugerido para un proyecto Flask:

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

Este es un repositorio de desarrollo de la App sugerido para un proyecto Chalice:

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
│       ├── admin.py
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

## Ejemplos de código y archivos de configuración JSON

El menú principal, los endpoints de la API y las configuraciones del editor CRUD se definen en los archivos de configuración JSON.

Puedes encontrar ejemplos sobre configuraciones y cómo codificar una App en la [Guía de Creación y Configuración de GenericSuite](../../Configuration-Guide/index.md).

## Uso

Consulta los [Scripts de desarrollo del backend de GenericSuite](../GenericSuite-Scripts/index.md) para más detalles.

## Especificación de la API

La especificación de la API está disponible en el directorio [FastApiTemplate/server](../../../code/fastapitemplate/server/README.md):

* JSON Swagger: [fastapitemplate-backend_openapi.json](../../../code/fastapitemplate/server/fastapitemplate-backend_openapi.json)
* YAML Swagger: [fastapitemplate-backend_openapi.yaml](../../../code/fastapitemplate/server/fastapitemplate-backend_openapi.yaml)

## Licencia

Este proyecto está licenciado bajo la Licencia ISC - vea el archivo [LICENSE](https://github.com/tomkat-cr/genericsuite-be/blob/main/LICENSE) para más detalles.

## Créditos

Este proyecto es desarrollado y mantenido por Carlos J. Ramirez. Para más información o para contribuir al proyecto, visita [GenericSuite en GitHub](https://github.com/tomkat-cr/genericsuite-be).

¡Feliz codificación!