#!/bin/sh
#
# scripts/aws/update_additional_envvars.sh
#
# Updates environment variables values in config file
#
# Parameters:
# 1. CONFIG_FILE - path to config file where the environment variables values will be replaced
# 2. REPO_BASEDIR - path to the repository where the .env file is located (default: current directory)
#
# 2024-03-28 | CR

# New 2024-06-16
# Set the App specific secrets
export APP_SECRETS="FDA_API_KEY"

CONFIG_FILE="$1"
if [ "${CONFIG_FILE}" = "" ]; then
    # New 2024-06-16
    echo "ExampleApp: CONFIG_FILE not set. Exiting..."
    # echo "1st parameter (CONFIG_FILE) not set"
    # exit 1
else
    REPO_BASEDIR="$2"
    if [ "${REPO_BASEDIR}" = "" ]; then
        REPO_BASEDIR="`pwd`"
    fi

    set -o allexport; . "${REPO_BASEDIR}/.env"; set +o allexport;

    perl -i -pe"s|FLASK_APP_placeholder|${FLASK_APP}|g" "${CONFIG_FILE}"

    # INSTRUCTIONS:

    # 1) Add you additional environment variables replacements here as:
    # perl -i -pe"s|ENVVAR_NAME_placeholder|${ENVVAR_NAME}|g" "${CONFIG_FILE}"
    # ... replacing "ENVVAR_NAME" with the name of the environment variable

    # 2) And remember to add the additional environment variables to the .env file

    # GsSecretParameter
    # perl -i -pe"s|FDA_API_KEY_placeholder|${FDA_API_KEY}|g" "${CONFIG_FILE}"
fi
