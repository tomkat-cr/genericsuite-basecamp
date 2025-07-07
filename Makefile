# .DEFAULT_GOAL := local
.PHONY: tests venv
SHELL := /bin/bash

# General Commands
help:
	cat Makefile

install:
	sh scripts/mkdocs_install.sh

transfer:
	sh scripts/mkdocs_transfer_site.sh

transfer_cicd:
	# Set DEBUG to false to avoid blocking automation in CI environments
	DEBUG="false" sh scripts/mkdocs_transfer_site.sh

publish: transfer

venv:
	. scripts/mkdocs_run.sh

build:
	sh scripts/mkdocs_run.sh build

serve:
	sh scripts/mkdocs_run.sh serve

run: serve

exampleapp-install:
	cd docs/Sample-Code/exampleapp && make install

exampleapp-update:
	cd docs/Sample-Code/exampleapp && make update

exampleapp-run:
	cd docs/Sample-Code/exampleapp && make run

exampleapp-clean:
	sh docs/Sample-Code/exampleapp/scripts/clean_directory.sh ./docs/Sample-Code/exampleapp false true
