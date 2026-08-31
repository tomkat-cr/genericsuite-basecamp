# 20260830 - v1.0.0 - Guía de Migración

Cambios a realizar en las aplicaciones GS con la versión antigua de GS:

## Interfaz de Usuario

* Revisa `ui/package.json` para comprobar los scripts de ejecución que anteriormente apuntaban a /genericsuite/scripts':

Reemplaza `node_modules/genericsuite/scripts` por `node_modules/genericsuite-fe-scripts/scripts`:

```json
  "scripts": {
    "start:gs-dev": "bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh dev && bash ./node_modules/genericsuite/scripts/run_app_frontend.sh dev",
    "start:gs-qa": "bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh qa && bash ./node_modules/genericsuite/scripts/run_app_frontend.sh qa",
    "start:gs-demo": "bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh demo && bash ./node_modules/genericsuite/scripts/run_app_frontend.sh demo",
    "start:gs-prod": "bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh prod && bash ./node_modules/genericsuite/scripts/run_app_frontend.sh prod",
    "build:vite-dev": "bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh dev && bash ./node_modules/genericsuite/scripts/run_method_build.sh build vite dev 0",
    "build:vite-qa": "bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh qa && bash ./node_modules/genericsuite/scripts/run_method_build.sh build vite qa 0",
    "build:vite-demo": "bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh demo && bash ./node_modules/genericsuite/scripts/run_method_build.sh build vite demo 0",
    "build:vite-prod": "bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh prod && bash ./node_modules/genericsuite/scripts/run_method_build.sh build vite prod 0",
    "install:vite": "bash ./node_modules/genericsuite/scripts/run_method_dependency_manager.sh install vite",
  }
```

A:

```json
  "scripts": {
    "start:gs-dev": "bash ./node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh dev && bash ./node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh dev",
    "start:gs-qa": "bash ./node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh qa && bash ./node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh qa",
    "start:gs-demo": "bash ./node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh demo && bash ./node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh demo",
    "start:gs-prod": "bash ./node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh prod && bash ./node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh prod",
    "build:vite-dev": "bash ./node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh dev && bash ./node_modules/genericsuite-fe-scripts/scripts/run_method_build.sh build vite dev 0",
    "build:vite-qa": "bash ./node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh qa && bash ./node_modules/genericsuite-fe-scripts/scripts/run_method_build.sh build vite qa 0",
    "build:vite-demo": "bash ./node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh demo && bash ./node_modules/genericsuite-fe-scripts/scripts/run_method_build.sh build vite demo 0",
    "build:vite-prod": "bash ./node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh prod && bash ./node_modules/genericsuite-fe-scripts/scripts/run_method_build.sh build vite prod 0",
    "install:vite": "bash ./node_modules/genericsuite-fe-scripts/scripts/run_method_dependency_manager.sh install vite",
  }
```

* Actualiza `ui/package.json`

```json
"devDependencies": {
	"genericsuite-fe-scripts": "github:tomkat-cr/genericsuite-fe-scripts#develop",
},
"dependencies": {
	"genericsuite": "github:tomkat-cr/genericsuite-fe#develop",
    "genericsuite-ai": "github:tomkat-cr/genericsuite-fe-ai#develop"
}
```

O...

```bash
npm install -ui -D genericsuite-fe-scripts@latest
# o: pnpm add -D -filter ui genericsuite-fe-scripts
npm install -ui genericsuite@latest genericsuite-ai@latest
# o: pnpm up --latest -filter ui genericsuite genericsuite-ai
```

* Si NO estás usando Webpack:

```bash
npm uninstall css-loader postcss-loader style-loader
# o: pnpm remove -r -filter ui css-loader postcss-loader style-loader
```

* Limpieza de otras dependencias:

Para los consumidores de `genericsuite-fe` (estas eran dependencias pares, por lo que las apps descendientes las instalaban directamente):

```bash
npm uninstall react-icons web-vitals fs json-loader with constants-browserify crypto-browserify os-browserify stream-browserify tty-browserify url vm-browserify
# o: pnpm remove -r -filter ui react-icons web-vitals fs json-loader with constants-browserify crypto-browserify os-browserify stream-browserify tty-browserify url vm-browserify
```

Para cualquiera que esté construyendo/contribuyendo a `genericsuite-fe` en sí mismo (devDependencies, solo relevante si ejecutan `npm install` contra el package.json de este repo):

```bash
npm uninstall @babel/cli @babel/preset-stage-0 @rollup/plugin-typescript @testing-library/user-event file-loader url-loader path
# o: pnpm remove -r -filter ui @babel/cli @babel/preset-stage-0 @rollup/plugin-typescript @testing-library/user-event file-loader url-loader path
```

* Si no estás usando Github Pages para el despliegue:

```bash
npm uninstall gh-pages
# o: pnpm remove -r -filter ui gh-pages
```

* Si no estás usando Express:

```bash
npm uninstall express express-rate-limit
# o: pnpm remove -r -filter ui express express-rate-limit
```

* Si estás usando React Rewired:

1. Reemplaza tu "config-overrides.js" con el que se encuentra en "/node_modules/genericsuite-fe"

2. Archivo: "package.json"

- Si hay un atributo "type": "module", renómbralo a por ejemplo "type1"
- Si hay un atributo "homepage": "..." renómbralo a por ejemplo "homepage1" (a menos que realmente necesites un sufijo URL #)
- Si hay un atributo "eslintConfig": "..." renómbralo a por ejemplo "eslintConfig1"
- Agrega la siguiente entrada a "scripts":
    "start-dev:react-app-rewired": "bash ../node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh dev && npx react-app-rewired start",
- Instala typescript: "npm installl -D typescript" o "npm installl -D -w ui typescript"
- Después de cambiar "package.json", ejecuta "npm update" o "npm update -w ui" antes de iniciar la app.

* Actualización de dependencias:

```bash
npm install -D jest@latest jest-environment-jsdom@latest @babel/core
# o: pnpm up --latest -D -filter ui jest jest-environment-jsdom
```

* Actualizar `ui/Makefile`

Reemplazos:

* `. ./node_modules/genericsuite/scripts` -> `. ../node_modules/genericsuite-fe-scripts/scripts`

* `bash ./node_modules/genericsuite/scripts` -> `bash ../node_modules/genericsuite-fe-scripts/scripts`


Agregar `tailwind-build` a deploy_* y run_* para asegurarse de que el CSS se construya antes de desplegar o ejecutar la app.

```makefile
deploy: tailwind-build config
	bash ../node_modules/genericsuite-fe-scripts/scripts/aws_deploy_to_s3.sh

deploy_qa: tailwind-build config_qa
	bash ../node_modules/genericsuite-fe-scripts/scripts/aws_deploy_to_s3.sh

deploy_demo: tailwind-build config_demo
	bash ../node_modules/genericsuite-fe-scripts/scripts/aws_deploy_to_s3.sh

run: tailwind-build config
	bash ../node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh dev

run_qa: tailwind-build config_qa
	bash ../node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh qa

run_prod: tailwind-build build-prod
	# bash ../node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh prod
	npm start

server: run
start: run
local: run
```

En monorepos, añade `copy_root_env` al Makefile de tu repositorio `ui/frontend`.

```makefile
.DEFAULT_GOAL := help
.PHONY: help install update lock build-dev build-prod build dev clean fresh link_config_dirs unlink_config_dirs tests-dev tests test test-run-build test-run-build-restore eject-dev config config_qa config_demo deploy deploy_qa deploy_demo run run_qa server start local run_prod tailwind tailwind-build add_submodules create_ssl_certs
SHELL := /bin/bash
        .
        .

build-dev: copy_root_env
	...

build-prod: copy_root_env
	...

        .
        .

copy_root_env:
	cp ../.env .env

link_config_dirs: copy_root_env

        .
        .

test-run-build:
	. ../node_modules/genericsuite-fe-scripts/scripts/build_prod_test.sh
	. ../node_modules/genericsuite-fe-scripts/scripts/build_prod_test.sh restore
 
test-run-build-restore:
	. ../node_modules/genericsuite-fe-scripts/scripts/build_prod_test.sh restore

        .
        .

config: link_config_dirs
	bash ../node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh dev

config_qa: link_config_dirs
	bash ../node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh qa

config_demo: link_config_dirs
	bash ../node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh demo

deploy: config
	bash ../node_modules/genericsuite-fe-scripts/scripts/aws_deploy_to_s3.sh

deploy_qa: config_qa
	bash ../node_modules/genericsuite-fe-scripts/scripts/aws_deploy_to_s3.sh

deploy_demo: config_demo
	bash ../node_modules/genericsuite-fe-scripts/scripts/aws_deploy_to_s3.sh

run: config
	bash ../node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh dev

run_qa: config_qa
	bash ../node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh qa

        .
        .

run_prod: build-prod
	# bash ../node_modules/genericsuite-fe-scripts/scripts/run_app_frontend.sh prod
	npm start

add_submodules:
	bash ../node_modules/genericsuite-fe-scripts/scripts/add_github_submodules.sh

create_ssl_certs:
	bash ../node_modules/genericsuite-fe-scripts/scripts/create_ssl_certs.sh
```

## SERVIDOR

* Actualiza `server/package.json`

```json
  "devDependencies": {
    "genericsuite-be-scripts": "github:tomkat-cr/genericsuite-be-scripts#develop"
  }
```

* Actualiza `server/Makefile`

```makefile
.DEFAULT_GOAL := help
.PHONY:  help install install_dev locked_dev locked_install lock_pip_file requirements clean clean_rm clean_temp_dir clean_logs fresh install_tools lsof test test_only lint types coverage format format_check qa local-db-up local-db-down mongo_backup mongo_restore config config_dev config_local config_qa config_qa_for_deployment config_staging build build_local build_check unbuild unbuild_qa unbuild_staging delete_stack create_s3_bucket_dev create_s3_bucket_qa create_s3_bucket_staging create_s3_bucket_prod create_s3_bucket_demo create_aws_config generate_sam_dynamodb deploy_qa deploy_run_local_qa deploy_validate_qa deploy_package_qa deploy_staging deploy_prod deploy_demo deploy run run_qa down_qa restart_qa run_local_docker run_prod add_submodules init_submodules local_dns local_dns_restart local_dns_rebuild local_dns_down local_dns_test copy_ssl_certs create_ssl_certs_only create_ssl_certs init_sam init_chalice generate_seed lock pre-publish publish pypi-build pypi-publish-test pypi-publish create-supad
SHELL := /bin/bash

        .
        .

#- mongo_docker:
local-db-up: copy_root_env
	# Anteriormente: mongo_docker

#- mongo_docker_down:
local-db-down: copy_root_env
	# Anteriormente: mongo_docker_down

        .
        .

local-db-logs: copy_root_env
	bash ../node_modules/genericsuite-be-scripts/scripts/local_db/run_local_db_docker.sh logs

create-supad: copy_root_env
	# E.g. CHECKING=1 STAGE=dev make create_supad
	bash ../node_modules/genericsuite-be-scripts/scripts/run_create_supad.sh

mongo_backup: copy_root_env
	# E.g. STAGE=qa BACKUP_DIR=/tmp/fastapitemplate make mongo_backup
	bash ../node_modules/genericsuite-be-scripts/scripts/mongo/db_mongo_backup.sh ${STAGE} ${BACKUP_DIR}

mongo_restore: copy_root_env
	# E.g. STAGE=qa RESTORE_DIR=/tmp/fastapitemplate make mongo_restore

#- create-supad:
#- 	# E.g. CHECKING=1 STAGE=dev make create-supad
#- 	bash ../node_modules/genericsuite-be-scripts/scripts/run_create_supad.sh

        .
        .

## Postgres

generate_cf_postgres: copy_root_env
	# Generar sentencias SQL para crear las tablas...
	#   ACTION=generate STAGE=dev make generate_cf_postgres
	# Crear las tablas en la base de datos...
	#   ACTION=create_tables STAGE=dev make generate_cf_postgres
	#
	DB_TYPE=postgres bash ../node_modules/genericsuite-be-scripts/scripts/sql_db/generate_sql_db_cf/generate_sql_db_cf.sh 

generate_postgres_dev_sql: copy_root_env
	ACTION=generate STAGE=dev make generate_cf_postgres

create_postgres_dev_tables: copy_root_env
	ACTION=create_tables STAGE=dev make generate_cf_postgres

deploy_postgres: copy_root_env
	# Listar las tablas en la base de datos...
	#   ACTION=list_tables STAGE=dev make deploy_postgres
	TARGET=postgres bash ../node_modules/genericsuite-be-scripts/scripts/sql_db/run_sql_db_deploy.sh

## MySQL

generate_cf_mysql: copy_root_env
	# Generar sentencias SQL para crear las tablas...
	#   ACTION=generate STAGE=dev make generate_cf_mysql
	# Crear las tablas en la base de datos...
	#   ACTION=create_tables STAGE=dev make generate_cf_mysql
	#
	DB_TYPE=mysql bash ../node_modules/genericsuite-be-scripts/scripts/sql_db/generate_sql_db_cf/generate_sql_db_cf.sh 

generate_mysql_dev_sql: copy_root_env
	ACTION=generate STAGE=dev make generate_cf_mysql

create_mysql_dev_tables: copy_root_env
	ACTION=create_tables STAGE=dev make generate_cf_mysql

deploy_mysql: copy_root_env
	# Listar las tablas en la base de datos...
	#   ACTION=list_tables STAGE=dev make deploy_mysql
	#
	TARGET=mysql bash ../node_modules/genericsuite-be-scripts/scripts/sql_db/run_sql_db_deploy.sh

# Directorios de Configuración

copy_root_env:
	cp ../.env .env

        .
        .

link_config_dirs: copy_root_env

        .
        .

build: copy_root_env
    ...

build_local: copy_root_env
    ...

build_check: copy_root_env
    ...

unbuild_qa: copy_root_env
    ...

unbuild_staging: copy_root_env
    ...

delete_stack: copy_root_env
    ...

create_s3_bucket_dev: copy_root_env
    ...

create_s3_bucket_qa: copy_root_env
    ...

create_s3_bucket_staging: copy_root_env
    ...

create_s3_bucket_prod: copy_root_env
    ...

create_aws_config: copy_root_env
    ...

generate_sam_dynamodb: copy_root_env
    ...

generate_cf_dynamodb: copy_root_env
    ...

deploy_ecr_creation: copy_root_env
    ...

deploy_ec2: copy_root_env
    ...

deploy_dynamodb: copy_root_env
    ...

aws_secrets: copy_root_env
    ...
```

Actualizar la versión de Python a 3.14

* Archivo: `server/.python-version`

```python
3.14
```

* Archivo: `server/scripts/aws_big_lambda/template-sam.yml`

Reemplazar:

```yaml
	HUGGINGFACE_TEXT_TO_IMAGE_ENDPOINT: HUGGINGFACE_TEXT_TO_IMAGE_ENDPOINT_placeholder
```

Con:

```yaml
	HUGGINGFACE_DEFAULT_CHAT_MODEL: HUGGINGFACE_DEFAULT_CHAT_MODEL_placeholder
```

Eliminar:

```yaml
	Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /asset/{item_id}
            Method: get
            RestApiId:
              Ref: RestAPI
```

Reemplazar:

```yaml
		Runtime: python3.12  ## or python3.11, 3.10, etc.
```

Con:

```yaml
		Runtime: python3.14
```

Agregar `v1/` a todas las definiciones de endpoints:

```yaml
	...
        paths:
			...

# Ejemplo: `/menu_options:` -> `/v1/menu_options:`
```

Si planeas usar la plantilla AWS Big Lambda con FastAPI múltiples Orígenes CORS:

* Archivo: `server/scripts/aws_big_lambda/template-sam.yml`

Comenta la sección de Cors para permitir todos los orígenes y dejar que FastAPI gestione el CORS. FastAPI gestionará múltiples orígenes al dividir la cadena `CORS_ORIGIN` si contiene comas.

```yaml
      # Cors:
      #   AllowMethods: "'GET,POST,PUT,DELETE,OPTIONS'"
      #   AllowHeaders: "'Access-Control-Allow-Origin,Authorization,Content-Type,X-Amz-Date,X-Amz-Security-Token,X-Api-Key'"
      #   AllowOrigin: "'APP_CORS_ORIGIN_placeholder'"
      #   AllowCredentials: "'true'"
```

Reemplaza todo:

```yaml
        paths:
			...
          /v1/<path>:
		  		...
            get:  ## o post, put, delete, etc.
		  		...
            options:
				...
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                requestTemplates:
                  application/json: '{"statusCode": 200}'
                passthroughBehavior: when_no_match
                type: mock
                contentHandling: CONVERT_TO_TEXT
```

Con:

```yaml
        paths:
			...
          /v1/<path>:
		  		...
            get:  ## o post, put, delete, etc.
		  		...
            options:
				...
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                type: aws_proxy
```

Y reemplaza todo:

```yaml
        paths:
			...
          /v1/<path>:
		  		...
            get:  ## o post, put, delete, etc.
		  		...
            options:
				...
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                type: aws_proxy
```

Y reemplaza todo:

```yaml
        paths:
			...
          /v1/<path>:
		  		...
            get:  ## o post, put, delete, etc.
		  		...
            options:
				...
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                    responseParameters:
                      method.response.header.Access-Control-Allow-Methods: '''GET,OPTIONS'''
                      method.response.header.Access-Control-Allow-Origin: '''http://localhost:3000'''
                      method.response.header.Access-Control-Allow-Headers: '''Access-Control-Allow-Origin,Authorization,Content-Type,X-Amz-Date,X-Amz-Security-Token,X-Api-Key'''
                      method.response.header.Access-Control-Expose-Headers: '''Authorization,Access-Control-Allow-Origin,Content-Type,Content-Disposition,Content-Length'''
                      method.response.header.Access-Control-Max-Age: '''600'''
                      method.response.header.Access-Control-Allow-Credentials: '''true'''
                requestTemplates:
                  application/json: '{"statusCode": 200}'
                passthroughBehavior: when_no_match
                type: mock
                contentHandling: CONVERT_TO_TEXT
```

Con:

```yaml
        paths:
			...
          /v1/<path>:
		  		...
            get:  ## o post, put, delete, etc.
		  		...
            options:
				...
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                type: aws_proxy
```

## MÓVIL

* Archivo: `mobile/web/index.html`

```css
      #loading img {
        ...
        border-radius: 50%;
      }
```

### MCP

Archivo: `mcp_server/mcp_server.py` o `server/lib/mcp_server.py`

Añade import dotenv y load_dotenv() al principio (antes de las importaciones de GS):

```python
import dotenv

# Para evitar que autopep8 y/o flake8 (u otros formateadores/linters)
# muevan `dotenv.load_dotenv()` después de las importaciones:
# 1. usa `# noqa: F401` para indicar a los linters/formatters que ignoren esa línea.
# 2. usa comentarios 'isort: off/on' para indicar a isort que ignore reordenamiento,

# isort: off
dotenv.load_dotenv()  # noqa: F401
# isort: on
```


## SOLUCIÓN DE PROBLEMAS

### npm error Missing script: "build"

Para resolver el error 'npm error Missing script: "build"' al actualizar el paquete ui/frontend:

```bash
cd /ruta/a tu/app/momonorepo/raíz
make install
```

```text
> genericsuite-fe-scripts@1.0.0 publish
│ > bash scripts/npm_publish.sh publish
│ Turn on module...
│ npx @tailwindcss/cli -i ./src/input.css -o ./public/output.css
│ npm warn Unknown env config "20". This will stop working in the next major version of npm. See `npm help npmr…
│ npm warn Unknown env config "_jsr-registry". This will stop working in the next major version of npm. See `np…
│ ≈ tailwindcss v4.3.2
│ Specified input file `./src/input.css` does not exist.
│ make[1]: *** [tailwind-build] Error 1
│ Checking react-app-rewired installation... ()
│ Checking vite installation... ()
│ Checking webpack installation... ()
│ Testing app...
│ npm warn Unknown env config "20". This will stop working in the next major version of npm. See `npm help npmr…
│ npm warn Unknown env config "_jsr-registry". This will stop working in the next major version of npm. See `np…
│ > genericsuite-fe-scripts@1.0.0 test
│ > echo "No test necessary for genericsuite-fe-scripts"
│ No test necessary for genericsuite-fe-scripts
│ Package Lock (to update App version)...
│ npm warn Unknown env config "20". This will stop working in the next major version of npm. See `npm help npmr…
│ npm warn Unknown env config "_jsr-registry". This will stop working in the next major version of npm. See `np…
│ up to date, audited 1 package in 75ms
│ found 0 vulnerabilities
│ Building React app...
│ npm warn Unknown env config "20". This will stop working in the next major version of npm. See `npm help npmr…
│ npm warn Unknown env config "_jsr-registry". This will stop working in the next major version of npm. See `np…
│ npm error Missing script: "build"
│ npm error
│ npm error To see a list of scripts, run:
│ npm error   npm run
│ npm error A complete log of this run can be found in: $HOME/.npm/_logs/2026-07-12T16_38_45_382…
│ ERROR running: npm run build
└─ Failed in 1.3s at $HOME/Library/pnpm/store/v10/tmp/_tmp_xxx_yyyyyyy
$HOME/desarrollo/genericsuite/packages/genericsuite-basecamp/mkdocs_root/code/exampleapp/apps/ui:
 ERR_PNPM_PREPARE_PACKAGE  Failed to prepare git-hosted package fetched from "https://codeload.github.com/tomkat-cr/genericsuite-fe-scripts/tar.gz/3c4f6edbce4fb9e62a0b2251fc97f360469db3ed": genericsuite-fe-scripts@1.0.0 npm-run-publish: `npm run publish`
Exit status 1
```

SOLUCIÓN:
* Agrega los scripts "test" y "build" al package.json de GS FE Scripts.

### ERESOLVE unable to resolve dependency tree... While resolving: formik@2.4.5

Para resolver el siguiente error actualizando el paquete ui/frontend:
"ERESOLVE unable to resolve dependency tree... While resolving: ui@x.x.x. formik@2.4.5"

Por ejemplo:

```bash
cd ui
make build
```

```text
npm error code ERESOLVE
npm error ERESOLVE unable to resolve dependency tree
npm error
npm error While resolving: ui@1.0.0
npm error Found: formik@2.4.5
npm error node_modules/formik
npm error   peer formik@"2.4.5" from genericsuite-ai@1.2.0
npm error   node_modules/genericsuite-ai
npm error     genericsuite-ai@"*" from the root project
npm error
npm error Could not resolve dependency:
npm error peer formik@"^2.4.9" from genericsuite@1.2.0
npm error node_modules/genericsuite
npm error   genericsuite@"*" from the root project
npm error   peer genericsuite@"github:tomkat-cr/genericsuite-fe#develop" from genericsuite-ai@1.2.0
npm error   node_modules/genericsuite-ai
npm error     genericsuite-ai@"*" from the root project
npm error
npm error Fix the upstream dependency conflict, o retry
npm error this command with --force or --legacy-peer-deps
npm error to accept an incorrect (and potentially broken) dependency resolution.
```

Ejemplo de solución (solo para la app de ejemplo)

```bash
npm install genericsuite genericsuite-ai --legacy-peer-deps
# o
npm install tomkat-cr/genericsuite#develop genericsuite-ai#develop --legacy-peer-deps
# o
pnpm up --latest -D -filter ui tomkat-cr/genericsuite#develop tomkat-cr/genericsuite-ai#develop
```

Eso evita el conflicto de pares; no soluciona la desalineación en upstream.

* Recomendación: soluciona en upstream alineando `formik` a ^2.4.9 en tu app. Usa --legacy-peer-deps solo si necesitas que la app de ejemplo funcione de inmediato.

SOLUCIÓN:
* Elimina todos `node_modules` en tu app (desde la raíz del monorepo y `./ui`), luego ejecuta `make install` para actualizar las dependencias.

### ERESOLVE unable to resolve dependency tree... While resolving: @babel/core@8.0.1

```bash
cd /path/to/genericsuite/packages/genericsuite-basecamp/mkdocs_root/code/exampleapp/apps/ui
make install
```

```text
npm install
npm error code ERESOLVE
npm error ERESOLVE unable to resolve dependency tree
npm error
npm error While resolving: ui@1.0.0
npm error Found: @babel/core@8.0.1
npm error node_modules/@babel/core
npm error   dev @babel/core@"^8.0.1" from the root project
npm error
npm error Could not resolve dependency:
npm error peer @babel/core@"^7.0.0-0" from @babel/plugin-proposal-private-property-in-object@7.21.11
npm error node_modules/@babel/plugin-proposal-private-property-in-object
npm error   dev @babel/plugin-proposal-private-property-in-object@"7.21.11" from the root project
npm error
npm error Fix the upstream dependency conflict, o retry this command with --force or --legacy-peer-deps to accept an incorrect (and potentially broken) dependency resolution.
npm error
make: *** [install] Error 1
```

SOLUCIÓN:
* Downgrade las dependencias de @babel a las siguientes versiones:

    "@babel/core": "^7.29.7"
    "@babel/plugin-syntax-jsx": "^7.23.3"
    "@babel/plugin-transform-class-properties": "^7.27.1"
    "@babel/preset-env": "^7.23.3"
    "@babel/preset-react": ^"7.23.3"
    "@babel/preset-typescript": "^7.27.1"

### Invalid hook call. Hooks can only be called inside of the body of a function component.

Actualizando `vite` de 5.4.x a 8.x y/o `vite-plugin-require` de 1.2.x a 1.3.x:

```bash
npm install -D vite@latest vite-plugin-require@latest
# o
npm install -w ui -D vite@latest vite-plugin-require@latest
# o
pnpm up --latest -D -filter ui vite vite-plugin-require
```

La app mostrará una página en blanco y lanzará el siguiente error en las herramientas de desarrollo (Consola de JS):

```text
Warning: Invalid hook call. Hooks can only be called inside of the body of a function component. This could happen for one of the following reasons:
1. You might have mismatching versions of React and the renderer (such as React DOM)
2. You might be breaking the Rules of Hooks
3. You might have more than one copy of React in the same app
See https://reactjs.org/link/invalid-hook-call for tips about how to debug and fix this problem.
```

SOLUCIÓN:

Archivo: `ui/vite.config.js` o `ui/vite.config.mjs`

Reemplazar:

```js
  resolve: {
      alias: {
          '@': resolve(__dirname, 'src'),
      },
      extensions: ['.js', '.jsx', '.ts', '.tsx', '.json', '.svg']
  },
```

Con:

```js
  resolve: {
      alias: {
          '@': resolve(__dirname, 'src'),
          // Resolver los módulos de React y React DOM a la versión correcta en este workspace, no en el workspace raíz
          // react: resolve(__dirname, 'node_modules/react'),
          // 'react-dom': resolve(__dirname, 'node_modules/react-dom'),
      },
      // Resolver los módulos de React y React DOM a la versión correcta en este workspace, no en el workspace raíz
      // dedupe: ['react', 'react-dom'],
      extensions: ['.js', '.jsx', '.ts', '.tsx', '.json', '.svg']
  },
```

### Your Vite config uses features that are unsupported by configLoader: 'native'

Para resolver el siguiente error actualizando el paquete ui/frontend:

```text
(!) Your Vite config uses features that are unsupported by `configLoader: 'native'`, which is planned to become the default in a future major version of Vite: `__dirname` (vite.config.mjs:54:42). Use `import.meta.dirname` instead
```

SOLUCIÓN:
* Actualiza el archivo `vite.config.mjs`, reemplazando todos `__dirname` por `import.meta.dirname`.


### UNLOADABLE_DEPENDENCY: Could not load node_modules/react | react-dom

Usando pnpm v11 o superior, puede ocurrir el siguiente error al ejecutar el paquete frontend:

```text
 [UNLOADABLE_DEPENDENCY] Could not load node_modules/react
     ╭─[ ../../node_modules/.pnpm/genericsuite-ai@https+++codeload.github.com+tomkat-cr+genericsuite-fe-ai+tar.gz+5b577fc_2117b50704b308a2c56f07e031a263a8/node_modules/genericsuite-ai/dist/esm/index.js:1:64 ]
     │
   1 │ import React, { useState, useRef, useEffect, useReducer } from 'react';
     │                                                                ───┬───
     │                                                                   ╰───── No such file or directory (os error 2)
  ───╯

  [UNLOADABLE_DEPENDENCY] Could not load node_modules/react/jsx-runtime
       ╭─[ ../../node_modules/.pnpm/react-markdown@10.1.0_@types+react@19.1.0_react@18.3.1_supports-color@8.1.1/node_modules/react-markdown/lib/index.js:109:35 ]
       │
   109 │ import {Fragment, jsx, jsxs} from 'react/jsx-runtime'
       │                                   ─────────┬─────────
       │                                            ╰─────────── No such file or directory (os error 2)
  ─────╯

  [UNLOADABLE_DEPENDENCY] Could not load node_modules/react-dom
      ╭─[ ../../node_modules/.pnpm/react-router@7.18.2_react-dom@18.3.1_react@18.3.1__react@18.3.1/node_modules/react-router/dist/development/dom-export.mjs:53:27 ]
      │
   53 │ import * as ReactDOM from "react-dom";
      │                           ╭───────┬─────
      │                                ╰─────── No such file or directory (os error 2)
  ────╯

      at aggregateBindingErrorsIntoJsError ... {
    errors: [Getter/Setter]
  }
```

Causa raíz: ui/src importa React, react-dom/client y react-router-dom directamente, pero ui/package.json nunca los declaró como dependencias — eran solo dependencias pares de genericsuite/genericsuite-ai. Bajo el aislamiento estricto de pnpm, una dependencia par solo se enlaza en node_modules de un paquete si ese paquete lo lista explícitamente. Así que ui/node_modules/react nunca existió, y el alias de vite.config.mjs (react: resolve(import.meta.dirname, 'node_modules/react')) apuntaba a una ruta inexistente, lo que hizo que el optimizador de dependencias de Vite/Rolldown se bloqueara con UNLOADABLE_DEPENDENCY ... No se encontró el directorio.

SOLUCIÓN:
* Añade react, react-dom y react-router-dom como dependencias a `ui/package.json`.

```json
"dependencies": {
      ...
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^7.18.2"
}
```