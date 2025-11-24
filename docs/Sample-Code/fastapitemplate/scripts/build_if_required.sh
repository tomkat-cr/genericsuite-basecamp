#!/bin/sh
# scripts/build_if_required.sh
# Build all if required (meaning node_modules does not exist on any of the ./server, ./ui, ./api_server, ./mcp_server directories)
# 2025-11-20 | CR

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
if [ "$ONLY_ONE_INSTALL" = "" ]; then
    ONLY_ONE_INSTALL="false"
fi
echo ""
echo "Building ExampleApp if required..."
echo ""
DIRS_TO_CHECK=(
    ""
    "ui"
)
DIRS_TO_PROCESS=(
    ""
    "ui"
    "mcp-server"
    "server"
)
echo "DIRS_TO_CHECK: ${DIRS_TO_CHECK[@]}"
echo "DIRS_TO_PROCESS: ${DIRS_TO_PROCESS[@]}"
RUN_INSTALL="false"
for dir in "${DIRS_TO_CHECK[@]}"; do
    echo "Checking directory: $SCRIPT_DIR/../$dir/node_modules"
    if [ ! -d "$SCRIPT_DIR/../$dir/node_modules" ]; then
        echo "Node modules not found in: $SCRIPT_DIR/../$dir/node_modules"
        RUN_INSTALL="true"
        break
    fi
done
echo "RUN_INSTALL: $RUN_INSTALL"
if [ "$RUN_INSTALL" = "true" ]; then
    if [ "$ONLY_ONE_INSTALL" = "true" ]; then
        echo ""
        echo "Installing dependencies for all workspaces"
        echo "--------"
        make install
        echo ""
    else
        for dir in "${DIRS_TO_PROCESS[@]}"; do
            echo ""
            echo "Installing dependencies for: $dir"
            echo "--------"
            cd "$SCRIPT_DIR/../$dir" && make install && cd -
            echo ""
        done
    fi
fi
