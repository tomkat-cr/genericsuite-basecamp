---
name: translate-docs
description: Translate uncommitted documentation changes to Spanish using the project AI translation pipeline
disable-model-invocation: true
---

Run the translation pipeline for any uncommitted documentation changes in the `docs/` directory.

Steps:
1. Check for uncommitted changes in `docs/en/` by running: `git status docs/`
2. Show the user which files have pending changes
3. Run: `make translate_uncommitted`
4. After it completes, show a summary of which `docs/es/` files were updated
5. Ask the user if they want to review any specific translated file

If there are no uncommitted doc changes, tell the user and suggest they make their English edits first before translating.
