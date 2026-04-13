#!/bin/bash
# deploy/run-deploy.sh
# Run the GenericSuite monorepo app on docker/podman containers
# 2025-11-22 CR

get_version_from_package_json() {
    if [ ! -f ../package.json ]; then
        echo "Error: package.json file not found in 'root' directory"
        exit 1
    fi
    export APP_VERSION=$(cat ../package.json | grep version | cut -d '"' -f 4)
}

docker_dependencies() {
    echo ""
    echo "Configured containers engine (CONTAINERS_ENGINE): ${CONTAINERS_ENGINE}"

    if ! source ${SCRIPTS_DIR}/container_engine_manager.sh start "${CONTAINERS_ENGINE}" "${OPEN_CONTAINERS_ENGINE_APP}"; then
        echo "Error running ${SCRIPTS_DIR}/container_engine_manager.sh start \"${CONTAINERS_ENGINE}\" \"${OPEN_CONTAINERS_ENGINE_APP}\""
        exit 1
    fi

    echo "Selected containers engine (DOCKER_CMD): ${DOCKER_CMD}"
    echo "Selected containers engine (DOCKER_COMPOSE_CMD): ${DOCKER_COMPOSE_CMD}"

    if [ -z "${DOCKER_CMD}" ];then
        echo "ERROR: missing DOCKER_CMD"
        exit 1
    fi

    if [ -z "${DOCKER_COMPOSE_CMD}" ];then
        echo "ERROR: missing DOCKER_COMPOSE_CMD"
        exit 1
    fi

    if ! ${DOCKER_CMD} ps > /dev/null 2>&1;
    then
        echo "${DOCKER_CMD} is not running"
        exit 1
    fi
}

set_docker_env_vars() {
    if [ "${APP_DOMAIN_NAME}" = "" ];then
        echo "Error: APP_DOMAIN_NAME environment variable not set"
        exit 1
    fi

    if [ "${APP_STAGE}" = "" ];then
        export APP_STAGE="dev"
    fi
    export STAGE_UPPERCASE=$(echo "${APP_STAGE}" | tr '[:lower:]' '[:upper:]')

    export APP_HOST_NAME="${APP_DOMAIN_NAME}"
    export APP_DB_ENGINE=$(eval echo \$APP_DB_ENGINE_${STAGE_UPPERCASE})
    export APP_DB_NAME=$(eval echo \$APP_DB_NAME_${STAGE_UPPERCASE})
    if [[ "${GET_SECRETS_ENABLED}" = "0" || "${GET_SECRETS_CRITICAL}" = "0" ]]; then
        APP_DB_URI_DEV="mongodb://root:example@fastapitemplate-mongo:27017"
        # APP_DB_URI_DEV="mongodb://fastapitemplate-mongo:27017/?directConnection=true"
        export APP_DB_URI=$(eval echo \$APP_DB_URI_${STAGE_UPPERCASE})
    else
        export APP_DB_URI=""
    fi
    export APP_CORS_ORIGIN="$(eval echo \"\$APP_CORS_ORIGIN_${STAGE_UPPERCASE}\")"
    export AWS_S3_CHATBOT_ATTACHMENTS_BUCKET=$(eval echo \$AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_${STAGE_UPPERCASE})
    export DYNAMDB_PREFIX=$(eval echo \$DYNAMDB_PREFIX_${STAGE_UPPERCASE})

    echo ""
    echo ">>> run-deploy.sh | set_docker_env_vars()"
    echo ""
    local masked_app_db_uri=$(echo ${APP_DB_URI} | perl -i -pe's/./*/g')
    echo "APP_STAGE: ${APP_STAGE}"
    echo "APP_DOMAIN_NAME: ${APP_DOMAIN_NAME}"
    echo "APP_DB_URI: ${masked_app_db_uri}"
    echo "APP_DB_NAME: ${APP_DB_NAME}"
    echo "APP_DB_ENGINE: ${APP_DB_ENGINE}"
    echo "APP_CORS_ORIGIN: ${APP_CORS_ORIGIN}"
    echo "AWS_S3_CHATBOT_ATTACHMENTS_BUCKET: ${AWS_S3_CHATBOT_ATTACHMENTS_BUCKET}"
    echo "DYNAMDB_PREFIX: ${DYNAMDB_PREFIX}"
    echo ""

    get_version_from_package_json
}

load_envs() {
    echo ""
    echo "Current directory: $(pwd)"
    if [ ! -f ../.env ]; then
        echo "Error: .env file not found in 'root' directory"
        exit 1
    fi
    echo "Loading environment variables from ../.env"
    set -o allexport; . ../.env; set +o allexport ;
}

start_up_function() {
    # Start up code
    echo "Starting up services..."
}

clean_up_function() {
    # Clean up code
    echo "Cleaning up services..."
    # Remove all files and directories except for the .env file
    rm -rf ../mcp-server/lib
    rm -rf ../server/server-entrypoint.sh
}

create_docker_images() {
    echo "Creating ${DOCKER_CMD} images..."
    cd docker_images
    if ! DOCKER_CMD=${DOCKER_CMD} bash ./build_docker_images.sh
    then
        echo "Error creating ${DOCKER_CMD} images"
        exit 1
    fi
    cd ..
}

cleanup_when_specific_container_is_specified() {
    if [ "${CONTAINER_TO_RUN}" != "" ]; then
        echo "Running only ${CONTAINER_TO_RUN}"
        ${DOCKER_COMPOSE_CMD} --project-name deploy down
        ${DOCKER_COMPOSE_CMD} --project-name ${APP_NAME_LOWERCASE} down
    fi
}

is_docker_port_in_use() {
    # Port to check
    local port="$1"
    # Container name to check (evaluation container name)
    local container_name="$2"

    # Check if the port is used by any running Docker container
    local running_container=""
    echo "Checking if port $port is in use by any running ${DOCKER_CMD} container..."
    if [ "${CONTAINERS_ENGINE}" = "podman" ]; then
        running_container=$(podman ps --all | grep "${port}->")
    else
        running_container=$(${DOCKER_CMD} ps --filter "publish=$port" --format "{{.Names}}" | head -n 1)
    fi

    if [ -n "$running_container" ]; then
        if [ "$running_container" = "$container_name" ]; then
            echo "0" # The port is in use by the same evaluation container
        else
            echo "1" # The port is in use by another container
        fi
    else
        echo "0" # The port is not in use
    fi
}

load_envs

SCRIPTS_DIR="../node_modules/genericsuite-be-scripts/scripts"
docker_dependencies

APP_NAME_LOWERCASE=$(echo "$APP_NAME" | tr '[:upper:]' '[:lower:]')
APP_NAME_LOWERCASE=$(echo "$APP_NAME_LOWERCASE" | tr '[:blank:]' '_')

if [ -z "$APP_NAME_LOWERCASE" ]; then
    echo "ERROR: APP_NAME environment variable not set"
    exit 1
fi

ACTION=$1
if [ -z "$ACTION" ]; then
    echo "Error: No action specified"
    exit 1
fi

OTHER_DOCKER_COMPOSE_PARAMS=""
# Check if the port 27017 (MongoDb) is already taken by any running docker container
# For example by GSAM, GS BE or other services that use MongoDb
if [ "$(is_docker_port_in_use 27017 fastapitemplate-mongo)" = "0" ]; then
    if [ "$USE_LOCAL_MONGODB" != "0" ]; then
        OTHER_DOCKER_COMPOSE_PARAMS="${OTHER_DOCKER_COMPOSE_PARAMS} --profile use_local_mongodb"
    else
        echo ""
        echo "WARNING: Port 27017 is in use by any running ${DOCKER_CMD} container different than 'fastapitemplate-mongo'"
    fi
fi

# Check if the port 8081 (MongoDb Express) is already taken by any running docker container
# For example by GSAM, GS BE or other services that use MongoDb
if [ "$(is_docker_port_in_use 8081 fastapitemplate-mongo-express)" = "0" ]; then
    if [ "$USE_LOCAL_MONGODB" != "0" ]; then
        OTHER_DOCKER_COMPOSE_PARAMS="${OTHER_DOCKER_COMPOSE_PARAMS} --profile use_local_mongodb_express"
    else
        echo ""
        echo "WARNING: Port 8081 is in use by any running ${DOCKER_CMD} container different than 'fastapitemplate-mongo-express'"
    fi
fi

# Specific container environment variables

if [ "$USE_LOCAL_MONGODB" != "0" ]; then
    #
    # Use USE_LOCAL_MONGODB=1 to enable only local database on the docker compose
    # E.g. to use the 'make dev' command (running frontend and backend without
    # docker compose) with local database in docker compose
    #
    export MONGODB_HOST_NAME=fastapitemplate-mongo
    export MONGODB_HOST_PORT=27017
    export MONGODB_USER=root
    export MONGODB_PASSWORD=example
    export MONGODB_URI=mongodb://$MONGODB_USER:$MONGODB_PASSWORD@$MONGODB_HOST_NAME:$MONGODB_HOST_PORT
    # export MONGODB_URI=mongodb://$MONGODB_HOST_NAME:$MONGODB_HOST_PORT/?directConnection=true
fi

if [ "$ACTION" = "restart" ]; then
    echo "Restarting services..."
    ${DOCKER_COMPOSE_CMD} --project-name ${APP_NAME_LOWERCASE} restart ${CONTAINER_TO_RUN}
    exit 0
elif [ "$ACTION" = "run" ]; then
    set_docker_env_vars
    start_up_function
    create_docker_images
    echo "Starting services..."
    if ! ${DOCKER_CMD} network create my_shared_network 2>/dev/null; then
        echo "my_shared_network already exists"
    fi
    cleanup_when_specific_container_is_specified
    echo "${DOCKER_COMPOSE_CMD} ${OTHER_DOCKER_COMPOSE_PARAMS} --project-name ${APP_NAME_LOWERCASE} up -d ${CONTAINER_TO_RUN}"
    ${DOCKER_COMPOSE_CMD}  ${OTHER_DOCKER_COMPOSE_PARAMS} --project-name ${APP_NAME_LOWERCASE} up -d ${CONTAINER_TO_RUN}
    exit 0
elif [ "$ACTION" = "down" ]; then
    echo "Stopping services..."
    cleanup_when_specific_container_is_specified
    if ! ${DOCKER_COMPOSE_CMD} --project-name ${APP_NAME_LOWERCASE} down
    then
        echo "Error stopping services... skipping clean up function"
    fi
    clean_up_function
    exit 0
elif [ "$ACTION" = "logs" ]; then
    echo "Showing logs..."
    ${DOCKER_COMPOSE_CMD} --project-name ${APP_NAME_LOWERCASE} logs
    exit 0
elif [ "$ACTION" = "logs-f" ]; then
    echo "Showing logs..."
    ${DOCKER_COMPOSE_CMD} --project-name ${APP_NAME_LOWERCASE} logs -f
    exit 0
elif [ "$ACTION" = "logs-f-server-client" ]; then
    echo "Showing logs..."
    ${DOCKER_COMPOSE_CMD} --project-name ${APP_NAME_LOWERCASE} logs -f fastapitemplate-server fastapitemplate-client
    exit 0
else
    echo "Error: Invalid action specified: $ACTION"
    exit 1
fi