# .DEFAULT_GOAL := local
.PHONY: help install transfer_debug transfer_cicd transfer publish venv build serve run clean exampleapp-install exampleapp-install-all exampleapp-update exampleapp-update-all exampleapp-run exampleapp-create-ssl-certs exampleapp-clean
SHELL := /bin/bash

EXAMPLEAPP_SERVICES = mcp-server api-chalice api-fastapi api-flask ui


# General Commands
help:
	cat Makefile

install:
	bash scripts/mkdocs_install.sh

prepare_docs:
	make exampleapp-clean
	make fastapitemplate-clean

generate_openapi: fastapitemplate-install
	cd docs/code/fastapitemplate/server && \
	RUN_PROTOCOL=http PATH_TO_SAVE_OPENAPI="." make run_qa && \
	cd -

translate_uncommitted:
	sh scripts/translation/run_translate_uncommitted.sh

sample_code_prepare:
	sh scripts/sample_code_prepare.sh

prepare_all: generate_openapi translate_uncommitted sample_code_prepare prepare_docs

transfer_debug: prepare_all
	bash scripts/mkdocs_transfer_site.sh

transfer_cicd: prepare_all
	# Set DEBUG to false to avoid blocking automation in CI environments
	DEBUG="false" sh scripts/mkdocs_transfer_site.sh

transfer: transfer_cicd

publish: transfer

nvm_use:
	export NVM_DIR="${HOME}/.nvm" && [ -s "${NVM_DIR}/nvm.sh" ] && \. "${NVM_DIR}/nvm.sh" && if ! nvm use; then echo "❌ NVM use failed. Please install it."; fi

venv:
	if ! . scripts/mkdocs_run.sh; then if ! source scripts/mkdocs_run.sh; then @echo "❌ scripts/mkdocs_run.sh failed..."; fi; fi

build: prepare_all
	bash scripts/mkdocs_run.sh build

serve:
	bash scripts/mkdocs_run.sh serve -a localhost:8015

run: prepare_all serve

exampleapp-install: nvm_use
	cd docs/code/exampleapp && make install

exampleapp-install-all: nvm_use
	$(foreach service,$(EXAMPLEAPP_SERVICES),cd docs/code/exampleapp/apps/$(service) && pwd && make install && cd ../../../../../;)

exampleapp-update: nvm_use
	cd docs/code/exampleapp && make update

exampleapp-update-all: nvm_use
	$(foreach service,$(EXAMPLEAPP_SERVICES),cd docs/code/exampleapp/apps/$(service) && pwd && make update && cd ../../../../../;)

exampleapp-run:
	cd docs/code/exampleapp && make run

exampleapp-create-ssl-certs:
	cd docs/code/exampleapp && make create-ssl-certs

exampleapp-clean:
	cd docs/code/exampleapp && sh scripts/link_common_assets.sh unlink
	if [ "${DEBUG}" = "true" ]; then @echo "" && \
	@echo "Press Enter to continue to clean all directories (node_modules, dist, etc.)" && \
	@read; fi
	bash docs/code/exampleapp/scripts/clean_directory.sh ./docs/code/exampleapp false "${DEBUG}"
	bash docs/code/exampleapp/scripts/clean_directory.sh ./docs/code/exampleapp/apps/mcp-server false "${DEBUG}"
	bash docs/code/exampleapp/scripts/clean_directory.sh ./docs/code/exampleapp/apps/api-chalice false "${DEBUG}"
	bash docs/code/exampleapp/scripts/clean_directory.sh ./docs/code/exampleapp/apps/api-fastapi false "${DEBUG}"
	bash docs/code/exampleapp/scripts/clean_directory.sh ./docs/code/exampleapp/apps/api-flask false "${DEBUG}"

fastapitemplate-install: nvm_use
	cd docs/code/fastapitemplate && make install

fastapitemplate-install-all: nvm_use
	cd docs/code/fastapitemplate && make install-all

fastapitemplate-update: nvm_use
	cd docs/code/fastapitemplate && make update

fastapitemplate-update-all: fastapitemplate-update

fastapitemplate-run:
	cd docs/code/fastapitemplate && make dev

fastapitemplate-create-ssl-certs:
	cd docs/code/fastapitemplate && make create-ssl-certs

fastapitemplate-clean:
	cd docs/code/fastapitemplate && make unlink-config-dirs && cd ../..
	if [ "${DEBUG}" = "true" ]; then @echo "" && \
	@echo "Press Enter to continue to clean all directories (node_modules, dist, etc.)" && \
	@read; fi
	bash docs/code/exampleapp/scripts/clean_directory.sh ./docs/code/fastapitemplate false "${DEBUG}"
	bash docs/code/exampleapp/scripts/clean_directory.sh ./docs/code/fastapitemplate/server false "${DEBUG}"

clean:
	npm cache clean --force && rm -rf venv .pytest_cache .cache

clean-all: clean exampleapp-clean fastapitemplate-clean

lsof:
	sudo lsof -PiTCP -sTCP:LISTEN
