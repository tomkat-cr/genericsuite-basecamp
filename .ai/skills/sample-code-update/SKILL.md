---
name: sample-code-update
description: Update ExampleApp and FastAPI Template sample code to use the latest GenericSuite packages
disable-model-invocation: true
---

Guide through updating the sample code (ExampleApp and FastAPI Template) to use the latest GenericSuite packages.

Steps:
1. Run `make sample_code_prepare` to execute the automated preparation script
2. Check for any errors in the output and report them to the user
3. If successful, show which packages were updated by running:
   - `git diff docs/code/exampleapp/ | grep "^[+-].*version\|genericsuite" | head -40`
   - `git diff docs/code/fastapitemplate/ | grep "^[+-].*version\|genericsuite" | head -40`
4. Ask the user if they want to:
   - Run `make exampleapp-install` to test the updated dependencies
   - Run `make fastapitemplate-install` to test the updated dependencies
5. If the user confirms, run the install commands and report any dependency errors
6. Summarize what changed and suggest commit message following the project convention (e.g., `Change: update all sample code packages [GS-NNN]`)
