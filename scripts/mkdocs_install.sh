#!/bin/bash
# mkdocs_install.sh
# 2024-04-17 | CR

set -e

if [ -d "venv" ]; then
    echo "🔍 venv directory already exists, removing it"
    rm -rf .venv
fi

echo "🔍 Creating venv directory"
if [ -d .venv ]; then
    rm -rf .venv
fi
python3 -m venv .venv
source .venv/bin/activate

echo "🔍 Installing mkdocs and dependencies"
pip install mkdocs-material mkdocs-print-site-plugin mkdocs-git-committers-plugin mkdocs-exclude-search

# pip install mkdocs-minify-plugin
# pip install mkdocs-git-revision-date-localized-plugin
# pip install mkdocs-material-extensions
# pip install mkdocs-macros-plugin
# pip install mkdocs-awesome-pages-plugin

echo "🔍 Freezing requirements"
pip freeze > requirements.txt

echo "🔍 Deactivating venv"
deactivate

echo "🔍 Done"
