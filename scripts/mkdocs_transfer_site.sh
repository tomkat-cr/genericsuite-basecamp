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

FAKE_PASSWORD=$(echo ${REMOTE_PASSWORD} | perl -i -pe's/./*/g')

echo ""
echo "MKDOCS TRANSFER"
echo ""
echo "Source directory path: ${SOURCE_DIRECTORY_PATH}"
echo ""
echo "Remote host: ${REMOTE_HOST}"
echo "Remote username: ${REMOTE_USERNAME}"
echo "Remote password: ${FAKE_PASSWORD}"
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

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

if ! mkdocs build
then
    echo "ERROR: 'mkdocs build' failed"
    exit 1
fi
deactivate

echo ""
echo "'mkdocs build' completed"

# Automate the ftp transfer of all files/directories under the `./site` directory  to a remote host, replacing all existing ones

echo ""
echo "Verifying tools..."
echo ""

if ! lftp --help > /dev/null 2>&1
then
if ! lftp --help > /dev/null 2>&1
then
    if ! brew install lftp
    then
        if ! sudo apt install lftp
        then
            if ! sudo yum install lftp
            then
                echo "ERROR: could not install lftp"
                exit 1
            fi
        fi
    fi
fi

echo ""
echo "Begin FTP transfer..."
echo ""

# Transfer the entire local directory to the FTP server
lftp -u ${REMOTE_USERNAME},${REMOTE_PASSWORD} -e "set ssl:verify-certificate no" ${REMOTE_HOST} <<EOF
mirror -R ${SOURCE_DIRECTORY_PATH} ${REMOTE_DIRECTORY_PATH}
bye
EOF
if [ $? -ne 0 ]; then
    echo "ERROR: FTP transfer failed"
    exit 1
fi

echo ""
echo "FTP transfer complete"






