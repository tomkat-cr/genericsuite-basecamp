# 20260218 - The 2nd Anniversary Edition

![GS_Release_2026-02-18_Image_1A.png](./images/GS_Release_2026-02-18_Image_1A.png)

Date: 2026-02-18

## Summary

Celebrating 2 Years of Innovation: GenericSuite Release 2026-02-18 is Live! 🚀

As we hit our 2nd-anniversary milestone, we are thrilled to announce a transformative update to the GenericSuite ecosystem. This release focuses on three pillars: Flexibility, Performance, and Security.

Key Professional Benefits:

* Database & Cloud Agnostic: We’ve broken the limits. Support now extends to PostgreSQL, MySQL, and Supabase, along with the already existing MongoDB and DynamoDB. 

* Enhanced Developer Experience: With the new FastAPI Template, automated dependency synchronization for Dockerfiles, Podman container engine, and MCP server standard startup script, automatic local database tables structure creation, super user creation, setting up robust backend services is faster than ever.

* Frontend Optimization: A complete refactor of our Generic CRUD Editor (GCE_RFC) using React performance hooks significantly reduces component reloads, paired with a modern "rounded-xl" UI.

* AI & Security: Integrated AI Conversation attachments URL masking/pre-signed URLs prevents over-billing attacks during LLM interactions.

* Cloud storage abstraction layer: opening a path to switch between AWS S3, Azure Blob, and Google Cloud Storage (AWS is 100% implemented so far).

* Modern Data Validation: Migrating to Pydantic ensures faster, more reliable data serialization and strictly typed schemas, reducing runtime errors.

This "2nd Anniversary Edition" is designed to scale with your business needs, providing the foundation for high-performance, AI-driven applications. Check out the full changelog for details on our new Cloudflare Tunnel integration and Python 3.12 support!

## GenericSuite Frontend Core

### Package, Pull Request and Tag

* Package: [https://www.npmjs.com/package/genericsuite/v/1.2.0](https://www.npmjs.com/package/genericsuite/v/1.2.0)
* Pull Request: [https://github.com/tomkat-cr/genericsuite-fe/pull/9](https://github.com/tomkat-cr/genericsuite-fe/pull/9)
* Tag: [https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.2.0](https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.2.0)

### Pull Request Overview

Generic editor form page child listings with external tables, API versioning, and better monorepo compatibility

This pull request introduces a comprehensive set of enhancements and optimizations across the application, primarily focusing on the Generic CRUD Editor's capabilities, state management, and overall user experience. It refactors core components to leverage React's performance hooks, standardizes environment configurations, and streamlines build processes. These changes aim to provide a more robust, performant, and developer-friendly foundation for future development.

Highlights

- Enhanced Generic CRUD Editor (GCE_RFC): The Generic CRUD Editor now supports external tables with subType: "table" for child listings, allowing for more flexible data relationships. Field types h1 to h6 have been added for better form page structuring, and the SuggestionDropdown component has been improved with debounce and useCombobox hook for better performance and user experience. API calls within GCE_RFC have been optimized to avoid repetitions.
- API Key Management and User Data Caching: API keys are now managed in a separate users_api_keys table, and the user profile page includes a dedicated section for API keys. User data caching (getUserDataCache, setUserDataCache) has been implemented to optimize user data retrieval.
- Improved State Management and Performance: Key contexts (MainSectionContext, UsersContext, AppContext) have been refactored to utilize useCallback, useMemo, useRef, and useReducer hooks, significantly reducing unnecessary component reloads and improving overall application performance. A caching mechanism (fetchOrCache) has been introduced in the MainSectionProvider to optimize data fetching.
- Flexible Environment Variable Handling: Frontend environment variables have been standardized to avoid conflicts in monorepo setups, allowing REACT_APP_ prefixed variables to be replaced by APP_ prefixed ones. New environment variables like API_VERSION, API_KEYS_PREFIX, USE_CONTAINERS_ENGINE_APP, and RUN_PROTOCOL_AND_PORT_REPLACEMENT have been added for greater configuration flexibility.
- UI/UX Refinements: Buttons and input fields across the application have been updated with a more rounded rounded-xl style. Error messages on the login page are enhanced, and a close button has been added to GCE_RFC index messages. Animation classes have been renamed for clarity, and a new error icon has been added to GsIconLib.
- Build Process and Tooling Updates: The project's dependencies, including babel-jest, jest, and postcss-loader, have been updated. New Makefile targets (tailwind-build) and a new script (link_external_configs.sh) have been added to streamline Tailwind CSS rebuilding and external JSON configuration linking for local development and testing.

### CHANGELOG.md

#### [1.2.0] - 2026-02-18

##### Added
- API_VERSION envvar to set the API version, default to "v1" [GS-245].
- Generic editor form page child listings now accepts external tables with the subType "table" [GS-159].
- Horizontal rule separator before child elements in generic editor form pages [GS-250].
- API_KEYS_PREFIX envvar to set the API keys prefix, default to "sk-gsu-" [GS-159].
- WAIT_ANIMATION_MARGIN_TOP_CLASS constant to add top margin to <WaitAnimation /> in the <App /> component [GS-246].
- UPDATE_SNAPSHOTS envvar to "make publish" to run "npm test -- -u" instead of "npm run test".
- "UPDATE_SNAPSHOTS=1 make publish" documentation on Makefile.
- Field types h1 to h6 to JSON files [GS-250].
- "make tailwind-build" to rebuild the Tailwind CSS files (without stay watching for changes) [GS-63].
- "make tailwind-build" added to the publish bash script [GS-63].
- getUserDataCache and setUserDataCache to set a cache reading current user's data, ad implemented in the Users.jsx specific functions [GS-251].
- Close button for GCE_RFC Index page emerging messages (e.g. "X items deleted...") shown returning from the Form Data page [GS-251].
- Api Keys child component added to User Profile [GS-159].
- "customOnChange()" function added to <PutOneFormfield /> as "onChange" parameter, also Formik setFieldValue() added as "setValue" parameter, so "component" type fields can update the Formik internal values and therefore saved in the database [GS-252].
- ShowAsDisabledField component can render the custom component as a simulated disabled field (current behavior) or as a Formik Field, customizable with the new "showAsField", "isReadOnly", "type", "onChange", "onBlur" parameters. OnChange allows to store the calculated value in the Formik internal values and therefore saved in the database [GS-252].
- USE_CONTAINERS_ENGINE_APP envvar to control whether to use containers engine app for local development environment when RUN_PROTOCOL="https" [GS-257].
- RUN_PROTOCOL_AND_PORT_REPLACEMENT envvar to control automatic protocol and port replacement for local development environment variables APP_FE_URL_DEV and APP_API_URL_DEV [GS-257].
- "link_external_configs.sh" script to link external JSON configs directory so it can be tested in GenericSuite FE Core [GS-258].
- "config_name" field type change to "suggestion_dropdown" in "Admin > Users > User Configurations", so the Suggestion Dropdown can be tested in GenericSuite FE Core [GS-258].
- Error icon to GsIconLib [GS-258].
- <ChatBotButtonGeneric /> component to add a try-catch layer to field definitions that has "chatbot_popup" set to true [GS-258].
- Comprehensive parameter documentation for `GenericSelectDataPopulator`.
- Comprehensive documentation for `getUrlParams`.
- VERBOSE_RUN_CONFIG envvar to enable verbose logging in run_config.sh.
- MD5 utilities [GS-266].
- BSON-type ObjectId() generation to "id.utilities.jsx" [GS-266].
- "UsersUserHistory.jsx" and "users_user_history.json" to debug child listings with dates and MondoDB BSON-type ObjectId() generation [GS-266].
- Implement navigation helpers for testability [GS-267].
- "generalUtilities" to detect different element types, including dict and list [GS-251].

##### Changed
- Enhance error message in the login page [GS-246].
- Update class_name_constants.jsx to make buttons more rounded and remove unused comments [GS-246].
- Update getFetch() to check if the response is ok using the [200, 201, 202, 204] status codes [GS-245].
- Rename style class constants: PAGE_ANIMATION_CLASS to WAIT_ANIMATION_CLASS, SHOW_HIDE_PAGE_ANIMATION_ENABLED_CLASS to WAIT_ANIMATION_ENABLED_CLASS, SHOW_HIDE_PAGE_ANIMATION_DISABLED_CLASS to WAIT_ANIMATION_DISABLED_CLASS [GS-246].
- Rename component <ShowHidePageAnimation /> to <ShowHideWaitAnimation /> [GS-246].
- Horizontal rule separator <hr /> is now dashed [GS-250].
- API keys now are in a separate table "users_api_keys", not an array of the "users" table [GS-159].
- Rename "parentKeyNames" to "endpointKeyNames" in JSON config files [GS-159].
- Move "parentUrl" attribute from "endpointKeyNames" to the root of the JSON config files [GS-159].
- MainSectionContext, UsersContext and AppContext implemment useCallback, useMemo, useRef, and useReducer instead of useState, to avoid components unnecessary reloads [GS-251].
- Configs README referece the official GenericSuite documentation instead of repeating its content [GS-251].
- getFieldElementsYupValidations() enabled to have validations on the Form Data page [GS-251].
- Rename state and setState with errorState, setErrorState on AppContext.jsx, App.jsx, generic.editor.rfc.selector.jsx, generic.menu.service.jsx [GS-251].
- Rename status and setStatus with errorStatus, setErrorStatus on generic.editor.rfc.formpage.jsx [GS-251]
- Rename <FormPage /> parameters: mode_par, id_par, and editor_par to mode, id, and editor [GS-251].
- Rename the frontend envvars to avoid conflicts with the same envvar used in the backend and be able to merge the ".env" files in a monorepo: GIT_SUBMODULE_LOCAL_PATH to GIT_SUBMODULE_LOCAL_PATH_FRONTEND, and RUN_METHOD to RUN_BUNDLER [GS-243].
- REACT_APP_APP_NAME envvar can be removed and replaced by APP_NAME in monorepos [GS-243].
- REACT_APP_DEBUG envvar can be removed and replaced by APP_DEBUG in monorepos [GS-243].
- If REACT_APP_API_URL is not set, APP_API_URL can be used instead [GS-243].
- If REACT_APP_URI_PREFIX is not set, URI_PREFIX can be used instead [GS-243].
- If REACT_APP_X_TOKEN is not set, X_TOKEN can be used instead [GS-243].
- If REACT_APP_USE_AXIOS is not set, USE_AXIOS can be used instead [GS-243].
- Send "currentObj" to "select_component" and "component" field types now receive "currentObj" as a parameter in getSelectDescription() [GS-258].
- Pass `dbRow` to form fields types "select_component" and "component" for enhanced data context [GS-37].
- Export `buildDescription` utility on "generic.editor.rfc.selector" and enhance "GenericSelectGenerator" documentation [GS-37].
- Pass `currentObj` as a parameter to `dataPopulator` on getSelectFieldsOptions() [GS-37].
- Centralize and enhance API error message extraction with a new `getErrorMsgFromApi` helper to avoid error messages like "[object Object]" when axios is used [GS-262].
- Rename "idUtilities.getUuidV4" to "uuidUtilities.getUuidV4" [GS-266].
- Login page design enhanced by isolating the logo from the user and password box.

##### Fixed
- Error message when using axios and the session expires or the user credentials are invalid [GS-246].
- API "errorMsg" as an array when there are errors in the main API call or in the specific functions API calls [GS-251].
- getFileExtension() to remove the URL query parameters [GS-72].
- Optimize the Generic CRUD Editor (GCE_RFC) API calls, avoiding repeated calls [GS-251].
- Optimize the Generic Menu Generator (GMG) API calls, avoiding repeated calls [GS-251].
- Login button shown on each page refresh, while menus are loading [GS-251].
- GMG shows the "URL not found..." message during the menu loading [GS-251].
- GCE_RFC doesn't show the error message when the session has been expired [GS-251].
- Suppress warning on the LoginPage about the username and password autocomplete attributes (More info: https://goo.gl/9p2vKq)
- Fix input field color in the <SuggestionDropdown /> component [GS-252].
- Fix the Cache initialization in the Generic CRUD Editor provider (MainSectionProvider) [GS-252].
- Fix SuggestionDropdown component: use debounce to limit the number of calls to the API, and replace legacy Downshift component with useCombobox hook [GS-258].
- Show the error message in the login page when using axios and the session expires or the user credentials are invalid [GS-37] [GS-202].
- Implement secure markdown rendering for messages [GS-262].
  * The includesAppValidLinks function is used as a security heuristic to determine if an error message should be rendered as HTML. This check was insufficient as it only verifies if the message contains a hardcoded 'valid' email or URL. An attacker can bypass this check by including one of these strings (e.g., 'support@exampleapp.com') in a malicious payload. If the error message contains untrusted data, such as reflected input from an API error response, this leads to a Cross-Site Scripting (XSS) vulnerability when the message is rendered in the UI.
- Optimize user data fetching with request caching to avoid race conditions [GS-262].
- "TypeError: stringDate.indexOf is not a function" on addMissingTz when the supplied date is a number [GS-194].
- "[object Object] EFFF-020" when the API returns an error deleting/updating the item on EditFormFormikFinal() [GS-194].
- Date not shown on read-only child listings data forms: timestampDbPostRead() use resultset[0] for calling processTimestampToDate() because "date" and "datetime-local" fields shown as "mm/dd/yyyy, --:-- --" [GS-266]
- Use MD5 utilities to hash rowId in data forms when there's no row._id or row[editor.primaryKeyName], avoiding the "Encountered two children with the same key, `<table_name>_row_undefined_tr_enclosure`" warning [GS-266].
- Query parameters are not recognized in getUrlParams() [GS-266].
- Show only content when `menu=0` in the main page [GS-266].
- Disable next page button and avoid show "Page 1 of 0" message when the table has no items on the GCE_RFC [GS-266].
- Fix the drop-down menus closing when any other element is clicked [GS-266].
- Prevent React warnings by handling null/undefined form field values in getFieldElementsDbValues() [GS-266] [GS-262].

##### Security
- Upgrade jest and babel to latest versions to fix the "npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful." warning [GS-219] [GS-267].
- 37 security vulnerabilities (including high and critical ones) found in the project's dependencies were addressed, adding an "overrides" section to package.json to force secure versions of transitive dependencies (elliptic, json5, minimatch, postcss, loader-utils) without breaking your high-level setup [GS-219] [GS-267].

## GenericSuite Frontend AI

### Package, Pull Request and Tag

* Package: [https://www.npmjs.com/package/genericsuite-ai/v/1.2.0](https://www.npmjs.com/package/genericsuite-ai/v/1.2.0)
* Pull Request: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/9](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/9)
* Tag: [https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.2.0](https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.2.0)

### Pull Request Overview

Fix AI Assistant popup routing to use hash-based URLs, API versioning, and better monorepo compatibility

This pull request primarily focuses on enhancing the frontend's environment variable management for better monorepo compatibility and standardizing build processes. It introduces new environment variables for API versioning, snapshot updates, and verbose logging, while also renaming existing ones to prevent conflicts. A significant fix addresses the Chatbot popup routing to correctly utilize hash-based URLs, improving navigation. Additionally, the build configurations for both Vite and Webpack have been refined, and an unused dependency and TailwindCSS plugin were removed.

Highlights

- Chatbot Routing Fix: The AI Assistant popup routing has been updated to correctly use hash-based URLs (/#/chatbot), resolving previous navigation issues.
- API Endpoint Standardization: API endpoint calls within chatbot components (VoiceMessageRecorder and FileUploader) were updated to use 'fetchUtilities.getBaseApiUrl()' for consistent API versioning.
- Environment Variable Refactoring: Frontend environment variables were renamed for monorepo compatibility (e.g., GIT_SUBMODULE_LOCAL_PATH to GIT_SUBMODULE_LOCAL_PATH_FRONTEND, RUN_METHOD to RUN_BUNDLER) and now support APP_ prefixed variables as fallbacks for REACT_APP_ prefixed ones. New environment variables like API_VERSION, UPDATE_SNAPSHOTS, and VERBOSE_RUN_CONFIG were also added.
- Build Process Enhancements: Build output directories for both Vite and Webpack configurations were adjusted, and a new 'npm_publish.sh' script was introduced to standardize the publishing workflow. The 'text-encoding' dependency and '@tailwindcss/vite' were removed to streamline the build.

### CHANGELOG.md

#### [1.2.0] - 2026-02-18

##### Added
- Add API_VERSION envvar to set the API version, default to "v1" [GS-245].
- Add UPDATE_SNAPSHOTS envvar to "make publish" to run "npm test -- -u" instead of "npm run test"
- Add VERBOSE_RUN_CONFIG envvar to enable verbose logging in run_config.sh.
- Specific GS FE AI version of "run_publish.sh" command to publish the package to NPM.

##### Changed
- Rename the frontend envvars to avoid conflicts with the same envvar used in the backend and be able to merge the ".env" files in a monorepo: GIT_SUBMODULE_LOCAL_PATH to GIT_SUBMODULE_LOCAL_PATH_FRONTEND, and RUN_METHOD to RUN_BUNDLER [GS-243].
- Refactor environment variable handling for monorepo compatibility:
  - REACT_APP_APP_NAME envvar can be removed and replaced by APP_NAME in monorepos [GS-243].
  - REACT_APP_DEBUG envvar can be removed and replaced by APP_DEBUG in monorepos [GS-243].
  - If REACT_APP_API_URL is not set, APP_API_URL can be used instead [GS-243].
  - If REACT_APP_URI_PREFIX is not set, URI_PREFIX can be used instead [GS-243].
  - If REACT_APP_X_TOKEN is not set, X_TOKEN can be used instead [GS-243].
  - If REACT_APP_USE_AXIOS is not set, USE_AXIOS can be used instead [GS-243].
- The error message in the AI Assistant chat is now floating [GS-246].
- Rename "idUtilities.getUuidV4" to "uuidUtilities.getUuidV4" [GS-266].

##### Fixed
- Fix "npm warn deprecated text-encoding@0.7.0: no longer maintained" by removing "text-encoding" dependency and rollup external configuration [GS-219].
- Fix "make publish" build error by reverting all run_lib changes in package.json and "public/static" removal.
- Update chatbot popup routing to use hash-based URLs.
- Adjust build output directories [GS-262].

##### Security
- Implement URL sanitization in ConversationBlock and input sanitization in ChatBotButton to prevent XSS vulnerabilities, along with corresponding tests [GS-262].
- Upgrade jest and babel to latest versions to fix the "npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful." warning [GS-219] [GS-267].
- 37 security vulnerabilities (including high and critical ones) found in the project's dependencies were addressed, adding an "overrides" section to package.json to force secure versions of transitive dependencies (elliptic, json5, minimatch, postcss, loader-utils) without breaking your high-level setup [GS-219] [GS-267].

##### Removed
- Remove @tailwindcss/vite

## GenericSuite Backend Core

### Package, Pull Request and Tag

* Package: [https://pypi.org/project/genericsuite/0.3.0/](https://pypi.org/project/genericsuite/0.3.0/)
* Pull Request: [https://github.com/tomkat-cr/genericsuite-be/pull/14](https://github.com/tomkat-cr/genericsuite-be/pull/14)
* Tag: [https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.3.0](https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.3.0)

### Pull Request Overview

Postgres, Supabase, MySQL support, AWS generate_presigned_url, and OpenAPI schema files

This pull request significantly expands the backend's capabilities by introducing support for a wider range of databases and cloud storage providers, enhancing its flexibility and scalability. It also modernizes core components by migrating to Pydantic for data validation and refining API key authentication. The changes streamline API management through versioning and standardize endpoint structures, while also boosting security and maintainability through dependency updates and code cleanup. A new logging endpoint provides better observability for application behavior.

Highlights

- Expanded Database Support: Added comprehensive support for PostgreSQL, Supabase, and MySQL databases, alongside existing MongoDB and DynamoDB, through a refactored and extended database abstraction layer.
- Unified Cloud Storage Abstraction: Implemented a new abstraction layer for cloud storage, enabling seamless integration with AWS S3, Azure Blob Storage, and Google Cloud Storage. This includes features like AWS presigned URLs for secure, time-limited access and enhanced URL masking.
- API Versioning and Endpoint Standardization: Introduced an API_VERSION environment variable to manage API versions, and standardized endpoint URL prefixes across Chalice, FastAPI, and Flask frameworks to include the API version (e.g., /v1/users). The storage retrieval URL prefix was also standardized from /asset to /assets.
- Pydantic Migration for Schema Validation: Migrated the application's schema validation mechanism from Marshmallow to Pydantic, improving data validation and serialization.
- Enhanced API Key Authentication: Reimplemented API key authentication to use a dedicated users_api_keys table, improving security and flexibility. The get_access_token function was added to retrieve MCP access tokens from headers.
- New Logging Endpoint: A dedicated endpoint for client-side logging (/logs) was implemented across all frameworks, allowing for centralized log collection.
- Dependency Updates and Security Fixes: Updated urllib3 and werkzeug to address known security vulnerabilities. Unused dependencies like boto3, pymongo, python-dateutil, marshmallow, requests, dnspython, wheel, fastmcp, and mcp were removed from core dependencies, and requests-toolbelt was added.
- Improved Email Functionality: The send_email utility was enhanced with parameter validation, HTML stripping, type hints, and the addition of a Message-ID header to prevent emails from being rejected by providers like Google.

### CHANGELOG.md

#### [0.3.0] - 2026-02-18

##### Added
- API_VERSION envvar to set the API version, default to "v1" [GS-245].
- Postgres database support [GS-194].
- Supabase support [GS-161].
- MySQL support [GS-249].
- Implement storage abstraction layer for S3, Azure and GCP [GS-72].
- Implement AWS generate_presigned_url() to protect S3 bucket access, so they can be set to expire in a short time and configured to block all public access. Configuration available with STORAGE_PRESIGNED_EXPIRATION_SECONDS (default to 5 minutes or 300 seconds) [GS-72].
- Save OpenAPI schema files (JSON and YAML) to a directory specified by the PATH_TO_SAVE_OPENAPI envvar [GS-245].
- "requests-toolbelt" dependency because it's required by parse_multipart.py [GS-248].
- "make test" command to run tests [GS-248].
- "pymongo" and "boto3" to dev group dependencies to run tests [GS-248].
- APP_LOGGER_OPTIONS envvar to configure logging options, initially to disable the debug message at the application startup when "silent" is set [GS-245].
- MCP access token retrieval from headers (Authorization: Bearer <token>) with the get_access_token() function in mcplib utilities [GS-159].
- MCP_MANDATORY_USER_ID envvar to force MCP authentication with user_id and api_key. Default to "0" to allow api key only authentication [GS-159].
- Implement logs endpoint [GS-250].
- Add Message-ID header to outgoing emails [GS-37].
- Allow configuring email debug mode via the SEND_EMAIL_DEBUG environment variable [GS-37].
- `db_engine` configuration to SqlTable so methods like array_fields_management() and array_fields_value() can use the corresponding functions [GS-194].
- Implement $inc, $push, $addToSet and $pull operations to the SQL abstraction [GS-194].
- Add `get_table_structure()` and `quote_value()` on generic DB helpers to fix the  `super_admin_create()` ("supad-create" endpoint) execution on apps with specific user table mandatory attributes needing default values [GS-125].
- Introduce $elemMatch support in all database abstractions. Enhance query handling by extracting and filtering $elemMatch conditions, improving data retrieval accuracy [GS-161] [GS-194] [GS-249] [GS-102].

##### Changed
- Refactor: standardize storage retrieval URL prefix from `/asset` to `/assets` across all frameworks [GS-245].
- Refactor: standardize return_resultset_jsonified_or_exception() function status code parameter name from "http_error" to "status_code" in "utilities.py" and "users.py" [GS-245].
- Enhance logging in aws.py for better debugging, including an initial message in the app startup to show the logging level.
- STORAGE_URL_SEED envvar is now required only if STORAGE_URL_ENCRYPTION is enabled [GS-72].
- STORAGE_ENCRYPTION envvar renamed to STORAGE_URL_ENCRYPTION [GS-72].
- Enhance AWS S3 URL masking feature to avoid exposing the bucket name. It can be configured with envvars: STORAGE_URL_ENCRYPTION, STORAGE_URL_SEED, RUN_PROTOCOL, URL_MASK_EXTERNAL_HOSTNAME, URL_MASK_EXTERNAL_PROTOCOL. Does not work with API Gateway, only EC2 instances or VPS servers [GS-72].
- The URL_MASK_EXTERNAL_HOSTNAME envvar replaced DEV_MASK_EXT_HOSTNAME, and DEV_MASK_EXT_HOSTNAME is still being used, but has precedence assigning URL_MASK_EXTERNAL_HOSTNAME [GS-72].
- Migrate Marshmallow to Pydantic: update schema_verification() function to use Pydantic instead of Marshmallow [GS-248].
- Rename "parentKeyNames" to "endpointKeyNames" in JSON config files [GS-159].
- Reimplement API key authentication using a dedicated table "users_api_keys" [GS-159].
- Remove example users_api_keys from app context.
- Enhance `send_email.py` to return a resultset with error information when an error occurs, parameters validation, HTML stripping, and type hints [GS-37].

##### Fixed
- Remove "/" prefix in the key to avoid double "/" in get_bucket_key_from_url() and fix encoded chars in get_s3_presigned_url() [GS-245].
- Clean up unused imports and comments in create_app.py.
- Update delete_params_file return type in app_context.py.
- DynamoDB abstractor table object scan error "AttributeError: 'tuple' object has no attribute 'update'" [GS-102].
- Robustify ObjectId conversion by casting to string in fetch_list() when "_id_ is in like_query_params.
- Allow `Request` objects as input for current user data functions to make the users onboarding workflow work [GS-37].
- Prevent "AssertionError: AuthenticationMiddleware must be installed to access request.user" in `get_curr_user_id` when it's a normal Request with no JWT authentication [GS-37].
- `send_email` includes "Message-ID" header to prevent google (and others) from rejecting emails [GS-37].
- Update SQL abstraction to handle NULL comparisons dynamically [GS-262]. 
- "bson.errors.InvalidId" error when creating a new user with Supabase, assigning `parent_keys["_id"] = ObjectId(parent_keys["id"])` [GS-251].

##### Security
- Update "urllib3" to "^2.6.3" to fix security vulnerabilities [GS-219]:
    * "Allocation of Resources Without Limits or Throttling": "CWE-770", "CVE-2025-66418", "CVSS 8.9", "SNYK-PYTHON-URLLIB3-14192443"
    * "Improper Handling of Highly Compressed Data (Data Amplification)": "CWE-409", "CVSS 8.9", "CVE-2025-66471", "CVE-2026-21441", "CWE-409".
- Update "werkzeug" to "^3.1.6" to fix security vulnerabilities [GS-219]:
    * "Improper Handling of Windows Device Names": "CWE-67", "CVSS 6.3", "CVE-2025-66221", "CVE-2026-27199", "CWE-67".
- Upgrade "cryptography" to "^46.0.5" to fix security vulnerabilities [GS-219]:
    * "Insufficient Verification of Data Authenticity": "CVE-2026-26007", "CWE-345".
- Add mandatory filters to get_item_from_db() and GenericEndpointHelper.generic_crud_main() [GS-262].
- Add sanitization to "message" parameter in POST /log endpoint [GS-262].

##### Removed
- "boto3" and "pymongo" dependencies, so each project can have its own dependencies depending on the selected database and cloud storage provider [GS-245].
- save_all_users_params_files() function and /users/caujf endpoint [GS-240] [GS-245].
- "python-dateutil", "marshmallow", "requests", "dnspython", "wheel" dependencies, because they are not used [GS-248].
- "fastmcp" and "mcp" dependencies, so each project can install them if needed [GS-248].

## GenericSuite Backend AI

### Package, Pull Request and Tag

* Package: [https://pypi.org/project/genericsuite-ai/0.3.0/](https://pypi.org/project/genericsuite-ai/0.3.0/)
* Pull Request: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/12](https://github.com/tomkat-cr/genericsuite-be-ai/pull/12)
* Tag: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.3.0](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.3.0)

### Pull Request Overview

Add create_app() for Flask, try-except to all optional imports to report what dependency is missing, and security fixes

This pull request significantly enhances the project's flexibility, security, and maintainability. It introduces a standardized application creation pattern for Flask, expands database and cloud storage capabilities, and integrates advanced AI conversation masking features. A major focus has been placed on improving dependency management by making many packages optional and providing clearer installation instructions, alongside critical security updates to core libraries. These changes collectively streamline development, reduce operational overhead, and bolster the application's resilience.

Highlights

- Enhanced Modularity and Framework Support: Introduced a standardized create_app() function for Flask applications and integrated AI Conversation Masking across FastAPI, Flask, and Chalice frameworks, improving application setup and consistency.
- Improved Dependency Management and Error Reporting: Implemented try-except blocks for all optional imports, providing clearer error messages to developers about missing dependencies and streamlining the installation process. Many dependencies were also removed or made optional to reduce project size.
- Expanded Database and Cloud Storage Capabilities: Added support for PostgreSQL and MySQL databases and developed a robust storage abstraction layer for AWS S3, Azure, and Google Cloud Platform, including the use of AWS presigned URLs for secure, time-limited access to S3 buckets.
- Critical Security Updates: Addressed multiple security vulnerabilities by updating key dependencies such as urllib3, langchain-core, and langchain to their latest secure versions.
- Configuration and Model Updates: Updated the default HuggingFace model, adjusted API base URLs for AIMLAPI and Groq, and fixed faiss-cpu version compatibility for AWS Lambda deployments.

### CHANGELOG.md

#### [0.3.0] - 2026-02-18

##### Added
- API_VERSION envvar to set the API version, default to "v1" [GS-245].
- Postgres database support [GS-194].
- MySQL support [GS-249].
- Implement storage abstraction layer for AWS S3, Azure and GCP [GS-72].
- Implement AWS generate_presigned_url() to protect S3 bucket access, so they can be set to expire in a short time and configured to block all public access. Configuration available with STORAGE_PRESIGNED_EXPIRATION_SECONDS (default to 5 minutes or 300 seconds) [GS-72].
- FastAPI, Flask, and Chalice support to AI Conversation Masking using AWS presigned URLs [GS-72].
- create_app() for Flask [GS-15].
- try-except to all optional imports to report what dependency is missing, so the developer can "pip install" it [GS-248].
- Model documentation links in `.env.example` [GS-172].
- Note about the old google translator module replacement in `translator.py` [GS-252].

##### Changed
- Update HuggingFace default model to "moonshotai/Kimi-K2-Instruct-0905" because "mistralai/Mixtral-8x7B-Instruct-v0.1" is not longer available [FA-233].
- Update AIMLAPI_BASE_URL to include "/v1" at the end [GS-172].

##### Fixed
- Update faiss-cpu to version 1.12.0 and adjust the project Python version compatibility to >=3.10,<3.15 to fix "Could not find a version that satisfies the requirement faiss-cpu==1.13.1 (from versions: 1.7.3, 1.7.4, 1.8.0, 1.8.0.post1, 1.9.0, 1.9.0.post1, 1.12.0)" running the AWS lambda deployment [GS-251].

##### Security
- Update "urllib3" to "^2.6.3" to fix security vulnerabilities [GS-219]:
    * "Allocation of Resources Without Limits or Throttling": "CWE-770", "CVE-2025-66418", "CVSS 8.9", "SNYK-PYTHON-URLLIB3-14192443"
    * "Improper Handling of Highly Compressed Data (Data Amplification)": "CWE-409", "CVSS 8.9", "CVE-2025-66471", "CVE-2026-21441", "CWE-409".
- Update "langchain-core" to "^1.2.5" to fix security vulnerabilities [GS-219]:
    * "Template Injection": "CWE-1336", "CVSS 8.3"
    * "Deserialization of Untrusted Data": "CVE-2025-68664", "CWE-502"
- Update "langchain" to "^1.2.0" to fix security vulnerabilities [GS-219]:
    * "Template Injection": "CWE-1336", "CVSS 8.3"
- Update "langchain-openai" to "^1.1.9" to fix vulnerabilities [GS-219].
    * "Server-side Request Forgery (SSRF)": "CVE-2026-26013", "CWE-918"

##### Removed
- "langchain-groq" dependency because its API is now called with the OpenAI API [GS-248].
- "clarifai", "google-api-python-client", "transformers", "pypdf", "langchain-google-genai", "langchain-anthropic", "langchain-ollama", "langchain-google-vertexai", "langchain-text-splitters", "langchain-aws", dependencies to make it optional by default [GS-248].
- "tiktoken", "openai", "click", "jmespath", "pyyaml", "six", "typing-extensions", "pillow", and "jq" dependencies to reduce the dependencies size and most of them are not used in this project and/or are dependencies of other dependencies [GS-248].

## GenericSuite Backend Scripts

### Package, Pull Request and Tag

* Package: [https://www.npmjs.com/package/genericsuite-be-scripts/v/1.3.0](https://www.npmjs.com/package/genericsuite-be-scripts/v/1.3.0)
* Pull Request:
    - [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/13](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/13)
    - [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/14](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/14)
* Tag: [https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.3.0](https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.3.0)

### Pull Request Overview

Sync Dependencies module, super admin user creation, Postgres, Supabase, MySQL support, and Cloudflare Tunnel

This pull request significantly enhances the development and deployment workflow by introducing automated dependency synchronization, expanding database support to include Postgres and MySQL, and integrating Cloudflare Tunnel for secure local development access. It also brings substantial improvements to AWS Lambda deployments, including Python 3.12 runtime and OpenAPI 3.0.1, alongside various fixes and optimizations for local environment setup and security practices.

Highlights

- Dependency Synchronization Module: Introduced a new scripts/dependency-sync module to automatically synchronize Python dependencies from pyproject.toml files in backend directories (./server and ./mcp-server) to Dockerfiles, ensuring up-to-date and consistent dependencies.
- Enhanced Database Support: Added comprehensive support for Postgres and MySQL databases, including new make targets for generating SQL, creating development tables, and deploying CloudFormation resources. Local database management now uses a unified local_db directory, replacing previous mongo and postgres specific folders.
- Cloudflare Tunnel Integration: Implemented Cloudflare Tunnel support to enable secure HTTPS access to local development environments without requiring Docker or local DNS, making localhost publicly accessible for testing purposes.
- AWS Lambda Deployment Improvements: Upgraded AWS Lambda runtime to Python 3.12, updated API Gateway to OpenAPI 3.0.1 with CORS, and refactored endpoint definitions. Added a 'zip' deployment option for Lambda functions and new environment variables (CICD, USE_EXISTING_ZIP, PATH_TO_SAVE_OPENAPI) for more flexible and automated deployments.
- Local Development Environment Enhancements: Standardized the MCP server bash script, added a make create-supad target for initial super admin user creation, and introduced validation for local backend ports. Compatibility with Podman was improved by refactoring Docker Compose configurations and local DNS setup.
- Security and Maintenance: All requirements.txt files are now ignored and recreated on demand to ensure the latest dependencies and mitigate vulnerabilities. Cleanup commands in run_aws.sh were commented out to prevent accidental file deletion.

### CHANGELOG.md

#### [1.3.0] - 2026-02-18

##### Added
- Sync Dependencies module ("scripts/dependency-sync") to sync python dependencies in a Dockerfile from GenericSuite monorepo backend directories ("./server" and "./mcp-server" with a "pyproject.toml" file) [GS-243].
- "scripts/run_mcp_server.sh" to standardize the MCP server bash script [GS-243].
- Postgres database support [GS-194].
- Makes for Postgres:
```
make generate_postgres_dev_sql
make create_postgres_dev_tables
make generate_cf_postgres
make deploy_postgres
```
- MySQL database support [GS-249].
- Makes for MySQL:
```
make generate_mysql_dev_sql
make create_mysql_dev_tables
make generate_cf_mysql
make deploy_mysql
```
- "make create-supad" to create the initial super admin user (supad) for local development environment [GS-125].
- Field types h1 to h6 to JSON files [GS-250].
- Validation for BACKEND_LOCAL_PORT and BACKEND_DEBUG_LOCAL_PORT to be different on the "secure_local_server/run.sh" script.
- Ports and local database UI managers documentation in "scripts/local_db/local_db_stack.yml" [GS-249] [GS-194].
- Zip option to AWS lambda deployment [GS-248].
- AWS_LAMBDA_DEPLOYMENT_TYPE envvar to select the deployment type for AWS Lambda functions ("zip" or "container", default "container"). If the project includes GS BE AI, it cannot be "zip" due to AWS Lambda zip file size limit of 250 MB max [GS-248].
- CICD envvar to "big_lambdas_manager.sh" to avoid asking for confirmation on several steps and run it non-interactively [GS-248].
- USE_EXISTING_ZIP envvar to "big_lambdas_manager.sh" to use an existing zip file instead of building a new one [GS-248].
- PATH_TO_SAVE_OPENAPI envvar to "run_aws.sh" to save the OpenAPI schema files [GS-245].
- Implement Cloudflare Tunnel to allow https access to local development environment without Docker/local DNS and make localhost public for testing purposes, e.g. to access the PC camera (no port forwarding needed) [GS-257].
- Add USE_CONTAINERS_ENGINE_APP envvar to turn on/off use containers engine app for local development environment when RUN_PROTOCOL="https" [GS-257].
- Add RUN_PROTOCOL_AND_PORT_REPLACEMENT envvar to turn on/off automatic protocol and port replacement for local development environment variables APP_CORS_ORIGIN (assigned from APP_CORS_ORIGIN_{STAGE}), APP_FE_URL (assigned from APP_FE_URL_{STAGE}), and REACT_APP_API_URL (assigned from APP_API_URL_{STAGE}), depending on RUN_PROTOCOL value [GS-257].
- Configure uvicorn to process proxy headers and forwarded IPs in the `run_aws.sh` script [GS-37].

##### Changed
- Allow merge ".env" files between GenericSuite monorepo backends ("./server" and "./mcp-server"), rename APP_MAIN_FILE and APP_DIR envvars to MCP_APP_MAIN_FILE_DEV and MCP_APP_DIR_DEV in run_mcp_server.sh [GS-243].
- Rename APP_DB_ENGINE values "MONGO_DB" and "DYNAMO_DB" to "MONGODB" and "DYNAMODB" [GS-194].
- Profiles added to "local_db_stack.yml" so only the selected APP_DB_ENGINE is enabled [GS-194].
- Remove all "link", "depends_on" and "healthcheck" sections in "local_db_stack.yml" to make it compatible with Podman [GS-215] [GS-194].
- STORAGE_URL_SEED envvar is only required when STORAGE_URL_ENCRYPTION is set to 1 in "run_aws.sh" and "set_chalice_cnf.sh" [GS-72].
- Rename "mongo" and "postgres" folders to more appropriate names, as they are now used for several databases: "mongo" is now "local_db", including local Docker containers for MongoDB, DynamoDB, Postgres, and MySQL. "postgres" is now "sql_db" because it works for Postgres and MySQL. [GS-249]:
```
/postgres -> /sql_db
/postgres/generate_postgres_cf -> /sql_db/generate_sql_db_cf
/postgres/generate_postgres_cf/run-postgres-deploy.sh -> /sql_db/generate_sql_db_cf/run_sql_db_deploy.sh

/mongo/run_mongo_docker.sh -> /local_db/run_local_db_docker.sh
/mongo/mongodb_stack_for_test.yml -> /local_db/local_db_stack.yml

make mongo_docker -> make local-db-up
make mongo_docker_down -> make local-db-down
make mongo_logs -> make local-db-logs
set_chalice_cnf.sh mongo_docker -> set_chalice_cnf.sh local_db_docker
```
- Rename HUGGINGFACE_TEXT_TO_IMAGE_ENDPOINT to HUGGINGFACE_DEFAULT_CHAT_MODEL [GS-59].
- Pump up Python version to 3.12 on Big Lambdas Amazon Linux deployment, EC2 ELB deployment and local server Dockerfiles [GS-248].
- Big Lambda python version 3.11 Dockerfile is on the "Dockerfile-big-lambda-AL2-python3.11" file [GS-248].
- Add "v1" to endpoints defined in "aws_big_lambda/template-sam-endpoint-entry.yml" [GS-245].
- Add additional debug to "run-cf-deployment.sh" and "aws_secrets_manager.sh" [GS-248].
- Rename "dns/docker-compose.yml" to "dns/docker-compose-template.yml" [GS-215].
- Due to the "fastmcp" and "mcp" dependencies removal, run_mcp_server.sh now verifies if both are installed [GS-248].
- Upgrade Lambda runtime to Python 3.12, update API Gateway to OpenAPI 3.0.1 with CORS, and refactor endpoint definitions in "aws_big_lambda/template-sam.yml" [GS-245].

##### Fixed
- Comment out cleanup commands in "run_aws.sh" to prevent accidental deletion of important files during the clean operation.
- Rename CONTAINER_ENGINE with CONTAINERS_ENGINE [GS-215].
- Fix "secure_local_server/run.sh" to run secure local server with Podman by creating a named volume to mount configuration files in the nginx container "/etc/nginx/conf.d" directory which is read-only and Podman does not allow to mount read-only directories the same way Docker does. Now GS is compatible with Podman [GS-215].
- Local_dns works with Podman [GS-215].
- APP_VERSION removed from CORE_ENVS in "aws_secrets/aws_secrets_manager.sh" separated from the rest of the environment variables that are pushed to AWS Secrets Manager and included in the AWS Lambda Function CloudFormation template "aws_big_lambda/template-sam.yml".

##### Security
- All "requirements.txt" files are now ignored and recreated on demand to avoid vulnerability reposts and have the latest dependencies [GS-219].

## GenericSuite BaseCamp

### Pull Request and Tag

* Pull Request:
    - [https://github.com/tomkat-cr/genericsuite-basecamp/pull/15](https://github.com/tomkat-cr/genericsuite-basecamp/pull/15)
    - [https://github.com/tomkat-cr/genericsuite-basecamp/pull/17](https://github.com/tomkat-cr/genericsuite-basecamp/pull/17)
* Tag: [https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.5.0](https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.5.0)

### Pull Request Overview

FastAPI Template app, multi-language support, enhanced App creation, JSON configuration files, CRUD editor, and file environment variable documentation

This pull request introduces the FastAPI Template app, enhancing the development experience for template applications, and, significantly enhances the project's documentation infrastructure by introducing multi-language support, restructuring content for better organization, and updating external links for improved reliability. It also streamlines the development workflow by adding new tools for Cloudflare Tunnel management and refining environment variable configurations, ultimately making the project more accessible and easier to develop against. Changes focus on improving documentation accuracy, standardizing environment variable naming conventions to avoid conflicts, and strengthening various build and cleanup scripts. These updates collectively contribute to a more consistent, reliable, and well-documented foundation for integrating and managing different application templates within the project.

Highlights

- FastAPI Template app.
- Multi-language Documentation: Implemented multi-language support for documentation, starting with Spanish and English, and added environment variables for future automatic translation using OpenAI.
- Documentation Structure Refactoring: Restructured the documentation by renaming numerous files and directories, consolidating sample code under a new 'docs/code' path, and removing old index files.
- Support for Postgres, MySQL, and Supabase databases.
- Extensive documentation for CRUD Editor configurations, AI Preamble Models, and new field types.
- API_VERSION environment variable
- Documentation Refinements: Various documentation sections have been updated and corrected, including configuration guides, Python package manager instructions, and example app READMEs, to ensure accuracy and clarity for developers working with template applications like FastAPI.
- Environment Variable Standardization: Key frontend environment variables, such as 'RUN_METHOD' (now 'RUN_BUNDLER') and 'GIT_SUBMODULE_LOCAL_PATH' (now 'GIT_SUBMODULE_LOCAL_PATH_FRONTEND'), have been renamed to prevent conflicts and improve consistency across monorepo setups, benefiting all integrated applications.
- Environment Variable Enhancements: Introduced new environment variables for saving OpenAPI schema files, controlling container engine usage for local development, and managing automatic protocol/port replacement for frontend URLs.
- Changelog and Release Updates: Detailed entries for recent releases (versions 1.3.1 and 1.3.2) have been incorporated into the main changelog and release notes, documenting new features, enhancements, and bug fixes that apply to the overall project, including template applications.
- Script Enhancements and Cleanup: Backend application 'clean' scripts for Chalice, FastAPI, Flask, and MCP Server have been improved, and the 'run_mcp_server.sh' script has been refactored for better directory handling, contributing to a more robust development environment for template apps.
- Updating documentation links to be relative instead of absolute URLs.
- Fixing installation instructions for uv and poetry.
- Build processes have been enhanced with new "prepare_docs" and "generate_openapi" targets
- "make serve" now binds to localhost:8015
- Documentation images have been converted from SVG to PNG
- Various installation instructions and environment variable descriptions have been clarified or expanded, including a new 'Preamble models' section for AI.
- Several fixes address issues with Podman, npm clean, broken documentation links, and FileNotFoundError for static UI assets.
- Link Updates: Replaced relative links to .pdf files and example app source code with direct GitHub GS Basecamp raw content URLs.
- The common Chatbot and other common logic were moved from api-chalice to api-fastapi in ExampleApp.
- Cloudflare Tunnel Integration: Added Makefile targets for managing Cloudflare tunnels in both the exampleapp and fastapitemplate projects, along with related documentation.
- A security update for urllib3 is also included.

### CHANGELOG.md

#### [1.5.0] - 2026-02-18

##### Added
- Multi-language documentation, starting with spanish and english (thanks to @otobonh for the idea) [GS-252].
- Spanish docs, using Google Translate and OpenAI gpt-5-nano [GS-252].
- Cloudflare tunnel Makefile targets to exampleapp and fastapitemplate [GS-257].
- PATH_TO_SAVE_OPENAPI envvar to main Makefile to save the OpenAPI schema files [GS-245].
- USE_CONTAINERS_ENGINE_APP envvar to turn on/off use containers engine app for local development environment when RUN_PROTOCOL="https" [GS-257].
- Documentation for RUN_PROTOCOL_AND_PORT_REPLACEMENT envvar to turn on/off automatic protocol and port replacement for local development environment variables APP_CORS_ORIGIN (assigned from APP_CORS_ORIGIN_{STAGE}), APP_FE_URL (assigned from APP_FE_URL_{STAGE}), and REACT_APP_API_URL (assigned from APP_API_URL_{STAGE}), depending on RUN_PROTOCOL value [GS-257].
- OPENAI_API_KEY, OPENAI_MODEL, OPENAI_TEMPERATURE envvars to prepare future automatic documentation translation [GS-252].
- Add 2nd anniversary release changelog [GS-262].

##### Changed
- Replace `.pdf` files relative links with Github GS Basecamp raw content links [GS-252].
- Replace exampleapp and fastapitemplate source code relative links with Github GS Basecamp URLs [GS-252].
- "docs_prepare.py" filter certain unneeded filenames [GS-252].
- Implement Cloudflare Tunnel documentation [GS-257].
- Refactor `.env.example` files for common variables and enhance documentation on fastapitemplate and exampleapp [GS-252].
- Update environment setup documentation [GS-252].
- Rename "docs/Sample-Code" to "docs/code" [GS-252].

##### Fixed
- Add PyGithub to `mkdocs_install.sh` script because `mkdocs-git-committers-plugin` requires it [GS-262].
- Fix users_api_keys primary key (_id) definition.


#### [1.4.0] - 2026-01-21

##### Added
- FastAPI Template app [GS-243].
- Postgres database support [GS-194].
- MySQL database support [GS-249].
- Supabase support [GS-161].
- API_VERSION envvar to set the API version, default to "v1" [GS-245].
- Sample-Code main documentation page.
- GenericSuite Release 20251117 changelog file: "docs/Releases/GS_Release_2025-11-17_Changelog.md".
- "specific_function": "ai_conversation_masking" to "frontend/ai_chatbot_conversations.json" on genericsuite_configs, ExampleApp and FastAPI Template.
- Documentation for field type "array" and "specific_function" examples in Generic CRUD Editor Configuration Documentation.
- Documentation and examples for Preamble Models (usually needed to configure AI thinking LLMs) in GenericSuite AI documentation.
- Field types h1 to h6 to JSON files [GS-250].
- AWS_LAMBDA_DEPLOYMENT_TYPE envvar to select the deployment type for AWS Lambda functions (zip or container, default zip) [GS-248].
- "make generate_openapi" command to save OpenAPI schema files (JSON and YAML) and included in the transfer and build process (make build, make serve, make transfer_debug, make transfer_cicd) [GS-245].
- Documentation for the new databases supported.
- Optional dependencies to example projects (boto3, pymongo).
- Create Super Admin user documentation.
- Local database stack and operations documentation.
- Python classes and TypeScript interfaces for CRUD editor JSON config files validation and update the corresponding guide [GS-172].
- How to create tables and forms documentation [GS-172].
- How to stablish 1-to-many relationships between tables documentation [GS-172].
- Api Keys to User Profile on exampleapp and fastapitemplate [GS-251].
- Privacy policy [GS-252].
- Introduce documentation preparation scripts, to reduce the FTP transfer time [GS-252].
- "make translate_uncommitted" command to translate uncommitted changes in the "docs" directory before publishing [GS-252].
- "make sample_code_prepare" to prepare sample code (exampleapp and fastapitemplate) to use the latest packages before publishing [GS-262].

##### Changed
- Enhance "exampleapp/apps/mcp-server/run_mcp_server.sh" separating the SCRIPT_DIR and BASE_DIR envvars.
- Rename the frontend envvars to avoid conflicts with the same envvar used in the backend and be able to merge the ".env" files in a monorepo: GIT_SUBMODULE_LOCAL_PATH to GIT_SUBMODULE_LOCAL_PATH_FRONTEND, and RUN_METHOD to RUN_BUNDLER [GS-243].
- Clean documentation and exampleapp code related with old "authenticationService".
- Add "-PRESENT" to all LICENSE files.
- Change documentation top bar options order.
- Enhance documentation for STORAGE_URL_ENCRYPTION and STORAGE_URL_SEED.
- STORAGE_URL_SEED envvar is only required when STORAGE_URL_ENCRYPTION is set to 1 [GS-72].
- 'Special Installation' and './Other/special-installs.md' renamed to 'Installation' and './Other/installation.md' respectively.
- docs: Enhance backend project setup guide with monorepo structures, detailed dependency management, and new database/cloud service installation sections, adding `psycopg2-binary`.
- Update all .env.example with new supported databases.
- Replace "/mongo" with "/local_db" and "mongo_docker" with "local_db_docker" in Makefile files. 
- Due to the "fastmcp" and "mcp" dependencies removal, run_mcp_server.sh now verifies both are installed [GS-248].
- Avoid asking confirmations when cleaning directories during the build process of "make publish".
- Update "mkdocs_transfer_site.sh" to turn debug mode off unless specified.
- Remove Podman warning in Backend Development documentation.
- MkDocs install scripts removes the .venv to include latest dependencies version.
- Serve and run in main Makefile changed so "make run" makes a complete clean, regeneration and "make serve", and "make serve" only runs "mkdocs serve".
- Upgrade Lambda runtime to Python 3.12, update API Gateway to OpenAPI 3.0.1 with CORS, and refactor endpoint definitions in "aws_big_lambda/template-sam.yml" [GS-245].
- Rename "parentKeyNames" to "endpointKeyNames" in JSON config files [GS-159].
- Move "parentUrl" attribute from "endpointKeyNames" to the root of the JSON config files [GS-159].
- Rename AI chatbot "GPT functions" to "AI Tools" in exampleapp comments.
- Bind mkdocs serve to localhost:8015 to avoid conflicts with other GS APIs [GS-172].
- All .svg logos are now embedded as .png in all .md files, so it can be displayed in GitHub and the documentation mobile app [GS-252].
- ExampleApp: common "lib" files moved from "exampleapp/apps/api-chalice" to "exampleapp/apps/api-fastapi".

##### Fixed
- Fix "podman" engine issues with the `podman composer` command.
- Fix uv and poetry installation instructions on Python Package Managers documentation.
- Fix "npm clean" for main and all workspaces.
- Fix the configuration guide links on the documentation, because it was pointing to "https://github.com/tomkat-cr/genericsuite-fe/tree/main/src/configs".
- Fix "FileNotFoundError: [Errno 2] No such file or directory: 'docs/Sample-Code/exampleapp/ui/public/static'" by adding "remove_ui_public_static" to clean_directory.sh.
- "create-ssl-certs" label in exampleapp Makefile was defined in a wrong way.
- Refine documentation broken links.
- APP_VERSION removed from CORE_ENVS in "aws_secrets/aws_secrets_manager.sh" separated from the rest of the environment variables that are pushed to AWS Secrets Manager and included in the AWS Lambda Function CloudFormation template "aws_big_lambda/template-sam.yml".
- Rename "CONTAINER_ENGINE" to "CONTAINERS_ENGINE" in .env.example files [GS-252].
- Fix: add ".venv" to the clean bash scripts.
- Reduce the FTP transfer time by build a temporary directory "docs_for_ftp", copying there only the necessary files and use it as a source for MkDocs. 

##### Security
- Update "urllib3" to "^2.6.2" in main requirements.txt to fix security vulnerabilities [GS-219]:
    * "Allocation of Resources Without Limits or Throttling": "CWE-770", "CVE-2025-66418", "CVSS 8.9", "SNYK-PYTHON-URLLIB3-14192443"
    * "Improper Handling of Highly Compressed Data (Data Amplification)": "CWE-409", "CVSS 8.9", "CVE-2025-66471", "SNYK-PYTHON-URLLIB3-14192442".

##### Removed
- AWS_API_GATEWAY_STAGE envvar removed from all .env.example files.
- boto3 and pymongo dependencies, so each project can have its own dependencies depending on the selected database and cloud storage provider [GS-245].
- Unused generic API endpoints from OpenAPI specification.
