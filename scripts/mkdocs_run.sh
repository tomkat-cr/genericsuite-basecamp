#!/bin/bash
# mkdocs_run.sh
# 2024-04-26 | CR
#
# Usage:
# mkdocs_run.sh serve
# mkdocs_run.sh build
#
# Run this script from the root directory of the repository

echo ""
echo "Creating and activating virtual environment..."
echo ""
if ! python3 -m venv .venv
then
    echo "ERROR: 'python3 -m venv .venv' failed"
    exit 1
fi
if ! source .venv/bin/activate
then
    echo "ERROR: 'source .venv/bin/activate' failed"
    exit 1
fi
if ! pip install -r requirements.txt
then
    echo "ERROR: 'pip install -r requirements.txt' failed"
    exit 1
fi

echo ""
echo "Preparing docs..."
echo ""
if ! bash scripts/run_docs_prepare.sh
then
    echo "ERROR: 'bash scripts/run_docs_prepare.sh' failed"
    exit 1
fi

echo ""
echo "Running mkdocs..."
echo ""
if [ "$1" != "" ]; then
    if ! mkdocs $1 $2 $3 $4 $5 $6 $7 $8 $9
    then
        echo "ERROR: 'mkdocs $1 $2 $3 $4 $5 $6 $7 $8 $9' failed"
        exit 1
    fi
    deactivate
else
    echo "ERROR: No command specified"
    exit 1
fi
