#!/bin/sh
# scripts/build_if_required.sh
# Build ExampleApp if required (meaning node_modules does not exist on any of the ./apps/* directories)
# 2025-07-04 | CR

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

echo ""
echo "Building ExampleApp if required..."
echo ""
DIRS_TO_PROCESS=(
    "."
    "./apps/ui"
    "./apps/api-chalice"
    "./apps/api-fastapi"
    "./apps/api-flask"
)
echo "DIRS_TO_PROCESS: ${DIRS_TO_PROCESS[@]}"
for dir in "${DIRS_TO_PROCESS[@]}"; do
    if [ ! -d "$SCRIPT_DIR/../$dir/node_modules" ]; then
        echo ""
        echo "Building $dir..."
        echo "--------"
        cd "$SCRIPT_DIR/../$dir" && npm install && npm run build && cd -
        echo ""
    fi
done
