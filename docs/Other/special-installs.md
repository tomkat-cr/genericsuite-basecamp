# Special Installations

## Frontend

### Install from Git repositories

To install any of the the frontend solutions (Core, AI, etc) from a specific branch in the Git repositories, e.g. "branch_x":

* Preparation steps:

Edit the `package.json` file in the project root directory and add these lines:

```json
"overrides": {
    "genericsuite": {
      "main": "dist/index.js"
    },
    "genericsuite-ai": {
      "main": "dist/index.js"
    }
}
```

Re-generate the `package-lock.json` file:

```bash
make lock
```

Install additional dependencies:

```bash
npm install \
    react-router-dom
```
```bash
npm install --save-dev \
    assert \
    os-browserify \
    crypto-browserify \
    stream-browserify \
    vm-browserify \
    tty-browserify \
    constants-browserify \
    url
```

* Run the corresponding install command(s):

```bash
npm install ../genericsuite-fe
cd ./node_modules/genericsuite && npm install && make build && cd ../..
```
```bash
npm install ../genericsuite-fe-ai
cd ./node_modules/genericsuite-ai && npm install && make build && cd ../..
```

Run the `link` commands:

```bash
npm link ../genericsuite-fe/node_modules/react
npm link ../genericsuite-fe/node_modules/react-router-dom
```
```bash
npm link ../genericsuite-fe-ai/node_modules/react
npm link ../genericsuite-fe-ai/node_modules/react-router-dom
```

### Install from local directory

To install any of the the backend solutions (Core, AI, etc) from a local directory:

* Follow the same preparation steps as the [Install from Git repositories](./special-installs.md#install_from_git_repositories)

* Run the corresponding install command(s):

```bash
npm install ../genericsuite-fe
cd ../node_modules/genericsuite && npm install && make build & cd ../..
```
```bash
npm install ../genericsuite-fe-ai
cd ../node_modules/genericsuite && npm install && make build & cd ../..
```

### Post use procedure

Once finished working with the Git or Local libraries, remember to reinstall from the NPMJS repositories and revert the changes made:

* Post-use steps:

Edit the `package.json` file in the project root directory and remove these lines:

```json
"overrides": {
    "genericsuite": {
      "main": "dist/index.js"
    },
    "genericsuite-ai": {
      "main": "dist/index.js"
    }
}
```

Uninstall the additional dependencies:

```bash
npm uninstall \
    react-router-dom
```
```bash
npm uninstall \
    assert \
    os-browserify \
    crypto-browserify \
    stream-browserify \
    vm-browserify \
    tty-browserify \
    constants-browserify \
    url
```

Run the corresponding install command(s):

```bash
npm uninstall genericsuite && npm install genericsuite
```
```bash
npm uninstall genericsuite-ai && npm install genericsuite-ai
```

## Backend

### Install from Git repositories

To install any of the the backend solutions (Core, AI, etc) from a specific branch in the Git repositories, e.g. "branch_x":

Pip
```bash
pip install git+https://github.com/tomkat-cr/genericsuite-be@branch_x
```
```bash
pip install git+https://github.com/tomkat-cr/genericsuite-be-ai@branch_x
```

Pipenv
```bash
pipenv install git+https://github.com/tomkat-cr/genericsuite-be@branch_x
```
```bash
pipenv install git+https://github.com/tomkat-cr/genericsuite-be-ai@branch_x
```

Poetry
```bash
poetry add git+https://github.com/tomkat-cr/genericsuite-be@branch_x
```
```bash
poetry add git+https://github.com/tomkat-cr/genericsuite-be-ai@branch_x
```

To install the backend scripts from a specific branch in the Git repositories, e.g. "branch_x":

```bash
npm install tomkat-cr/genericsuite-be-scripts#branch_x
```

### Install from local directory

To install any of the the backend solutions (Core, AI, etc) from a local directory:

Pip
```bash
pip install ../genericsuite-be
```
```bash
pip install ../genericsuite-be-ai
```

Pipenv
```bash
pipenv install ../genericsuite-be
```
```bash
pipenv install ../genericsuite-be-ai
```

Poetry
```bash
poetry add ../genericsuite-be
```
```bash
poetry add ../genericsuite-be-ai
```

To install the backend scripts from a local directory:

```bash
npm install ../genericsuite-be-scripts
```
