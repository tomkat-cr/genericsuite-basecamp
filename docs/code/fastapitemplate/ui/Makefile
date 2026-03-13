# .DEFAULT_GOAL := local
# .PHONY: tests
SHELL := /bin/bash

# General Commands

help:
	cat Makefile

install:
	# npm install
	@echo "Installing dependencies made by root npm install"

update:
	npm update

lock:
	npm install --package-lock-only

build-dev:
	npm run build

build-prod:
	npm run build-prod

build: build-dev

dev:
	npm install --dev

clean:
	npm run clean

fresh: clean install

# Config directories

link_config_dirs:
	if [ -d ./src/configs ]; then rm -rf ./src/configs; fi
	cp -R ../config_dbdef ./src/configs

unlink_config_dirs:
	if [ -d ./src/configs ]; then rm -rf ./src/configs; fi

# Development Commands

tests-dev:
	npm run test-dev

tests:
	npm test

test: tests

test-run-build:
	. ./node_modules/genericsuite/scripts/build_prod_test.sh
	. ./node_modules/genericsuite/scripts/build_prod_test.sh restore
 
test-run-build-restore:
	. ./node_modules/genericsuite/scripts/build_prod_test.sh restore

eject-dev:
	npm run eject-dev

config: link_config_dirs
	bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh dev

config_qa: link_config_dirs
	bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh qa

config_demo: link_config_dirs
	bash ./node_modules/genericsuite/scripts/change_env_be_endpoint.sh demo

deploy: config
	bash ./node_modules/genericsuite/scripts/aws_deploy_to_s3.sh

deploy_qa: config_qa
	bash ./node_modules/genericsuite/scripts/aws_deploy_to_s3.sh

deploy_demo: config_demo
	bash ./node_modules/genericsuite/scripts/aws_deploy_to_s3.sh

run: config
	bash ./node_modules/genericsuite/scripts/run_app_frontend.sh dev

run_qa: config_qa
	bash ./node_modules/genericsuite/scripts/run_app_frontend.sh qa

server: run
start: run
local: run

run_prod: build-prod
	# bash ./node_modules/genericsuite/scripts/run_app_frontend.sh prod
	npm start

tailwind:
	npx @tailwindcss/cli -i ./src/input.css -o ./public/output.css --watch

tailwind-build:
	npx @tailwindcss/cli -i ./src/input.css -o ./public/output.css

add_submodules:
	bash ./node_modules/genericsuite/scripts/add_github_submodules.sh

create_ssl_certs:
	bash ./node_modules/genericsuite/scripts/create_ssl_certs.sh
