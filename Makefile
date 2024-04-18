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
	mkdocs build

serve:
	mkdocs serve

run: serve
