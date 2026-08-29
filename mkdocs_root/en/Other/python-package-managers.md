# Python Package Managers

# From pipenv to uv or poetry

Old versions of GenericSuite used "pipenv" as the Python package and dependency management tool. Now, we're migrating to "uv" as the default tool. Poetry is also supported.

To convert an application from **pipenv** to **uv** or **poetry**, follow these steps:

1. Go to the project root directory, initialize "uv" or "poetry" and add GenericSuite dependencies:

For `uv`:

```bash
# Initialize "uv" and add GenericSuite dependencies

uv init

# NOTE: modify the pyproject.toml file to add the "name", "version", and "description" fields.
nano pyproject.toml

# Add the GenericSuite backend and AI dependencies

uv add genericsuite-be genericsuite-be-ai

# Add the backend framework dependencies

uv add chalice
#      o
uv add fastapi fastapi-cors mangum "uvicorn[standard]" python-multipart
#      o
uv add flask flask-cors gunicorn python-multipart

# Add the development dependencies

uv add --dev pytest coverage cfn-lint
```

For `poetry`:


```bash
# Initialize "poetry" and add GenericSuite dependencies

poetry init

# NOTE: modify the pyproject.toml file to add the "name", "version", and "description" fields.
nano pyproject.toml

# Add the GenericSuite backend and AI dependencies

poetry add genericsuite-be genericsuite-be-ai

# Add the backend framework dependencies

poetry add chalice
#      o
poetry add fastapi fastapi-cors mangum "uvicorn[standard]" python-multipart
#      o
poetry add flask flask-cors gunicorn python-multipart

# Add the development dependencies

poetry add --dev pytest coverage cfn-lint
```

2. Reinstall GS BE Scripts

```bash
npm install genericsuite-be-scripts@latest
```

3. Update the `Makefile` file changing every `pipenv` reference to `bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh` + the Makefile tag:

For example:

Replace:
    ```
    npm install
    ```

With:
    ```
    bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh install
    ```

Here's the complete example:

```makefile
install:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh install
	npm install

install_dev:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh install_dev
	npm install

update:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh update
	npm update

update_dev:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh update_dev
	npm update

locked_dev:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh locked_dev

locked_install:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh locked_install

lock:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh lock

requirements:
	bash node_modules/genericsuite-be-scripts/scripts/aws/run_aws.sh requirements

			.
			.
			.

clean_rm:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh clean_rm

			.
			.
			.

lint:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh lint

types:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh types

coverage:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh coverage

format:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh format

format_check:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh format_check

pycodestyle:
	bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh pycodestyle
```

4. Search for every non-implemented reference to `pipenv` in the `Makefile` file and replace it with `uv` or `poetry`. The non-implemented references are those different from: `install`, `install_dev`, `update`, `update_dev`, `locked_dev`, `locked_install`, `lock`, `requirements`, `clean_rm`, `lint`, `types`, `coverage`, `format`, `format_check`, 

5. Search for every reference to "pipenv" in the *.sh files and replace it with:

```bash
PEM_TOOL=uv
    .
    .
# Replace "pipenv" with "${PEM_TOOL}"
```

6. Search for every reference to `pipenv` in the `package.json` file and replace it with `uv` or `poetry`.

7. Update the `.env` and `.env.example` files adding the reference to the `PEM_TOOL` variable and removing the comment `#` from the line that contains the dependency management tool that you want to use:

```env
# Python package and dependency management tool (uv, pipenv, and poetry), default to "uv"
# PEM_TOOL=pipenv
# PEM_TOOL=uv
# PEM_TOOL=poetry
```
