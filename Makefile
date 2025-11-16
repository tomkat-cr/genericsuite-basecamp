# .DEFAULT_GOAL := local
.PHONY: help install transfer_debug transfer_cicd transfer publish venv build serve run clean exampleapp-install exampleapp-install-all exampleapp-update exampleapp-update-all exampleapp-run exampleapp-create-ssl-certs exampleapp-clean
SHELL := /bin/bash

EXAMPLEAPP_SERVICES = mcp-server api-chalice api-fastapi api-flask ui


# General Commands
help:
	cat Makefile

install:
	bash scripts/mkdocs_install.sh

transfer_debug:
	bash scripts/mkdocs_transfer_site.sh

transfer_cicd:
	# Set DEBUG to false to avoid blocking automation in CI environments
	DEBUG="false" sh scripts/mkdocs_transfer_site.sh

transfer: transfer_cicd

publish: transfer

nvm_use:
	export NVM_DIR="${HOME}/.nvm" && [ -s "${NVM_DIR}/nvm.sh" ] && \. "${NVM_DIR}/nvm.sh" && if ! nvm use; then echo "❌ NVM use failed. Please install it."; fi

venv:
	if ! . scripts/mkdocs_run.sh; then if ! source scripts/mkdocs_run.sh; then @echo "❌ scripts/mkdocs_run.sh failed..."; fi; fi

build:
	bash scripts/mkdocs_run.sh build

serve:
	bash scripts/mkdocs_run.sh serve

run: serve

clean:
	npm cache clean --force && rm -rf venv .pytest_cache .cache

exampleapp-install: nvm_use
	cd docs/Sample-Code/exampleapp && make install

exampleapp-install-all: nvm_use
	cd docs/Sample-Code/exampleapp && make install && cd ../../../;
	$(foreach service,$(EXAMPLEAPP_SERVICES),cd docs/Sample-Code/exampleapp/apps/$(service) && make install && cd ../../../../../;)

exampleapp-update: nvm_use
	cd docs/Sample-Code/exampleapp && make update

exampleapp-update-all: nvm_use
	cd docs/Sample-Code/exampleapp && make update
	$(foreach service,$(EXAMPLEAPP_SERVICES),cd docs/Sample-Code/exampleapp/apps/$(service) && make update && cd ../../../../../;)

exampleapp-run:
	cd docs/Sample-Code/exampleapp && make run

exampleapp-create-ssl-certs:
	cd docs/Sample-Code/exampleapp && make create-ssl-certs

exampleapp-clean:
	cd docs/Sample-Code/exampleapp && sh scripts/link_common_assets.sh unlink
	@echo ""
	@echo "Press Enter to continue to clean all directories (node_modules, dist, etc.)"
	@read
	bash docs/Sample-Code/exampleapp/scripts/clean_directory.sh ./docs/Sample-Code/exampleapp false true
