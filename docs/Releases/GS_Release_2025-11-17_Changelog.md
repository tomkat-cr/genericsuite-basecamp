# 20251117 - The MCP Server Edition

![GS_Release_2025-11-17_Image_1.png](./images/GS_Release_2025-11-17_Image_1.png)

Date: 2025-11-17

## Summary

We are thrilled to announce the release of GenericSuite: The MCP Server Edition (2025-11-17). This release represents a major leap forward in backend architecture and developer experience.

Key Highlights:

* MCP Implementation: We have introduced a foundational Microservice Communication Protocol (MCP) server in the Backend Core, enhancing inter-process communication. The ExampleApp now features a live MCP server implementation for nutrition management tools.

* Enhanced Security: We have significantly bolstered our security posture. API key authentication has moved from temporary files to direct database lookups to mitigate risks. We also patched critical vulnerabilities in dependencies like axios, urllib3, and transformers across the stack.

* Modernized Dev Stack: We now treat uv and poetry as first-class citizens for Python package management, alongside pipenv. Additionally, we upgraded to Node.js 20 and improved Linux compatibility for our build scripts.

* GitOps Evolution: A new Nginx Router module with automated SSL certificate generation (Let's Encrypt/Mkcert) is now available to streamline traffic management.

This update ensures GenericSuite remains a robust, secure, and modern choice for scalable software architecture.

## GenericSuite Frontend Core

### Package, Pull Request and Tag

* Package: https://www.npmjs.com/package/genericsuite/v/1.1.0
* Pull Request: https://github.com/tomkat-cr/genericsuite-fe/pull/8
* Tag: https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.1.0

### Pull Request Overview

Summary of Changes

This pull request delivers a comprehensive set of updates primarily focused on bolstering the application's security posture and enhancing its robustness. It addresses critical security vulnerabilities by updating key dependencies and implementing protective measures like rate limiting. Furthermore, it resolves a significant bug in API Key creation and refines URL handling for redirects, ensuring a more secure and reliable user experience. The changes also include various code modernizations and build process improvements.

Highlights

* Security Enhancements: Multiple dependencies have been updated to address security vulnerabilities, including axios (CVE-2025-7783, DoS attacks), postcss (line return parsing error), react-syntax-highlighter (DOM Clobbering), and babel-loader (Regular Expression Denial of Service). Additionally, several vulnerabilities identified by npm audit fix --force have been resolved, and basic rate limiting has been implemented in server.js to mitigate DoS attacks.

* API Key Creation Fix: Resolved an issue in API Key creation where an empty value in the fieldValues object could lead to an error during the merge of 'resultset' in the reduceAllResponses function. The UsersApiKeyDbPreRead function now correctly assigns the generated access_token within the resultset object.

* URL Parameter Parsing and Redirect Sanitization: Fixed the getUrlParams() function to correctly parse URL parameters, especially when a redirect parameter contains a hash (#). The LoginPage component now includes a sanitizeRedirectUrl function to validate and sanitize redirect URLs, preventing open redirect vulnerabilities, and new test cases have been added to cover this functionality.

* Build Configuration Updates: The Babel configuration has been updated to replace @babel/plugin-proposal-class-properties with @babel/plugin-transform-class-properties. The webpack configuration now conditionally logs options and environment variables based on local environment detection, and the Makefile's clean target has been updated for a more thorough cleanup.

* Code Modernization and Refactoring: Numerous code sections across various files (dist/cjs/index.js, dist/esm/index.js, src/lib/helpers/NavLib.jsx, etc.) have been refactored to use modern JavaScript syntax such as template literals for string concatenation, nullish coalescing (??) for default values, and object spread (...) for merging objects, improving readability and maintainability.

### CHANGELOG.md

#### [1.1.0] - 2025-11-17

##### Added
- Add test cases for redirect functionality in LoginPage component [GS-219].

##### Changed
- Update CHANGELOG format to be more semantic [GS-222].

##### Fixed
- Fix the merge of "resultset" when following values has same key but empty in the "fieldValues" object (GCE_RFC Specific Functions handling, reduceAllResponses function) [GS-159].
- Replace class-properties plugin with transform-class-properties to fix the "npm warn deprecated @babel/plugin-proposal-class-properties@7.18.6: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-class-properties instead." warning [GS-219].
- Fix the URL parameter parsing in getUrlParams() to handle the redirect parameter with a hash (#) in the value [GS-219].
- Enhance webpack configuration to conditionally log options and environment variables based on local environment detection.
- Fix: "generic.editor.rfc.specific.func.jsx" to prevent TypeError when merging fieldValues in the "reduceAllResponses" function [GS-230].

##### Security
- Update "axios" to ^1.13.0 to fix the security vulnerability [GS-219]:
  - "form-data" CWE-343, CVE-2025-7783, CVSS 9.4.
  - "Axios is vulnerable to DoS attack through lack of data size check"
  - "form-data uses unsafe random function in form-data for choosing boundary"
- Fix "PostCSS line return parsing error" by updating "postcss" to "^8.5.6" [GS-219].
- Fix "Basic rate limiting to mitigate DoS via expensive FS operations" in "server.js" [GS-219].
- Enhance LoginPage redirect handling with URL sanitization [GS-219].
- Update "react-syntax-highlighter" to "^16.1.0" to fix the security vulnerability [GS-219]:
  - "PrismJS DOM Clobbering vulnerability"
- Bump babel-loader to ^10.0.0 to fix "@eslint/plugin-kit is vulnerable to Regular Expression Denial of Service attacks through ConfigCommentParser" [GS-219].
- The following security vulnerabilities were fixed by running "npm audit fix --force" [GS-219]:
  - "Prototype Pollution in JSON5 via Parse Method"
  - "pbkdf2 returns predictable uninitialized/zero-filled memory for non-normalized or unimplemented algos"
  - "pbkdf2 silently disregards Uint8Array input, returning static keys"
  - "Prototype pollution in webpack loader-utils"
  - "sha.js is missing type checks leading to hash rewind and passing on crafted data"

...

## GenericSuite Frontend AI

### Package, Pull Request and Tag

* Package: https://www.npmjs.com/package/genericsuite-ai/v/1.1.0
* Pull Request: https://github.com/tomkat-cr/genericsuite-fe-ai/pull/8
* Tag: https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.1.0

### Pull Request Overview

Summary of Changes

This pull request delivers a significant update focused on bolstering security, enhancing the user experience of the AI Assistant, and modernizing the project's dependency management. Key security vulnerabilities have been patched through dependency upgrades and the introduction of rate limiting. The AI Assistant's code block rendering has been fixed for improved readability, and the build process has been streamlined by updating Babel configurations and removing obsolete development tools. These changes collectively contribute to a more secure, stable, and user-friendly application.

Highlights

* Critical Security Enhancements: Addressed multiple security vulnerabilities by updating key dependencies like "axios" and "postcss", fixing issues such as CWE-343, CVE-2025-7783, and "PrismJS DOM Clobbering". Rate limiting was also introduced in "server.js" to prevent DoS attacks.

* AI Assistant UI Fixes: Resolved an issue where AI Assistant chat code blocks lacked proper word-wrapping and horizontal scrolling, significantly improving readability.

* Dependency Modernization: Updated Babel configurations to use "@babel/plugin-transform-class-properties" and removed obsolete development dependencies (Vite, Webpack, React-App-Rewired) to streamline the build and publishing process.

* Optimized Code Highlighting: The "ChatCodeBlock" component now intelligently imports supported languages from "react-syntax-highlighter", making the code cleaner and more robust.

* Improved Build Process: Enhanced Jest configuration to correctly handle ES modules from "node_modules" and updated the "Makefile" for better dependency management during publishing.

### CHANGELOG.md

#### [1.1.0] - 2025-11-17

##### Added
- Add local run protocol options (RUN_PROTOCOL) in .env.example.

##### Changed
- Update CHANGELOG format to be more semantic.
- Remove logging in AudioPlayer component for clarity.
- Modify Makefile to move development dependencies before pre-publishing [GS-230].
- Optimize ChatCodeBlock component by import the list of supported languages directly from react-syntax-highlighter instead of defining a long, hardcoded list of languages in getPrismLanguajes() [GS-230].

##### Fixed
- Fix the AI Assistant chat shows code blocks wrong with no word-wrapping or horizontal scrolling [GS-225].
- Remove Vite, Webpack and React-App-Rewired dependencies before publishing to NPM.
- Replace class-properties plugin with transform-class-properties to fix the "npm warn deprecated @babel/plugin-proposal-class-properties@7.18.6: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-class-properties instead." warning [GS-219].
- Fix the "[!] Only inline sourcemaps are supported when bundling to stdout." error when running "make publish" (specifically in the "rollup -c" command) because of `react-syntax-highlighter` v16+ and its dependencies now use ES modules exclusively, and Jest needs explicit configuration to transform these modules from `node_modules` (which are normally ignored by default) [FA-83].

##### Security
- Update "axios" to ^1.13.0 to fix the following security vulnerability [GS-219]:
  - "form-data" CWE-343, CVE-2025-7783, CVSS 9.4.
  - "Axios is vulnerable to DoS attack through lack of data size check"
  - "form-data uses unsafe random function in form-data for choosing boundary"
- Fix "PostCSS line return parsing error" by updating "postcss" to "^8.5.6" [GS-219].
- Basic rate limiting to mitigate DoS via expensive FS operations in "server.js" [GS-219].
- Update "react-syntax-highlighter" to "^16.1.0" to fix the security vulnerability [GS-219]:
  - "PrismJS DOM Clobbering vulnerability"
- Bump babel-loader to ^10.0.0 to fix "@eslint/plugin-kit is vulnerable to Regular Expression Denial of Service attacks through ConfigCommentParser" [GS-219].
- The following security vulnerabilities were fixed by running "npm update" [GS-219]:
  - "Prototype Pollution in JSON5 via Parse Method"
  - "pbkdf2 returns predictable uninitialized/zero-filled memory for non-normalized or unimplemented algos"
  - "pbkdf2 silently disregards Uint8Array input, returning static keys"
  - "Prototype pollution in webpack loader-utils"
  - "sha.js is missing type checks leading to hash rewind and passing on crafted data"

...

## GenericSuite Backend Core

### Package, Pull Request and Tag

* Package: https://pypi.org/project/genericsuite/0.2.0/
* Pull Request: https://github.com/tomkat-cr/genericsuite-be/pull/13
* Tag: https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.2.0

### Pull Request Overview

Summary of Changes

This pull request introduces the foundational implementation of an MCP (Microservice Communication Protocol) server, significantly enhancing the backend's microservice capabilities and inter-process communication. It also brings crucial security updates by overhauling API key authentication and updating several core dependencies to patch known vulnerabilities. The changes include substantial refactoring to improve modularity and maintainability, alongside updates to development environment configurations and build processes.

Highlights

* MCP Server Implementation: The core of this pull request is the implementation of an MCP (Microservice Communication Protocol) server, including new endpoints for user management (login, super admin creation, current user data, API key file generation) and a framework abstraction layer to support MCP.

* Enhanced Security: Significant security improvements have been made, particularly by moving API key authentication from temporary files in /tmp to direct database lookup. This mitigates risks associated with sensitive data storage in world-writable directories. Additionally, numerous dependency updates address various security vulnerabilities in libraries like urllib3, Werkzeug, cryptography, Requests, fastmcp, mcp, and dnspython.

* Architectural Refactoring for Modularity: The GenericDbHelper has been refactored into GenericDbHelperSuper (a base class without request context) and GenericDbHelperWithRequest (a request-aware class). This separation of concerns improves reususability and supports the new MCP server's operational model, which doesn't always involve a web request context.

* Dependency and Environment Management Improvements: The project now supports Python 3.10+ and Node.js 20. New environment variables (PEM_TOOL, AUTO_RELOAD, RUN_METHOD, etc.) have been introduced for more flexible configuration of Python package managers and local development. The Makefile has been updated with help and install commands, and poetry run is now used for build and publish steps.

* Code Quality and Maintainability: Various code quality improvements include fixing docstrings, removing unused code, simplifying environment variable handling with get_non_empty_value, and centralizing logging initialization logic into a private helper function to adhere to DRY principles.

### CHANGELOG.md

#### [0.2.0] - 2025-11-17

##### Added
- Implement MCP on GS BE Core [GS-189].
- Add PEM_TOOL envvar to select the Python package and dependency management tool (uv, pipenv, and poetry), default to "uv" [GS-77].
- Add AUTO_RELOAD envvar to .env.example, to fix some issues with the "--auto-reload" / "--reload" option running the app in "run_aws.sh", Turborepo and "uv", default to "1" [GS-77].
- Add get_non_empty_value function to handle envvars declared in docker-composer.yml with no value.
- Add "help" command to Makefile.
- Add "install" command to Makefile for easier dependency management.  

##### Changed
- Change Node.js version in .nvmrc to 20.
- Update README for clarity and accuracy.
- Update CHANGELOG format to be more semantic, for consistency, clarity, and "Keep a Changelog" standard.
- Update author email in pyproject.toml and setup.py.
- Modify pyproject.toml for compatibility with Python 3.10 and above.
- Add .vscode and .idea to the .gitignore file.
- Use Poetry to run build and publish commands in Makefile.  
- Code clean-up and linting changes.
- Authenticate API Keys from Database [GS-240]
- get_non_empty_value() function simplified using a more idiomatic Python pattern.

##### Fixed
- Update urllib3 dependency to version 2.5.0 to fix a "make publish" error.
- Add new development dependencies "build" and "twine" to fix a "make publish" error.
- Fix the "boto3" and "s3transfer" conflict by removing "s3transfer" and "botocore" dependencies in the pyproject.toml file, because they are already included in "boto3".
- Update error handling in set_tool_context() function to retrieve a more concise error message from app_context [GS-240].

##### Security
- Update "urllib3" to "^2.5.0" to fix security vulnerabilities [GS-219]:
    * "Catastrophic backtracking in URL authority parser when passed URL containing many @ characters"
    * "`Cookie` HTTP header isn't stripped on cross-origin redirects"
    * "urllib3 redirects are not disabled when retries are disabled on PoolManager instantiation"
    * "urllib3's Proxy-Authorization request header isn't stripped during cross-origin redirects"
    * "urllib3's request body not stripped after redirect from 303 status changes request method to GET"
    * "Using default SSLContext for HTTPS requests in an HTTPS proxy doesn't verify certificate hostname for proxy connection"
    * "`Cookie` HTTP header isn't stripped on cross-origin redirects"
- Update "Werkzeug" to "^3.0.6" to fix security vulnerabilities [GS-219]:
    * "Werkzeug possible resource exhaustion when parsing file data in forms"
    * "Werkzeug safe_join not safe on Windows"
- Update "cryptography" to "^44.0.1" to fix security vulnerability [GS-219]:
    * "pyca/cryptography has a vulnerable OpenSSL included in cryptography wheels"
- Update "Requests" to "^2.32.4" to fix security vulnerabilities [GS-219]:
    * "Requests vulnerable to .netrc credentials leak via malicious URLs"
    * "Using default SSLContext for HTTPS requests in an HTTPS proxy doesn't verify certificate hostname for proxy connection"
    * "Vulnerable OpenSSL included in cryptography wheels"
- Update "fastmcp" to "^2.13.0" to fix security vulnerabilities [GS-219]:
    * "FastMCP Auth Integration Allows for Confused Deputy Account Takeover"
    * "Authlib is vulnerable to Denial of Service via Oversized JOSE Segments"
- Update "mcp" to ">=1.21.0" to fix security vulnerabilities [GS-219]:
    * "Starlette vulnerable to O(n^2) DoS via Range header merging in ``starlette.responses.FileResponse``"
- Update "dnspython" to ">=2.6.1" to fix security vulnerabilities [GS-219]:
    * "Potential DoS via the Tudoor mechanism in eventlet and dnspython"
- Read the user data from the database in "get_api_key_auth()" instead of the "/tmp/params_[user_id].json" because storing sensitive or configuration data in a world-writable directory like /tmp is a security risk [GS-240].
- Add USER_PARAMS_FILE_ENABLED envvar to enable/disable user's parameters file "/tmp/params_[user_id].json", default to "0" to avoid security risks when running in a production environment [GS-240].

...

## GenericSuite Backend AI

### Package, Pull Request and Tag

* Package: https://pypi.org/project/genericsuite-ai/0.2.0/
* Pull Request: https://github.com/tomkat-cr/genericsuite-be-ai/pull/11
* Tag: https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.2.0

### Pull Request Overview

Summary of Changes

This pull request delivers a significant update focused on enhancing the security, maintainability, and development experience of the project. It addresses critical security vulnerabilities by updating core dependencies, streamlines the integration of HuggingFace models, and refines the build and configuration processes. These changes aim to improve the stability and robustness of the application while providing clearer development guidelines.

Highlights

* Security Updates: Multiple dependencies including transformers, urllib3, setuptools, clarifai, pypdf, and langchain have been updated to address various security vulnerabilities, such as Regular Expression Denial of Service (ReDoS), path traversal, and XML External Entity (XXE) attacks.

* HuggingFace Model Refactoring: The handling of HuggingFace models has been refactored. The huggingface model type now integrates with the OpenAI API for text generation, while the previous behavior is moved to a new langchain_huggingface type. Custom GsHuggingFaceEndpoint and GsChatHuggingFace classes have been removed in favor of the new Hugging Face with OpenAI API calls.

* Dependency Management and Build Process Improvements: The project's Python version requirement has been updated from 3.9 to 3.10. New install commands have been added to the Makefile for easier dependency management, and build and publish commands now explicitly use poetry run.

* Configuration and Environment Variables: New environment variables PEM_TOOL (for Python package management) and AUTO_RELOAD (for local development) have been introduced. Debugging flags across various AI modules are now configurable via environment variables (e.g., AI_CHATBOT_DEBUG, AI_AUDIO_PROCESSING_DEBUG, etc.). The .env.example file has been updated for clarity and to reflect new configuration options.

* Langchain Compatibility and Code Clean-up: Imports from langchain.* have been migrated to langchain_classic.* to ensure compatibility with Langchain 1.0.x. Several DEBUG flags have been made configurable via environment variables, and numerous code formatting and docstring improvements have been made, including correcting typos and adding noqa: E501 for long lines.

* Removed Dependencies: The langchain-together, text-generation and clarifai dependencies have been removed from the project.

### CHANGELOG.md

#### [0.2.0] - 2025-11-17

##### Added
- Add "install" command to Makefile for easier dependency management.  
- Add PEM_TOOL envvar to .env.example, to select the Python package and dependency management tool (uv, pipenv, and poetry), default to "uv" [GS-77].
- Add AUTO_RELOAD envvar to .env.example, to fix some issues with the "--auto-reload" / "--reload" option running the app in "run_aws.sh", Turborepo and "uv", default to "1" [GS-77].
- Add DEBUG envvars to all AI modules to enable debug logging, default to "0" (they must be set on the .env file) [GS-230].

##### Changed
- Update README for clarity and accuracy.
- Update CHANGELOG format to be more semantic.
- Update author email in pyproject.toml and setup.py.
- Bump urllib3 to 2.5.0 and numpy to 2.0.2 to have compatibility with GS BE Core.
- Refactor imports in ai_langchain_models.py to include ChatBedrock (AWS Bedrock) and langchain-aws conditionally.
- Enhance HuggingFace text query functions ("huggingface_remote" model type) to support OpenAI API integration.
- Change "huggingface" model type to use OpenAI API instead of langchain's HuggingFaceEndpoint and ChatHuggingFace, so "langchain-huggingface" dependency is not required.
- The old "huggingface" model type is now "langchain_huggingface" and requires the "langchain-huggingface" dependency, which is optional by default.
- The "gs_huggingface" model type is the same as the "huggingface_remote" model type, calling Hugging Face with requests.

##### Fixed
- Fix AI tools calling error due to pydantic parameter type mismatch, changing the type annotation from Dict to Any.
- Fix the "langchain_community not found" by adding the "langchain-community" dependency. This addition required the upgrade of dependencies "langchain" to "0.3.26" and "faiss-cpu" to "^1.11.0.post1".
- Fix "huggingface_remote" text query functions streaming responses errors.
- Fix the issues with the new langchain 1.0.x migrating some langchain.* imports to langchain_classic.* imports.
- Add new development dependencies including build and twine to fix a "make publish" error.
- Use Poetry to run build and publish commands in Makefile to fix a "make publish" error. 

##### Security
- Update "transformers" to "^4.57.1" to fix security vulnerabilities [GS-219]:
    * "Regular Expression Denial of Service (ReDoS)", CVE-2025-5197 and CWE-1333
    * "Hugging Face Transformers Regular Expression Denial of Service (ReDoS) vulnerability"
    * "Hugging Face Transformers vulnerable to Regular Expression Denial of Service (ReDoS) in the AdamWeightDecay optimizer"
    * "Hugging Face Transformers library has Regular Expression Denial of Service"
    * "Hugging Face Transformers is vulnerable to ReDoS through its MarianTokenizer "
    * "Transformers is vulnerable to ReDoS attack through its DonutProcessor class"
    * "Transformers's Improper Input Validation vulnerability can be exploited through username injection"
- Update "urllib3" to "^2.5.0" to fix security vulnerabilities [GS-219]:
    * "Catastrophic backtracking in URL authority parser when passed URL containing many @ characters"
    * "`Cookie` HTTP header isn't stripped on cross-origin redirects"
    * "urllib3 redirects are not disabled when retries are disabled on PoolManager instantiation"
    * "urllib3's Proxy-Authorization request header isn't stripped during cross-origin redirects"
    * "urllib3's request body not stripped after redirect from 303 status changes request method to GET"
    * "Using default SSLContext for HTTPS requests in an HTTPS proxy doesn't verify certificate hostname for proxy connection"
    * "`Cookie` HTTP header isn't stripped on cross-origin redirects"
- Update "setuptools" to "^78.1.1" to fix the security vulnerability [GS-219]:
    * "setuptools has a path traversal vulnerability in PackageIndex.download that leads to Arbitrary File Write"
- Remove "text-generation" to fix the security vulnerability (also it's not used in this project) [GS-219]:
    * "Code injection vulnerability exists in the huggingface/text-generation-inference repository"
- "llama-index-core" vulnerabilities are solved because it's no longer a dependency of this project (due to clarifai removal):
    * "llama-index-core insecurely handles temporary files"
    * "LlamaIndex affected by a Denial of Service (DOS) in JSONReader"
    * "LlamaIndex vulnerable to Path Traversal attack through its encode_image function"
    * "LlamaIndex vulnerable to DoS attack through uncontrolled recursive JSON parsing"
    * "LlamaIndex has Incomplete Documentation of Program Execution related to JsonPickleSerializer "
- Install "pypdf" latest version "^6.1.3" to fix security vulnerabilities (it was a dependency of clarifai) [GS-219]:
    * "pypdf possibly loops infinitely when reading DCT inline images without EOF marker"
    * "pypdf can exhaust RAM via manipulated LZWDecode streams"
    * "PyPDF's Manipulated FlateDecode streams can exhaust RAM"
- Update all langchain dependencies to latest versions to fix security vulnerabilities [GS-219]:
    * "LangChain Text Splitters is vulnerable to XML External Entity (XXE) attacks due to unsafe XSLT parsing"

##### Removed
- Remove "langchain-together" to enable upgrade of all other langchain dependencies, and routes Together AI calls through the OpenAI API.
- Remove "clarifai" to make it optional by default [GS-219].
- Remove GsHuggingFaceEndpoint and GsChatHuggingFace classes because they were replaced by the new Hugging Face with OpenAI API calls.

...

## GenericSuite Backend Scripts

### Package, Pull Request and Tag

* Package: https://www.npmjs.com/package/genericsuite-be-scripts/v/1.2.0
* Pull Request: https://github.com/tomkat-cr/genericsuite-be-scripts/pull/11
* Tag: https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.2.0

### Pull Request Overview

Summary of Changes

This pull request introduces significant enhancements to the project's dependency management and local development workflows. It integrates modern Python package managers 'uv' and 'poetry' as first-class citizens, providing a unified interface through a new 'run_pem.sh' script. The changes also include an upgrade to Node.js 20, more flexible auto-reload configurations for local application servers, and a broad refactoring of shell scripts to improve consistency and Linux compatibility. These updates aim to provide developers with more choice and a smoother experience when managing project dependencies and running local services.

Highlights

* Python Package Management Overhaul: Introduced 'uv' and 'poetry' as alternative Python package and dependency management tools, alongside 'pipenv', with 'uv' now set as the default. A new wrapper script, 'run_pem.sh', centralizes all package manager operations for consistency.

* Enhanced Development Environment: Updated the Node.js version to 20, refined auto-reload options for local servers (Chalice, Gunicorn, Uvicorn), and adjusted MongoDB service restart policies to 'unless-stopped' for better local development experience.

* Scripting Consistency and Linux Compatibility: Standardized shell script execution by replacing 'sh' with 'bash' across numerous Makefile targets and internal script calls, improving compatibility and consistency, especially for Linux environments.

* Improved Dependency Management Workflows: Added new 'make update' and 'make update_dev' targets, and ensured 'npm install' runs before Python dependency installations, streamlining the process of keeping project dependencies current.

### CHANGELOG.md

#### [1.2.0] - 2025-11-17

##### Added
- Add "uv" and "poetry" Python package and dependency management tools [GS-77].
- Add PEM_TOOL envvar to select the Python package and dependency management tool (uv, pipenv, and poetry), default to "uv" [GS-77].
- Add AUTO_RELOAD envvar to fix some issues with the "--auto-reload" / "--reload" option running the app in "run_aws.sh", Turborepo and "uv", default to "1" [GS-77].
- Add Linux compatibility: replace "sh" by "bash" in Makefile and package.json files to run on Linux [GS-230].
- Add "make update" and "make update_dev" to update the dependencies.

##### Changed
- Update: increment Node.js version in .nvmrc to 20.
- Modify author email in package.json.
- Enhance README for license and credits clarity.
- Update CHANGELOG format to be more semantic.
- Change: update MongoDB service restart policy from 'always' to 'unless-stopped' in the test stack configuration.
- Change "make install" and "make install_dev" to call "sh node_modules/genericsuite-be-scripts/scripts/run_pem.sh install" and "sh node_modules/genericsuite-be-scripts/scripts/run_pem.sh install_dev" respectively

##### Fixed
- Change "make install" and "make install_dev" so "npm install" is called before "sh node_modules/genericsuite-be-scripts/scripts/run_pem.sh" to install the GS BE Scripts and avoid the error "Error: Cannot find module 'genericsuite-be-scripts' [GS-77].
- Fix "change_local_ip_for_dev.sh" adding parameter $2 & $3 checks to avoid overwriting BACKEND_LOCAL_PORT and FRONTEND_LOCAL_PORT envvars [GS-230].

...

## GenericSuite BaseCamp

### Pull Request and Tag

* Pull Request: 
  - https://github.com/tomkat-cr/genericsuite-basecamp/pull/10
  - https://github.com/tomkat-cr/genericsuite-basecamp/pull/11
  - https://github.com/tomkat-cr/genericsuite-basecamp/pull/12
* Tag: https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.3.0

### Pull Request Overview (Summary)

Summary of Changes

This update significantly enhances the ExampleApp by integrating a new MCP server for nutrition management. Beyond features, we have modernized the development environment by switching to uv for Python management and refining our pnpm build processes. The release also includes a comprehensive restructuring of the GenericSuite documentation and essential security patches to ensure a more robust and developer-friendly ecosystem.

Highlights

* New MCP Server for ExampleApp: A new Model Context Protocol (MCP) server has been added to the ExampleApp, introducing food and nutrition management tools and becoming a fourth backend option alongside FastAPI, Flask, and Chalice. Also, new 'make' commands were included to simplify the installation and update processes for all ExampleApp services.

* Python Environment & Dependency Management: The ExampleApp project is transitioning to Python 3.12 and adopting 'uv' as the preferred Python package and dependency management tool, with comprehensive documentation provided for migrating from 'pipenv'.

* Documentation Updates: Documentation has been expanded and clarified, covering detailed ExampleApp configuration, guidance on Python package managers, and new AI module debug flags.

* Specs Restructuring and Enhancement: The project's specs documents has undergone a significant overhaul, with the former 'GEMINI.md' being replaced by a suite of detailed context files (Project Brief, Product Context, Active Context, System Patterns, Tech Context). This provides a more structured and comprehensive overview of the GenericSuite ecosystem.

* Dependency and Build System Updates: Key dependency files like .gitignore, pnpm-lock.yaml, and requirements.txt have been updated to reflect new packages, remove unused ones, and ensure consistent dependency resolution. Build scripts and configurations have also been adjusted to support the new MCP server and improve overall stability.

* Improved Developer Experience: Changes include adding documentation for symlinking GenericSuite libraries for hot-reloading, updating .env.example files for clarity, and fixing the mkdocs_install.sh script for proper dependency management, all aimed at streamlining the development workflow.

* ExampleApp Pydantic Validation and AI Prompt Generation: The ai_gpt_fn_app.py file now includes Pydantic field validators for various units and meal types, ensuring data integrity. New functions for generating nutrition analysis and meal planning AI prompts have also been added.

* New Makefile Command: A new update-pnpm command has been added to the ExampleApp Makefile to streamline the installation process.

* Changelog Standardization: The project's CHANGELOG.md files have been updated to strictly follow the 'Keep a Changelog' standard, ensuring a consistent and semantic format for release notes across all components.

* Dependency Updates: Several dependencies in pnpm-lock.yaml have been updated, including @vitejs/plugin-react, postcss, and @rolldown/pluginutils, along with adjustments to Babel plugins and peer dependencies.

* PNPM Workspace Configuration: The pnpm-workspace.yaml file has been enhanced to specify onlyBuiltDependencies for better package management.

* Security Improvements: Key security enhancements have been implemented, such as updating critical package dependencies (e.g., turbo, dotenv, GS BE Core/AI libraries) and disabling the 'X-Powered-By' header in the UI to prevent exposure of framework information.

### CHANGELOG.md

#### [1.3.0] - 2025-11-17

##### Added
- Add new MCP server for ExampleApp with food and nutrition management tools [GS-189]. 
- Add Linux compatibility: replace "sh" by "bash" in Makefile and package.json files to run on Linux [GS-230].
- Add PEM_TOOL envvar to select the Python package and dependency management tool (uv, pipenv, and poetry), default to "uv" [GS-77].
- Add AUTO_RELOAD envvar to fix some issues with the "--auto-reload" / "--reload" option running the app in "run_aws.sh", Turborepo and "uv", default to "1" [GS-77].
- Add the `make exampleapp-update-all` and `make exampleapp-install-all` commands to update and install all ExampleApp apps.
- Add the `make link_gs_libs` documentation to the GS BE Scripts.
- Add unlinking common assets and prompting user confirmation before cleaning directories in the `make exampleapp-clean` command.
- Add "clean" command in Makefile for asset management.
- Add new `update-pnpm` command in ExampleApp Makefile for streamlined installation.
- Add the MCP_SERVER_PORT, MCP_SERVER_HOST, MCP_TRANSPORT, GS_USER_NAME, GS_USER_ID, and GS_API_KEY envvars to the ExampleApp MCP server .env.example file [GS-189].
- Add the "mcp_server.log" file to the ExampleApp MCP server directory so it can be debugged more easily.
- Add HUGGINGFACE_PROVIDER envvar to configure the Hugging Face inference provider, default to "auto" [GS-241].
- Add LANGCHAIN_AGENT_TYPE=lcel option to the GenericSuite AI documentation.
- Add DEBUG envvars to all AI modules to enable debug logging, default to "0" (they must be set on the .env file) [GS-230].

##### Changed
- Update .gitignore to include IDE configurations and remove unused utility files.
- Remove unused utility files from ExampleApp all 3 backends.
- The "GEMINI.md" file was renamed and moved to "specs/productContext.md".
- Update the "productContext.md" file to reflect the new ExampleApp and MCP server.
- Add memory bank documents in the "specs" directory.
- Update CHANGELOG format to be more semantic.
- Enhance documentation for ExampleApp configuration, including: detailed directory structure and backend/frontend distinctions.
- ExampleApp MCP server: use the GS BE MCP library changes, enhance envvars management in the run script, and update requirements.txt for compatibility with new library versions.
- Replace HUGGINGFACE_ENDPOINT_URL envvar by HUGGINGFACE_DEFAULT_CHAT_MODEL and HUGGINGFACE_DEFAULT_IMG_GEN_MODEL envvars in the ExampleApp .env.example template files.
- Update Python default version to 3.12 in the documentation and ExampleApp .python-version files [GS-230].
- Update Python minimum version to 3.10 in the documentation [GS-230].
- Update all GenericSuite dependencies to the latest versions (npm, uv, pipenv) on the ExampleApp [GS-230].

##### Fixed
- Fix "mkdocs_install.sh" to update mkdocs dependencies to the latest version and rebuild requirements.txt file appropiately.

##### Security
- Update package dependencies in package.json and pnpm-lock.yaml to upgrade turbo and dotenv [GS-219].
- ExampleApp UI: Disable X-Powered-By header to avoid exposing framework information in server.js [GS-219].
- Update GS BE Core and AI libraries in ExampleApp to fix dependabot alerts [GS-219].
- Add USER_PARAMS_FILE_ENABLED envvar to enable/disable user's parameters file "/tmp/params_[user_id].json", default to "0" to avoid security risks when running in a production environment [GS-240].

...

## GenericSuite Gitops

### Pull Request and Tag

* Pull Request: https://github.com/tomkat-cr/genericsuite-gitops/pull/4
* Tag: https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.4.0

### Pull Request Overview # 2

Summary of Changes

This pull request significantly expands the GenericSuite GitOps toolkit by introducing a new Nginx Router module for robust web traffic management and automated SSL certificate generation. It standardizes operational practices across various services like Ollama, N8n, Kubernetes, Docker, GitLab Runner, and VPS deployments by adding comprehensive Makefiles and READMEs. The changes also focus on improving script robustness, enhancing Docker container lifecycle management, and providing detailed internal documentation to streamline development and deployment workflows.

Highlights

* Nginx Router Module: Introduced a new Nginx Router module, complete with example configurations, Docker Compose setup, and Makefile targets for managing its lifecycle (run, stop, restart, logs, SSL certificate generation).

* Automated SSL Certificate Generation: Added scripts for generating SSL certificates using both Let's Encrypt (for Debian/Ubuntu and macOS) and auto-signed certificates via Mkcert, enhancing security and ease of setup for web services.

* Standardized Documentation and Automation: Added README.md and Makefile files to ollama, n8n, k8, docker, gitlab_runner, vps, and scripts directories, providing consistent documentation and automated command execution for each module.

* Enhanced Ollama Management: Integrated ollama_update functionality into the Ollama manager, allowing for easier updates of the local LLM service.

* Improved N8n Configuration and Docker Integration: Added an init command to N8n for initial configuration setup and included Docker configuration files (docker-compose.yml, .env) in .gitignore to prevent accidental version control.

* Robustness and Best Practices for Shell Scripts: Implemented set -euo pipefail across numerous shell scripts for improved error handling and robustness, along with modernizing variable assignments and command checks.

* Docker Restart Policy Update: Changed the Docker restart policy to unless-stopped for n8n, postgres, and pgadmin services, ensuring containers automatically restart after system reboots unless explicitly stopped.

* Comprehensive Internal Documentation: Added several memory bank documents (activeContext.md, productContext.md, projectBrief.md, systemPatterns.md, techContext.md) to the specs directory, detailing the project's context, architecture, and technical decisions.

### CHANGELOG.md

#### [0.4.0] - 2025-11-17

##### Added
- Add Nginx Router module [GS-180] [GS-234].
- Add SSL certificate generation with Let's Encrypt and Mkcert [GS-180].
- Add "README.md" and "Makefile" files to the "ollama", "n8n", "k8", "docker", "gitlab_runner", "vps", and "scripts" directories [GS-231].
- Add "ollama_update" to ollama manager [GS-229].
- Add memory bank documents in the "specs" directory [GS-208].
- Improved user experience with additional helper scripts and commands, e.g. Tmux cheatsheet [GS-231].

##### Changed
- Update CHANGELOG format to be more semantic [GS-222].
- Vps - scripts enhanced to implement better linux server practices [GS-231].
- N8n - add init command and gitignore docker configuration files [GS-141].
- Change restart policy to 'unless-stopped' for n8n, postgres, and pgadmin services [GS-141].

##### Fixed
- Fix connectivity checks across services [GS-231]
- Fix vps/create_server_users_and_groups.sh error when adding user to sudoers group [GS-230].
