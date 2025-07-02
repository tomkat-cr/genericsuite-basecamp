#!/bin/bash
# File: scripts/docker_build_vars.sh
# 2022-02-25 | CR
#
# Parameters
if [ "$1" != "" ]; then
    export APP_VERSION="$1";
else
    CURRENT_DIR="`dirname "$0"`";
    export APP_VERSION="${CURRENT_DIR}/../../version.txt"
fi

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

export DOCKER_ACCOUNT="${DOCKER_ACCOUNT}"
# export DOCKER_PASSWORD="xxx" # Defined on the CI/CD Secure Variables
export DOCKER_APP_NAME="${APP_NAME_LOWERCASE}_frontend"
export DOCKER_APP_VERSION="v${APP_VERSION}-amd64"
export DOCKER_APP_PORTS="3001:3001"
