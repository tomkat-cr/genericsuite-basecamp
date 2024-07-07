#!/bin/bash
# mkdocs_run.sh
# 2024-04-26 | CR
#
# Usage:
# mkdocs_run.sh serve
# mkdocs_run.sh build
#
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
if [ "$1" != "" ]; then
    mkdocs $1
    deactivate
else
    bash
fi