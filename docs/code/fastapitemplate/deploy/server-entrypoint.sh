#!/bin/bash
# deploy/server-entrypoint.sh
# 2025-09-01 | CR

run_server() {
    cd /code/server && uvicorn lib.main:app --host 0.0.0.0 --port 8000 --env-file /var/scripts/.env --reload
}

run_mcp_server() {
    export CURRENT_FRAMEWORK="mcp"
    cd /code/server && python -m lib.mcp_server --async
}

run_server & run_mcp_server & wait
