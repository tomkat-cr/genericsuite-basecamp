#!/bin/bash
# File: scripts/vps/run-server-containers.sh
#
set -o allexport; source ".env" ; set +o allexport ;
if [ "${DOCKER_ACCOUNT}" = "" ]; then
    echo "ERROR: DOCKER_ACCOUNT environment variable not defined"
    exit 1
fi
if [ "${REACT_APP_APP_NAME}" = "" ]; then
    echo "ERROR: REACT_APP_APP_NAME environment variable not defined"
    exit 1
fi
export APP_NAME_LOWERCASE=$(echo ${REACT_APP_APP_NAME} | tr '[:upper:]' '[:lower:]')

CURRENT_DIR="`dirname "$0"`"
cd "${CURRENT_DIR}" ;

export APP_VERSION="`cat "version.txt"`"

if ! docker info > /dev/null 2>&1; then
    echo "This script uses docker, and it isn't running - Try to start it..."
    service docker start
fi

if [ -f "${CURRENT_DIR}/.env" ]; then
    set -o allexport; . "${CURRENT_DIR}/.env" ; set +o allexport ;
fi

export cmd_par="$1";
if [ "$1" == "" ] ;
then
    export cmd_par="up -d";
fi
if [ "$2" == "rmi" ] ;
then
    docker image rm ${DOCKER_ACCOUNT}/${APP_NAME_LOWERCASE}_frontend:v${APP_VERSION}-amd64;
fi
docker-compose -f ./docker-compose.yml ${cmd_par} ;
docker ps ;
