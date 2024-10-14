# CHANGELOG

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a Changelog](http://keepachangelog.com/).



## Unreleased
---

### New

### Changes

### Fixes

### Breaks


## Unreleased
## 0.0.13 (2024-10-13)
---

### New
VPS Install scripts [GS-141].
Implement ollama server [GS-139].


## 0.0.12 (2024-10-07)
---

### New
Make DynamoDb tables with prefix work with the GS DB Abstraction [GS-102].
Implement HF (HuggingFace) local pipelines [GS-59].
Implement Falcon Mamba with HF [GS-118].
Implement Meta Llama 3.1 with HF [GS-119].
Implement HF (HuggingFace) image generator [GS-117].
Implement Flux.1 image generator [GS-117].
Implement Anthropic Claude 3.5 Sonnet [GS-33].
Implement Groq chat model [GS-92].
Add LOCALSTACK_AUTH_TOKEN documentation [GS-97].
Implement Amazon Bedrock chat and image generator [GS-131].
Add HUGGINGFACE_PIPELINE_DEVICE to configure the "device" pipeline() parameter [FA-233].
Implement o1-mini/o1-preview models use through AI/ML API aimlapi.com [GS-138].
Implement GS Huggingface lightweight model, identified by model_types "huggingface_remote" or "gs_huggingface" [GS-136].

### Changes
Replace react-bootstrap entirely and use only Tailwind CSS [GS-63].
"index-template.html" is not longer required because the %PUBLIC_URL% issue in public/index.html file running the app with webpack was fixed [GS-116].
Replace GPT-3.5 with gpt-4o-mini as default OpenAI model [GS-109].
HUGGINGFACE_ENDPOINT_URL replaced by HUGGINGFACE_DEFAULT_CHAT_MODEL [GS-59].
<HashRouter> was replaced by <RouterProvider> and createBrowserRouter() [GS-112].

# Fixes
Fix the %PUBLIC_URL% issue in public/index.html file running the app with webpack [GS-116].

### Breaks
Bootstrap CSS is not longer used [GS-63].
FontAwesome is not longer used [GS-115].
SVG images removed and included in the "GsIcons" library [GS-115].
Get rid of eval() in the GS FrontEnd [GS-127].


## 0.0.11 (2024-07-27)
---

### New
Add "mkdocs-print-site-plugin" to create the "site/print_page/index.html" file and be able to generate a .pdf documentation.
Add LOCAL_DNS_DISABLED and BRIDGE_PROXY_DISABLED envvars to GenericSuite BE Core, to disable local services working on the road.
Add GET_SECRETS_ENABLED envvar to GenericSuite BE Core, to enable/disable cloud provider secrets [GS-41].
Add CLOUD_PROVIDER envvar to GenericSuite BE Core, to select between AWS, GCP and Azure secrets management [GS-41].
Add AWS_DEPLOYMENT_TYPE envvar to GenericSuite BE Core, to select between AWS Lambda Function, EC2 or Fargate deployments [GS-96].
Add: Node global version instructions in special-installs.
Add: ".nvmrc" file to set the repo default node version.

### Changes
Update README introduction removing the "this repository" hyperlink and add links in "instructions" and "code examples".
Update main index document GS Core and GS AI descriptions.
Updated presentation V2.
Add: GET_SECRETS_ENVVARS and GET_SECRETS_CRITICAL envvars to the GS BE Core documentation to fine-grained disabling of cloud secrets manager for critical secrets and plain envvars [GS-41].


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
