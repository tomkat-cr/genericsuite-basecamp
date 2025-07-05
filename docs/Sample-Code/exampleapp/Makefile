# .DEFAULT_GOAL := local
.PHONY: tests venv
SHELL := /bin/bash

# General Commands
help:
	cat Makefile

install:
	pnpm install

build:
	pnpx turbo build --force

check:
	pnpx turbo check-types

check-build:
	pnpx turbo check-types build

run:
	pnpx turbo start --force

unlink:
	sh scripts/link_common_assets.sh unlink
	cd apps/ui && sh node_modules/genericsuite/scripts/run_symlinks_handler.sh remove

link:
	sh scripts/link_common_assets.sh link

dev: link
	# pnpx turbo dev
	pnpx turbo watch dev; (exit_code=$$?; make unlink; exit $$exit_code)
