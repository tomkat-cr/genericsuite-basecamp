.PHONY: help ui-build dbdef-copy up run run-db-only down restart hard-restart logs logs-f server-logs clean-docker docker-prune status install install-dev install-all lock update update-all build start dev clean unlink-config-dirs list-scripts build-if-required copy-env-files init-app-environment rebuild-ui create-ssl-certs cf-tunnel-login cf-tunnel-create cf-tunnel-run cf-tunnel-list cf-tunnel-check cf-tunnel-delete

# Default target
help:
	cat Makefile

ui-build:
	cd ui && export REACT_APP_API_URL_FOR_BUILD="http://localhost:3000/api" && npm run build && cd -

dbdef-copy:
	cd ui && make link_config_dirs && cd -
	cd server && make link_config_dirs && cd -

# Start all services
up: build-if-required copy-env-files dbdef-copy ui-build
	cd deploy && make up && make logs-f-server-client

run: up

run-db-only:
	# To run only the local containerized database:
	CONTAINER_TO_RUN="fastapitemplate-mongo fastapitemplate-mongo-express" make run

# Stop all services
down:
	cd deploy && make down

# Restart all services
restart:
	cd deploy && make restart

# Restart all services
hard-restart: copy-env-files dbdef-copy ui-build
	cd deploy && make hard-restart

# Show logs
logs:
	cd deploy && make logs

# Follow logs
logs-f:
	# cd deploy && make logs-f
	cd deploy && make logs-f-server-client

server-logs:
	docker logs fastapitemplate-server -f

# Clean up - stop services and remove volumes
clean-docker:
	cd deploy && docker compose down -v
	docker system prune -f
	@echo ""
	@echo "Done cleaning up"

docker-prune: clean-docker

local-db-down:
	bash node_modules/genericsuite-be-scripts/scripts/local_db/run_local_db_docker.sh down

# Show service status
status:
	cd deploy && docker compose ps

install:
	npm install

install-dev:
	npm install --include=dev

install-all: copy-env-files install
	npm run install:all
	@echo ""
	@echo "Done installing dependencies for all workspaces"

lock:
	npm install --package-lock-only && npm install --package-lock-only -w ui

update:
	npm update

update-all: update
	npm run update:all
	@echo ""
	@echo "Done updating dependencies for all workspaces"

build:
	npm run build
	@echo ""
	@echo "Done building"

start:
	npm run start

dev: build-if-required copy-env-files dbdef-copy
	npm run dev

clean:
	npm run clean
	@echo ""
	@echo "Done cleaning up"

unlink-config-dirs:
	npm run unlink-config-dirs
	@echo ""
	@echo "Done unlinking config directories"

list-scripts:
	npm run --workspace=server
	npm run --workspace=ui
	npm run --workspace=mcp-server
	npm run --workspace=fastapitemplate-extension

build-if-required:
	bash ./scripts/build_if_required.sh

copy-env-files:
	bash ./scripts/copy_env_files.sh

init-app-environment:
	bash ./scripts/init_app_environment.sh
	@echo ""
	@echo "Done initializing app environment"
	@echo "Please update the .env file with your own values"
	@echo "and then run 'make dev' or 'make run' to start the services"
	@echo ""

rebuild-ui:
	cd ui && make build && cd .. && docker restart fastapitemplate-client

create-ssl-certs:
	cd server && make create_ssl_certs && cd -

# Cloudfared tunnel manager

cf-tunnel-login:
	ACTION=login bash node_modules/genericsuite-be-scripts/scripts/cloudfared-tunnel-manager.sh

cf-tunnel-create:
	ACTION=create bash node_modules/genericsuite-be-scripts/scripts/cloudfared-tunnel-manager.sh

cf-tunnel-run:
	ACTION=run bash node_modules/genericsuite-be-scripts/scripts/cloudfared-tunnel-manager.sh

cf-tunnel-list:
	ACTION=list bash node_modules/genericsuite-be-scripts/scripts/cloudfared-tunnel-manager.sh

cf-tunnel-check:
	ACTION=check bash node_modules/genericsuite-be-scripts/scripts/cloudfared-tunnel-manager.sh

cf-tunnel-delete:
	ACTION=delete bash node_modules/genericsuite-be-scripts/scripts/cloudfared-tunnel-manager.sh

lsof:
	bash node_modules/genericsuite-be-scripts/scripts/run_lsof.sh
