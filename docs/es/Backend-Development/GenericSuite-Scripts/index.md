# Los Scripts de GenericSuite

[Scripts de GenericSuite (versión backend)](https://github.com/tomkat-cr/genericsuite-be-scripts) es una suite de características para mejorar el desarrollo de APIs en Python.

Este repositorio contiene los scripts de backend necesarios para construir e implementar APIs creadas por [GenericSuite (versión backend)](../GenericSuite-Core/index.md) y [GenericSuite AI (versión backend)](../GenericSuite-AI/index.md).

## Características

- **Despliegue AWS**: Despliegue a AWS como función Lambda con API Gateway usando SAM (AWS Serverless Application Model).
- **Entorno de desarrollo local**: ejecución con http o https, con o sin Docker.
- **Servidor DNS local**: para permitir acceso a la API mediante HTTPS con un nombre de dominio como `app.exampleapp.local` y permitir el acceso desde otros dispositivos localmente (p. ej. smartphones) para probar tu App.
- **Creación de certificados SSL autofirmados**: para permitir que los entornos de desarrollo frontend y backend locales funcionen sobre conexiones HTTPS seguras.
- **Gestión común de configuración JSON**: para añadir el Submódulo de Git con los directorios de configuración JSON comunes.
- **Contenedor Docker de base de datos local**: utilizado por el sitio de pruebas y permite tener un entorno de desarrollo local fuera de línea.

## Requisitos previos

- Node versión 20+, instalado vía [NVM (Node Package Manager)](https://nodejs.org/en/download/package-manager) o instalación de [NPM y Node](https://nodejs.org/en/download).
- [Los requisitos previos de The GenericSuite (versión backend)](https://github.com/tomkat-cr/genericsuite-be?tab=readme-ov-file#pre-requisites).
- Para APIs con funcionalidades de IA: [La guía de instalación de The GenericSuite AI (versión backend)](https://github.com/tomkat-cr/genericsuite-be-ai?tab=readme-ov-file#installation).

## Inicio

Para comenzar con GenericSuite, sigue estos pasos:

### Iniciar tu proyecto

Consulta [La guía de inicio rápido de The GenericSuite](https://github.com/tomkat-cr/genericsuite-be?tab=readme-ov-file#getting-started) para más detalles.

### Instalar los Scripts Backend de GenericSuite

```bash
npm init
```

```bash
npm install -D genericsuite-be-scripts
```

Para generar certificados SSL autofirmados, se requiere: 

```bash
npm install -D office-addin-dev-certs
```

### Preparar el Makefile

Copia la plantilla de `Makefile` desde `node_modules/genericsuite-be-scripts`:

```bash
cp node_modules/genericsuite-be-scripts/Makefile ./Makefile
```

### AWS SAM

#### Preparar las plantillas de AWS/SAM

Crea los directorios del proyecto `scripts/aws_big_lambda` y `scripts/aws` y copia las plantillas:

```bash
make init_sam
```

O...

```bash
bash node_modules/genericsuite-be-scripts/scripts/aws_big_lambda/init_sam.sh
```

<br>

Si vas a desarrollar con el framework Chalice:

Crea el directorio `.chalice` y copia la plantilla `.chalice/config-example.json`:<br>

```bash
make init_chalice
```

O...

```bash
bash node_modules/genericsuite-be-scripts/scripts/aws/init_chalice.sh
```

<br>

#### Personalizar plantillas SAM

Si necesitas hacer alguna personalización en el `samconfig.toml`:

Edita el archivo `template-samconfig.toml`:<br>

```bash
vi scripts/aws_big_lambda/template-samconfig.toml
# o
# code scripts/aws_big_lambda/template-samconfig.toml
```

Revisa si se necesita alguna personalización.

NOTA: El script de despliegue [big_lambdas_manager.sh](https://github.com/tomkat-cr/genericsuite-be-scripts/blob/main/scripts/aws_big_lambda/big_lambdas_manager.sh) reemplazará `APP_NAME_LOWERCASE_placeholder` por el nombre de la aplicación definido en la variable `APP_NAME` en el archivo `.env`.

<br>

#### Añadir nuevos Endpoints a la Plantilla SAM

Cuando necesites añadir nuevos endpoints a tu App:

Edita `template-sam.yml`:<br>

```bash
vi scripts/aws_big_lambda/template-sam.yml
# o
# code scripts/aws_big_lambda/template-sam.yml
```

En este archivo es donde se definen los endpoints, así como otros elementos de despliegue de SAM como las variables de entorno utilizadas por la función Lambda de AWS. Puedes añadir nuevos endpoints o personalizarlo según lo necesites.

Existe una plantilla de definición de endpoint en el archivo [node_modules/genericsuite-be-scripts/scripts/aws_big_lambda/template-sam-endpoint-entry.yml](https://github.com/tomkat-cr/genericsuite-be-scripts/blob/main/scripts/aws_big_lambda/template-sam-endpoint-entry.yml).

Ten cuidado con los elementos que terminan en `_placeholder` ya que son reemplazados por el script de despliegue `big_lambdas_manager.sh` con los valores correspondientes.

<br>

#### Añadir Variables de Entorno

Si necesitas añadir variables de entorno adicionales a tu App:

Edita el archivo `update_additional_envvars.sh`:<br>

```bash
vi scripts/aws/update_additional_envvars.sh
# o
# code scripts/aws/update_additional_envvars.sh
```

Añade tus reemplazos de variables de entorno adicionales en `scripts/aws/update_additional_envvars.sh` como:<br>

```bash
perl -i -pe"s|ENVVAR_NAME_placeholder|${ENVVAR_NAME}|g" "${CONFIG_FILE}"
```
... sustituyendo "ENVVAR_NAME" por el nombre de la variable de entorno

Añade las variables de entorno adicionales al archivo:
```.env
ENVVAR_NAME=ENVVAR_VALUE
```
... sustituyendo "ENVVAR_NAME" por el nombre de la variable de entorno y ENVVAR_VALUE por su valor.

Añade las variables de entorno adicionales al archivo `scripts/aws_big_lambda/template-sam.yml`, en la sección `APIHandler > Properties > Environment > Variables`. Por ejemplo:<br>

```yaml
      .
      .
   APIHandler:
         .
         .
      Properties:
            .
            .
         Environment:
         Variables:
            ENVVAR_NAME: ENVVAR_VALUE
                  .
                  .
```
... sustituyendo "ENVVAR_NAME" por el nombre de la variable de entorno y ENVVAR_VALUE por su valor.

Si usas el framework Chalice, añade las variables de entorno adicionales al archivo `.chalice/config-example.json`, en la sección principal `environment_variables`. Por ejemplo:<br>

   ```
   {
      "version": "2.0",
            .
            .
      "environment_variables": {
               .
               .
         "ENVVAR_NAME": "ENVVAR_NAME_placeholder"
      },
      "stages": {
            .
            .
   ```
... sustituyendo "ENVVAR_NAME" por el nombre de la variable de entorno (en ambos lugares).

## Uso

### Iniciar el servidor de desarrollo

Para iniciar el servidor de desarrollo para la etapa `dev` y un contenedor MongoDB de Docker local:

   ```bash
   make run
   ```

Para iniciar el servidor de desarrollo para la etapa `qa` y MongoDB Atlas:

   ```bash
   make run_qa
   ```

Cuando haya cambios en las dependencias o en el archivo `.env`, reinicia el servidor de desarrollo local:

   ```bash
   make restart_qa
   ```

### Crear usuario Super Admin

Para crear el usuario Super Administrador inicial para el desarrollo local, así como para entornos de producción:

```bash
make create-supad
```

### Desplegar QA

Para realizar un despliegue QA como función Lambda de AWS y API Gateway de AWS:

```bash
make deploy_qa
```

Para vincular la API de backend al dominio de la App:

* Ve a Route 53.
* Haz clic en la zona correspondiente al dominio de la App.
* Haz clic en 'Crear registro'.
* Introduce el subdominio: 'api-qa', 'api-staging', 'api-demo' o 'api' (para producción).
* Habilita 'alias'.
* En 'Route traffic to' selecciona la opción 'Alias to API Gateway API'.
* En 'Choose region' selecciona la región de la App.
* En 'Choose endpoint' selecciona el que corresponde al dominio de la App.
* Haz clic en 'Create Records'.

### Instalar dependencias

* Instala las categorías de paquetes por defecto desde Pipfile.<br>
Ejecuta `pipenv install`.<br>
Referencias: https://pipenv.pypa.io/en/latest/commands.html#install

```bash
make install
```

* Instala tanto las categorías de paquetes de desarrollo como las predeterminadas desde Pipfile.<br>
Ejecuta `pipenv install --dev`.

```bash
make install_dev
```

* Instala desde Pipfile.lock y omite por completo la información de Pipfile.<br>
Ejecuta `pipenv install --ignore-pipfile`.

```bash
make locked_install
```

* Instala tanto las categorías de paquetes de desarrollo como las predeterminadas desde Pipfile.lock y omite por completo la información de Pipfile.<br>
Ejecuta `pipenv install --dev --ignore-pipfile`.

```bash
make locked_dev
```

* ReCrea el archivo de bloqueo de Pipenv.<br>
Ejecuta `pipenv lock`.

```bash
make lock
```

* Genera el archivo `requirements.txt`.<br>
Ejecuta `sh scripts/aws/run_aws.sh pipfile`.

```bash
make requirements
```

* Instalación limpia.<br>
Alias que ejecuta `make clean_rm` y `make install`.

```bash
make fresh
```

### Limpieza

* Alias para ejecutar `make clean_rm`, `make clean_temp_dir`, y `make clean_logs`.

```bash
make clean
```

* Elimina un entorno virtual creado por "pipenv run".<br>
Ejecuta `pipenv --rm`.

```bash
make clean_rm
```

* Limpiar logs (en el directorio /logs).<br>
Ejecuta el script `scripts/clean_logs.sh`.

```bash
make clean_logs
```

* Limpiar logs, caché y archivos temporales.<br>
Ejecuta `sh scripts/aws/run_aws.sh clean`.

```bash
make clean_temp_dir
```

### Utilidades de CLI

* Instalar herramientas de desarrollo (pyenv, pipenv, make, y opcionalmente: poetry, saml2aws).<br>
Consulta [node_modules/genericsuite-be-scripts/scripts/install_dev_tools.sh](https://github.com/tomkat-cr/genericsuite-be-scripts/blob/main/scripts/install_dev_tools.sh) para más detalles sobre cómo configurarlo vía el archivo `.env`.

```bash
make install_tools
```

* Mostrar puertos en uso.<br>
Ejecuta `sh scripts/run_lsof.sh`.

```bash
make lsof
```

### Pruebas automatizadas

* Inicia el contenedor de la base de datos local y ejecuta las pruebas.<br>
Ejecuta `sh scripts/run_app_tests.sh`.

```bash
make test
```

* Ejecuta la prueba sin iniciar el contenedor Docker de la base de datos local.<br>
Ejecuta `sh scripts/aws/run_tests.sh`.

```bash
make test_only
```

### Linting

* Ejecutar Prospector.<br>
Ejecuta `pipenv run prospector`.

```bash
make lint
```

* Ejecutar MyPy.<br>
Ejecuta `pipenv run mypy .`.

```bash
make types
```

* Ejecutar Coverage.<br>
Ejecuta `pipenv run coverage run -m unittest discover tests` y `pipenv run coverage report`.

```bash
make coverage
```

* Ejecutar Yapf Formatter y PyCodeStyle.<br>
Ejecuta `pipenv run yapf -i *.py **/*.py **/**/*.py` y `pycodestyle`.<br>
Referencias:<br>
   * [https://github.com/google/yapf](https://github.com/google/yapf)<br>
   * [https://pycodestyle.pycqa.org/en/latest/](https://pycodestyle.pycqa.org/en/latest/)<br>

```bash
make format
```

* Ejecutar Yapf (en modo "imprimir la diff para el código fuente arreglado") y PyCodeStyle.<br>
Ejecuta `pipenv run yapf --diff *.py **/*.py **/**/*.py` y `pycodestyle`.

```bash
make format_check
```

### Comandos de desarrollo

* Realiza un Lint completo, verificación de tipos, pruebas unitarias e de integración, verificación de formato y estilo antes de las implementaciones.<br>
Alias para ejecutar `make lint`, `make types`, `make tests`, `make format_check` y `make pycodestyle`.

```bash
make qa
```

* Inicia el contenedor Docker de la base de datos local (utilizado para pruebas y ejecución de la etapa `dev`).<br>
Ejecuta `sh scripts/local_db/run_local_db_docker.sh run`.

```bash
make local-db-up
```

NOTAS:<br>

**_Pila local de MongoDB_**:

Usa `mongodb://root:example@mongo:27017/` como URL para conectarte a la base de datos MongoDb local.<br>
<br>
Usa [http://localhost:8081](http://localhost:8081) para acceder a la UI de administración de MongoDb.<br>
Usa el usuario: `admin` y la contraseña: `pass` como credenciales para acceder a la UI de administrador.<br>

**_Pila local de DynamoDB_**:

El puerto de la base de datos es 8000.<br>
      * dynamodb.endpoint = 'http://127.0.0.1:8000'<br>
      * dynamodb.endpoint = 'http://dynamodb-local:8000'<br>
<br>
Usa http://localhost:8095 para acceder a la UI de DynamoDB Manager.<br>
Configúrala para conectarte a DynamoDB local:<br>
<br>
     [Añadir conexión]<br>
       * Alias: Local<br>
       * Endpoint: http://127.0.0.1:8000<br>
       * Región: us-east-1<br>
       * Access Key: test<br>
       * Secret Key: test<br>

**_Pila local de Postgres_**:

El puerto de la base de datos es 5432.<br>
Usa "postgresql://user:pass@postgres-local:5432/db" como URL para conectarte a la base de datos Postgres local.<br>
<br>
Usa http://localhost:8080 para acceder a la UI de pgAdmin.<br>
Usa usuario: "admin@admin.com" y contraseña: "admin" para acceder a la UI de pgAdmin.<br>

**_Pila local de MySQL_**:

Usa http://localhost:8082 para acceder a la UI de phpMyAdmin.<br>
Usa usuario: "root" y contraseña: "pass" como credenciales para acceder a la UI de phpMyAdmin.<br>
<br>
El puerto de la base de datos es 3306.<br>
Usa "mysql://root:pass@mysql-local:3306/db" como URL para conectarte a la base de datos MySQL local.<br>

**_Pila local de Supabase_**:

No hay implementación local para Supabase.

Para más información sobre la pila de bases de datos local, consulta el archivo [local_db_stack.yml](https://github.com/tomkat-cr/genericsuite-be-scripts/blob/main/scripts/local_db/local_db_stack.yml).

* Muestra registros del contenedor de la base de datos local.<br>
Ejecuta `sh scripts/local_db/run_local_db_docker.sh logs`

```bash
make local-db-logs
```

* Detiene el contenedor Docker de la base de datos local.<br>
Ejecuta `sh scripts/local_db/run_local_db_docker.sh down`

```bash
make local-db-down
```

* Respaldar una base de datos mongoDB.<br>
Ejecuta `sh scripts/mongo/db_mongo_backup.sh ${STAGE} ${BACKUP_DIR}`<br>

```bash
make mongo_backup
```

Ej.  
```bash
STAGE=qa BACKUP_DIR=./dumps make mongo_backup
```

* Restaurar una base de datos mongoDB.<br>
Ejecuta `sh scripts/mongo/db_mongo_restore.sh ${STAGE} ${RESTORE_DIR}`

```bash
make mongo_restore
```

Ej.
```bash
STAGE=qa RESTORE_DIR=./dumps/bkp-mongodb-[exampleapp]_[stage]-[date]_[time].zip make mongo_restore
```

### Comandos específicos de Chalice

* Establecer parámetros en `.chalice/config.json` para la etapa de producción.<br>
Ejecuta `sh scripts/aws/set_chalice_cnf.sh prod`.

```bash
make config
```

* Establecer parámetros en `.chalice/config.json` sin una etapa específica.<br>
Ejecuta `sh scripts/aws/set_chalice_cnf.sh`.

```bash
make config_dev
```

* Establecer parámetros en `.chalice/config.json` como la etapa de Desarrollo.<br>
Ejecuta `sh scripts/aws/set_chalice_cnf.sh local_db_docker`.

```bash
make config_local
```

* Establecer parámetros en `.chalice/config.json` como la etapa de QA con reemplazo de variables CORS para permitir usar la base de datos en vivo de QA desde el entorno de desarrollo local.<br>
Ejecuta `sh scripts/aws/set_chalice_cnf.sh qa`.<br>
Referencias: 
   * `APP_CORS_ORIGIN_QA_CLOUD` y `APP_CORS_ORIGIN_QA_LOCAL` en el archivo [.env.example](https://github.com/tomkat-cr/genericsuite-be/blob/main/.env.example).<br>

```bash
make config_qa
```

* Establecer parámetros en `.chalice/config.json` para preparar el despliegue QA.<br>
Ejecuta `sh scripts/aws/set_chalice_cnf.sh qa deploy`,

```bash
make config_qa_for_deployment
```

* Establecer parámetros en `.chalice/config.json` como la etapa de Staging.<br>
Ejecuta `sh scripts/aws/set_chalice_cnf.sh staging`.

```bash
make config_staging
```

* Crear la pila de AWS vía Chalice (comando).</BR/>
Ejecuta `sh scripts/aws/run_aws.sh create_stack`.

```bash
make build
```

* Genera el `requirements.txt`.<br>
Ejecuta `sh scripts/aws/run_aws.sh pipfile`.

```bash
make build_local
```

* Describir la pila de AWS con el comando Chalice.<br>
Ejecuta `sh scripts/aws/run_aws.sh describe_stack`.

```bash
make build_check
```

* Alias para ejecutar `make unbuild_qa`.

```bash
make unbuild
```

* Eliminar la App Chalice QA.<br>
Ejecuta `sh scripts/aws/run_aws.sh delete_app qa`.

```bash
make unbuild_qa
```

* Eliminar la App Chalice de Staging.<br>
Ejecuta `sh scripts/aws/run_aws.sh delete_app staging`

```bash
make unbuild_staging
```

* Eliminar la pila de AWS creada por Chalice.<br>
Ejecuta `sh scripts/aws/run_aws.sh delete_stack`

```bash
make delete_stack
```

### AWS S3

Crear los buckets de AWS S3 para diferentes entornos y otras utilidades de AWS.

* Crear bucket S3 para desarrollo.<br>
Ejecuta `sh scripts/aws/create_chatbot_s3_bucket.sh dev`.

```bash
make create_s3_bucket_dev
```

   * NOTAS:

      * Los scripts `create_s3_bucket_*` también permiten crear o reasignar la Política del Bucket S3.


      * Si recibes el mensaje `AWS_S3_CHATBOT_ATTACHMENTS_CREATION is not set to 1`, define esa variable de entorno o ejecuta el script de esta forma:

         ```bash
         AWS_S3_CHATBOT_ATTACHMENTS_CREATION=1 make create_s3_bucket_dev
         ```


* Crear bucket S3 para QA.<br>
Ejecuta `sh scripts/aws/create_chatbot_s3_bucket.sh qa`.

```bash
make create_s3_bucket_qa
```

* Crear bucket S3 para Staging.<br>
Ejecuta `sh scripts/aws/create_chatbot_s3_bucket.sh staging`.

```bash
make create_s3_bucket_staging
```

* Crear los buckets S3 de Producción.<br>
Ejecuta `sh scripts/aws/create_chatbot_s3_bucket.sh prod`.

```bash
make create_s3_bucket_prod
```

### DynamoDB

* Generar definiciones de tablas DynamoDB<br>

Para despliegue CF (CloudFormation):

Lee todas las definiciones de tablas desde el directorio de configuración JSON y genera un archivo que puede usarse como plantilla de AWS Cloud Formation.

```bash
make generate_cf_dynamodb
```

Para despliegue SAM (Serverless Application Model):

Lee todas las definiciones de tablas desde el directorio de configuración JSON y genera un archivo de plantilla que puede insertarse en el archivo SAM `template.yml`.

```bash
make generate_sam_dynamodb
```

* Crear una configuración predeterminada de AWS en `${HOME}/.aws/config`<br>
Ejecuta `sh scripts/aws/create_aws_config.sh`.

```bash
make create_aws_config
```

### Bases de datos SQL

#### Postgres

```bash
make generate_postgres_dev_sql
```

Genera el archivo SQL de Postgres para crear las tablas en cualquier entorno.

```bash
make create_postgres_dev_tables
```

Crea las tablas de Postgres para cualquier entorno.

```bash
make generate_cf_postgres
```

Genera la plantilla de CloudFormation de Postgres para crear las tablas en AWS RDS.

```bash
make deploy_postgres
```

Despliega las tablas de Postgres en AWS RDS.

#### MySQL

```bash
make generate_mysql_dev_sql
```

Genera el archivo SQL de MySQL para crear las tablas en cualquier entorno.

```bash
make create_mysql_dev_tables
```

Crea las tablas de MySQL para cualquier entorno.

```bash
make generate_cf_mysql
```

Genera la plantilla de CloudFormation de MySQL para crear las tablas en AWS RDS.

```bash
make deploy_mysql
```

Despliega las tablas de MySQL en AWS RDS.

### Secrets

* Generar una nueva semilla para el enmascarado de URLs de almacenamiento

Para asignar la variable de entorno STORAGE_URL_SEED.

```bash
make generate_seed
```

### Despliegue

#### Despliegue de AWS Serverless

Realiza el despliegue de la aplicación con AWS Lambda Functions y API Gateway, usando SAM (Serverless Application Model).

* Desplegar la App en QA.<br>
Ejecuta `make create_s3_bucket_qa`, `sh scripts/aws_big_lambda/big_lambdas_manager.sh sam_deploy qa`

```bash
make deploy_qa
```

* Probar localmente la API Gateway y la función Lambda de AWS, usando SAM local. Ejecuta `sam build` para probar posibles problemas de paquetes y dependencias, y luego `sam run local`.<br>
Ejecuta `make create_s3_bucket_qa`, `sh scripts/aws_big_lambda/aws_big_lambda/big_lambdas_manager.sh sam_run_local qa`

```bash
make deploy_run_local_qa
```

**NOTA**: establece la variable de entorno `SAM_BUILD_CONTAINER=1` en `.env` para forzar `sam build --use-container --debug`.


* Validar las plantillas de despliegue SAM en QA.<br>
Ejecuta `make create_s3_bucket_qa`, `sh scripts/aws_big_lambda/big_lambdas_manager.sh sam_validate qa`

```bash
make deploy_validate_qa
```

* Crear solo el paquete de despliegue QA.<br>
Útil para verificar el tamaño del paquete y probar la imagen con un contenedor Docker local.<br>
Ejecuta `make create_s3_bucket_qa`, `sh scripts/aws_big_lambda/big_lambdas_manager.sh package qa`.

```bash
make deploy_package_qa
```

* Desplegar la App en Staging.<br>
Ejecuta `make create_s3_bucket_staging`, `sh scripts/aws_big_lambda/big_lambdas_manager.sh sam_deploy staging` 

```bash
make deploy_staging
```

* Desplegar la App en Demo.<br>
Ejecuta `make create_s3_bucket_demo`, `sh scripts/aws_big_lambda/big_lambdas_manager.sh sam_deploy demo` 

```bash
make deploy_demo
```

* Desplegar la App en Producción.<br>
Ejecuta `make create_s3_bucket_prod`, `sh scripts/aws_big_lambda/big_lambdas_manager.sh sam_deploy prod`

```bash
make deploy_prod
```

* Alias para ejecutar `make deploy_qa`.

```bash
make deploy
```

* Previsualizar el comportamiento de los entornos en vivo QA/Staging/Prod.<br>
Ejecuta el script bash `scripts/build_prod_test.sh`.

```bash
# Ejecutar la prueba
make test-run-build
```

```bash
# Restaurar el entorno tras la prueba
make test-run-build-restore
```

#### AWS secrets

* Gestionar secretos de AWS.
Ejecuta: `sh scripts/aws_secrets/aws_secrets_manager.sh`

```bash
make aws_secrets
```

Opciones:

`ACTION`: `run` (crear los secretos), `destroy` (destruir los secretos), `describe` (describir los secretos)

`STAGE`: `dev`, `qa`, `staging`, `demo`, `prod`

`TARGET`: `kms` (gestionar claves KMS), `secrets` (gestionar los secretos).

`ENGINE`: `localstack` (usar LocalStack como backend), `aws` (usar AWS como backend). Por defecto es `aws`

`AWS_DEPLOYMENT_TYPE`: usado para definir la variable de entorno `APP_HOST_NAME`. Las opciones son: `lambda` (aplicación desplegada como AWS Lambda), `fargate` (aplicación desplegada como AWS Fargate), `ec2` (aplicación desplegada como AWS EC2). Por defecto es `lambda`.

`KMS_KEY_ALIAS`: alias para la clave KMS. Por defecto `genericsuite-key`.

`CICD_MODE`: `0` (modo verbose), `1` (menos verbose, más adecuado para CI/CD). Por defecto `0`

`TMP_BUILD_DIR`: directorio de trabajo temporal. Por defecto `/tmp/${APP_NAME_LOWERCASE}_aws_secrets_tmp`

`DEBUG`: `1` (activar modo debug), `0` (desactivar modo debug). Por defecto `1`

Uso:

```bash
# Crear las claves KMS en QA en la nube de AWS
ACTION=run STAGE=qa TARGET=kms make aws_secrets
```

```bash
# Crear las claves KMS en QA usando LocalStack
ACTION=run STAGE=qa TARGET=kms ENGINE=localstack make aws_secrets
```

```bash
# Crear los secretos en QA en la nube de AWS
ACTION=run STAGE=qa TARGET=secrets make aws_secrets
```

#### Despliegue AWS EC2

Despliegue de la aplicación con instancias AWS EC2, ALB (Application Load Balancer), ECR (Elastic Container Registry), AWS Secrets Manager y CloudFormation.

* Preparar la imagen ECR para una etapa dada (p. ej. QA, staging, Demo, Prod).<br>
Ejecuta `sh scripts/aws_ec2_elb/run-fastapi-ecr-creation.sh`

```bash
make deploy_ecr_creation
```

Uso:

```bash
ECR_IMAGE_TAG="0.0.16" STAGE=qa make deploy_ecr_creation
```

* Gestiona despliegues EC2 en las diferentes etapas (p. ej. QA, staging, Demo, Prod).<br>
Ejecuta `sh scripts/aws_ec2_elb/run-ec2-cloud-deploy.sh`

```bash
make deploy_ec2
```

Opciones:

`ACTION`: `run` (realizar el despliegue), `destroy` (destruir el despliegue)

`STAGE`: `dev`, `qa`, `staging`, `demo`, `prod`

`TARGET`: `ec2` (desplegar ALB + instancia EC2), `domain` (desplegar el dominio asociado al ALB).

`ECR_DOCKER_IMAGE_TAG`: Etiqueta de la imagen Docker en el repositorio ECR

`ENGINE`: `localstack` (usar LocalStack como backend), `aws` (usar AWS como backend). Por defecto `aws`

`CICD_MODE`: `0` (modo verbose), `1` (menos verbose, más adecuado para CI/CD). Por defecto `0`

`TMP_WORKING_DIR`: directorio de trabajo temporal. Por defecto `/tmp`

`DEBUG`: `1` (activar modo debug), `0` (desactivar modo debug). Por defecto `1`

Uso:

```bash
# Realizar el despliegue ALB (Elastic Load Balancer) + instancia EC2 en la nube de AWS
ACTION=run STAGE=qa TARGET=ec2 ECR_DOCKER_IMAGE_TAG=0.0.16 make deploy_ec2
```

```bash
# Realizar el despliegue del Dominio en la nube de AWS
ACTION=run STAGE=qa TARGET=domain ECR_DOCKER_IMAGE_TAG=0.1.16 make deploy_ec2
```

```bash
# Destruir el despliegue ALB + instancia EC2 en la nube de AWS
ACTION=destroy STAGE=qa TARGET=ec2 ECR_DOCKER_IMAGE_TAG=0.0.16 make deploy_ec2
```

```bash
# Realizar el despliegue del Dominio en la nube de AWS local
ACTION=run STAGE=qa TARGET=domain ECR_DOCKER_IMAGE_TAG=0.1.16 ENGINE=localstack make deploy_ec2
```

```bash
# Realizar el despliegue de la instancia EC2 en la nube de AWS local (ALB no se puede simular localmente)
ACTION=run STAGE=qa TARGET=ec2 ECR_DOCKER_IMAGE_TAG=0.0.16 ENGINE=localstack make deploy_ec2
```

#### Despliegue DynamoDB AWS

* Gestiona despliegues DynamoDB en las diferentes etapas (p. ej. QA, staging, Demo, Prod).<br>
Ejecuta `sh scripts/aws_dynamodb/run-dynamodb-deploy.sh`.

```bash
make deploy_dynamodb
```

Opciones:

`ACTION`: `run` (realizar el despliegue), `destroy` (destruir el despliegue), `describe` (describir las tablas DynamoDB), `list_tables` (listar todas las tablas DynamoDB).

`STAGE`: `dev`, `qa`, `staging`, `demo`, `prod`

`TARGET`: `dynamodb` (desplegar la tabla DynamoDB).

`ENGINE`: `localstack` (usar LocalStack como backend), `aws` (usar AWS como backend). Por defecto `aws`

`CICD_MODE`: `0` (modo verbose), `1` (menos verbose, más adecuado para CI/CD). Por defecto `0`

`TMP_BUILD_DIR`: directorio de trabajo temporal. Por defecto `/tmp/${APP_NAME_LOWERCASE}_dynamodb_tmp`

`DEBUG`: `1` (activar modo debug), `0` (desactivar modo debug). Por defecto `1`

Uso:

```bash
# Realizar el despliegue de DynamoDB en la nube de AWS local
ACTION=run STAGE=qa TARGET=dynamodb ENGINE=localstack make deploy_dynamodb
```

```bash
# Realizar el despliegue de DynamoDB en la nube de AWS
ACTION=run STAGE=qa TARGET=dynamodb make deploy_dynamodb
```

### Aplicación: Comandos Específicos

* Ejecutar la App localmente utilizando la base de datos de desarrollo, pidiendo ejecutarla sobre `http` o `https`.<br>
Ejecuta `make config_qa`, `make clean_logs`, y `sh scripts/aws/run_aws.sh run_local`.
[???]

```bash
make run
```

* Ejecutar la App localmente utilizando la base de datos QA, pidiendo ejecutarla sobre `http` o `https`.<br>
Ejecuta `make config_qa`, `make clean_logs`, y `sh scripts/aws/run_aws.sh run_local qa`.

```bash
make run_qa
```

* Ejecuta `make config_qa`, `make clean_logs`, y `sh scripts/secure_local_server/run.sh "down" ""`
Detén y destruye el contenedor local de Docker de la App (para cualquier etapa en ejecución).<br>

```bash
make down_qa
```

* Reiniciar el contenedor local de Docker de la App en ejecución en QA.<br>
Ejecuta `make config_qa`, `make clean_logs`, `sh scripts/secure_local_server/run.sh "down" ""` y `sh scripts/aws/run_aws.sh run_local qa`.

```bash
make restart_qa
```

* Ejecutar la App localmente utilizando la base de datos de desarrollo (en un contenedor local de Docker), pidiendo ejecutarla sobre `http` o `https`.<br>
Ejecuta `make config_local`, `make clean_logs`, `sh scripts/aws/run_aws.sh run_local dev`.
[???]

```bash
make run_local_docker
```

* Ejecutar `chalice local --port $PORT --stage PROD`<br>
Ejecuta `make config`, `make clean_logs`, `sh scripts/aws/run_aws.sh run`.

```bash
make run_prod
```

* Enlazar las librerías de GenericSuite al proyecto.<br>
Enlaza las librerías locales de GenericSuite (repos con el código fuente) para tener recarga en caliente sin necesidad de ejecutar "pipenv update" cada vez que el código de las librerías cambia.<br>
Ejecuta `sh scripts/link_gs_libs_for_dev.sh`

```bash
make link_gs_libs
```

**NOTA**: establece la variable de entorno `BASE_DEVELOPMENT_PATH` para la ruta base de las librerías de GenericSuite (ruta al directorio padre de los repos "genericsuite-be*") en el archivo `.env`.

```env
# Consulta "genericsuite-be-scripts/scripts/link_gs_libs_for_dev.sh"
# BASE_DEVELOPMENT_PATH="/Users/username/base_path_to_genericsuite_repos"
```

### Configuración JSON común

* Añadir el Submódulo de Git con los directorios de configuración JSON comunes.<br>
Ejecuta `sh scripts/add_github_submodules.sh`.

```bash
make add_submodules
```

### Servidor DNS local

* Iniciar el Servidor DNS local.<br>
Ejecuta `sh scripts/dns/run_local_dns.sh`

```bash
make local_dns
```

* Ejecuta `sh scripts/dns/run_local_dns.sh restart` para reiniciar el servidor DNS local.<br>

```bash
make local_dns_restart
```

* Reiniciar y volver a construir la configuración del servidor DNS local cuando la IP local o cualquier parámetro DNS haya cambiado.<br>
Ejecuta `sh scripts/dns/run_local_dns.sh rebuild`

```bash
make local_dns_rebuild
```

* Detener y destruir el servidor DNS local.<br>
Ejecuta `sh scripts/dns/run_local_dns.sh down`.

```bash
make local_dns_down
```

* Probar el servidor DNS local.<br>
Ejecuta `sh scripts/dns/run_local_dns.sh test`.

```bash
make local_dns_test
```

### Certificados SSL autofirmados

* Crear los certificados SSL locales autofirmados (requeridos para ejecutar el frontend y backend de desarrollo local sobre https).<br>
Ejecuta `sh scripts/local_ssl_certs_creation.sh`.

```bash
make create_ssl_certs_only
```

* Copiar los certificados SSL locales autofirmados al directorio frontend/repositorio local.<br>
Ejecuta `sh scripts/local_ssl_certs_copy.sh`.

```bash
make copy_ssl_certs
```

* Alias para ejecutar `make create_ssl_certs_only` y `make copy_ssl_certs`.<br>

```bash
make create_ssl_certs
```

### Scripts de paquetes NPM

* Actualizar el archivo package.json con la versión y todos los demás parámetros excepto dependencias.<br>
Ejecuta `npm install --package-lock-only`.

```bash
make npm_lock
```

* Probar el publish a NPMJS sin publicar realmente.<br>
Ejecuta `sh scripts/npm_publish.sh pre-publish`.

```bash
make pre-publish
```

* Publicar el paquete de scripts a NPMJS.<br>
Ejecuta `sh scripts/npm_publish.sh publish`.<br>
Requisitos:<br>
   * [Cuenta de NPMJS](https://www.npmjs.com/signup).

```bash
make publish
```

### Scripts de paquetes PyPI

* Construir el directorio 'dist' necesario para la publicación en PyPI.<br>
Ejecuta `poetry lock --no-update`, `rm -rf dist` y `python3 -m build`.<br>
Requisitos:<br>
   * [poetry](https://python-poetry.org/).

```bash
make pypi-build
```

* Publicación de pruebas a PyPI.<br>
Ejecuta `make pypi-build`, y `python3 -m twine upload --repository testpypi dist/*`.<br>
Requisitos:<br>
   * [twine](https://pypi.org/project/twine/).<br>
   * [Cuenta TestPypi](https://test.pypi.org/account/register/).

```bash
make pypi-publish-test
```

* Publicación de PyPI en producción<br>
Ejecuta `make pypi-build`, y `python3 -m twine upload dist/*`.<br>
Requisitos:<br>
   * [twine](https://pypi.org/project/twine/).<br>
   * [Cuenta PyPI](https://www.pypi.org/account/register/).

```bash
make pypi-publish
```

## Solución de problemas

- Si obtienes el error `Warning: Python >=3.9,<4.0 was not found on your system...` al hacer `make install`:

```bash
make install
```
... y la respuesta es similar a:
```
pipenv install
Warning: Python >=3.9,<4.0 was not found on your system...

You can specify specific versions of Python with:
$ pipenv --python path/to/python
make: *** [install] Error 1
```

Solución con estos comandos:

```bash   
# Establecer la versión de Python del proyecto con pyenv
pyenv local 3.12
```
```bash
# Establecer la ruta de Python con pipenv
pipenv --python ${HOME}/.pyenv/shims/python
```

Y repetir `make install`

- Si obtienes la advertencia `This version of npm is compatible with lockfileVersion@1...` al hacer `make install`:

```bash
npm install
```
... y la respuesta es similar a:
```
npm WARN read-shrinkwrap
This version of npm is compatible with lockfileVersion@1,
but package-lock.json was generated for lockfileVersion@3.
I'll try to do my best with it!
```

Es porque estás usando una versión antigua de Node. Para solucionarlo:

```bash
nvm use 20
```

Y repetir `make install`

- Si recibes `APP_NAME not set` al hacer cualquier `make run`, es porque el archivo `.env` debe crearse o revisarse. Consulta la [Configuración de GenericsSuite (versión backend)](https://github.com/tomkat-cr/genericsuite-be?tab=readme-ov-file#configuration) o la [Configuración de GenericsSuite AI (versión backend)](https://github.com/tomkat-cr/genericsuite-be-ai?tab=readme-ov-file#configuration)

- Si obtienes errores de CORS en la comunicación entre el frontend y el backend:

   1. Para hacer que ambos usen `localhost` y `http`, cambia estas variables en el archivo `.env`:

```bash
# Archivo .env del frontend:
APP_LOCAL_DOMAIN_NAME=localhost
```
```bash
# Archivo .env del backend:
APP_CORS_ORIGIN_QA_LOCAL=http://localhost:3000
```
   Y `make run` para el frontend y el backend con la opción `http`.

   2. Para hacer que ambos usen el servidor DNS local y `https`, cambia estas variables en el archivo `.env`:

```bash
# Archivo .env del frontend:
APP_LOCAL_DOMAIN_NAME=app.exampleapp.local
```
```bash
# Archivo .env del backend:
APP_CORS_ORIGIN_QA_LOCAL=https://app.exampleapp.local:3000
```
**NOTA**: reemplaza `exampleapp` por el nombre de tu App, todo en minúsculas.

Y `make run` para el frontend y el backend con la opción `https`.<br>

- Si el servidor DNS local parece no ser alcanzable o no funciona:

Reinicia el servidor backend local:

```bash
make local_dns_restart
```

Si la IP local cambia, asegúrate de:
  1) Ejecutar `make local_dns_rebuild`.<br><br>
  2) Copiar la `IP` reportada por el comando anterior.<br>Ej.:<br>
     `Local DNS domain 'app.exampleapp.local' is pointing to IP address '192.168.1.158'`.<br><br>
  3) Ejecutar `make restart_qa`<br><br>
  4) Añadir la `IP` a los Servidores DNS en la configuración de red de tu ordenador (`Network > DNS servers`). La nueva IP del Servidor DNS debe ser la primera de la lista de servidores DNS.<br><br>
  5) Reiniciar la conexión de red WiFi o LAN de la computadora.

## Licencia

GenericSuite es software de código abierto licenciado bajo la licencia ISC.

## Créditos

Este proyecto es desarrollado y mantenido por Carlos J. Ramirez. Para más información o para contribuir al proyecto, visita [Los Scripts de GenericSuite (versión backend) en GitHub](https://github.com/tomkat-cr/genericsuite-be-scripts).

¡Feliz codificación!