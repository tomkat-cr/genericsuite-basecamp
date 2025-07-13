# 20250705 - The ExampleApp Monorepo Edition

![GS_Release_2025-07-05_Image_4B.png](./images/GS_Release_2025-07-05_Image_4B.png)

Release Date: 2025-07-12

## Summary

GenericSuite July 5th, 2025 Release: A Major Leap in Modernization and Developer Experience

We are excited to announce the GenericSuite release for July 5th, 2025, a significant update focused on modernizing the development stack and enhancing developer productivity. This release, "The ExampleApp Monorepo Edition," introduces a wealth of new features, integrations, and improvements across the entire suite.

Key highlights of this release include:

* Modernized Frontend Tooling: We have integrated Vite as an alternative to Webpack, offering a faster and more efficient development experience. The frontend core now also officially supports Axios for more robust data fetching, alongside major dependency upgrades to React Router v7 and Tailwind CSS v4.

* Enhanced Backend Flexibility: On the backend, JWT expiration times are now configurable via environment variables, providing greater control over security policies. Request handling for both Flask and FastAPI has also been refactored for greater consistency.

* Expanded AI Capabilities: We are broadening our AI integration support with the addition of new providers, including Google Vertex AI and OpenRouter. This allows developers to leverage a wider range of powerful models for their applications.

* Introducing the "ExampleApp" Monorepo: A cornerstone of this release is a new, fully-featured example application built as a monorepo using Turborepo and pnpm. This provides a practical, real-world blueprint for developers to learn from and accelerate their own projects.

* Improved Developer Experience: We've introduced several quality-of-life improvements, such as a new script for live-linking local libraries for faster development cycles and enhanced local SSL certificate management using mkcert.

This release underscores our commitment to providing a powerful, flexible, and developer-friendly ecosystem. We invite you to explore the detailed release notes and dive into the new ExampleApp to see these enhancements in action.

## GenericSuite Frontend Core

### Package, Pull Request and Tag 1.0.25

* https://www.npmjs.com/package/genericsuite/v/1.0.25
* https://github.com/tomkat-cr/genericsuite-fe/pull/7
* https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.25

### Pull Request Overview # 1

This PR implements Axios as an alternative to Fetch while also upgrading dependencies and adding support for Vite as a run method.

- Extracts and renames the App component import in index.tsx.
- Adds new scripts and updates existing ones to manage symlinks, module settings, SSL certificates, and run method dependencies.
- Upgrades package versions (e.g. react-router-dom, Tailwind CSS) and adjusts build tooling configurations.

### Pull Request Overview # 2

Implements API key management, enhances the generic select component with multi‐field descriptions, and corrects default‐value cloning and password‐validation logic.

- Introduce UsersApiKey component, register its frontend/backend configs and endpoint (GS-159).
- Extend GenericSelectGenerator with a description_fields parameter for compound option labels (GS-155).
- Fix default‐value cloning in genericFuncArrayDefaultValue and tighten UsersPasswordValidations to prevent fall‐through.

### Pull Request Overview # 3

This PR integrates Axios as an alternative to fetch, centralizes environment variable definitions for both Webpack and Vite, and expands local configuration utilities.

- Introduces gsFetch wrapper that delegates to Axios or Fetch based on REACT_APP_USE_AXIOS
- Refactors dbApiService to use gsFetch and adds optional Access-Control-Expose-Headers
- Updates both Webpack and Vite configs for unified process.env, HTTPS support, and debugging output

### CHANGELOG.md

#### 1.0.25 (2025-07-08)
---

##### New
- Implement axios as alternative to fetch [GS-202] [GS-15].
- Add envvar REACT_APP_USE_AXIOS to use axios instead of fetch by default.
- Add Vite as alternative to webpack [GS-195].
- Add: "run_method_dependency_manager.sh" to unify the run method dependency install or uninstall [GS-195].
- Add getAdditionalHeaders() in the dbApiService class to send the 'Access-Control-Expose-Headers': 'Content-Disposition' header and receive file names from the backend [GS-15].
- Add envvar REACT_APP_USE_EXPOSE_HEADERS to add the 'Access-Control-Expose-Headers' header calling the backend (defaults to be off) [GS-15].
- Configure lines per page in the CRUD editor: save and restore it from the LocalStorage. Defaults to 30 (previous was 5) [GS-185].
- Add GCE_RFC configurations to local-config's buildConfigData() [GS-185].
- Add new "getLocalConfigItem" function to local-config to get a configuration item from the local storage config variable [GS-185].
- Add envvar REACT_APP_GCE_ACTIONS_ALLOW_MOUSE_OVER to allow MouseOver in GCE_RFC actions [GS-185].
- Add envvar REACT_APP_GCE_ACTIONS_ALLOW_MAGIC_BUTTON to allow the Magic Button (3-dots) in GCE_RFC actions [GS-185].
- Add getErrorDetail() function to get the error details from the error object [GS-15].
- Add getUuidV4() function to generate a UUID v4 [GS-15].
- Add getContentTypeFromHeadersOrFilename() function to get the content type from the headers or filename [GS-15].
- Add copy_ssl_certs Makefile target to copy the SSL certificates generated in the backend to the frontend [GS-198].
- Add setupTests.js to fix jest test with "react-router-dom" to v7 [GS-199].
- Add setupTests.js and jest.config.cjs to the package.json "files" entry, so they'll be available in node_modules [GS-199].
- Add "@types/node" to resolve paths without error using "@/" prefix [GS-112].
- Implement RUN_PROTOCOL envvar to have the http/https protocol automatically on app local running, no user intervention, as part of the Turborepo initiative [GS-188].
- Add the "TARGET_DIR" (defaults to "public") and "BASE_DIR" (defaults to ".") parameters to the "build_copy_images.sh" script to copy the images to the "public" directory [GS-188].
- Add the "run_method_build.sh" script to run the build process using the specified run method [GS-188].

##### Changes
- GCE_RFC and class_name_constants code cleanup.
- convertId() function moved from db.service.jsx to id.utilities.jsx [GS-185].
- fixBlob() receives headers parameter to get the content type from the headers, performs a try-catch to handle errors in URL.createObjectURL(), if the error is 'Overload resolution failed', try it using binaryData.push(blobObj) [GS-15].
- isBinaryFileType() receives additional contentType parameter to get the content type from the headers or filename [GS-15].
- getFilenameFromContentDisposition() verifies if the content disposition header contains a filename with or without quotes [GS-15].
- Install vite, webpack or react-app-rewired dependencies running run_app_frontend.sh according to the RUN_METHOD env var [GS-198].
- Remove vite, webpack and react-app-rewired dependencies running npm_publish.sh [GS-198].
- Implement RUN_METHOD in aws_deploy_to_s3.sh and build_prod_test.sh, so it use vite, webpack or react-app-rewired [GS-199].
- React Router updated from "^v6.18.0" to "^v7.5.3" [GS-199].
- Default node version upgraded to 20 in ".nvmrc" [GS-199].
- Tailwind CSS updated from "^v3.4.9" to "^v4.1.5" [GS-112].
- Add *.ts, *.tsx and ./index.html files to tailwind.config.js [GS-112].
- All debugging flags turned off.

##### Fixes
- Fix the net:ERR_CERT_AUTHORITY_INVALID error in GenericSuite FE/BE using the https protocol [GS-198].
- Fix the create_ssl_certs Makefile target to effectively call the backend self-signed SSL certificates creation [GS-198].
- Fix the React Router v7 Future Flag Warning by upgrading "react-router-dom" to v7 [GS-199].
- Fix the "'assert' is deprecated in import statements and support will be removed in a future version; use 'with' instead" running "make publish" and rollup.connfig.mjs.
- Fix Tailwind 4 input and texarea background color issue by adding the gs_core.css to index.html [GS-112].
- Fix prevent object mutation in Object.assign calls by adding empty object as first parameter
- Update "webpack.config.js" to fix the error "Error: Can't resolve 'process/browser'" and remove NODE_TLS_REJECT_UNAUTHORIZED envvar [GS-199] [GS-198] [GS-195].

...

## GenericSuite Frontend AI

### Package, Pull Request and Tag 1.0.23

* https://www.npmjs.com/package/genericsuite-ai/v/1.0.23
* https://github.com/tomkat-cr/genericsuite-fe-ai/pull/7
* https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.23

### Pull Request Overview # 1

This PR prepares the v1.0.23 release by upgrading core dependencies, adding Vite support alongside Webpack, updating Tailwind CSS, and introducing a new header logo prop.

- Add appLogoHeader property to the main App component and update changelog/version files.
- Integrate Vite configuration as an alternative to the existing Webpack setup.
- Upgrade Tailwind CSS to v4.x, move environment definitions into shared objects, and fix Jest test environment.

### CHANGELOG.md

#### 1.0.23 (2025-07-08)
---

##### New
- Add landscape logo to the App header (appLogoHeader) [GS-63].

##### Changes
- GenericSuite FE core upgraded to v1.0.25.
- convertId() function moved from db.service.jsx to id.utilities.jsx in GenericSuite FE [GS-185].
- Implement axios in all API calls to handle Flask backend files retrieval with all required headers [GS-15].
- Add Vite as alternative to webpack [GS-195].
- Tailwind CSS updated from "^v3.4.9" to "^v4.1.5" [GS-112].
- Add setupTests.js to fix jest test with "react-router-dom" to v7 [GS-199].
- Default node version upgraded to 20 in ".nvmrc" [GS-199].
- Add "@types/node" to resolve paths without error using "@/" prefix [GS-112] [PC-2].

##### Fixes
- Fix the net:ERR_CERT_AUTHORITY_INVALID error in GenericSuite FE/BE using the https protocol [GS-198].
- Fix the React Router v7 Future Flag Warning by upgrading "react-router-dom" to v7 [GS-199].
- Fix "Warning: Each child in a list should have a unique "key" prop. Check the render method of `ChatCodeBlock`" warning.
- Update "webpack.config.js" to fix the error "Error: Can't resolve 'process/browser'" and remove NODE_TLS_REJECT_UNAUTHORIZED envvar [GS-199] [GS-198] [GS-195].

...

## GenericSuite Backend Core

### Package, Pull Request and Tag 1.0.11

* https://pypi.org/project/genericsuite/0.1.11/
* https://github.com/tomkat-cr/genericsuite-be/pull/10
* https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.1.11

### Pull Request Overview # 1

This PR advances the project to v0.1.11, makes JWT expiration configurable, and enhances request handling in both Flask and FastAPI endpoint builders.

- Bump package version to 0.1.11 in setup.py and pyproject.toml
- Read EXPIRATION_MINUTES from environment in jwt module
- Refactor request abstraction and query-param parsing for Flask and FastAPI

### CHANGELOG.md

#### 0.1.11 (2025-07-08)

##### New
- Add SSL_CERT_GEN_METHOD, BASE_DEVELOPMENT_PATH and SAM_BUILD_CONTAINER documentation to the .env.example file.
- Add JWT expiration time configuration with the EXPIRATION_MINUTES envvar [GS-200].
- Add RUN_PROTOCOL documentation to the .env.example file [GS-137].

##### Changes
- Refactor query-param parsing for FastAPI [GS-200].
- Refactor request abstraction for Flask [GS-15].
- Add 'Access-Control-Expose-Headers' to the Flask response headers [GS-15].

##### Fixes
- Fix "AttributeError: 'Request' object has no attribute 'to_dict'" error in get_query_params() when Flask framework is used in generic_array_crud() [GS-15].
- Fix error reporting in modify_item_in_db() is not showing the "json_file" variable content [GS-196].
- Fix the filter issue in the CRUD editor using FastAPI [GS-200].
- Linting changes.

...

## GenericSuite Backend AI

### Package, Pull Request and Tag 1.0.13

* https://pypi.org/project/genericsuite-ai/0.1.13/
* https://github.com/tomkat-cr/genericsuite-be-ai/pull/9
* https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.13

### Pull Request Overview # 1

This release bumps to version 0.1.13, adds new AI providers (OpenRouter, Vertex AI), Flask endpoints, and mock support for audio TTS, while improving IBM WatsonX configurability and updating web search defaults.

- Bump package version and upgrade dependencies (langchain, duckduckgo-search, faiss-cpu)
- Introduce new AI providers: OpenRouter and Google Vertex AI, plus Flask REST endpoints
- Add GET_MOCKS_DEBUG for audio testing and unify IBM WatsonX environment-driven parameters

### CHANGELOG.md

#### 0.1.13 (2025-07-08)
---

##### New
- Implement OpenRouter AI provider and models [GS-182].
- Implement Vertex AI provider and models [GS-183].
- Add AI Endpoints for Flask [GS-15].
- Add envvar GET_MOCKS_DEBUG to test the text_to_audio_generator tool and save money in the sound AI API bill by using existing audio files already generated in the /tmp directory (GET_MOCKS_DEBUG="1") or a specific file path (GET_MOCKS_DEBUG="/path/to/file.mp3") [GS-185].

##### Changes
- Tool web_search() updated to use DEFAULT_MAX_RESULTS=30 [GS-87].
- Add envvars to configure various parameters of the IBM WatsonX provider (IBM_WATSONX_REGION, IBM_WATSONX_TEMPERATURE, IBM_WATSONX_REPETITION_PENALTY, IBM_WATSONX_MAX_NEW_TOKENS, IBM_WATSONX_MIN_NEW_TOKENS, IBM_WATSONX_DECODING_METHOD, IBM_WATSONX_MODERATION_HAP_THRESHOLD) [GS-184].
- Implement calls to AppContext.get_env_var() when AppContext is passed to the CustomLLM class, otherwise it calls to os.environ.get() [GD-184].
- Change "web_search.py" to use min() instead of max() to enforce a minimum between the DEFAULT_MAX_RESULTS and the number of results requested by the user/model. If the request is higher than the DEFAULT_MAX_RESULTS, it will use that value.
- Change "ADDITIONAL GUIDELINES:\n" to "REQUIREMENTS:\n" and add "* " (bulletpoints) to each line in build_gs_prompt (ai_chatbot_main_langchain) to have a better system prompt for AI model.
- Change "DEBUG" to use Config().DEBUG == "1" in web_search [GS-185].

##### Fixes
- Fix "ERROR: Failed building wheel for pyreqwest-impersonate" error running "sam build" (with "make deploy_run_local_qa") when "duckduckgo-search" were updated to version "6.1.1" [GS-87].
- Fix text-to-audio generation with text_to_audio_response() because sometimes with some models it never generate a new audio.
- Fix the missing model_name parameter calling get_openai_api().
- Set the DUCKDUCKGO_MAX_RESULTS to 5 to avoid the error "error: https://lite.duckduckgo.com/lite/ 202 Ratelimit" [GS-87].
- Set the DUCKDUCKGO_RATE_LIMIT_TOKEN to check the "202 Ratelimit" and switch to google search in case WEBSEARCH_DEFAULT_PROVIDER is not "ddg" or "google" [GS-87].

### Package, Pull Request and Tag 1.0.14

* https://pypi.org/project/genericsuite-ai/0.1.14/
* https://github.com/tomkat-cr/genericsuite-be-ai/pull/10
* https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.14

### Pull Request Overview # 2

This PR fixes rate-limiting issues with DuckDuckGo searches and referer-blocking errors with the Google Custom Search API, while bumping the package version.

- Bumps version to 0.1.14 and updates author email in setup.py and pyproject.toml
- Switches DuckDuckGo integration to use the ddgs library and adds configurable search method
- Adds a paginated Google search implementation, updates result sanitization, and updates changelog
- Updates Node version in .nvmrc from 18 to 20

### CHANGELOG.md

#### 0.1.14 (2025-07-12)
---

##### Fixes
- Fix DuckDuckGo Search "202 Ratelimit error" [GS-224].
- Fix Google Search API requests from referer empty are blocked error [GS-223].

...

## GenericSuite Backend Scripts

### Package, Pull Request and Tag 1.0.14

* https://www.npmjs.com/package/genericsuite-be-scripts/v/1.0.14
* https://github.com/tomkat-cr/genericsuite-be-scripts/pull/8
* https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.0.14

### Pull Request Overview # 1

This PR refactors scripting for local development and CI/CD by introducing a container engine abstraction (Docker/Podman), enhancing SSL workflows, and reorganizing Nginx configuration.

- Centralize container engine handling with container_engine_manager.sh and replace direct docker calls across scripts with DOCKER_CMD/DOCKER_COMPOSE_CMD
- Add SSL_CERT_GEN_METHOD + mkcert support in local_ssl_certs_creation.sh
- Restructure Nginx config into conf.d/ and add restart option in secure_local_server/run.sh

### Pull Request Overview # 2

This PR standardizes container engine commands across scripts with a new manager, adds Podman support, enhances SSL certificate handling via mkcert, introduces a development linking script, and updates versions and Makefile targets.

- Centralize Docker/Podman invocation using container_engine_manager.sh and DOCKER_CMD variables.
- Default SSL cert generation to mkcert, unify nginx conf into conf.d, and improve secure local server options.
- Add link_gs_libs_for_dev.sh and Makefile targets for live linking of GenericSuite libraries.

### CHANGELOG.md

#### 1.0.14 (2025-07-08)
---

##### New
- Add the "link_gs_libs_for_dev.sh" script to link LOCAL GenericSuite libraries and trigger the uvicorn/gunicorn reload without need to run "pipenv update". Add to the Makefile and run with `make link_gs_libs` [FA-84].
- Add the BASE_DEVELOPMENT_PATH envvar to specify the GS base development path (parent directory of genericsuite-be* repos) to enable "make link_gs_libs_for_dev" [FA-84].
- Add the SAM_BUILD_CONTAINER envvar to force "sam build --use-container --debug" when "make deploy_run_local_qa" is executed [GS-87].
- Add the "mkcert" method to enhance the self-signed SSL certificates creation for the local development environment using "https" (previously it was using "office-addin-dev-certs" by default) [GS-198].
- Add the SSL_CERT_GEN_METHOD envvar to select the SSL certificate generation method [GS-198].
- Add restart option to "secure_local_server/run.sh", so the backend dev container should not be rebuilt if it's not necesaty [GS-198].
- Add error and access logs to the secure_local_server nginx [GS-198].
- Add GOOGLE_MAPS_API_KEY, ANTHROPIC_API_KEY, GROQ_API_KEY, AIMLAPI_API_KEY, NVIDIA_API_KEY, RHYMES_CHAT_API_KEY, RHYMES_VIDEO_API_KEY, IBM_WATSONX_API_KEY, IBM_WATSONX_PROJECT_ID, OPENROUTER_API_KEY, XAI_API_KEY, TOGETHER_API_KEY to the EXTENSION_SECRETS envvar in aws_secrets_manager.sh [GS-198].
- Implement RUN_PROTOCOL envvar to have the http/https protocol automatically on app local running, no user intervention, as part of the Turborepo initiative [GS-188].
- Implement Podman as an alternative to Docker [GS-215].
- Add CONTAINER_ENGINE and OPEN_CONTAINERS_ENGINE_APP envvars to GenericSuite BE Core [GS-215].
- Add configurable backend ports using the envvar BACKEND_LOCAL_PORT and BACKEND_DEBUG_LOCAL_PORT to the "sls" (secure local server) [GS-137].

##### Changes
- Remove "make lock_pip_file" and replace it with "make requirements". Add "make lock" and "make npm_lock" [FA-84] [GS-15].
- "run_aws.sh" validates that CURRENT_FRAMEWORK is Chalice for "run", "deploy", "create_stack", "describe_stack", "delete_app", "delete_stack" commands, and runs "set_chalice_cnf.sh" for all those commands when it's Chalice [GS-15].

##### Fixes
- Fix poetry 2.x "The option --no-update does not exist" error message [FA-84].
- Fix error with the "Bottleneck" dependency building https dev environment (sls-backend) due to missing "gcc" in the "python:3.11-slim" image [GS-197].
- Fix the GenericSuite dependencies verification in "big_lambdas_manager.sh" to abort the execution if there are local dependencies [FA-169].
- Fix missing "g++" running docker build in "big_lambdas_manager.sh", adding "RUN yum -y groupinstall 'Development Tools'" to the "Dockerfile-big-lambda-AL2" [FA-169].
- Fix the error "The image manifest, config or layer media type for the source image xx.dkr.ecr.us-east-1.amazonaws.com/xxx:version is not supported" running docker build in "big_lambdas_manager.sh", adding `--provenance=false` to stop BuiltKit from generating said manifest [FA-169].
- Fix the net:ERR_CERT_AUTHORITY_INVALID error in GenericSuite FE/BE using the https protocol [GS-198].
- Fix TMP_BUILD_DIR assignment in dynamodb deploy script.
- Fix "run_aws.sh" to assign the correct AWS Stack Name and avoid the error "An error occurred (ValidationError) when calling the DescribeStacks operation: 1 validation error detected: Value '${APP_NAME_LOWERCASE}-be-stack' at 'stackName' failed to satisfy constraint: Member must satisfy regular expression pattern: [a-zA-Z][-a-zA-Z0-9]*|arn:[-a-zA-Z0-9:/._+]*" [GS-137].
- Fix ".chalice/config_example.json" to remove the API_GATEWAY_STAGE_placeholder from the "api_gateway_stage" attribute and assign the correct value, and remove unused attributes in the QA stage [FA-248].

...

## GenericSuite BaseCamp

### Pull Request and Tag 1.0.0

* https://github.com/tomkat-cr/genericsuite-basecamp/pull/7
* https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.0.0

### Pull Request Overview # 1

This PR updates and expands the documentation for GenericSuite, providing clearer instructions on build tools, deployment options, and installation commands. Key changes include:

- Correction of language (singular vs plural) in the AI chatbot endpoint description.
- Addition of new code examples for special installs and detailed build tool setups.
- Enhancements to deployment instructions across AWS services and updates in the changelog.

### Pull Request Overview # 2

This PR enhances the mkdocs deployment script with validation, defaults, cleanup steps, and robust lftp install logic; fixes a minor markdown grammar issue; updates the AWS SAM template runtime; and adds a full “ExampleApp” frontend scaffold under docs/Sample-Code/exampleapp.

- Added parameter validation, default values, directory cleanup, and multi-platform lftp installation to mkdocs_transfer_site.sh.
- Tweaked a bullet in docs/index.md for singular endpoint grammar and updated Python runtime in template-sam.yml.
- Introduced a complete Turborepo-based ExampleApp sample, including generators, scripts, configs, and presets.

### Pull Request Overview # 3

A concise update to include new repositories and strengthen the project’s introduction across documentation.

- Added new AI-related repos (GSAM, ASDT) and updated repo listings with consistent “GS” prefixes.
- Expanded the documentation index with “Why Choose” and “Key Features” sections to emphasize project value.
- Recorded the changes in CHANGELOG under an unreleased version.

### CHANGELOG.md

#### 1.1.0 (2025-07-12)
---

##### New
- Add the source code link in the Basecamp README.md file [GS-137].
- Add documentation for WEBSEARCH_DEFAULT_PROVIDER and WEBSEARCH_DUCKDUCKGO_METHOD [GS-223] [GS-224].

##### Changes
- Change "libraries" to "packages" when referring to GenericSuite frontend and backend packages.
- NodeJs default version updated to 20+ to fulfill the requirements of tailwindcss v4 and Shadcn v2+.
- Change "make transfer" to run in CI/CD mode by default.
- Change wording in history.md and exampleapp's README.md.
- Change build_if_required.sh to use bash arrays.

##### Fixes
- Fix the "Error: Cannot find module 'dotenv'" error by adding the exampleapp root directory to the "build_if_required.sh" script.
- Fix the "Failed to send compressed multipart ingest: langsmith.utils.LangSmithError" error running queries to the AI Assistant by commenting the "LANGCHAIN_API_KEY" and "LANGCHAIN_PROJECT" environment variables in the "exampleapp/apps/**/.env.example" files.

### Pull Request and Tag 1.1.0

* https://github.com/tomkat-cr/genericsuite-basecamp/pull/8
* https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.1.0

### Pull Request Overview # 4

This PR updates documentation and fixes build/runtime issues as part of the 1.1.0 release.

- Rename “libraries” references to “packages” and bump Node requirement to ≥20 across docs
- Add source code link in the example app README and enhance environment variable docs
- Fix build script to include the root directory and comment out problematic Langchain env vars

### CHANGELOG.md

#### 1.0.0 (2025-07-08)
---

##### New
- Add Code example monorepo [GS-137].
- Add "make exampleapp-run", "make exampleapp-install", "make exampleapp-update" and "make exampleapp-clean" commands to handle the example monorepo [GS-137].
- Add the EC2, KMS, Secrets Manager, and DynamoDB commands [GS-96].
- Add the "link_gs_libs_for_dev.sh" script to link LOCAL GenericSuite libraries and trigger the uvicorn/gunicorn reload without need to run "pipenv update". Add to the Makefile and run with `make link_gs_libs` [FA-84].
- Add the BASE_DEVELOPMENT_PATH envvar to specify the GS base development path (parent directory of genericsuite-be* repos) to enable "make link_gs_libs_for_dev" [FA-84].
- Add the SAM_BUILD_CONTAINER envvar to force "sam build --use-container --debug" when "make deploy_run_local_qa" is executed [GS-87].
- Add project overview document for Gemini CLI (or Claude Code).
- Implement Turborepo in the example monorepo [GS-188].
- Implement Pnpm in the example monorepo [GS-187].
- Implement RUN_PROTOCOL envvar to have the http/https protocol automatically on app local running, no user intervention [GS-188].
- Add the "TARGET_DIR" (defaults to "public") and "BASE_DIR" (defaults to ".") parameters to the "build_copy_images.sh" script to copy the images to the "public" directory [GS-188].
- Add the "run_method_build.sh" script to run the build process using the specified run method [GS-188].
- Add "make test-run-build" documentation.
- Implement Podman as an alternative to Docker [GS-215].
- Add CONTAINER_ENGINE and OPEN_CONTAINERS_ENGINE_APP envvars to GenericSuite BE Core [GS-215].
- Add the WEBSEARCH_DEFAULT_PROVIDER envvar documentation to GenericSuite AI [GS-87].
- Add configurable backend debug port using the envvar BACKEND_DEBUG_LOCAL_PORT to the "sls" (secure local server) [GS-137].

##### Changes
- Add new repos to the README, repos index and general documentation index [GS-1].
- Enhance intro in the documentation index to highlight the importance of the project [GS-1].
- Remove "make lock_pip_file" and replace it with "make requirements". Add "make lock" and "make npm_lock" [FA-84] [GS-15].
- Change wording and instruction fixes in the configuration guide
- Make the "mkdocs_transfer_site.sh" to be used in both macos and linux
- Change "vite.config.js" -> "vite.config.mjs"
- Change "fynapp_gitops" -> "genericsuite-gitops"

##### Fixes
- Fix: chalice config template file in documentation.

...

## GenericSuite Gitops

### Pull Request and Tag 0.3.0

* https://github.com/tomkat-cr/genericsuite-gitops/pull/2
* https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.3.0

### Pull Request Overview # 1

This PR enhances the WebUI management script by centralizing start/stop/run logic, adds an “update” workflow, and updates the n8n Docker Compose file to use the latest image tag.

- Refactor and extract common logic into run_webui, run_help, and run_done functions in run_webui.sh
- Introduce update and update_wo actions for pulling and redeploying the Open-WebUI container
- Change n8n service in docker-compose.yml to use the unpinned (latest) image by default

### Pull Request Overview # 2

This PR adds a new update workflow for the open-webui container and switches n8n to pull its latest image by default.

- Introduces update and update_watchtower commands in run_webui.sh to handle image pulls and container restarts.
- Modifies n8n/docker-compose.yml to use the untagged/latest n8n image and comments out the previous pinned version.
- Updates CHANGELOG.md to version 0.3.0, documenting the new webUI update feature and n8n version change.

### CHANGELOG.md

#### 0.3.0 (2025-07-07)
---

##### New
- Add documentation to replace exampleapp and other example names to the app specific ones [GS-141].
- Add WebUI update with sh `run_webui.sh update`.

##### Changes
- SECRET_GROUP envvar moved from apply_secrets.sh to .env [GS-141].
- Fix typos, add additional notes, remove hard-coded IDs in various files.
- Change to run "scripts/get_os_name_type.sh" with source or "." in the firewall manager. [GS-141]
- Change to get the latest n8n version in the docker compose file.
