# Special Installations

## Node global version

To set the default `Node` version to be used by `nvm`:

1. Run the following command in your terminal, replacing `<version>` with the Node version number you want to set as the default: `nvm alias default <version>`. For example, to use `Node 20`:

```sh
nvm alias default 20
```

2. Create a `.nvmrc` file in your project root directory with the Node version in its content, so the new version will be set when you run `nvm use` or when a Terminal is opened in your favorite code editor (e.g. Visual Studio Code or Cursor.sh). For example:

File: `.nvmrc`

```
20
```

3. Create a `.nvmrc` file in your user's home directory with the Node version and add the commands on the shell starter script, so the new version will be set when a new Terminal window is opened. For example:

MacOS:

File: `/Users/$USER/.zshrc` or `/Users/$USER/.bashrc`

Linux:

File: `/home/$USER/.bashrc` or `/home/$USER/.profile`

Add this lines:

```sh
# To set the Node version when new Terminal window is opened
if [ -f "./.nvmrc" ]; then
    nvm use
fi
```

And create the `.nvmrc` file mentioned earlier in the user's home directory: `/Users/$USER` or `/home/$USER`.


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

## Frontend

### Install from Git repositories

From the `main` branch:

```bash
npm install tomkat-cr/genericsuite-fe
```
```bash
npm install tomkat-cr/genericsuite-fe-ai
```

From a specific branch:

```bash
npm uninstall generisuite
npm install tomkat-cr/genericsuite-fe#branch_name
```
```bash
npm uninstall generisuite-ai
npm install tomkat-cr/genericsuite-fe-ai#branch_name
```

E.g.

```bash
npm uninstall genericsuite && npm install tomkat-cr/genericsuite-fe#develop
```
```bash
npm uninstall genericsuite-ai && npm install tomkat-cr/genericsuite-fe-ai#develop
```

Or all together:

```bash
npm uninstall genericsuite genericsuite-ai && npm install tomkat-cr/genericsuite-fe#develop tomkat-cr/genericsuite-fe-ai#develop
```

**IMPORTANT**:

* When you've made changes to any of the GenericSuite frontend packages code, perform a `make pre-publish` to rebuild the `dist` directory files before the Git `commit` and `push`, because those files are required for `npm install` to work. Then re-install the changed package in the parent project (your app) using the `npm install tomkat-cr/genericsuite-fe` or `npm install tomkat-cr/genericsuite-fe-ai` command.