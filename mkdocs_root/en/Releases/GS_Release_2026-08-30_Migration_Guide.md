# 20260830 - v1.0.0 - Migration Guide

Changes to be made in the GS applications with the old version of GS:

## UI

* Review `ui/package.json` to check run scripts the previously pointed to /genericsuite/scripts':

Replace `node_modules/genericsuite/scripts` with `node_modules/genericsuite-fe-scripts/scripts`:

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

To:

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

* Update `ui/package.json`

```json
"devDependencies": {
	"genericsuite-fe-scripts": "github:tomkat-cr/genericsuite-fe-scripts#develop",
},
"dependencies": {
	"genericsuite": "github:tomkat-cr/genericsuite-fe#develop",
    "genericsuite-ai": "github:tomkat-cr/genericsuite-fe-ai#develop"
}
```

Or...

```bash
npm install -ui -D genericsuite-fe-scripts@latest
# or: pnpm add -D -filter ui genericsuite-fe-scripts
npm install -ui genericsuite@latest genericsuite-ai@latest
# or: pnpm up --latest -filter ui genericsuite genericsuite-ai
```

* If you're NOT using Webpack:

```bash
npm uninstall css-loader postcss-loader style-loader
# or: pnpm remove -r -filter ui css-loader postcss-loader style-loader
```

* Other dependencies clean-up:

For consumers of `genericsuite-fe` (these were peer dependencies, so downstream apps installed them directly):

```bash
npm uninstall react-icons web-vitals fs json-loader with constants-browserify crypto-browserify os-browserify stream-browserify tty-browserify url vm-browserify
# or: pnpm remove -r -filter ui react-icons web-vitals fs json-loader with constants-browserify crypto-browserify os-browserify stream-browserify tty-browserify url vm-browserify
```

For anyone building/contributing to `genericsuite-fe` itself (devDependencies, only relevant if they run `npm install` against this repo's own `package.json`):

```bash
npm uninstall @babel/cli @babel/preset-stage-0 @rollup/plugin-typescript @testing-library/user-event file-loader url-loader path
# or: pnpm remove -r -filter ui @babel/cli @babel/preset-stage-0 @rollup/plugin-typescript @testing-library/user-event file-loader url-loader path
```

* If you're not using Github Pages deployment:

```bash
npm uninstall gh-pages
# or: pnpm remove -r -filter ui gh-pages
```

* If you are not using Express:

```bash
npm uninstall express express-rate-limit
# or: pnpm remove -r -filter ui express express-rate-limit
```

* If you're using React Rewired:

1. Replace your "config-overrides.js" with the one in "/node_modules/genericsuite-fe"

2. File: "package.json"

- If there is a "type": "module" attribute, rename it to e.g. "type1"
- If there is a "homepage": "..." attribute, rename it to e.g. "homepage1" (unless you really need a URL # suffix)
- If there is a "eslintConfig": "..." attribute, rename it to e.g. "eslintConfig1"
- Add the following entry to "scripts":
    "start-dev:react-app-rewired": "bash ../node_modules/genericsuite-fe-scripts/scripts/change_env_be_endpoint.sh dev && npx react-app-rewired start",
- Install typescript: "npm installl -D typescript" or "npm installl -D -w ui typescript"
- After changing "package.json", run "npm update" or "npm update -w ui" before start the app.

* Upgrade dependencies:

```bash
npm install -D jest@latest jest-environment-jsdom@latest @babel/core
# or: pnpm up --latest -D -filter ui jest jest-environment-jsdom
```

* Update `ui/Makefile`

Replacements:

* `. ./node_modules/genericsuite/scripts` -> `. ../node_modules/genericsuite-fe-scripts/scripts`

* `bash ./node_modules/genericsuite/scripts` -> `bash ../node_modules/genericsuite-fe-scripts/scripts`


Add `tailwind-build` to deploy_* and run_* targets to make sure the CSS is built before deploying or running the app.

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

On monorepos, add `copy_root_env` to the `Makefile` of your `ui/frontend` repo.

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
    ...

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

## SERVER

* Update `server/package.json`

```json
  "devDependencies": {
    "genericsuite-be-scripts": "github:tomkat-cr/genericsuite-be-scripts#develop"
  }
```

* Update `server/Makefile`

```makefile
.DEFAULT_GOAL := help
.PHONY:  help install install_dev locked_dev locked_install lock_pip_file requirements clean clean_rm clean_temp_dir clean_logs fresh install_tools lsof test test_only lint types coverage format format_check qa local-db-up local-db-down mongo_backup mongo_restore config config_dev config_local config_qa config_qa_for_deployment config_staging build build_local build_check unbuild unbuild_qa unbuild_staging delete_stack create_s3_bucket_dev create_s3_bucket_qa create_s3_bucket_staging create_s3_bucket_prod create_s3_bucket_demo create_aws_config generate_sam_dynamodb deploy_qa deploy_run_local_qa deploy_validate_qa deploy_package_qa deploy_staging deploy_prod deploy_demo deploy run run_qa down_qa restart_qa run_local_docker run_prod add_submodules init_submodules local_dns local_dns_restart local_dns_rebuild local_dns_down local_dns_test copy_ssl_certs create_ssl_certs_only create_ssl_certs init_sam init_chalice generate_seed lock pre-publish publish pypi-build pypi-publish-test pypi-publish create-supad
SHELL := /bin/bash

        .
        .

#- mongo_docker:
local-db-up: copy_root_env
	# Previously: mongo_docker

#- mongo_docker_down:
local-db-down: copy_root_env
	# Previously: mongo_docker_down

        .
        .

local-db-logs: copy_root_env
	bash ../node_modules/genericsuite-be-scripts/scripts/local_db/run_local_db_docker.sh logs

create-supad: copy_root_env
	# E.g. CHECKING=1 STAGE=dev make create-supad
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
	# Generate SQL statements to create the tables...
	#   ACTION=generate STAGE=dev make generate_cf_postgres
	# Create the tables in the database...
	#   ACTION=create_tables STAGE=dev make generate_cf_postgres
	#
	DB_TYPE=postgres bash ../node_modules/genericsuite-be-scripts/scripts/sql_db/generate_sql_db_cf/generate_sql_db_cf.sh 

generate_postgres_dev_sql: copy_root_env
	ACTION=generate STAGE=dev make generate_cf_postgres

create_postgres_dev_tables: copy_root_env
	ACTION=create_tables STAGE=dev make generate_cf_postgres

deploy_postgres: copy_root_env
	# List the tables in the database...
	#   ACTION=list_tables STAGE=dev make deploy_postgres
	TARGET=postgres bash ../node_modules/genericsuite-be-scripts/scripts/sql_db/run_sql_db_deploy.sh

## MySQL

generate_cf_mysql: copy_root_env
	# Generate SQL statements to create the tables...
	#   ACTION=generate STAGE=dev make generate_cf_mysql
	# Create the tables in the database...
	#   ACTION=create_tables STAGE=dev make generate_cf_mysql
	#
	DB_TYPE=mysql bash ../node_modules/genericsuite-be-scripts/scripts/sql_db/generate_sql_db_cf/generate_sql_db_cf.sh 

generate_mysql_dev_sql: copy_root_env
	ACTION=generate STAGE=dev make generate_cf_mysql

create_mysql_dev_tables: copy_root_env
	ACTION=create_tables STAGE=dev make generate_cf_mysql

deploy_mysql: copy_root_env
	# List the tables in the database...
	#   ACTION=list_tables STAGE=dev make deploy_mysql
	#
	TARGET=mysql bash ../node_modules/genericsuite-be-scripts/scripts/sql_db/run_sql_db_deploy.sh

# Config directories

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

Upgrade python version to 3.14

* File: `server/.python-version`

```python
3.14
```

* File: `server/scripts/aws_big_lambda/template-sam.yml`

Replace:

```yaml
	HUGGINGFACE_TEXT_TO_IMAGE_ENDPOINT: HUGGINGFACE_TEXT_TO_IMAGE_ENDPOINT_placeholder
```

With:

```yaml
	HUGGINGFACE_DEFAULT_CHAT_MODEL: HUGGINGFACE_DEFAULT_CHAT_MODEL_placeholder
```

Remove:

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

Replace:

```yaml
		Runtime: python3.12  ## or python3.11, 3.10, etc.
```

With:

```yaml
		Runtime: python3.14
```

Add `v1/` to all endpoint definitions:

```yaml
	...
        paths:
			...

# Example: `/menu_options:` -> `/v1/menu_options:`
```

If you plan to use the AWS Big Lambda template with FastAPI multiple CORS Origins:

* File: `server/scripts/aws_big_lambda/template-sam.yml`

Comment the `Cors` section to allow all origins and let FastAPI handle the CORS. FastAPI will handle multiple origins by splitting the `CORS_ORIGIN` string if it contains commas.

```yaml
      # Cors:
      #   AllowMethods: "'GET,POST,PUT,DELETE,OPTIONS'"
      #   AllowHeaders: "'Access-Control-Allow-Origin,Authorization,Content-Type,X-Amz-Date,X-Amz-Security-Token,X-Api-Key'"
      #   AllowOrigin: "'APP_CORS_ORIGIN_placeholder'"
      #   AllowCredentials: "'true'"
```

Replace all:

```yaml
        paths:
			...
          /v1/<path>:
		  		...
            get:  ## or post, put, delete, etc.
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

With:

```yaml
        paths:
			...
          /v1/<path>:
		  		...
            get:  ## or post, put, delete, etc.
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

And replace all:

```yaml
        paths:
			...
          /v1/<path>:
		  		...
            get:  ## or post, put, delete, etc.
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

With:

```yaml
        paths:
			...
          /v1/<path>:
		  		...
            get:  ## or post, put, delete, etc.
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

## MOBILE

* File: `mobile/web/index.html`

```css
      #loading img {
        ...
        border-radius: 50%;
      }
```

### MCP

File: `mcp_server/mcp_server.py` or `server/lib/mcp_server.py`

Add import dotenv and load_dotenv() at the beginning (before the GS imports):

```python
import dotenv

# To prevent autopep8 and/or flake8 (or other formatters/linters)
# from moving `dotenv.load_dotenv()` after imports:
# 1. use `# noqa: F401` to signal linters/flakers to ignore that line.
# 2. use 'isort: off/on' comments to instruct isort to ignore reordering,

# isort: off
dotenv.load_dotenv()  # noqa: F401
# isort: on
```


## TROUBLESHOOTING

### npm error Missing script: "build"

To solve the error 'npm error Missing script: "build"' updating the ui/frontend package:

```bash
cd /path/to/your/app/momnorepo/root
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

SOLUTION:
* Add the scripts "test" and "build" to the package.json of GS FE Scripts.

### ERESOLVE unable to resolve dependency tree... While resolving: formik@2.4.5

To solve the following error updating the ui/frontend package:
"ERESOLVE unable to resolve dependency tree... While resolving: ui@x.x.x. formik@2.4.5"

For example:

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
npm error Fix the upstream dependency conflict, or retry
npm error this command with --force or --legacy-peer-deps
npm error to accept an incorrect (and potentially broken) dependency resolution.
```

Workaround (example app only)

```bash
npm install genericsuite genericsuite-ai --legacy-peer-deps
# or
npm install tomkat-cr/genericsuite#develop genericsuite-ai#develop --legacy-peer-deps
# or
pnpm up --latest -D -filter ui tomkat-cr/genericsuite#develop tomkat-cr/genericsuite-ai#develop
```

That skips the peer conflict; it does not fix the upstream mismatch.

* Recommendation: fix upstream by aligning `formik` to ^2.4.9 in your app. Use --legacy-peer-deps only if you need the example app working immediately.

SOLUTION:
* Delete all `node_modules` on you app (from the monorepo root and `./ui`), then run `make install` to update the dependencies.

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
npm error Fix the upstream dependency conflict, or retry this command with --force or --legacy-peer-deps to accept an incorrect (and potentially broken) dependency resolution.
npm error
make: *** [install] Error 1
```

SOLUTION:
* Downgrade @babel dependencies to the following versions:

    "@babel/core": "^7.29.7"
    "@babel/plugin-syntax-jsx": "^7.23.3"
    "@babel/plugin-transform-class-properties": "^7.27.1"
    "@babel/preset-env": "^7.23.3"
    "@babel/preset-react": "^7.23.3"
    "@babel/preset-typescript": "^7.27.1"

### Invalid hook call. Hooks can only be called inside of the body of a function component.

Upgrading `vite` from 5.4.x to 8.x and/or `vite-plugin-require` from 1.2.x to 1.3.x:

```bash
npm install -D vite@latest vite-plugin-require@latest
# or
npm install -w ui -D vite@latest vite-plugin-require@latest
# or
pnpm up --latest -D -filter ui vite vite-plugin-require
```

The app will show a blank page and throw the following error in the Developer Tools (JS Console):

```text
Warning: Invalid hook call. Hooks can only be called inside of the body of a function component. This could happen for one of the following reasons:
1. You might have mismatching versions of React and the renderer (such as React DOM)
2. You might be breaking the Rules of Hooks
3. You might have more than one copy of React in the same app
See https://reactjs.org/link/invalid-hook-call for tips about how to debug and fix this problem.
```

SOLUTION:

File: `ui/vite.config.js` or `ui/vite.config.mjs`

Replace:

```js
  resolve: {
      alias: {
          '@': resolve(__dirname, 'src'),
      },
      extensions: ['.js', '.jsx', '.ts', '.tsx', '.json', '.svg']
  },
```

With:

```js
  resolve: {
      alias: {
          '@': resolve(__dirname, 'src'),
          // Resolve the React and React DOM modules to the correct version on this workspace, not the root workspace
          // react: resolve(__dirname, 'node_modules/react'),
          // 'react-dom': resolve(__dirname, 'node_modules/react-dom'),
      },
      // Resolve the React and React DOM modules to the correct version on this workspace, not the root workspace
      // dedupe: ['react', 'react-dom'],
      extensions: ['.js', '.jsx', '.ts', '.tsx', '.json', '.svg']
  },
```

### Your Vite config uses features that are unsupported by configLoader: 'native'

To solve the following error updating the ui/frontend package:

```text
(!) Your Vite config uses features that are unsupported by `configLoader: 'native'`, which is planned to become the default in a future major version of Vite: `__dirname` (vite.config.mjs:54:42). Use `import.meta.dirname` instead
```

SOLUTION:
* Update the `vite.config.mjs` file, replacing all `__dirname` with `import.meta.dirname`.


### UNLOADABLE_DEPENDENCY: Could not load node_modules/react | react-dom

Using pnpm v11 or higher, the following error may occur running the frontend package:

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
      │                           ─────┬─────
      │                                ╰─────── No such file or directory (os error 2)
  ────╯

      at aggregateBindingErrorsIntoJsError ... {
    errors: [Getter/Setter]
  }
```

Root cause: ui/src imports react, react-dom/client, and react-router-dom directly, but ui/package.json never declared them as dependencies — they were only peerDependencies of genericsuite/genericsuite-ai. **Under pnpm's strict, isolated node_modules, a peer dep only gets symlinked into a package's own node_modules if that package explicitly lists it**. So ui/node_modules/react never existed, and vite.config.mjs's alias (react: resolve(import.meta.dirname, 'node_modules/react')) pointed at a nonexistent path — causing Vite/Rolldown's dependency optimizer to crash with UNLOADABLE_DEPENDENCY ... No such file or directory.

SOLUTION:
* Add react, react-dom, and react-router-dom as dependencies to the ui/package.json file.

```json
"dependencies": {
      ...
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^7.18.2"
}
```
