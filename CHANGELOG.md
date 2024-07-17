# CHANGELOG

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a Changelog](http://keepachangelog.com/).



## Unreleased
---

### New

### Changes

### Fixes

### Breaks


## 0.0.12 (2024-07-17)
---

### Changes
Add: GET_SECRETS_CRITICAL and GET_SECRETS_CRITICAL envvars to the GS BE Core documentation to fine-grained disabling of cloud secrets manager for critical secrets and plain envvars [GS-41].


## 0.0.11 (2024-07-07)
---

### New
Add "mkdocs-print-site-plugin" to create the "site/print_page/index.html" file and be able to generate a .pdf documentation.
Add LOCAL_DNS_DISABLED and BRIDGE_PROXY_DISABLED envvars to GenericSuite BE Core, to disable local services working on the road.
Add GET_SECRETS_ENABLED envvar to GenericSuite BE Core, to enable/disable cloud provider secrets [GS-41].
Add CLOUD_PROVIDER envvar to GenericSuite BE Core, to select between AWS, GCP and Azure secrets management [GS-41].
Add AWS_DEPLOYMENT_TYPE envvar to GenericSuite BE Core, to select between AWS Lambda Function, EC2 or Fargate deployments [GS-96].

### Changes
Update README introduction removing the "this repository" hyperlink and add links in "instructions" and "code examples".
Update main index document GS Core and GS AI descriptions.
Updated presentation V2.


## 0.0.10 (2024-06-06)
---

### New
Add REACT_APP_USE_AXIOS env. var. to GenericSuite FE AI [GS-95].
Add "Presentations" section to main page.


## 0.0.9 (2024-06-02)
---

### New
Add GenericSuite presentations in both PDF and PPTx formats [GS-1].
Add Generate SAM DynamoDB table definitions instructions [GS-84].
Add local ports FRONTEND_LOCAL_PORT & BACKEND_LOCAL_PORT env. vars. instructions.

### Fixes
Publish error handling to cath mkdocs not installed [GS-85].


## 0.0.8 (2024-05-20)
---

### New
Add: GS FE special install from a git repo.

### Fixes
Fix: automatic FTP transfer.


## 0.0.7 (2024-05-09)
---

### New
Add STORAGE_URL_SEED env. vars. [GS-72].
Add sample code for genericsuite-be-scripts.
Add genericsuite-be-ai sample code files for AWS and AWS big lambdas deployment.

### Changes
Change special instructions to remove the fronend install from git/local directory (until find a way to make it work).


## 0.0.6 (2024-05-07)
---

### New
Add special install instructions.

### Changes
Navigation on the top.
Social icons and copyright notice on footer.
Repository reference on header.
Git committers on each page footer.
Add logos, readthedocs documentation URL and X url to README.
History and repositories pages revised.


## 0.0.5 (2024-05-05)
---

### New
Create a documentation mirror in readthedocs.org [GS-75].
Add API Key creation URL references.
Special installs section (from Git or Local directory).
Add Google Analytics config.
Add Cookie consent.

### Changes
Change: remove <a /> from "ACCOUNT_INACTIVE" in "app_constants.json".
Pipenv, poetry and pip instructions are not longer ### sections.

### Fixes
Fix homepage section's image paths.


## 0.0.4 (2024-04-28)
---

### Changes
Change: document the API Keys URLs for each configuration.

### Fixes
Add "mkdocs_run.sh" to fix the error running the "mkdocs serve" the first time.


## 0.0.3 (2024-04-18)
---

## Changes
More details on framework installation for GS BE Core, and instructions to link the Domains to frontend and backend Apps.


## 0.0.2 (2024-04-18)
---

### New
Add: Makefile to shortcut mkdocs "install", "serve", build" and "transfer" commands.
Add: "mkdocs_install.sh" and "mkdocs_transfer_site.sh" bash scripts.

### Changes
Change: sample files directories moved to "/docs"
Change: add minimized logos to all *.md files.

### Fixes
Fix: All links point to "index.md".
Fix: Configuration Guide index at the right side.


## 0.0.1 (2024-04-16)
---

### New

Initial commits [FA-257].
