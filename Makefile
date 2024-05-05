# .DEFAULT_GOAL := local
# .PHONY: tests
SHELL := /bin/bash

# General Commands
help:
	cat Makefile

install:
	sh scripts/mkdocs_install.sh

transfer:
	sh scripts/mkdocs_transfer_site.sh

build:
	sh scripts/mkdocs_run.sh build

serve:
	sh scripts/mkdocs_run.sh serve

run: serve
