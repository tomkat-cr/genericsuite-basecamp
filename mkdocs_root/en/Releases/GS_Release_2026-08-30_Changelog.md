# 20260830 - v1.0.0

![GS_Release_2026-08-30_Image_1A.png](./images/GS_Release_2026-08-30_Image_1A.jpeg)

Date: 2026-08-30

## Summary

Introducing v1.0.0: The GenericSuite Superproject is Live! 🚀

This release marks a foundational milestone for the ecosystem: a **Flutter mobile app development package**, **code generation skills**, **security tools and policies skills**, and a **documentation mobile app** are introduced. Also GenericSuite now ships as a unified **Superproject**, bringing all 16 packages together as git submodules under one monorepo, with shared automation and AI-agent context guiding every package alike. It's the biggest structural release in GenericSuite's history, and it's paired with a sweeping hardening and expansion pass across the board.

Key Professional Benefits:

* **New Packages**: `genericsuite-mobile`, `genericsuite-mobile-exampleapp` (for mobile app development with Flutter), `genericsuite-basecamp-app` (documentation mobile app), `genericsuite-skills` (application generation skills), `genericsuite-security` (security tools and policies), and `genericsuite-fe-scripts` (frontend common scripts), all debut this cycle, plus a new OpenTofu (Terraform) deployment path.

* **One Ecosystem, One Home**: The new Superproject orchestrates all GenericSuite packages — frontend, backend, mobile, scripts, docs, and now security — from a single root, with `AGENTS.md`/`GEMINI.md`/`CLAUDE.md` context files threaded through every package for AI coding assistants.

* **Security, Everywhere**: Python 3.14 and Node.js 26 across the board, MIT licensing ecosystem-wide, dozens of CVE fixes (axios, LangChain/aiohttp, Vite, Forge), FastAPI/Flask rate limiting, and a brand-new **GenericSuite Security Suite** — five Claude Skills born directly from responding to the Shai-Hulud npm supply-chain worm.

* **1-1 and 1-N Relationships, Everywhere**: The new `select_table` field type lands in both the React and Flutter CRUD editors, joining the Flutter `childComponents` support for 1-N relationships.

* **Cloud-Agnostic Storage and Secrets**: GCP Cloud Storage and Azure Blob Storage join AWS S3, plus GCP Secret Manager and Azure Key Vault as secret backends — genericsuite-be starts speaking to all three major clouds.

* **AWS deployments with OpenTofu**: The new OpenTofu (Terraform) deployment path alongside CloudFormation for AWS deployments.

Check out the full changelog for every detail across all 16 packages!

*IMPORTANT*: check the [20260830 - v1.0.0 - Migration Guide](./GS_Release_2026-08-30_Migration_Guide.md) to migrate from the previous version to the new one.

## GenericSuite Superproject

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite/pull/2](https://github.com/tomkat-cr/genericsuite/pull/2)
* Tag: [https://github.com/tomkat-cr/genericsuite/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite/releases/tag/1.0.0)

### Pull Request Overview

Introducing the GenericSuite superproject structure

This pull request establishes the GenericSuite Superproject as a monorepo orchestration layer, bringing all 16 GenericSuite packages together as git submodules under a single repository. It adds automation scripts to sync and manage packages, project-wide documentation, and AI Coding Assistant context files, laying the foundation for coordinated, whole-ecosystem releases like this one.

Highlights

- Monorepo orchestration layer: all GenericSuite packages (`genericsuite-fe`, `genericsuite-be`, `genericsuite-be-ai`, `genericsuite-fe-ai`, `genericsuite-basecamp`, and more) are now managed as git submodules under `packages/`, with `make update-packages` to sync them.
- AI Coding Assistant context: `AGENTS.md`, `GEMINI.md`, and `CLAUDE.md` give Claude Code, Gemini CLI, Cursor, Antigravity, and other assistants consistent guidance across the whole ecosystem.
- New `release-notes` AI skill: automates gathering changelogs, PRs, and tags across every package to produce this very release changelog and its social media summaries.

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Added
- Add: Introducing the GenericSuite superproject structure with git submodules, automation scripts, and project documentation, to make it easier to manage, change, and deploy the project as a whole [GS-319].
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- Add the `release-notes` skill to the `.ai./skills` directory, to generate release notes and social media summaries for the project [GS-191].

## GenericSuite Frontend Core

### Package, Pull Request and Tag

* Package: [https://www.npmjs.com/package/genericsuite/v/1.3.0](https://www.npmjs.com/package/genericsuite/v/1.3.0)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-fe/pull/11](https://github.com/tomkat-cr/genericsuite-fe/pull/11)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-fe/pull/12](https://github.com/tomkat-cr/genericsuite-fe/pull/12)
* Tag: [https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.3.0](https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.3.0)

### Pull Request Overview

AI agent docs, SAST testing, update dependencies, scripts directory moved to GS FE Scripts, MIT license, security fixes

This release adds AI-agent onboarding docs (AGENTS.md/GEMINI.md/CLAUDE.md), introduces SAST testing, and relocates the `scripts/` directory into the new standalone frontend scripts library. It adds a `select_table` field type for 1-1 relationship rendering in the Generic CRUD Editor, switches the license to MIT, and ships a broad security-dependency upgrade pass (axios, yup, react-router-dom, @babel/core) plus Rollup/webpack build fixes that were shipping stray test-declaration files and missing peer-dependency externals.

Highlights

- New `select_table` field type: listing/read-only views show related-record descriptions with client-side caching; create/edit renders a populated dropdown [GS-259].
- `scripts/` directory moved out to the new `genericsuite-fe-scripts` library [GS-107].
- License changed to MIT [FA-244]; SAST testing added [GS-315].
- Security: axios, yup, react-router-dom, @babel/core upgraded to fix multiple High/Critical Snyk/CVE vulnerabilities [GS-219].
- Build fixes: Rollup externals for `bson`/`js-md5`, excluded test files from `.d.ts` emission (~24 stray files removed from `dist`), cleaned up dead webpack polyfills and unused dependencies [GS-338].

### CHANGELOG.md

#### [1.3.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- Add SAST testing [GS-315].
- Add frontend scripts library [GS-107].
- `select_table` field type in the Generic CRUD Editor: listing and read-only form show the related record description (`{field}_description` from the backend, with client-side cached fallback); create/edit renders a dropdown populated from the related table. New JSON attributes: `related_table`, `related_key`, `description_fields`, `description_separator`, `related_filter` [GS-259].

##### Changed
- License changed to MIT [FA-244].
- Rename AWS_S3_BUCKET_NAME to AWS_S3_BUCKET_NAME_FE in the .env and .env.example files [GS-328].
- `webpack.config.js` and `config-overrides.js`: commented out the Node.js core module `resolve.fallback` polyfills (`os`, `url`, `crypto`, `stream`, `vm`, `tty`, `constants`) since nothing in the codebase needs them and Vite already runs fine without them; added `npm install --save-dev ...` notes above each so they can be re-enabled if a consumer's own dependency graph needs them [GS-338].
- Update .npmignore to include additional files and directories for Claude Code, AI Agents, and OpenTofu [GS-327].
- Update version to 1.3.0 in package.json, package-lock.json, and version.txt to reflect the latest release [GS-327].

##### Fixed
- getFieldElementsYupValidations() didn't work with action=CREATION, e.g. it has issues on the user creation (OpenAI API key and model are requested as mandatory when they have null values). Therefore, the Yup validations are disabled for now [GS-251].
- `bson` package version fixed to 7.2.0 to fix the "Uncaught TypeError: globalThis?.process?.getBuiltinModule is not a function" error after upgrading vite to version 8 [GS-268].
- `tsconfig.json` was missing an `exclude` for `*.test.tsx`, so every test file got its own `.d.ts` stub emitted into `dist/esm` and `dist/cjs` during the Rollup build. Since `dist` is fully included in the published npm package, this shipped ~24 useless declaration files with every release [GS-338].
- `rollup.config.mjs`: added `bson` and `js-md5` to the `external` array. Both are real peer dependencies used in `src/lib/services/id.utilities.jsx` and `md5.utilities.jsx`, but were missing from `external`, so Rollup was bundling them directly into `dist` instead of treating them as consumer-supplied peer dependencies like every other one [GS-338].
- Removed a bogus `"with"` entry from the webpack `resolve.fallback` config — `with` is not a Node.js core module, so the fallback never did anything [GS-338].
- "config-overrides.js" updated to fix errors running the app with RUN_BUNDLER="react-scripts" [GS-338] and refactored to use fileURLToPath for path resolution and clean up unused debug logs [GS-327].
- "process" dependency installation on "webpack.config.js" file documentation to to fix errors running the app [GS-338].
- "generic.editor.rfc.common.jsx" and "generic.editor.rfc.service.jsx" fixed to show eventual configuration errors on child listings, and updated to show the editor name in the error messages [GS-327].
- "vite.config.mjs" updated to fix the "(!) Your Vite config uses features that are unsupported by `configLoader: 'native'`, which is planned to become the default in a future major version of Vite: `__dirname` (vite.config.mjs:54:42). Use `import.meta.dirname` instead" after upgrading vite to version 8 [GS-268].

##### Security
- Upgrade dependencies to latest version: crypto-browserify@^3.12.1, downshift@^9.4.0, react-icons@^5.7.0, react-markdown@^10.1.0, react-syntax-highlighter@^16.1.1 [GS-219] [GS-214].
- Upgrade axios@^1.19.0 to fix the security vulnerabilities [GS-219]:
  - Server-side Request Forgery (SSRF) [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-17111062] in axios@1.15.1
  - Prototype Pollution [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-17111079] in axios@1.15.1
  - Insertion of Sensitive Information Into Sent Data [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-17172681] in axios@1.15.1
  - Improperly Controlled Modification of Dynamically-Determined Object Attributes [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-16299921] in axios@1.15.1
  - Prototype Pollution [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-17111060] in axios@1.15.1
  - Prototype Pollution [Critical Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-16417750] in axios@1.15.1
  - Improper Removal of Sensitive Information Before Storage or Transfer [High Severity][https://security.snyk.io/vuln/SNYK-JS-FOLLOWREDIRECTS-16032162] in follow-redirects@1.15.11
- Upgrade yup@^1.7.1 to fix the security vulnerabilities [GS-219]:
  - Arbitrary Code Injection [High Severity][https://security.snyk.io/vuln/SNYK-JS-LODASH-15869625] in lodash@4.17.23
    introduced by yup@0.32.11 > lodash@4.17.23
  - Arbitrary Code Injection [High Severity][https://security.snyk.io/vuln/SNYK-JS-LODASHES-15869627] in lodash-es@4.17.23
    introduced by yup@0.32.11 > lodash-es@4.17.23
- Upgrade react-router-dom@^7.18.2 to fix the security vulnerability [GS-219]:
  - React Router: RSC Mode CSRF Bypass Allows Action Execution Before 400 Response. This is a follow up to CVE-2026-22030 to address related CSRF flows in unstable RSC code paths.
- "react" and "react-dom" have now peer dependencies with "^18.2.0" that does not affect this codebase because it only uses BrowserRouter/Routes/Route/Link/Navigate, no RSC APIs. By the way React/ReactDOM will be upgraded to 19 on next release to fix the mentioned react-router-dom security vulnerability [GS-219].
- Bump Node.js version in .nvmrc to 26 [GS-339].
- "users_user_history.json", "users_config.json" and "users_api_keys.json" configuration files now use the "mandatoryFilters" parameter in the backend configuration to ensure the user history, config and API keys are forced to the current user [GS-327].
- "users_user_history_admin.json", "users_config_admin.json" and "users_api_keys_admin.json" configuration files don't use the "mandatoryFilters" parameter to let the superuser to see all the user history, config and API keys when editing users [GS-327].
- Upgrade @babel/core to ^7.29.7 to fix the @babel/core: Arbitrary File Read via sourceMappingURL Comment ([CVE-2026-49356](https://github.com/babel/babel/security/advisories/GHSA-4x5r-pxfx-6jf8)) [GS-219].

##### Removed
- The `scripts/` directory were moved to the [frontend scripts library](https://github.com/tomkat-cr/genericsuite-fe-scripts) [GS-107].
- Unused `peerDependencies`: `react-icons`, `web-vitals`, `fs`, `json-loader`, `with`, `constants-browserify`, `crypto-browserify`, `os-browserify`, `stream-browserify`, `tty-browserify`, `url`, `vm-browserify`. None are imported anywhere in `src/`, and the Node.js core module shims were only ever used by the (optional) webpack/`react-app-rewired` dev-server configs [GS-338].
- Unused `devDependencies`: `@babel/cli` (nothing invokes the `babel` CLI binary), `@babel/preset-stage-0` (not referenced by any Babel config), `@rollup/plugin-typescript` (superseded by `rollup-plugin-typescript2`, which is what's actually used), `@testing-library/user-event` (no test uses it), `file-loader` and `url-loader` (SVGs use webpack 5's native `asset/resource` instead), `path` (all `require('path')` calls resolve to Node.js's builtin, not this package) [GS-338].
- `id="copyButton"` attribute from the <CopyButton /> component [GS-327].

## GenericSuite Frontend AI

### Package, Pull Request and Tag

* Package # 1: [https://www.npmjs.com/package/genericsuite-ai/v/1.3.0](https://www.npmjs.com/package/genericsuite-ai/v/1.3.0)
* Package # 2: [https://www.npmjs.com/package/genericsuite-ai/v/1.3.1](https://www.npmjs.com/package/genericsuite-ai/v/1.3.1)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/11](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/11)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/12](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/12)
* Pull Request # 3: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/13](https://github.com/tomkat-cr/genericsuite-fe-ai/pull/13)
* Tag # 1: [https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.3.0](https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.3.0)
* Tag # 2: [https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.3.0](https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.3.1)

### Pull Request Overview

AI agent docs, scripts moved to GS FE Scripts, MIT license, and security updates

Mirrors the core FE release: AI-agent docs, MIT relicensing, and the scripts-directory move to `genericsuite-fe-scripts`. Adds ChatBot UI polish (icon-based copy button, better code-block rendering) and fixes a Formik dependency-resolution error affecting ExampleApp/FastApiTemplate consumers, alongside the same large security-dependency sweep as FE Core plus jest/rollup-plugin-typescript upgrades.

Highlights

- Fixed "Could not resolve dependency: formik@2.4.5" breaking ExampleApp/FastApiTemplate consumers [GS-254].
- ChatBot conversation code blocks: icon-based copy button and rendering fixes [GS-214].
- `scripts/` moved to `genericsuite-fe-scripts`; License changed to MIT [GS-107] [FA-244].
- Security: axios, yup, react-router-dom, jest, rollup-plugin-typescript2/typescript, @babel/core upgrades fixing numerous High/Critical vulnerabilities including RCE-class and DoS issues [GS-219].
- Build/dependency cleanup: removed unused peer/dev dependencies (css-loader, postcss-loader, gh-pages, etc.) [GS-338].

### CHANGELOG.md

## [1.3.1] - 2026-08-30

### Fixed
- Hotfix: remove the develop dependency on "genericsuite" package in "publish" Makefile command to avoid conflicts with the "genericsuite" package in the parent project [GS-327].

#### [1.3.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- Add SAST testing [GS-315].
- Add frontend scripts library [GS-107].

##### Changed
- License changed to MIT [FA-244].
- Rename AWS_S3_BUCKET_NAME to AWS_S3_BUCKET_NAME_FE in the .env file [GS-328].
- ChatBot conversation code blocks enhancements: replace copy text button by an icon, and enhance design [GS-214].
- Add "tailwind-build" script to deploy_* and run_* Makefile commands [GS-214].
- `webpack.config.js` and `config-overrides.js`: commented out the Node.js core module `resolve.fallback` polyfills (`os`, `url`, `crypto`, `stream`, `assert`, `vm`, `tty`, `constants`, `zlib`, `https`, `http`, `util`) since nothing in the codebase needs them and Vite already runs fine without them; added `npm install --save-dev ...` notes above each so they can be re-enabled if a consumer's own dependency graph needs them [GS-338].
- Update version to 1.3.0 in package.json, package-lock.json, and version.txt to reflect the latest release [GS-327].

##### Fixed
- "Could not resolve dependency: formik@2.4.5" error in `ExampleApp`, `FastApiTemplate` and all apps that uses `genericsuite-fe-ai` as a dependency [GS-254].
- "installHook.js:1 TypeError: JY.default.includes is not a function" error when certain ChatBot conversations are clicked and the page becomes empty [GS-214].
- `tsconfig.json` was missing an `exclude` for `*.test.tsx`, so every test file got its own `.d.ts` stub emitted into `dist/esm` and `dist/cjs` during the Rollup build. These 14 stray files were already committed to the repo and shipping in `dist/` with every npm publish [GS-338].
- Removed a bogus `"with"` entry from the `config-overrides.js` `resolve.fallback` config — `with` is not a Node.js core module, so the fallback never did anything [GS-338].
- The `webpack.config.js` fallback referenced `require.resolve("assert")` for a package that was never declared anywhere in `package.json`; documented it in the install note instead of leaving a silently-broken reference [GS-338].
- `rollup.config.mjs`: removed `formik` from the `external` array — it isn't a declared peer dependency and isn't imported anywhere in `src/` (leftover from copying `genericsuite-fe`'s Rollup config) [GS-338].
- "config-overrides.js" updated to fix errors running the app with RUN_BUNDLER="react-scripts" [GS-338], and refactor it to use fileURLToPath for path resolution and clean up unused debug logs [GS-327].
- "process" dependency installation on "webpack.config.js" file documentation to to fix errors running the app [GS-338].

##### Security
- json5, postcss, and prismjs security vulnerabilities fixed by upgrading their dependent packages [GS-214].
- Upgrade dependencies to latest version: crypto-browserify@^3.12.1, downshift@^9.4.0, react-icons@^5.7.0, react-markdown@^10.1.0, react-syntax-highlighter@^16.1.1 [GS-219] [GS-214].
- Upgrade axios@^1.19.0 to fix the security vulnerabilities [GS-219]:
  * Server-side Request Forgery (SSRF) [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-17111062] in axios@1.15.1
  * Prototype Pollution [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-17111079] in axios@1.15.1
  * Insertion of Sensitive Information Into Sent Data [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-17172681] in axios@1.15.1
  * Improperly Controlled Modification of Dynamically-Determined Object Attributes [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-16299921] in axios@1.15.1
  * Prototype Pollution [High Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-17111060] in axios@1.15.1
  * Prototype Pollution [Critical Severity][https://security.snyk.io/vuln/SNYK-JS-AXIOS-16417750] in axios@1.15.1
  * Improper Removal of Sensitive Information Before Storage or Transfer [High Severity][https://security.snyk.io/vuln/SNYK-JS-FOLLOWREDIRECTS-16032162] in follow-redirects@1.15.11
  * Allocation of Resources Without Limits or Throttling in Axios
  * form-data: CRLF injection in form-data via unescaped multipart field names and filenames
  * Axios: Incomplete Fix for CVE-2025-62718 — NO_PROXY Protection Bypassed via RFC 1122 Loopback Subnet (127.0.0.0/8) in Axios 1.15.0
  * Axios: Header Injection via Prototype Pollution
  * Axios: unbounded recursion in toFormData causes DoS via deeply nested request data
  * follow-redirects leaks Custom Authentication Headers to Cross-Domain Redirect Targets
- Upgrade yup@^1.7.1 to fix the security vulnerabilities [GS-219]:
  * Arbitrary Code Injection [High Severity][https://security.snyk.io/vuln/SNYK-JS-LODASH-15869625] in lodash@4.17.23
    introduced by yup@0.32.11 > lodash@4.17.23
  * Arbitrary Code Injection [High Severity][https://security.snyk.io/vuln/SNYK-JS-LODASHES-15869627] in lodash-es@4.17.23
    introduced by yup@0.32.11 > lodash-es@4.17.23
  * lodash vulnerable to Prototype Pollution via array path bypass in `_.unset` and `_.omit`
- Upgrade react-router-dom@^7.18.2 to fix the security vulnerability [GS-219]:
  * React Router: RSC Mode CSRF Bypass Allows Action Execution Before 400 Response. This is a follow up to CVE-2026-22030 to address related CSRF flows in unstable RSC code paths.
  * React Router's vendored turbo-stream v2 allows arbitrary constructor invocation via TYPE_ERROR deserialization leading to Unauth RCE
  * React Router vulnerable to XSS in unstable RSC redirect handling via javascript: redirect targets
  * React Router vulnerable to DoS via unbounded path expansion in __manifest endpoin
  * React Router vulnerable to Denial of Service via reflected user input in single-fetch #105
- Upgrade jest to "^30.4.2", jest-environment-jsdom to "^30.4.1", and "babel-jest" to "^30.4.1" to fix the security vulnerabilities [GS-219].
  * @babel/plugin-transform-modules-systemjs generates arbitrary code when compiling malicious input
  * ws: Memory exhaustion DoS from tiny fragments and data chunks 
  * brace-expansion: DoS via exponential-time expansion of consecutive non-expanding {} groups
  * js-yaml: YAML merge-key chains can force quadratic CPU consumption
  * @babel/core: Arbitrary File Read via sourceMappingURL Comment
- Upgrade rollup-plugin-typescript2 to "^0.37.0" and typescript to "^5.3.3" to fix the security vulnerabilities [GS-219].
  * Picomatch: Method Injection in POSIX Character Classes causes incorrect Glob Matching
- Other security vulnerabilities fixed by upgrading their dependent packages [GS-219]:
  * SVGO removeScripts plugin leaves some executable scripts intact
  * serialize-javascript [removed] Serialize JavaScript is Vulnerable to RCE via RegExp.flags and Date.prototype.toISOString() [CVE-2020-7660](https://github.com/advisories/GHSA-hxcc-f52p-wc94)
  * serialize-javascript [removed] Serialize JavaScript has CPU Exhaustion Denial of Service via crafted array-like objects
  * PostCSS: Arbitrary file read and information disclosure via attacker-controlled sourceMappingURL in CSS comments
  * fast-uri [removed] fast-uri vulnerable to path traversal via percent-encoded dot segments
  * fast-uri [removed] fast-uri vulnerable to host confusion via percent-encoded authority delimiters
  * fast-uri [removed] fast-uri vulnerable to host confusion via failed IDN canonicalization 
  * path-to-regexp [removed] path-to-regexp vulnerable to Regular Expression Denial of Service via multiple route parameters [CVE-2024-45296](https://github.com/advisories/GHSA-9wv6-86v2-598j)
  * ip-address [removed] ip-address: Address4 decodes leading-zero octets as decimal while resolvers decode them as octal, allowing SSRF and trust-boundary bypass
  * express-rate-limit [removed] express-rate-limit: IPv4-mapped IPv6 addresses bypass per-client rate limiting on servers with dual-stack network 
  * qs [removed] qs has a remotely triggerable DoS: qs.stringify crashes with TypeError on null/undefined entries in comma-format arrays when encodeValuesOnly is set
  * body-parser [removed] body-parser vulnerable to denial of service when invalid limit value silently disables size enforcement
  * elliptic [removed] Elliptic Uses a Cryptographic Primitive with a Risky Implementation
- "react" and "react-dom" have now peer dependencies with "^18.2.0" that does not affect this codebase because it only uses BrowserRouter/Routes/Route/Link/Navigate, no RSC APIs. By the way React/ReactDOM will be upgraded to 19 on next release to fix the mentioned react-router-dom security vulnerability [GS-219].
- Bump Node.js version in .nvmrc to 26 [GS-339].
- Upgrade @babel/core to ^7.29.7 to fix the @babel/core: Arbitrary File Read via sourceMappingURL Comment ([CVE-2026-49356](https://github.com/babel/babel/security/advisories/GHSA-4x5r-pxfx-6jf8)) [GS-219].

##### Removed
- The `scripts/` directory were moved to the [frontend scripts library](https://github.com/tomkat-cr/genericsuite-fe-scripts) [GS-107].
- Unused `peerDependencies`: `react-icons`, `web-vitals`, `fs`, `json-loader`, `with`, `constants-browserify`, `crypto-browserify`, `os-browserify`, `stream-browserify`, `tty-browserify`, `url`, `vm-browserify`, `browserify-zlib`, `https-browserify`, `net`, `stream-http`, `util`, `buffer`, `downshift`, `history`, `rxjs`, `react-markdown`, `yup`. None are imported anywhere in `src/`; the CRUD-editor-oriented ones (`buffer`, `downshift`, `history`, `rxjs`, `react-markdown`, `yup`) are already required transitively through the `genericsuite` peer dependency for anyone who needs them, and the Node.js core module shims were only ever used by the (optional) webpack/`react-app-rewired` dev-server configs [GS-338].
- Unused `devDependencies`: `@babel/cli`, `@babel/preset-stage-0`, `@rollup/plugin-typescript`, `file-loader`, `path`, `url-loader` (same reasoning as `genericsuite-fe`), and `whatwg-fetch` (no test needs it here). `@testing-library/user-event` was kept — unlike `genericsuite-fe`, it's genuinely used in `ChatCodeBlock.test.tsx` [GS-338].
- Unnecessary dependencies  (css-loader, postcss-loader, style-loader, and , gh-pages). The user can import them if webpack or github pages are going to be used in their app [GS-338].
- 'id="copyButton"' attribute from the <ChatCopyButton /> component [GS-327].

## GenericSuite Frontend Scripts

### Package, Pull Request and Tag

* Package: [https://www.npmjs.com/package/genericsuite-fe-scripts/v/1.0.0](https://www.npmjs.com/package/genericsuite-fe-scripts/v/1.0.0)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/2](https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/2)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/3](https://github.com/tomkat-cr/genericsuite-fe-scripts/pull/3)
* Tag: [https://github.com/tomkat-cr/genericsuite-fe-scripts/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-fe-scripts/releases/tag/1.0.0)

### Pull Request Overview

Create the GS FE scripts library, frontend deployment expanded to be used on landing pages, SAST testing, OpenTofu for FE deployment

The debut release of the GenericSuite Frontend Scripts library — split out of `genericsuite-fe`'s `scripts/` directory into its own standalone, reusable package. It expands S3 frontend deployment to support landing pages (not just the main app), and adds a full OpenTofu-based deployment pipeline (private S3 + CloudFront with Origin Access Control, SPA error routing, TLS 1.2, and S3 remote state) parallel to the existing bash-script deployment.

Highlights

- New standalone frontend scripts library, extracted from `genericsuite-fe` [GS-107].
- New OpenTofu `frontend-hosting` module: private S3 + CloudFront (OAC, TLSv1.2_2021, SPA routing) with a full `aws_tf_deploy_to_s3.sh` pipeline [GS-334].
- FE S3 deployment expanded to support landing pages, not just the main app [GS-328].

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Added
- Create the frontend scripts library [GS-107].
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- OpenTofu (Terraform-compatible) IaC frontend deployment in `scripts/aws_tf`: `frontend-hosting` module (private S3 + CloudFront with Origin Access Control, redirect-to-https, TLSv1.2_2021, SPA error routing) and `aws_tf_deploy_to_s3.sh` full pipeline (tofu apply + build + S3 sync + CloudFront invalidation), with S3 remote state — parallel to the existing `aws_deploy_to_s3.sh`, which remains unchanged [GS-334].

##### Changed
- Change FE S3 deployment to be used on Landing Pages [GS-328].
- Rename AWS_S3_BUCKET_NAME to AWS_S3_BUCKET_NAME_FE in the .env file and scripts [GS-328].
- Enhance `aws_deploy_to_s3.sh`: Set default values for RUN_BUNDLER, UPDATE_BUILD, and BUILD_DIR if not specified via CLI. Improve bucket name handling and CloudFront distribution checks. Update package.json homepage during deployment and restore after completion only if RUN_BUNDLER != none. Use BUILD_DIR to set the build directory, so mobile deployment -that's not react-vite- can be done.
- Update .npmignore to include additional files and directories for Claude Code, AI Agents, and OpenTofu [GS-327].

##### Security
- Bump Node.js version in .nvmrc to 26 [GS-339].

## GenericSuite Backend Core

### Package, Pull Request and Tag

* Package: [https://pypi.org/project/genericsuite/0.4.0/](https://pypi.org/project/genericsuite/0.4.0/)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-be/pull/16](https://github.com/tomkat-cr/genericsuite-be/pull/16)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-be/pull/16](https://github.com/tomkat-cr/genericsuite-be/pull/19)
* Tag: [https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.4.0](https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.4.0)

### Pull Request Overview

OPENSPEC, enhance AI agent documentation, improve security measures, MIT license and unit test

This release adds full GCP Cloud Storage and Azure Blob Storage abstraction-layer implementations (matching the existing AWS S3 support), plus GCP Secret Manager and Azure Key Vault secrets backends — extending the cloud-agnostic design to two more providers. It also adds FastAPI/Flask rate limiting, general unit test coverage, a `select_table` 1-1 relationship resolver across all DB engines, MIT relicensing, and a security-dependency pass (pyjwt, cryptography, urllib3) plus a path-traversal fix in `app_context.py`.

Highlights

- GCP Cloud Storage and Azure Blob Storage support fully implemented (upload/remove/presigned-URL/retrieval) [GS-318] [GS-317].
- GCP Secret Manager and Azure Key Vault `get_secrets()` backends added [GS-318] [GS-317].
- `select_table` field type: engine-agnostic 1-1 relationship resolver (DynamoDB BatchGetItem / MongoDB `$lookup` fast paths) [GS-259].
- Rate limiting (`slowapi`) integrated into FastAPI and Flask endpoints [GS-332].
- Security: pyjwt, cryptography, urllib3 upgraded; path traversal vulnerability fixed in `app_context.py`; migrated to Python 3.14 [GS-219] [GS-337].

### CHANGELOG.md

#### [0.4.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- SAST testing [GS-315].
- General unit tests [GS-21].
- AWS_SSL_CERTIFICATE_ARN_BE envvar to the `.env.example` file [GS-328].
- GCP Cloud Storage (GCS) object storage support: full implementation of `upload_file_to_storage`, `remove_from_storage`, `get_gcs_presigned_url`, `storage_retieval`, and `prepare_asset_url` in `genericsuite/util/gcp.py` [GS-318].
- Azure Blob Storage object storage support: full implementation of `upload_file_to_storage`, `remove_from_storage`, `get_blob_presigned_url` (SAS tokens), `storage_retieval`, and `prepare_asset_url` in `genericsuite/util/azure.py` [GS-317].
- GCP Secret Manager support: real `get_secrets()` implementation in `genericsuite/util/gcp_secrets.py` using `google-cloud-secret-manager` SDK; requires `GCP_PROJECT_ID` env var [GS-318].
- Azure Key Vault support: real `get_secrets()` implementation in `genericsuite/util/azure_secrets.py` using `azure-keyvault-secrets` + `azure-identity` SDKs; requires `AZURE_KEYVAULT_URL` env var [GS-317].
- Optional dependency groups `gcp` and `azure` in `pyproject.toml` for lazy SDK installation [GS-317] [GS-318].
- New env vars documented in `.env.example`: `GCP_PROJECT_ID`, `GCS_CHATBOT_ATTACHMENTS_BUCKET_*`, `AZURE_STORAGE_ACCOUNT_NAME`, `AZURE_STORAGE_ACCOUNT_KEY`, `AZURE_CHATBOT_ATTACHMENTS_CONTAINER_*`, `AZURE_KEYVAULT_URL`, `CLOUD_STORAGE_PRESIGNED_EXPIRY`, `CLOUD_STORAGE_PRESIGNED_ACTIVE` [GS-317] [GS-318].
- Unit tests for GCS storage (`tests/test_gcp_storage.py`), Azure Blob storage (`tests/test_azure_storage.py`), GCP Secret Manager (`tests/test_util_gcp_secrets.py`), and Azure Key Vault (`tests/test_util_azure_secrets.py`) [GS-317] [GS-318].
- Introduce `DEBUG_CORS` environment variable in FastAPI `create_app.py` to log CORS origins during development. This enhances debugging capabilities for CORS configuration [GS-329].
- `slowapi` for FastAPI rate limiting package [GS-332].
- Integrate rate limiting in FastAPI and Flask endpoints [GS-332].
- `select_table` field type: 1-1 relationship resolution in listings and reads. New JSON field attributes `related_table`, `local_field`, `related_key`, `description_fields`, `description_separator`, `related_filter`; rows now include `{field}_description`. Engine-agnostic `$in` resolver for all DB engines, with DynamoDB BatchGetItem and MongoDB `$lookup` fast paths [GS-259].

##### Fixed
- API Key MCP headers and API Key authentication issues: modify get_access_token to include all headers, update mcp_authenticate_api_key to only require user_id based on MCP_MANDATORY_USER_ID, improve user_id assignment logic when only API Key is provided. Adjust verify_app_context to raise a more descriptive error for missing user credentials [GS-243].

##### Changed
- License changed to MIT [FA-244].
- Update FastAPI abstraction layer CORS configuration in `create_app.py` to handle multiple origins by splitting the `CORS_ORIGIN` string if it contains commas [GS-329].
- Update CORS configuration in `framework_abstraction.py` to set `Access-Control-Allow-Origin` to '*' for handling multiple origins, as FastAPI manages origin splitting internally [GS-329].
- Remove request authentication for flexibility [GS-329].
- And add rate limit in `logs.py` for the `/logs` endpoint [GS-332].
- Enhance comments about how to specify the C0301 and E501 line-too-long lint conditions on `config.py`
- Replace Github Gemini code review with SonarQube and Claude code review [GS-336].
- Modify Makefile to allow optional arguments for twine upload during production publish, e.g. "--verbosity" [GS-327].
- Update version to 0.4.0 in package.json, pyproject.toml, and setup.py [GS-327].

##### Security
- Upgrade "pyjwt" to "^2.13.0" to fix security vulnerabilities [GS-219]:
    * Improper Verification of Cryptographic Signature [High Severity], SNYK-PYTHON-PYJWT-15518059
    * PyJWKClient: missing scheme allowlist enables CVE-2024-21643-class SSRF + token forgery via file://, ftp://, data: schemes
    * PyJWKClient unbounded JWKS endpoint requests via attacker-controlled kid values (DoS)
- Upgrade cryptography to "^50.0.0" to fix security vulnerabilities [GS-219].
    * python-cryptography: Duplicate self-signed intermediates can cause exponential path-building
    * cryptography: PKCS#7 EnvelopedData decryption exposes a Bleichenbacher oracle through distinguishable errors and timing
    * python-cryptography verifier accepts wildcard DNS names allowing escape from permittedSubtrees
- Avoid characters that are not allowed in filenames built from user_id or ObjectId in `app_context.py` [GS-219].
- Upgrade "urllib3" to "^2.7.0" to fix security vulnerabilities [GS-219].
- Fix "Unsanitized input from an HTTP header flows into json.dump, where it is used as a path. This may result in a Path Traversal vulnerability and allow an attacker to write arbitrary files." in app_context.py [GS-219].
- Migrate to Python 3.14 [GS-337].
- Bump Node.js version in .nvmrc to 26 [GS-339].

## GenericSuite Backend AI

### Package, Pull Request and Tag

* Package: [https://pypi.org/project/genericsuite-ai/0.4.0/](https://pypi.org/project/genericsuite-ai/0.4.0/)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/14](https://github.com/tomkat-cr/genericsuite-be-ai/pull/14)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/15](https://github.com/tomkat-cr/genericsuite-be-ai/pull/15)
* Tag: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.4.0](https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.4.0)

### Pull Request Overview

Enhance AI agent documentation and address security vulnerabilities

A security- and hygiene-focused release: AI-agent onboarding docs, SAST testing, MIT relicensing, and code review tooling switched from GitHub Gemini to SonarQube + Claude. The bulk of the change is a security-dependency upgrade pass across the LangChain stack (langchain, langchain-openai, langchain-core, langchain-community) fixing directory traversal, SSRF, ReDoS, and deserialization vulnerabilities, plus pytest/twine/fastapi/aiohttp/cryptography/pyjwt updates and a migration to Python 3.14.

Highlights

- LangChain stack upgraded (langchain, langchain-openai, langchain-core, langchain-community) fixing High-severity directory traversal, SSRF, ReDoS, and unsafe-deserialization issues [GS-219].
- cryptography and pyjwt upgraded to fix path-building and SSRF/token-forgery vulnerabilities [GS-219].
- License changed to MIT; code review tooling moved to SonarQube + Claude [FA-244] [GS-336].
- Migrated to Python 3.14; Node.js bumped to v26 in `.nvmrc` [GS-337] [GS-339].

### CHANGELOG.md

#### [0.4.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- SAST testing [GS-315].
- AWS_SSL_CERTIFICATE_ARN_BE envvar to the `.env.example` file [GS-328].

##### Changed:
- Remove all references to fynapp on `ai_conversations_conversion.py`
- Enhance comments about how to specify the C0301 and E501 line-too-long lint conditions on `config.py`
- License changed to MIT [FA-244].
- Replace Github Gemini code review with SonarQube and Claude code review [GS-336].
- Modify Makefile to allow optional arguments for twine upload during production publish, e.g. "--verbosity" [GS-327].
- Update version to 0.4.0 in package.json, pyproject.toml, and setup.py [GS-327].

##### Security
- Upgrade langchain to "^1.3.14", langchain-openai to "^1.4.1", langchain-core to "^1.5.2", langchain-community to "^0.4.2", to fix security vulnerabilities [GS-219].
    * Directory Traversal (new) [High Severity], SNYK-PYTHON-LANGCHAINCORE-15809257
    * Allocation of Resources Without Limits or Throttling [High Severity], SNYK-PYTHON-AIOHTTP-14871876, SNYK-PYTHON-AIOHTTP-14871877, SNYK-PYTHON-AIOHTTP-15873732, SNYK-PYTHON-BROTLICFFI-14172734
    * Infinite loop [High Severity], SNYK-PYTHON-AIOHTTP-14871979
    * Server-side Request Forgery (SSRF) (new) [High Severity], SNYK-PYTHON-AIOHTTP-15873738
    * Regular Expression Denial of Service (ReDoS) [High Severity], SNYK-PYTHON-LANGCHAINCLASSIC-14914754
    * Deserialization of Untrusted Data [High Severity], SNYK-PYTHON-LANGGRAPH-15433492, SNYK-PYTHON-LANGGRAPHCHECKPOINT-15353408, SNYK-PYTHON-LANGGRAPHCHECKPOINT-15433491
    * h2: Duplicate Host header could facilitate request smuggling
- Upgrade pytest to "^9.1.1", pytest-cov to "^7.1.0", twine to "^7.0.0", fastapi to "^0.140.13", pytest-mock to "^3.15.1", to fix security vulnerabilities [GS-219].
- Upgrade ddgs to "^9.14.4" to fix security vulnerabilities [GS-219].
- Pin "urllib3" to "^2.7.0" to fix "urllib3: Decompression-bomb safeguards bypassed in parts of the streaming API" security vulnerability [GS-219].
- Pin starlette to "^1.3.1" to fix "Starlette has missing Host header validation that poisons request.url.path, bypassing path-based security checks" security vulnerability (only for development dependencies) [GS-219].
- Pin aiohttp to "^3.14.3" to fix "Allocation of Resources Without Limits or Throttling [High Severity][https://security.snyk.io/vuln/SNYK-PYTHON-AIOHTTP-14871876]" security vulnerability. This must be removed once aiohttp is greater than "^3.14.3" by its dependers [GS-219].
- Upgrade cryptography to "^50.0.0" to fix security vulnerabilities [GS-219].
    * python-cryptography: Duplicate self-signed intermediates can cause exponential path-building
    * cryptography: PKCS#7 EnvelopedData decryption exposes a Bleichenbacher oracle through distinguishable errors and timing
    * python-cryptography verifier accepts wildcard DNS names allowing escape from permittedSubtrees 
- Upgrade pyjwt to "^2.13.0" to fix security vulnerabilities [GS-219].
    * PyJWKClient: missing scheme allowlist enables CVE-2024-21643-class SSRF + token forgery via file://, ftp://, data: schemes
    * PyJWKClient unbounded JWKS endpoint requests via attacker-controlled kid values (DoS)
- Migrate to Python 3.14 [GS-337].
- Bump Node.js version in .nvmrc to 26 [GS-339].

## GenericSuite Backend Scripts

### Package, Pull Request and Tag

* Package: [https://www.npmjs.com/package/genericsuite-be-scripts/v/1.4.0](https://www.npmjs.com/package/genericsuite-be-scripts/v/1.4.0)
* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/16](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/16)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-be-scripts/pull/17](https://github.com/tomkat-cr/genericsuite-be-scripts/pull/17)
* Tag: [https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.4.0](https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.4.0)

### Pull Request Overview

AI agent docs + OpenTofu modules + multiple CORS Origins to FastAPI + SAST testing + Python 3.14

Adds a full parallel OpenTofu (Terraform-compatible) IaC deployment path alongside the existing CloudFormation scripts — covering S3, DynamoDB, KMS, Secrets Manager, ECR, ACM/Route53, EC2+ALB, and Lambda+API Gateway — plus a matching DynamoDB tfvars generator. Also adds multi-origin CORS support for FastAPI's big-Lambda template, MCP server env-var handling fixes, AI-agent docs, SAST testing, and a Python 3.14 migration.

Highlights

- New OpenTofu IaC deployment stacks (`scripts/aws_tf`) parallel to existing CloudFormation, covering S3/DynamoDB/KMS/Secrets Manager/ECR/ACM/Route53/EC2+ALB/Lambda+API Gateway [GS-334].
- DynamoDB tfvars generator reading the same GenericSuite JSON config as the CloudFormation generator [GS-334].
- Multiple CORS Origins support added to FastAPI's `aws_big_lambda/template-sam.yml` [GS-329].
- Fixed multiple envvars (CLOUD_PROVIDER, APP_NAME, AWS_REGION, etc.) not being passed to the MCP server in `run_mcp_server.sh` [GS-243].
- Migrated to Python 3.14; License changed to MIT [GS-337] [FA-244].

### CHANGELOG.md

#### [1.4.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- SAST testing [GS-315].
- AWS_SSL_CERTIFICATE_ARN_BE to the `big_lambdas_manager.sh` script [GS-328]
- Multiple CORS Origins support to FastAPI in the `aws_big_lambda/template-sam.yml` file [GS-329].
- OpenTofu (Terraform-compatible) IaC deployments in `scripts/aws_tf`: generic wrapper (`run-tf-deployment.sh`), S3 remote state with native locking (`bootstrap-tf-state.sh`), and modules/stacks for S3 buckets, DynamoDB tables, KMS, Secrets Manager, ECR, ACM/Route53 app domains, EC2+ALB, and Lambda+API Gateway — parallel to the existing CloudFormation scripts, which remain unchanged [GS-334].
- DynamoDB tfvars generator (`scripts/aws_tf/generate_dynamodb_tfvars.py`) reading the same GenericSuite JSON config as the CloudFormation generator [GS-334].
- ADDITIONAL_MCP_RUN_ARGS envvar can be passed to the MCP server "run_mcp_server.sh" script, so additional arguments can be passed to the MCP server without having to modify the script [GS-243].

##### Changed
- License changed to MIT [FA-244].
- Enhance error handling and messaging in the `set_fe_cloudfront_domain.sh` script [GS-328]
- Initialize APP_ENVS variable in `update_additional_envvars.sh` for app-specific environment variables example [GS-329].
- Update `run_mcp_server.sh` to improve environment variable handling (removing double-quotes), adapt to MCP inspector 2.0, create a .env.mcp.json file to have both stdio and streamable-http servers in the MCP inspector instance, implement a function to manage environment variables, ensuring they are set correctly in the .env file., and improve error handling and streamline variable checks throughout the script [GS-243].
- Update .npmignore to include additional files and directories for Chalice, Claude Code, and OpenTofu [GS-327].
- Increment package version to 1.4.0 in package.json and package-lock.json [GS-327].

##### Fixed
- Fix envvars not being passed to the MCP server in "run_mcp_server.sh": CLOUD_PROVIDER, APP_NAME, AWS_REGION, STORAGE_URL_SEED, APP_SUPERADMIN_EMAIL, GIT_SUBMODULE_LOCAL_PATH, GET_SECRETS_ENABLED, GET_SECRETS_CRITICAL, and GET_SECRETS_ENVVARS [GS-243].
- Fix `pnpm install` calling the release command, treating the script named `publish` as an **npm lifecycle hook** while preparing a **git-hosted** dependency, instead of just cloning the repo. This happens when installing GS BE Scripts as a git-hosted dependency. Therefore, it won't be `publish`, `prepublish`, `prepublishOnly`, `prepack`, `prepare`, `postpack`, or `postpublish` reserved names in the NPM script names, so they were renamed to `npm-publish` and `npm-pre-publish` [GS-339].

##### Security
- Migrate to Python 3.14 [GS-337].
- Clean up output in "run_mcp_server.sh" by removing unnecessary echo statements [GS-243].
- Supress MCP server npm notice in "run_mcp_server.sh" by setting the MCP_DISABLE_NOTICE environment variable to true [GS-243].
- Bump Node.js version in .nvmrc to 26 [GS-339].
- Remove "office-addin-dev-certs" from package.json dependencies to let user choose to install it if needed, and fix security vulnerabilities [GS-219].
   * Forge has signature forgery in Ed25519 due to missing S > L check (CVE-2026-25793, CVE-2022-35961)
   * Forge has signature forgery in RSA-PKCS due to ASN.1 extra field (This issue is similar to CVE-2022-24771)
   * Forge has a basicConstraints bypass in its certificate chain verification (RFC 5280 violation) (same vulnerability class as: CVE-2014-0092, CVE-2015-1793, CVE-2020-0601)
   * uuid: Missing buffer bounds check in v3/v5/v6 when buf is provided

## GenericSuite BaseCamp

### Package, Pull Request and Tag

* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-basecamp/pull/19](https://github.com/tomkat-cr/genericsuite-basecamp/pull/19)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-basecamp/pull/22](https://github.com/tomkat-cr/genericsuite-basecamp/pull/22)
* Tag: [https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.6.0](https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/1.6.0)

### Pull Request Overview

Rename docs to mkdocs_root + et al.

This pull request is a broad documentation and tooling update spanning the whole GenericSuite ecosystem: the docs site was reorganized (`docs/` → `mkdocs_root/`, `specs/` → `docs/`), new documentation was added for Mobile Development, AI Skills, GS FE Scripts, and an OpenTofu deployment guide, the project license moved to MIT, SAST testing and dependency-vulnerability fixes were applied across ExampleApp and FastApiTemplate, and the main repository pointer was switched from GS Basecamp to the new GS Superproject.

Highlights

- Documentation site reorganization: `docs/` renamed to `mkdocs_root/`, new Mobile Development, AI Skills, GS FE Scripts, and OpenTofu deployment guide pages added, and the site's main repo now points to the GS Superproject.
- Security and compliance: SAST testing wired in, dependency upgrades (cryptography, crypto-browserify, `@babel/core` CVE-2026-49356 fix, Python 3.14 migration), license changed to MIT, and `mandatoryFilters` enforcement for user history/config/API-key tables.
- Developer tooling: `new-project-from-template.sh` and `rename-app.sh` scaffolding scripts, `make create-supad`, Makefile refactors to use `genericsuite-fe-scripts`, and three new AI skills (`add-doc`, `sample-code-update`, `translate-docs`).
- CRUD Editor and configuration: `select_table` field type and `SelectElementItem` inline select options documented for the Generic CRUD Editor.

### CHANGELOG.md

#### [1.6.0] - 2026-08-30

##### Added
- New architecture image for documentation index page [GS-327].
- Add AI Skills documentation page [GS-254].
- Add Security Skills documentation page [GS-339].
- GS FE Scripts documentation page [GS-107].
- Mobile Development documentation section: GenericSuite Flutter installation, JSON-driven CRUD, childComponents (1-N relationships), and the Apple-clean theming tokens [GS-261].
- OpenTofu deployment guide (`mkdocs_root/en/Deployment-Guide/opentofu.md`) covering the genericsuite-fe-scripts and genericsuite-be-scripts IaC stacks, with a nav entry in `mkdocs.yml` [GS-334].
- GS Superproject, Security Suite and GS FE Scripts to the repositories.md page [GS-319].
- SAST testing [GS-315]
- `select_table` field type documentation to Add 1-1 relationships support to the CRUD Editor listing/data pages [GS-259].
- Spanish nav_translations for Mobile Development docs section [GS-261].
- Introduce `SelectElementItem` model for inline select options in CRUD editor configuration. Update `select_elements` field to support both predefined IDs and inline {title, value} objects [GS-254]
- AWS_SSL_CERTIFICATE_ARN_FE and AWS_SSL_CERTIFICATE_ARN_BE envvars [GS-328].
- Multiple CORS Origins support to FastAPI in the `aws_big_lambda/template-sam.yml` file [GS-329].
- `make create-supad` to exampleapp/fastapitemplate server [GS-306].
- Scripts to copy and init a new project from "fastapitemplate" and "exampleapp": `scripts/new-project-from-template.sh` and `scripts/rename-app.sh` [GS-306].
- New AI skill definitions (`.ai/skills/`): add-doc, sample-code-update, translate-docs
- "zipp" dependency to main requirements.txt to address a vulnerability as recommended by Snyk [GS-219].

##### Changed
- Rename `docs/` to `mkdocs_root/` [GS-208].
- Rename `specs/` to `docs/` [GS-208].
- `.venv/` added to .gitignore and .dockerignore files.
- `run_translate_uncommitted.sh` creates and deletes `.venv` virtual environment [GS-316].
- License changed to MIT [FA-244].
- Enhance SSL certificate ARN documentation in the backend core for better clarity on the AWS_SSL_CERTIFICATE_ARN_FE and AWS_SSL_CERTIFICATE_ARN_BE envvars usage across backend and frontend scripts [GS-328].
- Initialize APP_ENVS variable in `update_additional_envvars.sh` for app-specific environment variables example [GS-329].
- Update FastApiTemplate Makefile with new utility targets, "tomkat-cr" replaced with "github-username" in ".env.example" [GS-306]
- Separate directory structure from CLAUDE.md to make it smalller [GS-303].
- Update FastAPI template setup with instructions to run the `new-project-from-template.sh` using `curl` [GS-306].
- Add FastApiTemplate reference to the configuration guide main document [GS-254]
- FastApiTemplate: Refactor UI components renaming "_components" > "components", "_images" > "images", and "_constants" > "constants" [GS-306].
- Update exampleap/fastapitemplate server and mcp-server development scripts for dynamic environment management, so stage can be set running `STAGE=dev make dev`(package.json now uses the STAGE variable on "dev": "make run_${STAGE:-qa}") [GS-306].
- FastApiTemplate: Make ".env.example" files to use default values for less user changes on project startup [GS-306].
- Enhance AGENTS.md, GEMINI.md, and CLAUDE.md files to provide better context and instructions to AI Coding Assistants [GS-303].
- Include .claude, .agents, .codex, .cursor, and .gemini directories to share skills/commande from the .ai directory [GS-254]
- Rename '.claude' to '.ai'
- Fix directory graphs ending directory lines
- Modify `food_moment_in_user` function documentation for clarity on user references. Clean up food moments operations documentation [GS-254].
- ExampleApp: broad exception handling in FDA food endpoint [GS-254].
- `mkdocs.yml` — one nav line ('AI Skills'), verified `build-safe` against the i18n folder convention [GS-254].
- ExampleApp: Update dependencies in `package.json` and `pnpm-lock.yaml` for dotenv and turbo. [GS-254]
- ExampleApp: Update `aiohappyeyeballs` and `aiohttp` versions in uv.lock files for API apps.
- ExampleApp and FastApiTemplate: Refactor Makefile to use `genericsuite-fe-scripts` for build and deployment commands in UI app [GS-107].
- Update index.md for improved clarity and content on Generic Suite features (one-liner followed by a brief description for quick reference, logos centered, new architecture image) [GS-327].
- Update Makefile with branch usage instructions using the BRANCH envvar to prepare code from develop branch.
- Frontend-Development/GenericSuite-Core: removed `@babel/cli`, `@babel/preset-stage-0`, `@testing-library/user-event`, `file-loader`, `path`, and `url-loader` from the "Install additional development dependencies" step — these are no longer required by `genericsuite-fe`'s own build/test pipeline [GS-338].
- Frontend-Development/GenericSuite-Core: remove: unnecessary dependencies (`css-loader`, `postcss-loader`, `style-loader`, `express`, `gh-pages`) from the same documentation. The user can import them if webpack or github pages are going to be used in their app [GS-338].
- ASDT documentation so LangGraph and Smolagents are planned, not supported yet.
- All CHANGELOG format unification.
- Main repo to be the GS Superproject `repo_url: https://github.com/tomkat-cr/genericsuite` instead of the GS Basecamp [GS-319].
- Main english post page to redirect to `https://www.carlosjramirez.com/en/genericsuite`.
- Move the 2nd anniversary release banner to the releases section.
- Replace Github Gemini code review with SonarQube and Claude code review [GS-336].
- Enhance translation script to support 'changed' mode for translating updated Markdown files. Added argument parsing for mode selection and implemented logic to identify changed files in mkdocs_root/en. Default mode is 'changed' and it can be set to 'uncommitted' for uncommitted files. This improves flexibility in translation processes [GS-252].

##### Fixed
- `mkdocs_transfer_site.sh` removes the `docs_for_ftp` and `site` directories, and uses `.venv` instead of `venv` to avoid multiple python environments [GS-301].
- `new-project-from-template.sh` branch and template user input because it wasn't asked due to early default values assignment [GS-306]
- NEW_NAME validation only if it's set (scripts/new-project-from-template.sh) [GS-306]
- BASECAMP_BRANCH documentation about default value to "main" (scripts/new-project-from-template.sh) [GS-306]
- `scripts/rename-app.sh` — new filename-rename pass for fastapitemplate* files (fixes the openapi.json/yaml leftover; tested in a throwaway dir, 5/5 checks, reproduced by the `packages/genericsuite-skills/skills/python-fastapi-code-builder` AI skill reviewer) [GS-254].
- "Could not resolve dependency: formik@2.4.5" error in ExampleApp [GS-254].
- Transfer scripts to use "mkdocs_root" instead of "docs" [GS-208].
- "config-overrides.js" updated to fix errors running the app with RUN_BUNDLER="react-scripts" [GS-338].
- FastApiTemplate AWS_S3_BUCKET_NAME* values in `.env.example`.
- Transfer scripts to use "mkdocs_root" instead of "docs" [GS-208].

##### Security
- Upgrade dependencies in exampleapp and fastapitemplate package-lock and uv.lock files for multiple applications. Notable changes include upgrading cryptography, crypto-browserify, downshift, react-icons, react-markdown, react-syntax-highlighter, react-router-dom, and yup [GS-219].
- Migrate to Python 3.14 [GS-337].
- Add rate limiter documentation to GS BE Core .env.example file [GS-332].
- Bump Node.js version in .nvmrc to 26 [GS-339].
- exampleapp and fastapitemplate: "users_user_history.json", "users_config.json" and "users_api_keys.json" configuration files now use the "mandatoryFilters" parameter in the backend configuration to ensure the user history, config and API keys are forced to the current user [GS-327].
- exampleapp and fastapitemplate: "users_user_history_admin.json", "users_config_admin.json" and "users_api_keys_admin.json" configuration files don't use the "mandatoryFilters" parameter to let the superuser to see all the user history, config and API keys when editing users [GS-327].
- exampleapp and fastapitemplate: Upgrade @babel/core to ^7.29.7 to fix the @babel/core: Arbitrary File Read via sourceMappingURL Comment ([CVE-2026-49356](https://github.com/babel/babel/security/advisories/GHSA-4x5r-pxfx-6jf8)) [GS-219].

##### Removed
- AGENTS.md symlink [GS-303]
- `activeContext.md` moved to GS Superproject directory [GS-319]
- ".ai/settings.json" MacOS-specific hooks (moved to ~/.claude/settings.json).
- Because Webpack is not used in exampleapp and fastapitemplate, remove the following dependencies: css-loader, postcss-loader, style-loader, react-icons, web-vitals, fs, json-loader, with, constants-browserify, crypto-browserify, os-browserify, stream-browserify, tty-browserify, url, vm-browserify, @babel/cli, @babel/preset-stage-0, @rollup/plugin-typescript, @testing-library/user-event, file-loader, url-loader, path, gh-pages, express, express-rate-limit

## GenericSuite BaseCamp App

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-basecamp-app/pull/2](https://github.com/tomkat-cr/genericsuite-basecamp-app/pull/2)
* Tag: [https://github.com/tomkat-cr/genericsuite-basecamp-app/releases/tag/1.0.0+4](https://github.com/tomkat-cr/genericsuite-basecamp-app/releases/tag/1.0.0+4)

### Pull Request Overview

Initial development

This release ("GS Doc", the Flutter documentation-viewer mobile app) adds AI agent context files, SAST testing, and a set of Makefile targets to open iOS/Android emulators, while completing the migration off the old `genericsuite-basecamp` git submodule in favor of pulling docs via `GS_BASECAMP_PATH`.

Highlights

- New `GS_BASECAMP_PATH` environment variable and updated `run_docs_converter.sh` to clone or reuse a local GenericSuite Basecamp checkout
- New `make open-ios-simulator` / `open-android-emulator` targets for local development
- The `genericsuite-basecamp` git submodule dependency removed in favor of the `GS_BASECAMP_PATH`-driven flow
- License changed to MIT [FA-244]; fixed images not showing after the language-prefix path change [GS-252]

### CHANGELOG.md

#### [1.0.0+4] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- Add SAST testing [GS-315].
- `GS_BASECAMP_PATH` environment variable to specify the path to the GenericSuite Basecamp repository.
- `README.md` content with pre-requisites, installation and usage instructions [GS-303].
- `make open-ios-simulator` to open the Apple iOS simulator.
- `open-android-emulator` and the `open-android-emulator.sh` script.

##### Changed
- Rename `assets/docs/` to `assets/mkdocs_root/` [GS-208].
- `run_docs_converter.sh` will clone the GenericSuite Basecamp repo in the `./genericsuite-basecamp` directory if `GS_BASECAMP_PATH` is empty, otherwise it will use the path specified in `GS_BASECAMP_PATH`.
- License changed to MIT [FA-244].

##### Fixed
- Images are not showing after adding the language prefix to the path [GS-252].

##### Removed
- Git submodule genericsuite-basecamp


## GenericSuite Gitops

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-gitops/pull/6](https://github.com/tomkat-cr/genericsuite-gitops/pull/6)
* Tag: [https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.5.0](https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.5.0)

### Pull Request Overview

Enhance AI agent documentation and improve directory structure

A focused maintenance release: AI agent context files, SAST testing, a directory-structure rename (`docs/` → `help/`, `specs/` → `docs/`), and the MIT license migration.

Highlights

- AGENTS.md, GEMINI.md, and CLAUDE.md AI agent context files added [GS-303]
- SAST testing added [GS-315]
- Directory structure unified: `docs/` renamed to `help/`, `specs/` renamed to `docs/` [GS-303]
- License changed to MIT [FA-244]

### CHANGELOG.md

#### [0.5.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- Add SAST testing [GS-315].

##### Changed
- Rename `docs/` directory to `help/` [GS-303].
- Rename `specs/` directory to `docs/` [GS-303].
- License changed to MIT on README.md files [FA-244].


## GenericSuite App Maker (GSAM)

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-app-maker/pull/15](https://github.com/tomkat-cr/genericsuite-app-maker/pull/15)
* Tag: [https://github.com/tomkat-cr/genericsuite-app-maker/releases/tag/0.6.0](https://github.com/tomkat-cr/genericsuite-app-maker/releases/tag/0.6.0)

### Pull Request Overview

AI Agent docs + SAST testing + vulnerability fixes + README typos and wording

This release adds AI agent documentation and SAST testing to GSAM, cleans up README wording, and updates `requirements.txt` dependencies to their latest versions to close out known vulnerabilities.

Highlights

- AGENTS.md, GEMINI.md, and CLAUDE.md AI agent context files added, plus SAST testing [GS-303] [GS-315]
- "upgrade" and "update" Makefile targets added for dependency maintenance [GS-219]
- `requirements.txt` dependencies upgraded to their latest versions to fix known vulnerabilities [GS-219]
- Regenerated lockfile drops several unused transitive packages (cohere, mistralai, gotrue, supafunc, huggingface-hub, pypdf, and multiple llama-index-*-openai integrations) [GS-219]

### CHANGELOG.md

#### [0.6.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- Add SAST testing [GS-315].
- "upgrade" and "update" targets to Makefile [GS-219].

##### Changed
- README typos and wording [GS-128].

##### Security
- Update requirements.txt to use the latest version of the dependencies [GS-219].
- Migrate to Python 3.14 [GS-337]
- "gsam_ottomator_agent/base_python_docker/Dockerfile" uses Python 3.14 [GS-337]

##### Removed
- Regenerated lockfile drops packages that weren't there before at all: cohere, mistralai, gotrue, supafunc, huggingface-hub, pypdf, beautifulsoup4/soupsieve, llama-index-readers-file, llama-cloud, and several other llama-index-*-openai integration packages [GS-219].


## GenericSuite ASDT

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-asdt-be/pull/6](https://github.com/tomkat-cr/genericsuite-asdt-be/pull/6)
* Tag: [https://github.com/tomkat-cr/genericsuite-asdt-be/releases/tag/0.3.0](https://github.com/tomkat-cr/genericsuite-asdt-be/releases/tag/0.3.0)

### Pull Request Overview

AI Agents docs + SAST testing + vulnerabilities fixes + MIT license + clean up

This release adds AI agent documentation, SAST testing, and dependency-upgrade Makefile targets to the Agentic Software Development Team package, migrates to Python 3.14, and documents that the LangGraph and Smolagents backends remain planned (not yet supported) alongside the primary CrewAI implementation.

Highlights

- New `make upgrade`, `make crewai_upgrade`, and `make camelai_upgrade` commands to keep dependencies current and fix vulnerabilities [GS-219]
- Documentation now clarifies LangGraph and Smolagents are planned, not yet supported [GS-327]
- Security: migrated to Python 3.14 [GS-337]
- License changed to MIT [FA-244]

### CHANGELOG.md

#### [0.3.0] - 2026-08-30

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- Add SAST testing [GS-315].
- `make upgrade`, `make crewai_upgrade`, and `make camelai_upgrade` commands to upgrade dependencies to the latest version and fix vulnerabilities [GS-219].

##### Changed
- License changed to MIT [FA-244].
- Change documentation so LangGraph and Smolagents are planned, not supported yet [GS-327].
- Enhance Makefile and scripts for Python version management and upgrade commands [GS-219].
- Update dependencies in all Python projects pyproject.toml and poetry.lock for improved compatibility and security fixes [GS-219].

##### Security
- Migrate to Python 3.14 [GS-337].

##### Removed
- Remove outdated and empty requirements.txt file [GS-219].


## GenericSuite Mobile

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-mobile/pull/2](https://github.com/tomkat-cr/genericsuite-mobile/pull/2)
* Tag: [https://github.com/tomkat-cr/genericsuite-mobile/releases/tag/0.5.0](https://github.com/tomkat-cr/genericsuite-mobile/releases/tag/0.5.0)

### Pull Request Overview

GenericSuite Mobile for Flutter initial development

This release lands 1-N `childComponents` relationship support in the Flutter CRUD Editor (tappable child sections, full-screen edit, `array`/`table` subtypes matching the genericsuite-fe behavior), an Apple-clean theme token system built on `shadcn_ui`, and a large batch of defensive bug fixes across the CRUD editor, forms, auth/session handling, and navigation — plus SAST testing and the `select_table` field type carried over from 0.4.2.

Highlights

- `childComponents` (1-N) support in the Flutter CRUD Editor, matching genericsuite-fe [GS-261].
- New Apple-clean `shadcn_ui`-based theme system with a `defaultThemeParams` merge contract [GS-261].
- Wide bug-fix pass: JWT decoding, dispose()/mounted leaks, missing null-checks, missing timeouts, sync API calls [GS-327].
- `select_table` field type with related-record description resolution, carried in from 0.4.2 [GS-259].

### CHANGELOG.md

#### [0.5.0] - 2026-08-30

##### Added
- `childComponents` (1-N relationships) support in the Flutter CRUD Editor: child components declared in the frontend JSON config render as tappable sections in the edit form, open full-screen with the parent row as `parentData`, and support `child_listing` editors with `array` and `table` subtypes (including the `<array_name>`/`<array_name>_old` write payloads), matching the genericsuite-fe CRUD Editor behavior [GS-261].
- Apple-clean theme tokens in `theme_config_defaults.dart` (`accentColor`, `borderRadius` 12px, `fontFamily`/`textTheme` typography tokens with Inter via google_fonts, near-black `textColor`, iOS system semantic colors) plus a `defaultThemeParams` merge contract so apps override only the keys they need [GS-261].
- `shadcn_ui` (flutter-shadcn-ui port) now owns the widget-tree root via `ShadApp.custom`; `CreateGsApp` builds the MaterialApp theme from the GenericSuite tokens; Save/Cancel form buttons use ShadButton [GS-261].
- `buildGsShadTheme()` builds `ShadThemeData` from GenericSuite theme tokens; new `shadColorSchemeName` theme param selects the shadcn base scheme (`green` default; any `ShadColorScheme.fromName` value), with `accentColor` overriding `primary`/`ring` and GS surface/text/error tokens applied via `copyWith` [GS-261].
- "lint" and "test" commands to Makefile.
- Test coverage for the project [GS-327].

##### Changed
- Default accent color changed from blue to green; app bar and drawer default to white surfaces with near-black text; genericsuite_flutter version bumped to 0.5.0 [GS-261].
- README.md detailed configuration instructions moved to the GS Basecamp documentation [GS-261].

##### Fixed
- http_service.dart [GS-327]:
  1. getJwtPayload uses ascii.decode(...) instead of utf8.decode(...) to decode the JWT payload. Any claim with non-ASCII characters throws FormatException, breaking login-gate checks, loadConfig(), and current_user_service.dart.
  2. No .timeout(...) on any http.get/post/put/delete/patch call (unlike ip_address_service.dart, which correctly uses one), so a hung connection stalls the caller indefinitely.
  3. The 200/201 success path (json.decode(response.body) also has no try/catch, unlike the error branch. Debug flags (debugJwtToken, debugConfigValues) would print full JWTs/API keys if ever flipped on (currently const false, compiled out); query-string builder encodes values but not keys.
  4. Add type annotations to bToA(str).
- create_gs_app.dart: payload["exp"] * 1000 has no null-check; a token whose payload lacks exp (or a malformed token where getJwtPayload returns {}) throws synchronously in build(), crashing app startup instead of falling back to LoginPage. Verified by direct read [GS-327].
- crud_editor.dart [GS-327]:
  1. _saveItem: when isCreation && editorConfig['createReenter'] is true after a successful save, the method returns without calling setState(); _isLoading was flipped to true via setState but is reset with a bare assignment, so the loading spinner can stick indefinitely.
  2. No mounted checks after await before setState/_setStateAndShowMessages calls (e.g. in _buildListItem's onTap, initState's _loadConfig().then); navigating away mid-request can throw "setState() called after dispose()".
  3. json.decode(localApiResp['resultset']) in _loadSelectedItem has no try/catch unlike the equivalent in _loadItems, and int.parse(...['rows_affected']) is unguarded.
  4. _getSelectFieldsOptions — sequential await in a loop instead of Future.wait, serializing network calls unnecessarily.
- crud_editor_commons.dart [GS-327]:
  1. (buildChildRowToSave): indexes editorConfig['parentData'][keyPair['parentElementName']] with no null check.
  2. parentData can be empty/missing (e.g. _setEndpointFilter silently no-ops), so saving/deleting on a child_listing editor can throw NoSuchMethodError.
- form_field_service.dart [GS-327]:
  1. select and select_component cases set DropdownButtonFormField.initialValue without checking the value exists among items, unlike the select_table case which correctly guards with containsKey(...) ? value : null.
  2. Stale/edited data crashes the form on open. Number/integer fields call double.parse/int.parse directly in onChanged on every keystroke; clearing the field or typing ./- throws uncaught FormatException while typing.
  3. TextEditingController(text: ...) is instantiated inline in build() for most field types and never disposed; every rebuild leaks the old controller and resets cursor/focus for all fields on screen.
- app_drawer.dart [GS-327]:
  1. Icon(item['callable']['icon']) throws if item['element'] isn't a key in callables; no fallback/guard.
  2. _loadConfig().then(...) has no error handling; exceptions become unhandled async errors instead of showing the drawer's error UI.
- error_reporter_widget.dart: ScaffoldMessenger.of(context).showSnackBar(...) is called synchronously inside build() — a known Flutter anti-pattern that should be deferred via addPostFrameCallback, as homepage.dart does elsewhere.
- login.dart [GS-327]:
  1. _usernameController/_passwordController are created but the widget has no dispose() override, leaking both TextEditingControllers.
  2. apiResponse['resultset']['token'] is accessed with no null-check on resultset. "password" field lacks autocorrect: false / enableSuggestions: false.
- current_user_service.dart: if (data['error'] == 'Not Found') can never be true since http_service.dart always sets error to a bool; this branch is dead code [GS-327].
- logout_service.dart: storage.delete(...) calls for jwt/api_key/user_data aren't awaited before navigating away; app kill right after logout can leave stale credentials in secure storage [GS-327].
- routing_services.dart: Added item['callable']['type'] = 'async' (default) | 'sync' to allow sync/async function calls and handle code change made to logout_service.dart [GS-327].
- locator_service.dart: registerLazySingleton has no isRegistered guard; re-invoking setup (hot restart, remount, tests) throws on duplicate registration [GS-327].
- timestamp_utilities.dart: 12-hour formatting doesn't special-case midnight; hour 0 renders as "0:MM AM" instead of "12:MM AM" [GS-327].
- homepage.dart: loadHomeData(true) called directly as the FutureBuilder's future: inside build() re-triggers the API call on every rebuild before data is loaded [GS-327].
- deviceid_service.dart: implicit ordering dependency on setupStorageLocator() having run first [GS-327].
- back_button.dart: Navigator.of(context, rootNavigator: true).pop(context) passing context as the pop result looks unintentional [GS-327].
- CRUD Editor save froze the spinner and aborted the write (`_zOrderIndex != null` in `overlay.dart`): `_runApiCall` replaced the form with `CircularProgressIndicator`, disposing dropdown/popup OverlayPortals while they were still hiding. The form/list now stays mounted under a loading overlay, and AppBar "Save" goes through `DataFormBody.submit()` so child rows persist the values on screen [GS-261].
- `suggestion_dropdown`: typed text is now stored in the in-memory row (`selectedItem`) on change and Save, matching genericsuite-fe. Picking a suggestion still copies related API fields and also writes the form field name [GS-261].
- `suggestion_dropdown`: suggestion rows are read the same way CRUD listings decode `resultset` (already-decoded list, JSON string, or nested `{resultset: [...]}`), so the overlay can show options when the API returns rows [GS-261].
- `suggestion_dropdown`: picking a suggestion no longer copies related-table keys (`_id`, `name`, …) onto the saved row. Only the form field and `autocomplete_fields` are written, matching genericsuite-fe [GS-261].
- Password field shows SHA-256 hash instead of plain text. The initial password must be blank [GS-261].

##### Removed
- `flutter_project_template` directory. Use [genericsuite-mobile-exampleapp](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp) instead [GS-261].

#### [0.4.2] - 2026-04-20

##### Added
- AGENTS.md, GEMINI.md, and CLAUDE.md files to provide context and instructions to AI Coding Assistants [GS-303].
- Add SAST testing [GS-315].
- `select_table` field type in the Flutter CRUD editor: listing and read-only form show the related record description (backend `{field}_description` with client-side cached fallback); create/edit renders a dropdown populated from the related table [GS-259].

##### Changed
- Minor fixes on README.md files
- License changed to MIT [FA-244].
- Update .gitignore to include AI agent directories [GS-303].

##### Fixed
- Improve error handling in create_gs_app.dart and ip_address_service.dart for better stability and fix Flutter web deployment to bootstrap [GS-252].

## GenericSuite Mobile ExampleApp

### Package, Pull Request and Tag

* Pull Request: [https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/pull/2](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/pull/2)
* Tag: [https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/releases/tag/1.0.0+1](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp/releases/tag/1.0.0+1)

### Pull Request Overview

Initial development. Moved from genericsuite-mobile

This is a new submodule split out of `genericsuite-mobile`'s former `flutter_project_template` directory into its own standalone example-app repository, giving the Flutter package a dedicated, independently versioned reference implementation.

Highlights

- Repo split out of `genericsuite-mobile`'s `flutter_project_template` [GS-261].
- Establishes a standalone, independently versioned Flutter example app.

### CHANGELOG.md

#### [1.0.0+1] - 2026-08-30

##### Added
- Moved from `genericsuite-mobile` to `genericsuite-mobile-exampleapp`.

## GenericSuite AI Agent Skills

### Package, Pull Request and Tag

* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-skills/pull/1](https://github.com/tomkat-cr/genericsuite-skills/pull/1)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-skills/pull/3](https://github.com/tomkat-cr/genericsuite-skills/pull/3)
* Tag: [https://github.com/tomkat-cr/genericsuite-skills/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-skills/releases/tag/1.0.0)

### Pull Request Overview

Add gs-app-builder-suite Claude Skills plugin [GS-254]

Introduces the `gs-app-builder-suite` plugin group — an orchestrator skill (`gs-app-builder`) plus specialized builder skills for app scaffolding, config, JSX, menus, endpoints, FastAPI, AI code/tools, and MCP servers — along with an eval suite and a reference-sync mechanism to keep skill docs aligned with the GenericSuite ecosystem docs.

Highlights

- New `gs-app-builder-suite` plugin group with an orchestrator plus 9 specialized builder skills [GS-254].
- `evals/evals.json` suite with runtime-validity assertions [GS-254].
- Reference-sync mechanism (`make sync-references`) to keep skills aligned with GS docs [GS-254].
- `release-notes` skill moved out to the GS Superproject [GS-191].

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Added
- Project ideation and initial development (2026-04-12) [GS-254].
- App-builder skill suite (`gs-app-builder-suite` plugin group) [GS-254]:
  `gs-app-builder` orchestrator (greenfield/brownfield mode detection, app-brief
  interview, checkpointed flow), `app-starter`, `config-builder` (updated),
  `jsx-code-builder` (updated), `menu-builder`, `endpoints-builder`,
  `python-fastapi-code-builder`, `python-ai-code-builder`,
  `python-ai-tools-code-builder`, `jsx-ai-code-builder`, `mcp-builder`.
- `evals/evals.json` suites (all suite skills except config-builder) with runtime-validity assertions, exercised in
  `playground/` [GS-254].
- Reference-sync mechanism: `skills/update-gs-docs` map + script,
  `make sync-references` [GS-254].
- Add SAST testing [GS-315].

##### Changed
- Marketplace plugin group `code-generation-skills` renamed to
  `gs-app-builder-suite`; metadata version 1.1.0 [GS-254].
- README rewritten around the app-builder suite, installation and
  publishing [GS-254].

##### Removed
- `release-notes` skill removed from marketplace, and delete SKILL.md file (moved to GS Superproject directory) [GS-191].

##### Security
- Migrate to Python 3.14 [GS-337].
- Bump Node.js version in .nvmrc to 26 [GS-339].

## GenericSuite Security

### Package, Pull Request and Tag

* Pull Request # 1: [https://github.com/tomkat-cr/genericsuite-security/pull/4](https://github.com/tomkat-cr/genericsuite-security/pull/3)
* Pull Request # 2: [https://github.com/tomkat-cr/genericsuite-security/pull/4](https://github.com/tomkat-cr/genericsuite-security/pull/4)
* Tag: [https://github.com/tomkat-cr/genericsuite-security/releases/tag/1.0.0](https://github.com/tomkat-cr/genericsuite-security/releases/tag/1.0.0)

### Pull Request Overview

Project ideation and initial development

New submodule created in direct response to the 2026-08-04 Keyv/Cacheable npm supply-chain attack. Ships five Claude skills for supply-chain and production-readiness auditing: IOC scanning, an org-wide repo corpus builder, a Docker/container image scanner, a GitHub Actions/package-pinning scanner, and a cross-project weakness/readiness analyzer — plus a registered marketplace plugin.

Highlights

- `supply-chain-ioc-scan` — detect whether a disclosed compromised npm/PyPI package affects this machine or repo tree [GS-339].
- `repo-corpus` → `repo-docker-scanner` → `repo-packages-scanner` — three-phase org-wide repository scanner (corpus manifest, mutable image references, unpinned Actions/dependencies).
- `project-weakness-analysis` — production-readiness and security-risk scoring across many projects, with a `--profile genericsuite` mode for this ecosystem's own non-negotiables.
- Hardened, hostile-input-safe cloning (hooks/LFS/credential prompts disabled, symlink-escape guarded).

### CHANGELOG.md

#### [1.0.0] - 2026-08-30

##### Added
- Project ideation and initial development as a response to the Keyv and Cacheable NPM supply chain attack (2026-08-04): https://socket.dev/supply-chain-attacks/keyv-and-cacheable-compromise [GS-339].
- New skill `supply-chain-ioc-scan`: use when a compromised npm/PyPI package or supply-chain worm is disclosed and you must determine whether this machine or repo tree is affected. Developed on 2026-08-04 due to the Shai-Hulud keyv and cacheable compromise.
- New skill `repo-corpus`:
  - `repo-corpus` skill (phase 1 of the org-wide repository scanner design): enumerates an org or user via `gh`, clones with hardened flags, and emits a `corpus.json` manifest. Ships `scripts/_walk.py` (shared walking with prune counting and unreadable-path tracking) and a self-test that proves the clone hardening holds.
  - `build_corpus.py --branch NAME` pins the corpus to one branch across every repository, checking it out as the working tree scanners walk. Repositories without that branch are recorded as `skipped` with a reason and summarised in `warnings[]`, never dropped and never counted as failures. Manifest entries gain `checked_out` (the branch on disk) alongside `default_branch` (the repository's own default).
- New skill `repo-docker-scanner`:
  - `repo-docker-scanner --resolve`: resolves an unpinned tag to its real digest via an anonymous registry bearer token (stdlib `urllib` only, no docker/skopeo dependency), producing a copy-pasteable `image:tag@sha256:…` suggestion per finding. Registry-agnostic — parses each registry's own `WWW-Authenticate` challenge rather than hardcoding Docker Hub's realm, verified live against both Docker Hub and ghcr.io.
  - `repo-docker-scanner` report.md now states, right after the summary, the exact command that produced it and the full list of repositories/branches/HEAD commits actually analyzed (also in findings.json as `scan_command` and `repos_analyzed`).
  - Design spec and phase 1 implementation plan under `docs/superpowers/`.
  - `repo-docker-scanner` skill (phase 2): detects mutable container image references across a corpus and prioritises them by execution context. Dockerfiles are parsed rather than grepped; YAML is read structurally by a stdlib-only indentation reader. Emits `report.md`, `findings.json` and SARIF 2.1.0, with a checked-in baseline for accepted risk and `probe.py` for adversarial verification.
- New skill `repo-packages-scanner`:
  - `repo-packages-scanner` skill (phase 3, completing the org-wide repository scanner design): detects unpinned GitHub Actions (`uses:` not pinned to a 40-hex commit SHA, including `docker://` and reusable-workflow calls), floating npm/PyPI/Poetry/PEP-621 ranges, missing lockfiles, `npm install`/`yarn install` used in CI instead of `npm ci`, `curl | bash` and other unpinned remote code execution, and Go/Rust/Ruby pinning gaps. Ships `report.md`, `findings.json`, and SARIF 2.1.0, all three built with the scan command, the exact repos/branches/commits analyzed, and a P0/P1/P2 legend generated from `policy/packages.json`'s `priority_rules`. `--resolve` optionally enriches unpinned Actions with owner/archived status via `gh api`.
- New skill `project-weakness-analysis`: decides whether projects are ready and safe to run in production, scoring production-readiness and auditing security weaknesses across many projects at once.
  - Five input modes — a root directory (`--root`), an explicit list (`--projects`), an existing corpus (`--corpus`), a GitHub org or user (`--org`/`--user`), and an optional read-only project registry table (`--db`, Supabase PostgREST or psql).
  - Two independent verdict axes, never averaged: a readiness tier (`production-ready` / `needs-work` / `not-ready` / `unknown`) and a security risk level (`critical` … `none`). `unknown` blocks — an unscanned project is not a safe one.
  - A deterministic pre-pass grounds two sonnet agents per project; a haiku agent writes the cross-project rollup.
  - A re-audit loop: a second run verifies every prior finding as `resolved` / `partial` / `open`, and no prior finding is ever dropped.
  - Output under `./insights`: `WEAKNESS-REPORT.md`, `insights.json`, a flat `insights-table.json` / `insights-table.csv` projection, `security-audit.json`, `projects/<slug>.json`, and `findings.sarif`.
  - Optional `--profile genericsuite` checks the ecosystem's non-negotiables (scrypt-only hashing, the standard result shape, parameterized SQL, `is_safe_url()` / `is_safe_local_path()` guards).
- `.claude-plugin/marketplace.json` registers the new skills: `supply-chain-security`, `repo-corpus`, `repo-docker-scanner`, `repo-packages-scanner`, and `project-weakness-analysis`; the plugin description now covers production-readiness analysis alongside supply-chain security.

##### Changed
- `repo-corpus` and the two planned scanners consume a corpus rather than enumerating repositories themselves, so single-repo lint mode and org-wide audit share one code path.

##### Fixed
- `repo-docker-scanner`'s "Priority tiers explained" section described the wrong scanner's rules; replaced with a legend generated from `policy/images.json`'s own `priority_rules`, so the text shown can never again describe rules that are not the ones actually applied.
- `repo-docker-scanner` was not tiering infrastructure-as-code templates as P0 unless their path happened to match an existing glob. CloudFormation is now detected by content (`AWSTemplateFormatVersion`, or a `Type: AWS::…` resource block) and tiered P0 regardless of where it lives in the tree.
- `repo-docker-scanner` was lowercasing part of template-composed references (class `unresolved`) when reporting them. Unresolved references are now reported and inventoried verbatim.
- `repo-docker-scanner` Dockerfile discovery and its `**/Dockerfile*` priority rule now match by prefix and case-insensitively, so a missed Dockerfile can no longer silently drop a whole file's worth of `FROM` lines from the report.
- `run_corpus.sh` crashed on macOS's bash 3.2 (empty-array expansion under `set -u`) and then reported the crash as `PARTIAL CORPUS`. It now uses positional parameters, and refuses to report any corpus outcome without a manifest to back it.
- The self-test built fixture repositories with `git init -b`, which requires git 2.28; macOS ships older. Fixture commands are now checked, and a preflight reports an unusable environment as a setup failure.
- Clone failures recorded git's trailing boilerplate rather than the line naming the cause.
- `.claude-plugin/marketplace.json` registered `./skills/supply-chain-security`, a path that does not exist; corrected to `./skills/supply-chain-ioc-scan`. A self-test assertion now fails if any registered skill path is missing from disk.

##### Security
- `build_corpus.py` warns when the repository list may be truncated (count hits `--limit`, or lands on an exact multiple of gh's 100-per-page size). A capped list is the one incompleteness a manifest cannot express as a failure.
- The self-test is hermetic with respect to the developer's git configuration; a global `core.hooksPath` would otherwise have made the central hook-hardening assertion pass for the wrong reason.
- Cloned repositories are treated as hostile input: hooks, LFS smudge/process filters and interactive credential prompts are disabled at clone time; clones are staged and promoted only on success; repository names are validated before use as path components; and file walking never follows a symlink out of its root.
- Migrate to Python 3.14 [GS-337].
- Bump Node.js version in .nvmrc to 26 [GS-339].
