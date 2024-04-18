#!/bin/bash
# mkdocs_transfer_site.sh
# 2024-04-17 | CR

# Run `mkdocs build` and automate the ftp transfer of all files/directories under the `./site` directory  to a remote host, replacing all existing ones

# The script reads the following parameters from .env:
# - remote host
# - remote username
# - remote password
# - remote directory path

set -o allexport; . .env ; set +o allexport ;

echo ""
echo "MKDOCS TRANSFER"
echo ""
echo "Source directory path: ${SOURCE_DIRECTORY_PATH}"
echo ""
echo "Remote host: ${REMOTE_HOST}"
echo "Remote username: ${REMOTE_USERNAME}"
echo "Remote password: ${REMOTE_PASSWORD}"
echo "Remote directory path: ${REMOTE_DIRECTORY_PATH}"

if [ "${SOURCE_DIRECTORY_PATH}" = "" ]; then
    echo "ERROR: SOURCE_DIRECTORY_PATH is not defined"
    exit 1
fi
if [ "${REMOTE_HOST}" = "" ]; then
    echo "ERROR: REMOTE_HOST is not defined"
    exit 1
fi
if [ "${REMOTE_USERNAME}" = "" ]; then
    echo "ERROR: REMOTE_USERNAME is not defined"
    exit 1
fi
if [ "${REMOTE_PASSWORD}" = "" ]; then
    echo "ERROR: REMOTE_PASSWORD is not defined"
    exit 1
fi
if [ "${REMOTE_DIRECTORY_PATH}" = "" ]; then
    echo "ERROR: REMOTE_DIRECTORY_PATH is not defined"
    exit 1
fi

echo ""
echo "Begin 'mkdocs build' run..."
echo ""

mkdocs build

echo ""
echo "'mkdocs build' completed"

# Automate the ftp transfer of all files/directories under the `./site` directory  to a remote host, replacing all existing ones

echo ""
echo "Begin FTP transfer..."
echo ""

if ! ftp
then
    brew install inetutils
fi

cd ${SOURCE_DIRECTORY_PATH}

ftp -n ${REMOTE_HOST} <<EOF

verbose
user ${REMOTE_USERNAME} ${REMOTE_PASSWORD}
binary
cd ${REMOTE_DIRECTORY_PATH}
mdelete *
mput *
bye
EOF

echo ""
echo "FTP transfer complete"






