## ADDED Requirements

### Requirement: mkdocs.yml references mkdocs_root
The `mkdocs.yml` configuration SHALL set `docs_dir: mkdocs_root` and `watch: - mkdocs_root/` so that MkDocs locates source files correctly.

#### Scenario: MkDocs serve succeeds
- **WHEN** `make serve` (or `mkdocs serve`) is run
- **THEN** MkDocs starts without a "docs_dir does not exist" error and serves pages at the configured port

#### Scenario: MkDocs build succeeds
- **WHEN** `make build` (or `mkdocs build`) is run
- **THEN** the `site/` directory is generated without errors

### Requirement: FTP transfer script swaps docs_dir correctly
The `scripts/mkdocs_transfer_site.sh` script SHALL swap `docs_dir: mkdocs_root` to `docs_dir: docs_for_ftp` before building the FTP copy, and restore it to `docs_dir: mkdocs_root` afterwards.

#### Scenario: Successful FTP publish cycle
- **WHEN** `make transfer` (or the transfer script) is run
- **THEN** `mkdocs.yml` is temporarily set to `docs_dir: docs_for_ftp`, the site is built, and `docs_dir` is restored to `mkdocs_root` on completion (success or failure)

### Requirement: Makefile sample-code targets use mkdocs_root paths
All Makefile targets that reference sample-code directories (exampleapp, fastapitemplate) SHALL use `mkdocs_root/code/` as the base path.

#### Scenario: exampleapp install target succeeds
- **WHEN** `make exampleapp-install` is run
- **THEN** npm install runs inside `mkdocs_root/code/exampleapp/` without a "no such directory" error

#### Scenario: fastapitemplate run target succeeds
- **WHEN** `make fastapitemplate-run` is run
- **THEN** the dev server starts from `mkdocs_root/code/fastapitemplate/` without path errors

### Requirement: Translation script targets mkdocs_root
`scripts/translation/translate_uncommitted.py` SHALL detect uncommitted files under `mkdocs_root/en/` and write translated output to `mkdocs_root/es/`.

#### Scenario: Uncommitted English doc is detected
- **WHEN** an uncommitted `.md` file exists under `mkdocs_root/en/`
- **THEN** the script identifies it and produces the translated Spanish file under `mkdocs_root/es/`

### Requirement: AI skills reference correct paths
The skill files `add-doc`, `translate-docs`, and `sample-code-update` SHALL reference `mkdocs_root/en/`, `mkdocs_root/es/`, and `mkdocs_root/code/` respectively, so that AI-assisted operations create or read files in the correct locations.

#### Scenario: add-doc skill creates file in correct directory
- **WHEN** the `add-doc` skill is invoked
- **THEN** the English file is created under `mkdocs_root/en/` and the Spanish stub under `mkdocs_root/es/`

### Requirement: Settings allowlist uses mkdocs_root paths
`.ai/settings.json` permission allowlist entries SHALL use `./mkdocs_root/code/` glob patterns so that reads of sample-code files do not trigger unnecessary permission prompts.

#### Scenario: Sample-code file read does not prompt
- **WHEN** Claude reads a file under `mkdocs_root/code/exampleapp/` or `mkdocs_root/code/fastapitemplate/`
- **THEN** the read is allowed automatically without a permission prompt

### Requirement: CLAUDE.md references mkdocs_root
`CLAUDE.md` cross-links and prose SHALL use `mkdocs_root/` paths so that AI coding assistants resolve file references correctly.

#### Scenario: CLAUDE.md file reference resolves
- **WHEN** an AI tool follows `@mkdocs_root/en/index.md`
- **THEN** the file is found at the referenced path
