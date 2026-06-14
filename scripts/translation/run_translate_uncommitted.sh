#!/bin/bash
# scripts/translation/run_translate_uncommitted.sh
# 2026-03-13 | CR
# Performs the english to spanish translation of uncommitted changes in the "docs" directory before publishing

# Create virtual environment and install dependencies
python3 -m venv .venv
.venv/bin/pip install pyyaml openai

# Run the translation script
.venv/bin/python3 scripts/translation/translate_uncommitted.py

# Remove virtual environment
rm -rf .venv
