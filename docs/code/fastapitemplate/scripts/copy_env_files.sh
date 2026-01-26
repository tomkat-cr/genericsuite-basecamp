#!/bin/sh
echo ""
echo "Copying .env files from:"
pwd
echo "--------"
cp .env ./server/.env
cp .env ./ui/.env
cp .env ./mcp-server/.env
