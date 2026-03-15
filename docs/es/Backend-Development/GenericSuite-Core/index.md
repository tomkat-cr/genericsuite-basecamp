# El GenericSuite para Python

![gs_logo_circle.png](../../../assets/images/gs_logo_circle.png)

[GenericSuite (versión de backend)](https://github.com/tomkat-cr/genericsuite-be) es una solución de backend versátil, diseñada para proporcionar un conjunto completo de características para APIs de Python. Soporta varios frameworks, incluyendo FastAPI, Flask y Chalice, haciéndola adaptable a una variedad de proyectos. Este repositorio contiene la lógica de backend, utilidades y configuraciones necesarias para construir e implementar aplicaciones escalables y mantenibles.

## Características

- **Independiente del framework**: Soporta los frameworks FastAPI, Flask y Chalice.
- **Soporte de base de datos**: Incluye operaciones de base de datos abstractas para MongoDB, DynamoDB, Postgres, MySQL o Supabase, ofreciendo flexibilidad al elegir la base de datos.
- **Autenticación**: Implementa autenticación basada en JWT, proporcionando acceso seguro a los endpoints.
- **Creación dinámica de endpoints**: Permite definir endpoints dinámicamente mediante configuraciones JSON.
- **Utilidades**: Colección de utilidades para tareas como enviar correos electrónicos, analizar datos multipart, manejar contraseñas y más.
- **Utilidades de facturación**: Herramientas para gestionar planes de facturación y suscripciones de usuarios.
- **Opciones de menú**: Funcionalidad para gestionar y recuperar opciones de menú autorizadas según los roles de usuario.

## Requisitos previos

- Versión de Python >= 3.10 y < 4.0 (instalar preferentemente con [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation); las versiones se especifican en los archivos `.python-version`)
- [Git](https://www.atlassian.com/git/tutorials/install-git)
- Make: [Mac](https://formulae.brew.sh/formula/make) | [Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
- Versión de Node 20+, instalada vía [NVM (Node Package Manager)](https://nodejs.org/en/download/package-manager) o [NPM y Node](https://nodejs.org/en/download)
- [Docker y Docker Composer](https://www.docker.com/products/docker-desktop)
- [uv](https://docs.astral.sh/uv/getting-started/installation/), [pipenv](https://pipenv.pypa.io/en/latest/), o [poetry](https://python-poetry.org/docs/) (para la gestión de dependencias de Python)

### Cuenta de AWS y credenciales

Si planeas desplegar la App en la Nube de AWS, usa DynamoDB o RDS para la base de datos:

* Cuenta de AWS, ver [nivel gratuito](https://aws.amazon.com/free).
* Token de AWS, ver [Claves de acceso](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/security_credentials?section=IAM_credentials).
* Interfaz de línea de comandos de AWS, ver [awscli](https://formulae.brew.sh/formula/awscli).

### MongoDB

Si planeas usar MongoDB para la base de datos:

* Instala el paquete de Python `pymongo`
* Ver [Community MongoDB](https://www.mongodb.com/try/download/community) o [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

### PostgreSQL

Si planeas usar PostgreSQL para la base de datos:

* Instala el paquete de Python `psycopg2-binary`
* Ver [PostgreSQL](https://www.postgresql.org/).

### Supabase

Si planeas usar Supabase para la base de datos:

* Instala el paquete de Python `supabase`
* Ve a [Supabase](https://supabase.com/), crea una cuenta y un proyecto.

### MySQL

Si planeas usar MySQL para la base de datos:

* Instala el paquete de Python `mysql-connector-python`
* Ver [MySQL](https://www.mysql.com/).

### MCP Server

Si planeas desarrollar un MCP Server:

* Instala los paquetes Python `mcp` y `fastmcp`

## Empezar

Para empezar con [GenericSuite](../../index.md), sigue estos pasos:

### Inicia tu proyecto

Para crear el directorio del proyecto para la API backend de la App. Por ejemplo, `your_app_name_backend` cuando quieras tener separadas las code del backend y del frontend. Para una estructura de proyecto como la siguiente:

```
your_app_name_backend/
└── src/                 # API application
    └── config_dbdef/    # Configuration database definitions
```

Crea el directorio del proyecto para la API del backend de la App de la siguiente manera:

```bash
mkdir -p your_app_name_backend/src
cd your_app_name_backend/src
```

Para un monorepo (p. ej. [exampleapp](../../../code/exampleapp/README.md) y [fastapitemplate](../../../code/fastapitemplate/README.md)), puede tener una estructura de directorios como la siguiente:

```
your_app_name/
├── config_dbdef/                 # Configuration database definitions
├── deployment/                   # App deployment files (Docker/Podman)
├── server/                       # Server application
├── ui/                           # User interface
└── mcp-server/                   # MCP server
```

Consulta la sección App Structure para tener el frontend y el backend en repos separados.

Crea el directorio del proyecto para la API del backend de la App de la siguiente manera:

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

**NOTA**: en las siguientes instrucciones solo mostraremos `pip install ...`.<br>
Si usarás `pipenv`, cámbialo por `pipenv install ...`.<br>
Si usarás `poetry`, cámbialo por `poetry add ...`.<br>
Si usarás `uv`, cámbialo por `uv add ...`.<br>

Consulta [esta documentación](../../Other/python-package-managers.md) para usar las diferentes herramientas de gestión de paquetes y dependencias de Python.

### From Git or Local Directory

Consulta [esta documentación](../../Other/installation.md) para instalar desde un repositorio/branch de Git o un Directorio Local.


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

### Servicios en la Nube

Dependiendo del servicio en la nube que uses, instala las dependencias necesarias:

#### AWS
```bash
pip install boto3
```

### Dependencias de prueba

Para ejecutar las pruebas unitarias y de integración, instala `pytest` y `coverage`:

```bash
pip install pytest coverage
```

## Opciones disponibles

1. **Selecciona tu Framework**: Según tu proyecto, elige entre [FastAPI](https://fastapi.tiangolo.com/), [Flask](https://flask.palletsprojects.com/) o [Chalice](https://aws.github.io/chalice/quickstart.html).
2. **Selecciona tu base de datos** de tu preferencia: Implementa operaciones de base de datos utilizando las funciones abstraídas proporcionadas para [MongoDB](https://www.mongodb.com/), [PostgreSQL](https://www.postgresql.org/), [MySQL](https://www.mysql.com/), [Supabase](https://supabase.com/), y [DynamoDB](https://aws.amazon.com/pm/dynamodb/).
3. **Autenticación incluida**: Tus endpoints estarán asegurados con autenticación basada en [JWT](https://jwt.io/libraries).
4. **Define Endpoints**: Utiliza la función de creación dinámica de endpoints definiendo tus endpoints en un archivo de configuración JSON. Consulta la [Guía de Configuración de Generic Suite](./../../Configuration-Guide/index.md) para más información.
5. **Define Opciones de Menú**: Utiliza la función de creación dinámica de menú definiendo tu menú y la seguridad de acceso a opciones en un archivo de configuración JSON. Consulta la [Guía de Configuración de Generic Suite](./../../Configuration-Guide/index.md) para orientación.
6. **Define Estructuras de Tabla**: Utiliza la función de creación dinámica de tablas definiendo tus editores CRUD en archivos de configuración JSON. Consulta la [Guía de Configuración de Generic Suite](./../../Configuration-Guide/index.md) para código de ejemplo y archivos.

## Configuración

Configura tu aplicación creando las variables de entorno necesarias.

Consulta los archivos [.env.example](https://github.com/tomkat-cr/genericsuite-be/blob/main/.env.example) y [config.py](https://github.com/tomkat-cr/genericsuite-be/blob/main/genericsuite/config/config.py) para las opciones disponibles.

Primero copia la plantilla `.env.example` a tu archivo `.env`:

```bash
curl https://raw.githubusercontent.com/tomkat-cr/genericsuite-be/main/.env.example > .env
```

Luego, edita el archivo `.env` para establecer los valores deseados:

```bash
vi .env
```

* Nombre de la aplicación
```env
APP_NAME=ExampleApp
```

* Dominio de la aplicación
```env
APP_DOMAIN_NAME=exampleapp.com
```

* Idioma por defecto de la aplicación
```env
DEFAULT_LANG=en
```

* Versión de la API (predeterminada a "v1")
```env
API_VERSION=v1
```

* Bandera de Stage y Debug
```env
# Depuración de la aplicación APP_DEBUG (0,1)
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

* Clave secreta de la aplicación (para uso en cifrado de contraseñas)
```env
# Clave secreta de la aplicación (para usar en el cifrado de contraseñas)
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
# DEV: Contenedor Docker
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

**NOTA**: deja `DYNAMDB_PREFIX_*` vacío y se establecerá por defecto a `<APP_NAME_LOWERCASE>_<STAGE>`.

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
- Para configurar Supabase con PostgreSQL, form example en el entorno QA, estable:
```env
APP_DB_ENGINE_QA=POSTGRES
APP_DB_URI_QA=postgresql://postgres:[YOUR_PASSWORD]@db.[SUPABASE_SERVER_SUBDOMAIN].supabase.co:5432
APP_DB_NAME_QA=postgres
```
- `YOUR_PASSWORD` no es la contraseña del usuario de Supabase, es una contraseña solicitada cuando se creó la cuenta de Supabase. Si necesitas restablecer esa contraseña, ve a "Database > Settings > Database password > [Reset database password]".
- `SUPABASE_SERVER_SUBDOMAIN` es el subdominio del servidor de Supabase. Puedes encontrarlo en la opción "Supabase Dashboard > Connect > Connection string".
- Para que esto funcione, debes adquirir el complemento de IPv4 en el panel de Supabase; de lo contrario obtendrás un error de conexión:
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

* Herramienta de gestión de paquetes y dependencias de Python (uv, pipenv y poetry), por defecto "uv"
```env
# Herramienta de gestión de paquetes y dependencias de Python (uv, pipenv y poetry), por defecto "uv"
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

* Configuración de ejecución local
```env
# Opciones: uvicorn, gunicorn, chalice, chalice_docker
# Caso FastAPI:
RUN_METHOD=uvicorn
# Caso Flask:
# RUN_METHOD=gunicorn
# Caso Chalice: "chalice" para usar http (ejecución sin docker) o "chalice_docker" para usar https (con docker)
# http:
# RUN_METHOD=chalice
# https:
# RUN_METHOD=chalice_docker
```

* Rutas y punto de entrada de la App
```env
#
# Directorio por defecto del código de la App
# para Chalice:
# https://aws.github.io/chalice/topics/packaging.html
# APP_DIR="."
# para FastAPI:
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=directory+structure#an-example-file-structure
# APP_DIR=app
# para Flask:
# https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/
# APP_DIR=flaskr
#
# Archivo principal de la App
# para Chalice:
# https://aws.github.io/chalice/topics/packaging.html
# APP_MAIN_FILE=app
# para FastAPI:
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=directory+structure#an-example-file-structure
# APP_MAIN_FILE=main
# para Flask:
# https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/
# APP_MAIN_FILE="__init__"
#
```

* Protocolo de ejecución local http/https, para que se active automáticamente en la ejecución local de la aplicación, sin intervención del usuario.
```env
# RUN_PROTOCOL=http
# RUN_PROTOCOL=https
#
# Deja en blanco para que el usuario seleccione el protocolo cuando inicie la ejecución del entorno de desarrollo local.
# RUN_PROTOCOL=""
```

* Configuración de recarga automática: a veces la recarga automática no funciona correctamente, por ejemplo al ejecutar Chalice con Turborepo y el gestor de paquetes "uv". En este caso, establece `AUTO_RELOAD=0` para desactivar la recarga automática y hacer que funcione.
```env
# Configuración de recarga automática para el entorno de desarrollo local.
# Opciones disponibles: `1` para activar, `0` para desactivar, y `-` para eliminar el parámetro de recarga automática de la línea de comandos. Por defecto: 1
# AUTO_RELOAD=1
# AUTO_RELOAD=0
# AUTO_RELOAD="-"
```

* Ubicación de archivos de configuración JSON y URL de Git
```env
GIT_SUBMODULE_LOCAL_PATH=lib/config_dbdef
GIT_SUBMODULE_URL=git://github.com/username/exampleapp_configs.git
```

* Ruta de la aplicación frontend (para copiar el archivo de versión durante el despliegue de lambdas grandes)
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
# Proveedor de nube IAAS
# Available options: `aws`, `gcp`, `azure`
CLOUD_PROVIDER=aws
```

* Habilitar/deshabilitar secretos del Proveedor de Nube (en lugar de variables de entorno).
```env
# Habilitar/deshabilitar secretos del Proveedor de Nube (en lugar de variables de entorno).
# Opciones disponibles: `1` para habilitar, `0` para deshabilitar. Por defecto: 1
# GET_SECRETS_ENABLED=0
#
# Gestión de secretos del Proveedor de Nube con granularidad fina:
#
# Habilitar/deshabilitar variables de entorno del Proveedor de Nube.
# Opciones disponibles: `1` para habilitar, `0` para deshabilitar. Por defecto: 1
# Configurar a "0" en el entorno de desarrollo local para que las variables de entorno como APP_CORS_ORIGIN puedan ser
# establecidas por los scripts y el archivo .env y acceder a recursos de QA desde DEV.
# GET_SECRETS_ENVVARS=0
#
# Habilitar/deshabilitar secretos críticos del Proveedor de Nube.
# Opciones disponibles: `1` para habilitar, `0` para deshabilitar. Por defecto: 1
# Configurar a "0" en el entorno de desarrollo local para que variables de entorno como APP_DB_URI puedan ser
# establecidas por los scripts y el archivo .env y acceder a recursos de QA desde DEV.
# GET_SECRETS_CRITICAL=0
```

* Configuración de AWS<br>
[https://console.aws.amazon.com](https://console.aws.amazon.com)

```env
# AWS S3 bucket name (used by set_fe_cloudfront_domain.sh to set the CloudFront domain name in the frontend for the CORS config)
AWS_S3_BUCKET_NAME_FE=exampleapp-frontend-website-[STAGE]
```
```env
# Región para todos los servicios de AWS de esta App
AWS_REGION=aws-region
```
```env
# Nombre base de AWS para Lambda Functions, API Gateway, EC2, ELB, etc.
AWS_LAMBDA_FUNCTION_NAME=exampleapp-backend
```
```env
# Rol de la función Lambda de AWS:
# Estas variables se usan solo si despliegas sin AWS SAM (deploy_without_sam) en big_lambdas_manager.sh. SAM genera este rol automáticamente
AWS_LAMBDA_FUNCTION_ROLE_QA=exampleapp-api_handler-role-qa
AWS_LAMBDA_FUNCTION_ROLE_STAGING=exampleapp-api_handler-role-staging
AWS_LAMBDA_FUNCTION_ROLE_DEMO=exampleapp-api_handler-role-demo
AWS_LAMBDA_FUNCTION_ROLE_PROD=exampleapp-api_handler-role-prod
```
```env
# ARN del certificado SSL de AWS (utilizado por big_lambdas_manager.sh)
AWS_SSL_CERTIFICATE_ARN=arn:aws:acm:AWS-REGION:AWS-ACCOUNT:certificate/AWS-CERTIFICATE-UUID
```

* Opciones de despliegue

```env
# Tipo de despliegue de AWS
# Available options: `lambda`, `ec2`, `fargate`. Defaults to: lambda
AWS_DEPLOYMENT_TYPE=lambda
```

```env
# Tipo de Despliegue de Lambda de AWS
# Available options: `zip`, `container`. Defaults to: zip
AWS_LAMBDA_DEPLOYMENT_TYPE=zip
```

* Cifrado de URL de almacenamiento (para enmascarar el nombre del bucket de AWS S3 y la clave)
```env
# Cifrado de URL de almacenamiento
#
# Storage URL encryption (default to 0)
# STORAGE_URL_ENCRYPTION=1
#
# Semilla de almacenamiento (para establecer el cifrado de URL de almacenamiento -e.g. AWS S3-)
# Genera una nueva con: `make generate_seed`
# STORAGE_URL_SEED=yyy
#
# Enmascaramiento de hostname externo en desarrollo
#   Para características como AI Vision, para enviar la URL de la imagen enmascarada.
#   Se recomienda configurarlo solo en el entorno de desarrollo.
#   Por ejemplo URL_MASK_EXTERNAL_HOSTNAME=app-dev.exampleapp.com
#   Deja en blanco para usar la misma URL almacenada -por ejemplo- en las conversaciones de AI Assistant.
# URL_MASK_EXTERNAL_HOSTNAME=
#
# Enmascaramiento de protocolo externo (http o https, por defecto RUN_PROTOCOL o https)
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
# Nombre de usuario de la cuenta de Docker: usado por el comando docker login para subir imágenes (p. ej. cuando se usa Kubernetes)
DOCKER_ACCOUNT=docker_account_username
```

* Configuración del motor de contenedores
```env
# Motor de contenedores: usado por el comando docker run para ejecutar el contenedor
# Available options: `docker`, `podman`. Defaults to: docker
# CONTAINERS_ENGINE=docker
# CONTAINERS_ENGINE=podman

# Aplicación del motor de contenedores
# Available options: `1` para habilitar, `0` para deshabilitar. Defaults to: 1
# OPEN_CONTAINERS_ENGINE_APP=1
# OPEN_CONTAINERS_ENGINE_APP=0
```

* Configuración de pruebas
```env
# Puerto de depuración local del backend
# Para http (predeterminado)
# BACKEND_DEBUG_LOCAL_PORT=5001
# Para https
# ADVERTENCIA: este puerto debe ser diferente al BACKEND_LOCAL_PORT, de lo contrario lanzará
# el error "Port already in use" al intentar iniciar el contenedor sls-nginx.
# BACKEND_DEBUG_LOCAL_PORT=5002

# Endpoint de pruebas
# Para http
# (por defecto "http://localhost:5001")
# TEST_APP_URL=http://app.exampleapp.local:5001
# Para https
# TEST_APP_URL=https://app.exampleapp.local:5002
```

* Puertos locales de la App
```env
# Puerto local del frontend (por defecto 3000)
FRONTEND_LOCAL_PORT=3000
#
# Puerto local de la API backend (por defecto 5001)
BACKEND_LOCAL_PORT=5001
```

* Método de creación de certificado SSL autogenerado local (utilizado cuando se ejecuta el entorno de desarrollo local con https o SLS-Secure Local Server)
```env
# Método de creación de certificado SSL autogenerado local
# (utilizado por "scripts/local_ssl_certs_creation.sh", por defecto "mkcert")
#
# SSL_CERT_GEN_METHOD="mkcert"
# SSL_CERT_GEN_METHOD="office-addin-dev-certs"
# SSL_CERT_GEN_METHOD="openssl"
```

* Deshabilitar servicios locales
  (útil cuando se ejecuta el entorno de desarrollo local sobre la marcha, offline, con internet móvil)
```env
# Deshabilitar el inicio del servidor DNS local durante la ejecución de la app
LOCAL_DNS_DISABLED=1
# Deshabilitar el inicio del proxy puente durante la ejecución de la app
BRIDGE_PROXY_DISABLED=1
```

* Localstack<br>
[https://www.localstack.cloud/](https://www.localstack.cloud/)

```env
# Configuración de Localstack
# LOCALSTACK_AUTH_TOKEN=""
# (Configura LOCALSTACK_AUTH_TOKEN en blanco cuando trabajes sin conexión, y asigna el Token de Autenticación para que servicios como EC2 funcionen correctamente)
```

* Archivo de parámetros general
```env
# Activar/desactivar la creación de un archivo de parámetros general en "/tmp/params_general.json"
# Opciones disponibles: `1` para activar, `0` para desactivar. Por defecto: 1
# PARAMS_FILE_ENABLED=0
# PARAMS_FILE_ENABLED=1
```

* Archivo de parámetros del usuario
```env
# Activar/desactivar la creación del archivo de parámetros del usuario en "/tmp/params_[user_id].json"
# Se recomienda activarlo en el entorno de desarrollo local para que funcione más rápido
# Por defecto es "0" para evitar riesgos de seguridad cuando se ejecuta en un entorno de producción
# Opciones disponibles: `1` para activar, `0` para desactivar.
# USER_PARAMS_FILE_ENABLED=0
# USER_PARAMS_FILE_ENABLED=1
```

* Configuración de Flask
```env
# Punto de entrada de la app Flask
FLASK_APP=__init__.py
# Clave secreta de Flask
FLASK_SECRET_KEY=xxxx
```

## Servidor Local SLS-Secure

Para usar recursos que solo funcionan usando el protocolo de capa de sockets seguros en el navegador (p. ej. la cámara) en el entorno de desarrollo local, se requiere el protocolo https en ambos servidores, backend y frontend. Hay dos opciones:

1. Usando Docker/Podman
2. Usando Cloudflare Tunnel

### Using Docker/Podman

Con este método, se crea un servidor local seguro utilizando contenedores Docker/Podman locales y certificados SSL autogenerados.

Para implementar SLS-Secure Local Server usando Docker/Podman, configura las siguientes variables en los archivos ".env" (backend y frontend, o monorepo):

1. `RUN_PROTOCOL="https"` (para activar el modo https)

2. `USE_CONTAINERS_ENGINE_APP=1` (para activar Docker/Podman por completo, de modo que arranque el SLS-Secure Local Server cuando `RUN_PROTOCOL="https"`)

3. `RUN_PROTOCOL_AND_PORT_REPLACEMENT=1` (para activar la sustitución automática de protocolo y puerto para las variables de entorno de desarrollo local `APP_CORS_ORIGIN` (tomadas de `APP_CORS_ORIGIN_{STAGE}`), y `REACT_APP_API_URL` (tomadas de `APP_API_URL_{STAGE}`) dependiendo del valor de `RUN_PROTOCOL`)

4. Define las siguientes variables de entorno:

* Backend:
  `APP_CORS_ORIGIN_DEV`: el hostname https local para el frontend usando la base de datos DEV
  `APP_CORS_ORIGIN_QA_LOCAL`: el hostname https local para el frontend usando la base de datos QA

* Frontend:
  `APP_API_URL_DEV`: el hostname https local para la API backend
  `APP_FE_URL_DEV`: el hostname https local para el frontend

* Ambos:
  `APP_NAME`: El nombre de la app
  `FRONTEND_LOCAL_PORT`: El puerto del frontend
  `BACKEND_LOCAL_PORT`: El puerto del backend

Ejemplo:

Para una app llamada "ExampleApp" y el dominio local "app.exampleapp.local":

- El hostname del frontend será: `https://app.exampleapp.local:3000`
- El hostname de la API backend será: `https://app.exampleapp.local:5000`

Debe haber una entrada en el archivo `/etc/hosts` para `app.exampleapp.local` que apunte a `127.0.0.1`.

```
127.0.0.1      app.exampleapp.local
```

Entonces los archivos ".env" del backend y frontend (o del monorepo) deberían tener las siguientes variables y valores:

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

* Ambos:

```env
APP_NAME="ExampleApp"
FRONTEND_LOCAL_PORT=3000
BACKEND_LOCAL_PORT=5000
RUN_PROTOCOL=https
USE_CONTAINERS_ENGINE_APP=1
RUN_PROTOCOL_AND_PORT_REPLACEMENT=1
```

#### Ejecutar los contenedores y la app

Ejecutar la app con los siguientes comandos iniciará automáticamente los contenedores (aplicación del backend, nginx y DNS local) y creará certificados SSL autofirmados:

```bash
# Monorepo
make dev

# O repos separados:
# make run
# make run_qa
```

### Usando Cloudflare Tunnel

Cloudflare Tunnel te ofrece una forma segura de conectar tus recursos locales a Cloudflare sin una dirección IP pública alcanzable. Con Tunnel, no envías tráfico a una IP externa: en su lugar, un demonio ligero en tu infraestructura (`cloudflared`) crea conexiones de salida hacia la red global de Cloudflare. Cloudflare Tunnel puede conectar servidores web HTTP, servidores SSH, escritorios remotos y otros protocolos de forma segura a Cloudflare. De esta manera, tus orígenes pueden servir tráfico a través de Cloudflare sin quedar expuestos a ataques que eviten Cloudflare.

[Documentación oficial de Cloudflare](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/)

Para implementar Cloudflare Tunnel, configura las siguientes variables en los archivos ".env" (backend y frontend, o monorepo):

1. `RUN_PROTOCOL="https"` (para activar el modo https)

2. `USE_CONTAINERS_ENGINE_APP=0` (para desactivar Docker/Podman por completo, de modo que no inicie el SLS-Secure Local Server cuando `RUN_PROTOCOL="https"`)

3. `RUN_PROTOCOL_AND_PORT_REPLACEMENT=0` (para desactivar la sustitución automática de protocolo y puerto para las variables de desarrollo local `APP_CORS_ORIGIN` (tomadas de `APP_CORS_ORIGIN_{STAGE}`), y `REACT_APP_API_URL` (tomadas de `APP_API_URL_{STAGE}`) dependiendo del valor de `RUN_PROTOCOL`)

4. Define las siguientes variables de entorno:
  `APP_NAME`: El nombre de la app
  `FRONTEND_LOCAL_PORT`: El puerto del frontend
  `BACKEND_LOCAL_PORT`: El puerto del backend
  `CF_HOSTING_DOMAIN`: El dominio de la cuenta de Cloudflare
  `CF_CONFIG_FILE` (opcional): La ruta al archivo de configuración. Por defecto: `${HOME}/.cloudflared/config-${CF_FRONTEND_SUBDOMAIN}.yml`

Los subdominios serán:
  `${APP_NAME en minúsculas}-dev`
  `${APP_NAME en minúsculas}-dev-api`

Ejemplo:

Para una app llamada "ExampleApp" y el dominio de Cloudflare "exampledomain.com":

- El hostname del frontend será: `https://exampleapp-dev.exampledomain.com`
- El hostname de la API backend será: `https://exampleapp-dev-api.exampledomain.com`

El backend y el frontend (o monorepo) deben tener una entrada en el archivo `/etc/hosts` para `exampleapp-dev.exampledomain.com` que apunte a `127.0.0.1`.

```
127.0.0.1      exampleapp-dev.exampledomain.com
```

Entonces los archivos ".env" del backend y frontend (o monorepo) deberían contener las siguientes variables y valores:

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

* Ambos:

```env
APP_NAME="ExampleApp"
FRONTEND_LOCAL_PORT=3000
BACKEND_LOCAL_PORT=5000
RUN_PROTOCOL=https
USE_CONTAINERS_ENGINE_APP=0
RUN_PROTOCOL_AND_PORT_REPLACEMENT=0
```

#### Crear el túnel

Para instalar la CLI `cloudfared` y crear el túnel de Cloudflare:
```bash
make cf-tunnel-create
```

#### Ejecutar el túnel y la app

Para ejecutar el túnel de Cloudflare (debe estar en una terminal distinta a las de los servidores de backend y frontend):
```bash
make cf-tunnel-run
```

Para detener el túnel de Cloudflare, pulsa `Ctrl-C`.

Luego la app puede ejecutarse localmente:

```bash
# Monorepo
make dev

# O repos separados:
# make run
# make run_qa
```

#### Otros comandos de túnel

Para listar el túnel de Cloudflare instalado:
```bash
make cf-tunnel-list
```

Para comprobar el túnel de Cloudflare (debe estar en ejecución):
```bash
make cf-tunnel-check
```

Para eliminar el túnel de Cloudflare:
```bash
make cf-tunnel-delete
```

## Estructura de la App

Puedes tener el frontend y el backend en repos diferentes o en el mismo repositorio.

En caso de necesitar que el frontend y el backend estén en repositorios diferentes, aquí tienes algunas estructuras de directorios sugeridas por framework:

* [Estructura de directorio de FastAPI](https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=directory+structure#an-example-file-structure)
* [Estructura de directorio de Flask](https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/)
* [Estructura de directorio de Chalice](https://aws.github.io/chalice/)

Este es un repositorio de desarrollo de App sugerido para un proyecto FastAPI:

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

Este es un repositorio de desarrollo de App sugerido para un proyecto Flask:

```
.
├── flaskr/
│   ├── __init__.py
│   ├── items.py
│   ├── users.py
│   ├── admin.py
│   └── index.py
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

Este es un repositorio de desarrollo de App sugerido para un proyecto Chalice:

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
│     └── __init__.py
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

Puedes encontrar ejemplos sobre configuraciones y cómo codificar una App en la [Guía de creación y configuración de GenericSuite](../../Configuration-Guide/index.md).

## Uso

Consulta [los scripts de desarrollo del backend de GenericSuite](../GenericSuite-Scripts/index.md) para más detalles.

## Especificación de la API

La especificación de la API está disponible en el directorio [FastApiTemplate/server](../../../code/fastapitemplate/server/README.md):

* JSON Swagger: [fastapitemplate-backend_openapi.json](../../../code/fastapitemplate/server/fastapitemplate-backend_openapi.json)
* YAML Swagger: [fastapitemplate-backend_openapi.yaml](../../../code/fastapitemplate/server/fastapitemplate-backend_openapi.yaml)

## Licencia

Este proyecto está licenciado bajo la Licencia ISC - vea el archivo LICENSE para más detalles.

## Créditos

Este proyecto es desarrollado y mantenido por Carlos Ramirez. Para más información o para contribuir al proyecto, visita [GenericSuite en GitHub](https://github.com/tomkat-cr/genericsuite-be).

¡Feliz Codificación!