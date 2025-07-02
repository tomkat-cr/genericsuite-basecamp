#!/bin/bash
# File: scripts/vps/deploy_to_vps.sh
#
set -o allexport; source ".env" ; set +o allexport ;
if [ "${REACT_APP_APP_NAME}" = "" ]; then
    echo "ERROR: REACT_APP_APP_NAME environment variable not defined"
    exit 1
fi
export APP_NAME_LOWERCASE=$(echo ${REACT_APP_APP_NAME} | tr '[:upper:]' '[:lower:]')

CURRENT_DIR="`dirname "$0"`"
cd "${CURRENT_DIR}" ;

# Set app version if 1st parameter is passed to this script
if [ "$1" != "" ]; then
    echo $1 > version.txt
fi

VPS_USER="ocrusr"
if [ "$2" != "" ]; then
    VPS_USER=$2
fi

VPS_NAME="vps.${APP_NAME_LOWERCASE}.com"
if [ "$3" != "" ]; then
    VPS_NAME=$3
fi

VPS_PORT="33007"
if [ "$4" != "" ]; then
    VPS_PORT=$4
fi

LOCAL_PRIVATE_KEY_PATH="~/.ssh/id_rsa_${VPS_USER}_${VPS_NAME}"
if [ "$5" != "" ]; then
    LOCAL_PRIVATE_KEY_PATH=$5
fi

VPS_DIRECTORY="~/${APP_NAME_LOWERCASE}_start_fe"
if [ "$6" != "" ]; then
    VPS_DIRECTORY=$6
fi

# Variables
SSH_CMD="ssh -p ${VPS_PORT} -i ${LOCAL_PRIVATE_KEY_PATH} -oStrictHostKeyChecking=no"

echo "" > .env
echo "APP_REACT_APP_API_URL=${APP_REACT_APP_API_URL}" >> .env;

# Copy minimum files to bring up the containers
rsync -arv -e "${SSH_CMD}" ./.env ${VPS_USER}@${VPS_NAME}:${VPS_DIRECTORY}/
rsync -arv -e "${SSH_CMD}" ./* ${VPS_USER}@${VPS_NAME}:${VPS_DIRECTORY}/

# Restart the containers on thee VPS
${SSH_CMD} ${VPS_USER}@${VPS_NAME} "sh -x ${VPS_DIRECTORY}/run-server-containers.sh down"
${SSH_CMD} ${VPS_USER}@${VPS_NAME} "sh -x ${VPS_DIRECTORY}/run-server-containers.sh '' rmi"

# Clean up
if [ -f version.txt ]; then
    rm version.txt
fi
rm .env
