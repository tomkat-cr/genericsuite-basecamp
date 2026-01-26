#!/bin/bash
# run_docs_prepare.sh
# 2026-01-24 | CR

# Run the converter
python3 scripts/docs_prepare.py --docs_dir ./docs --output_dir ./docs_for_ftp --mkdocs_path ./mkdocs.yml
