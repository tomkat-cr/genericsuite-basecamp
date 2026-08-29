## Why

The MkDocs root directory has been physically renamed from `docs/` to `mkdocs_root/` to avoid ambiguity with the general-purpose `docs/` convention, but all scripts, configuration files, and skills still reference the old path, causing broken builds and tooling failures. This change updates every reference to restore a working state.

## What Changes

- `mkdocs.yml`: Update `docs_dir: docs` → `docs_dir: mkdocs_root` and `watch: - docs/` → `watch: - mkdocs_root/`
- `scripts/mkdocs_transfer_site.sh`: Update path-based references from `docs/code/exampleapp/` to `mkdocs_root/code/exampleapp/`; update the `docs_dir` swap logic (functions `change_docs_dir_to_docs_for_ftp` / `restore_docs_dir_to_docs`) to swap between `mkdocs_root` and `docs_for_ftp` instead of `docs` and `docs_for_ftp`
- `Makefile`: Update all `docs/code/` references to `mkdocs_root/code/`
- `scripts/new-project-from-template.sh`: Update `TEMPLATE_PATH="docs/code/..."` to `mkdocs_root/code/...`
- `scripts/translation/translate_uncommitted.py`: Update `docs/en/` and `docs/es/` paths to `mkdocs_root/en/` and `mkdocs_root/es/`
- `.ai/settings.json`: Update all `docs/code/` path patterns in the permissions allowlist to `mkdocs_root/code/`
- `.ai/skills/add-doc/SKILL.md`: Update `docs/en/` and `docs/es/` references
- `.ai/skills/translate-docs/SKILL.md`: Update `docs/en/` and `docs/es/` references
- `.ai/skills/sample-code-update/SKILL.md`: Update `docs/code/` references
- `CLAUDE.md`: Update `@docs/en/`, `@docs/code/`, and prose references to `mkdocs_root/`

## Capabilities

### New Capabilities
- None

### Modified Capabilities
- None

## Impact

- All MkDocs build/serve/transfer commands (`make serve`, `make build`, `make transfer`) are currently broken because `docs/` no longer exists.
- All sample-code make targets (`exampleapp-*`, `fastapitemplate-*`) reference paths under `docs/code/` which no longer exist.
- AI skills that add or translate docs point to the wrong directories.
- The `.ai/settings.json` permission allowlist references stale paths, causing permission prompts for valid reads.
- No breaking API or schema changes — this is purely a path-rename propagation.
