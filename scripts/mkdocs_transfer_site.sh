#!/bin/bash
# mkdocs_transfer_site.sh
# 2024-04-17 | CR

# Run `mkdocs build` and automate the ftp transfer of all files/directories under the `./site` directory  to a remote host, replacing all existing ones

# The script reads the following parameters from .env:
# - remote host
# - remote username
# - remote password
# - remote directory path

change_docs_dir_to_docs_for_ftp()
{
    # Change 'docs_dir: docs' to 'docs_dir: docs_for_ftp' in mkdocs.yml
    if ! perl -i -pe's/docs_dir: docs/docs_dir: docs_for_ftp/g' mkdocs.yml
    then
        echo ""
        echo "ERROR: 'perl -i -pe\'s/docs_dir: docs/docs_dir: docs_for_ftp/g\' mkdocs.yml' failed"
        echo ""
        exit 1
    fi
}

restore_docs_dir_to_docs()
{
    # Restore 'docs_dir: docs_for_ftp' to 'docs_dir: docs' in mkdocs.yml
    if ! perl -i -pe's/docs_dir: docs_for_ftp/docs_dir: docs/g' mkdocs.yml
    then
        echo ""
        echo "ERROR: 'perl -i -pe\'s/docs_dir: docs_for_ftp/docs_dir: docs/g\' mkdocs.yml' failed"
        echo ""
    fi
}

set -o allexport; . .env ; set +o allexport ;

MASKED_PASSWORD=$(echo ${REMOTE_PASSWORD} | perl -i -pe's/./*/g')

echo ""
echo "MKDOCS TRANSFER"
echo ""
echo "Source directory path: ${SOURCE_DIRECTORY_PATH}"
echo ""
echo "Remote host: ${REMOTE_HOST}"
echo "Remote username: ${REMOTE_USERNAME}"
echo "Remote password: ${MASKED_PASSWORD}"
echo "Remote directory path: ${REMOTE_DIRECTORY_PATH}"
echo ""

# Validate required parameters

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

# Default values

if [ "${DOCS_DIRECTORY_PATH}" = "" ]; then
    DOCS_DIRECTORY_PATH="./docs"
fi
if [ "${EXAMPLEAPP_DIRECTORY_PATH}" = "" ]; then
    EXAMPLEAPP_DIRECTORY_PATH="${DOCS_DIRECTORY_PATH}/Sample-Code/exampleapp"
fi
if [ "${DEBUG}" = "" ]; then
    DEBUG="false"
fi

echo ""
echo "Cleaning up directories..."
echo ""
# Clean up all `node_modules`, `dist`, `build`, `.turbo`, `logs` directories under "docs/code/exampleapp" and sub-directories.
if ! bash ./docs/code/exampleapp/scripts/clean_directory.sh "${EXAMPLEAPP_DIRECTORY_PATH}" "false" "${DEBUG}"
then
    echo "ERROR: 'bash ./docs/code/exampleapp/scripts/clean_directory.sh \"${EXAMPLEAPP_DIRECTORY_PATH}\" \"false\" \"${DEBUG}\"' failed"
    exit 1
fi

echo ""
echo "Preparing docs..."
echo ""
if ! bash scripts/run_docs_prepare.sh
then
    echo "ERROR: 'bash scripts/run_docs_prepare.sh' failed"
    exit 1
fi

echo ""
echo "Change docs_dir to docs_for_ftp in mkdocs.yml..."
echo ""
change_docs_dir_to_docs_for_ftp

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

# Clean up all `node_modules`, `dist`, `build`, `.turbo`, `logs` directories and `.env*` files under "./site" and sub-directories.
if ! sh ./docs/code/exampleapp/scripts/clean_directory.sh "${SOURCE_DIRECTORY_PATH}" "true" "${DEBUG}"
then
    echo "ERROR: 'sh ./docs/code/exampleapp/scripts/clean_directory.sh \"${SOURCE_DIRECTORY_PATH}\" \"true\" \"${DEBUG}\"' failed"
    exit 1
fi

# FTP transfer of all files/directories under the "./site" directory to a remote host, replacing all existing content
echo ""
echo "Verifying tools..."
echo ""

if ! lftp --help > /dev/null 2>&1
then
    echo ""
    echo "lftp not found. Attempting to install..."
    echo ""
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
    restore_docs_dir_to_docs
    exit 1
fi

echo ""
echo "Restore docs_dir to docs in mkdocs.yml..."
echo ""
restore_docs_dir_to_docs

echo ""
echo "FTP transfer complete"






