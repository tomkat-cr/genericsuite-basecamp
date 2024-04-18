#!/bin/bash
# mkdocs_install.sh
# 2024-04-17 | CR

python3 -m venv venv
source venv/bin/activate
pip install mkdocs-material
# pip install mkdocs-minify-plugin
# pip install mkdocs-git-revision-date-localized-plugin
# pip install mkdocs-material-extensions
# pip install mkdocs-macros-plugin
# pip install mkdocs-awesome-pages-plugin
pip freeze > requirements.txt
deactivate

