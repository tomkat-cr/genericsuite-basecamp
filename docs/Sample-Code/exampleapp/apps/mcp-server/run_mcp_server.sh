#!/bin/bash

# ExampleApp MCP Server Startup Script

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# CLI Parameters
# APP_STAGE="${1:-qa}"
# DEBUG_MODE="${2:-0}"

# .env file read
if [ -f "$SCRIPT_DIR/.env" ]; then
    echo "🔍 Reading .env file..."
    set -o allexport; . "${SCRIPT_DIR}/.env"; set +o allexport ;
else
    echo "❌ .env file not found. Please create one."
    exit 1
fi

echo "🥗 Starting ExampleApp MCP Server..."
echo "📂 Server directory: $SCRIPT_DIR"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python not found. Please install Python 3.9 or later."
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "🐍 Using Python: $PYTHON_CMD"

# Check if requirements are installed
echo "📦 Checking dependencies..."
if ! pipenv run python -c "import fastmcp" &> /dev/null; then
    echo "📥 Installing dependencies..."
    pipenv install
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies. Please check requirements.txt"
        exit 1
    fi
fi

echo "✅ Dependencies verified"
echo "🚀 Starting MCP server..."
echo ""

# Set PYTHONPATH to include the server directory
# export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"

# Start the server
cd "$SCRIPT_DIR"

# Default values for environment variables

# Application stage (qa, stage, prod, demo) to run MCP server
if [ -z "$APP_STAGE" ]; then
    export APP_STAGE=qa
fi

# Debug mode
if [ -z "$DEBUG_MODE" ]; then
    export DEBUG_MODE="1"
fi

# MCP server port
if [ -z "$MCP_SERVER_PORT" ]; then
    export MCP_SERVER_PORT=8000
fi

# MCP server host
if [ -z "$MCP_SERVER_HOST" ]; then
    export MCP_SERVER_HOST=0.0.0.0
fi


STAGE_UPPERCASE=$(echo $APP_STAGE | tr '[:lower:]' '[:upper:]')
export APP_HOST_NAME="${DOMAIN_NAME:-localhost}"
export APP_DB_ENGINE=$(eval echo \$APP_DB_ENGINE_${STAGE_UPPERCASE})
export APP_DB_NAME=$(eval echo \$APP_DB_NAME_${STAGE_UPPERCASE})
if [[ "${GET_SECRETS_ENABLED}" = "0" || "${GET_SECRETS_CRITICAL}" = "0" ]]; then
    export APP_DB_URI=$(eval echo \$APP_DB_URI_${STAGE_UPPERCASE})
else
    export APP_DB_URI=""
fi
export APP_CORS_ORIGIN="$(eval echo \"\$APP_CORS_ORIGIN_${STAGE_UPPERCASE}\")"
export AWS_S3_CHATBOT_ATTACHMENTS_BUCKET=$(eval echo \$AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_${STAGE_UPPERCASE})

# PIPENV_ARGS="$(cat .env | grep -v '^#' | xargs) APP_STAGE=$APP_STAGE MCP_SERVER_PORT=$MCP_SERVER_PORT MCP_SERVER_HOST=$MCP_SERVER_HOST APP_DB_ENGINE=$APP_DB_ENGINE APP_DB_NAME=$APP_DB_NAME APP_CORS_ORIGIN=$APP_CORS_ORIGIN AWS_S3_CHATBOT_ATTACHMENTS_BUCKET=$AWS_S3_CHATBOT_ATTACHMENTS_BUCKET APP_HOST_NAME=$APP_HOST_NAME"

PIPENV_ARGS="APP_STAGE=$APP_STAGE MCP_SERVER_PORT=$MCP_SERVER_PORT MCP_SERVER_HOST=$MCP_SERVER_HOST APP_DB_ENGINE=$APP_DB_ENGINE APP_DB_NAME=$APP_DB_NAME APP_CORS_ORIGIN=$APP_CORS_ORIGIN AWS_S3_CHATBOT_ATTACHMENTS_BUCKET=$AWS_S3_CHATBOT_ATTACHMENTS_BUCKET APP_HOST_NAME=$APP_HOST_NAME"

if [ "$DEBUG_MODE" = "1" ]; then
    npx @modelcontextprotocol/inspector \
        pipenv \
        run \
        env $PIPENV_ARGS $PYTHON_CMD mcp_server.py
else
    pipenv run env $PIPENV_ARGS $PYTHON_CMD mcp_server.py
fi
