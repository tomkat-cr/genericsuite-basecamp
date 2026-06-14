## 1. Update mkdocs.yml

- [x] 1.1 Change `docs_dir: docs` to `docs_dir: mkdocs_root`
- [x] 1.2 Change `watch: - docs/` to `watch: - mkdocs_root/`

## 2. Update scripts/mkdocs_transfer_site.sh

- [x] 2.1 Update `change_docs_dir_to_docs_for_ftp`: change the perl regex pattern from `s/docs_dir: docs/docs_dir: docs_for_ftp/g` to `s/docs_dir: mkdocs_root/docs_dir: docs_for_ftp/g` (and update the error message)
- [x] 2.2 Update `restore_docs_dir_to_docs`: change the perl regex pattern from `s/docs_dir: docs_for_ftp/docs_dir: docs/g` to `s/docs_dir: docs_for_ftp/docs_dir: mkdocs_root/g` (and rename the function to `restore_docs_dir_to_mkdocs_root` and update call sites and error messages)
- [x] 2.3 Update `bash ./docs/code/exampleapp/scripts/clean_directory.sh` references (lines ~95–97) to `mkdocs_root/code/exampleapp/scripts/clean_directory.sh`
- [x] 2.4 Update `sh ./docs/code/exampleapp/scripts/clean_directory.sh` reference (line ~135) to `mkdocs_root/code/exampleapp/scripts/clean_directory.sh`

## 3. Update Makefile

- [x] 3.1 Replace all `docs/code/fastapitemplate` references with `mkdocs_root/code/fastapitemplate`
- [x] 3.2 Replace all `docs/code/exampleapp` references with `mkdocs_root/code/exampleapp`

## 4. Update scripts/new-project-from-template.sh

- [x] 4.1 Change `TEMPLATE_PATH="docs/code/${TEMPLATE_NAME}"` to `TEMPLATE_PATH="mkdocs_root/code/${TEMPLATE_NAME}"`

## 5. Update scripts/translation/translate_uncommitted.py

- [x] 5.1 Update the docstring/comment that mentions `docs/en` to `mkdocs_root/en`
- [x] 5.2 Change the path filter `path.startswith("docs/en/")` to `path.startswith("mkdocs_root/en/")`
- [x] 5.3 Change the destination path replacement from `replace("/docs/en/", "/docs/es/")` to `replace("/mkdocs_root/en/", "/mkdocs_root/es/")`
- [x] 5.4 Update the "no files found" message from `docs/en` to `mkdocs_root/en`

## 6. Update .ai/settings.json

- [x] 6.1 Replace all `./docs/code/` path patterns in the permissions allowlist with `./mkdocs_root/code/`

## 7. Update AI skills

- [x] 7.1 `.ai/skills/add-doc/SKILL.md`: change `docs/en/{section}/{filename}` and `docs/es/{section}/{filename}` to `mkdocs_root/en/...` and `mkdocs_root/es/...`
- [x] 7.2 `.ai/skills/translate-docs/SKILL.md`: update all `docs/en/`, `docs/es/`, and `docs/` references to `mkdocs_root/en/`, `mkdocs_root/es/`, and `mkdocs_root/`
- [x] 7.3 `.ai/skills/sample-code-update/SKILL.md`: update `docs/code/exampleapp/` and `docs/code/fastapitemplate/` references to `mkdocs_root/code/...`

## 8. Update CLAUDE.md

- [x] 8.1 Change `@docs/en/index.md` to `@mkdocs_root/en/index.md`
- [x] 8.2 Change `@docs/code/index.md` to `@mkdocs_root/code/index.md`
- [x] 8.3 Change `@docs/code/fastapitemplate/README.md` to `@mkdocs_root/code/fastapitemplate/README.md`
- [x] 8.4 Change `@docs/code/exampleapp/README.md` to `@mkdocs_root/code/exampleapp/README.md`
- [x] 8.5 Change prose reference `docs/ via AI` (in `make translate_uncommitted` description) to `mkdocs_root/`
- [x] 8.6 Change `docs/code/exampleapp/apps/api-fastapi/` path in the test runner note to `mkdocs_root/code/exampleapp/apps/api-fastapi/`

## 9. Verify

- [x] 9.1 Run `grep -r '"docs/' . --include="*.yml" --include="*.yaml" --include="*.sh" --include="*.py" --include="*.json" --include="*.md" | grep -v ".git\|node_modules\|openspec\|docs_for_ftp\|docs/assets\|docs/code/exampleapp\|docs/code/fastapitemplate" 2>/dev/null` and confirm zero unexpected references to `docs/` remain
- [x] 9.2 Run `make serve` and confirm MkDocs starts without errors
