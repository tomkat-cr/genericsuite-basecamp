# .DEFAULT_GOAL := local
.PHONY: tests venv
SHELL := /bin/bash

# General Commands
help:
	cat Makefile

install:
	pnpm install

update:
	pnpm update

update-pnpm: install

build:
	pnpx turbo build --force

check:
	pnpx turbo check-types

check-build:
	pnpx turbo check-types build

link:
	sh scripts/link_common_assets.sh link

unlink:
	sh scripts/link_common_assets.sh unlink
	cd apps/ui && bash node_modules/genericsuite/scripts/run_symlinks_handler.sh remove

down_docker:
	cd apps/api-chalice && make down_qa

shut_down: down_docker unlink

init-env-files:
	sh scripts/init_env_files.sh

build-if-required:
	bash scripts/build_if_required.sh

dev: link build-if-required
	# pnpx turbo dev; (exit_code=$$?; make shut_down; exit $$exit_code)
	# pnpx turbo watch dev; (exit_code=$$?; make shut_down; exit $$exit_code)
	node scripts/run-api-conditional.js; (exit_code=$$?; make shut_down; exit $$exit_code)

run: dev
	# pnpx turbo start --force

make create-ssl-certs:
	cd apps/api-chalice && make create_ssl_certs
	cp apps/api-chalice/*.crt apps/api-fastapi
	cp apps/api-chalice/*.key apps/api-fastapi
	cp apps/api-chalice/*.crt apps/api-flask
	cp apps/api-chalice/*.key apps/api-flask
