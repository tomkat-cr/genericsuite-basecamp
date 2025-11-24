# .DEFAULT_GOAL := local
.PHONY:  help install install_dev lock locked_dev locked_install requirements clean test test_only config config_dev config_local config_qa config_qa_for_deployment config_staging run run_qa down_qa restart_qa run_local_docker run_prod
SHELL := /bin/bash
MCP_SERVER_ENABLED := true

## General Commands

help:
	cat Makefile

## Installation

install:
	@echo "No installation needed for MCP server"

install_dev:
	@echo "No installation needed for MCP server"

lock:
	@echo "No locking needed for MCP server"

locked_dev:
	@echo "No locked development needed for MCP server"

locked_install:
	@echo "No locked installation needed for MCP server"

requirements:
	@echo "No requirements needed for MCP server"

## Cleaning

clean:
	@echo "No cleaning needed for MCP server"

## Automated Testing

test:
	cd ../server && make test

test_only:
	cd ../server && make test_only

## Chalice Specific Commands

config:
	cd ../server && bash ../node_modules/genericsuite-be-scripts/scripts/aws/set_chalice_cnf.sh prod

config_dev:
	cd ../server && bash ../node_modules/genericsuite-be-scripts/scripts/aws/set_chalice_cnf.sh

config_local:
	cd ../server && bash ../node_modules/genericsuite-be-scripts/scripts/aws/set_chalice_cnf.sh mongo_docker

config_qa:
	cd ../server && bash ../node_modules/genericsuite-be-scripts/scripts/aws/set_chalice_cnf.sh qa

config_qa_for_deployment:
	cd ../server && bash ../node_modules/genericsuite-be-scripts/scripts/aws/set_chalice_cnf.sh qa deploy

config_staging:
	cd ../server && bash ../node_modules/genericsuite-be-scripts/scripts/aws/set_chalice_cnf.sh staging

## Application Specific Commands

run: 
	if [ ${MCP_SERVER_ENABLED} = "true" ]; then make config_local && cd ../server && bash ../node_modules/genericsuite-be-scripts/scripts/mongo/run_mongo_docker.sh run "0" dev && cd ../mcp-server && bash ./run_mcp_server.sh; else @echo "MCP Server (local) is DISABLED temporarily..." && read; fi

run_qa:
	if [ ${MCP_SERVER_ENABLED} = "true" ]; then make config_qa && cd ../mcp-server && bash ./run_mcp_server.sh; else @echo "MCP Server (qa) is DISABLED temporarily..." && read; fi

run_local_docker: run

run_prod:
	if [ ${MCP_SERVER_ENABLED} = "true" ]; then make config && cd ../mcp-server && bash ./run_mcp_server.sh; else @echo "MCP Server (prod) is DISABLED temporarily..." && read; fi
