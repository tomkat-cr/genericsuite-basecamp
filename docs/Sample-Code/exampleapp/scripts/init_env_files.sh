#!/bin/sh
# scripts/init_env_files.sh
# Initialize environment files for ExampleApp
# 2025-07-04 | CR

echo ""
echo "Initializing environment files for ExampleApp..."
echo ""
DIRS_TO_PROCESS="./apps/ui ./apps/api-chalice ./apps/api-fastapi ./apps/api-flask ./apps/mcp-server"
echo "DIRS_TO_PROCESS: $DIRS_TO_PROCESS"
for dir in $DIRS_TO_PROCESS; do
    if [ ! -f "$dir/.env" ]; then
        echo ""
        echo "Initializing $dir..."
        echo "--------"
        cp "$dir/.env.example" "$dir/.env"
    else
        echo "File $dir/.env already exists. Skipping..."
    fi
done
