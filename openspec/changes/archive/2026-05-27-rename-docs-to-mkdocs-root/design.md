## Context

The MkDocs source directory was physically renamed from `docs/` to `mkdocs_root/` at the filesystem level, but none of the tooling was updated. The project uses MkDocs with the `mkdocs-static-i18n` plugin (folder structure: `mkdocs_root/en/` and `mkdocs_root/es/`), plus sample code trees under `mkdocs_root/code/exampleapp/` and `mkdocs_root/code/fastapitemplate/`. Roughly 10 files across config, scripts, skills, and AI settings reference the old `docs/` prefix.

## Goals / Non-Goals

**Goals:**
- Every file that references `docs/` (as the MkDocs root) is updated to `mkdocs_root/`
- The FTP-publish script's temporary `docs_for_ftp` swap logic works correctly against the new base name
- All `make` targets build and serve without errors
- AI skills produce correct file paths when run

**Non-Goals:**
- Moving or restructuring any content inside `mkdocs_root/`
- Renaming `docs_for_ftp` (the temporary FTP copy directory name stays the same)
- Updating `.readthedocs.yaml` or any external CI that reads the directory name from `mkdocs.yml` at runtime (they will pick up the new value automatically once `mkdocs.yml` is correct)

## Decisions

**Mechanical string replacement, not a script.**
All changes are deterministic path substitutions (`docs/` → `mkdocs_root/`, `docs_dir: docs` → `docs_dir: mkdocs_root`). There is no architectural ambiguity — the right approach is to edit each file directly. A sed-based migration script would add complexity without benefit for a one-time rename.

**`docs_for_ftp` swap functions.**
`mkdocs_transfer_site.sh` temporarily changes `docs_dir` in `mkdocs.yml` to point at a cleaned copy (`docs_for_ftp`) before publishing to FTP, then restores it. With the rename, the baseline value changes from `docs` to `mkdocs_root`. The functions `change_docs_dir_to_docs_for_ftp` and `restore_docs_dir_to_docs` (including its name) must be updated to swap between `mkdocs_root` and `docs_for_ftp`, and the restore function should be renamed `restore_docs_dir_to_mkdocs_root` for clarity. The perl one-liner patterns must match the new baseline.

**`.ai/settings.json` path patterns.**
The permission allowlist uses glob patterns like `./docs/code/...`. Each must be changed to `./mkdocs_root/code/...` so that the harness does not prompt unnecessarily when reading sample-code files.

**Symlinked skill files.**
Skills live in `.ai/skills/` (source of truth) and are symlinked to `.agents/skills/`, `.claude/skills/`, etc. Editing the source file in `.ai/skills/` is sufficient — the symlinks will reflect the change automatically.

## Risks / Trade-offs

- **Missed reference** → Any `docs/` reference left behind produces a runtime error (file not found). Mitigation: after applying, run `grep -r '"docs/' . --include="*.yml" --include="*.yaml" --include="*.sh" --include="*.py" --include="*.json" --include="*.md" | grep -v ".git\|mkdocs_root\|node_modules\|openspec"` to confirm zero remaining occurrences.
- **`docs_for_ftp` name collision** → The FTP script creates a sibling directory `docs_for_ftp` at the project root, which is unrelated to `mkdocs_root`. Keeping its name unchanged avoids confusion and preserves any `.gitignore` entries for it.
- **CLAUDE.md cross-linking** — `CLAUDE.md` uses `@docs/en/index.md` style links that may be resolved by AI tooling. These must be updated to `@mkdocs_root/en/index.md` or the tool will fail to read the referenced file.

## Migration Plan

1. Update `mkdocs.yml` first (it is the source of truth for MkDocs).
2. Update `scripts/mkdocs_transfer_site.sh` (depends on the value in `mkdocs.yml`).
3. Update `Makefile`, `scripts/new-project-from-template.sh`, `scripts/translation/translate_uncommitted.py`.
4. Update `.ai/settings.json`.
5. Update `.ai/skills/` files (`add-doc`, `translate-docs`, `sample-code-update`).
6. Update `CLAUDE.md`.
7. Run the grep verification command to confirm no `docs/` references remain.
8. Run `make serve` locally to confirm MkDocs starts without errors.

Rollback: git revert the commits; the physical directory rename was already done outside version control, so no FS changes are needed.

## Open Questions

None — the scope is fully understood and bounded.
