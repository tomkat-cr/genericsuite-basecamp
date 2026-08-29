# Instalación de GenericSuite

## Requisitos previos

### Bash

Si planeas usar un entorno de desarrollo con Windows, debes instalar `Git Bash` desde el paquete de [Git for Windows](https://gitforwindows.org/). También necesitarás instalar la utilidad [Make](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows).

Si planeas usar un entorno de desarrollo con MacOS o Linux, la shell bash y la utilidad Make ya están instaladas.

### NodeJS

Se recomienda usar [nvm](https://github.com/nvm-sh/nvm) (Node Version Manager) para gestionar múltiples versiones de [NodeJS](https://nodejs.org).

Para establecer la versión predeterminada de `NodeJS` que será utilizada por `nvm`:

1. Ejecuta el siguiente comando en tu terminal, sustituyendo `<version>` por el número de versión de Node.js que deseas establecer como predeterminada: `nvm alias default <version>`. Por ejemplo, para usar **Node.js 26**:

```sh
nvm alias default 26
```

2. Crea un archivo `.nvmrc` en el directorio raíz de tu proyecto con la versión de Node.js en su contenido, de modo que la nueva versión se establezca cuando ejecutes `nvm use` o cuando se abra una Terminal en tu editor de código favorito (p. ej. Visual Studio Code o Cursor.sh). Por ejemplo:

Archivo: `.nvmrc`

```
26
```

3. Crea un archivo `.nvmrc` en el directorio home de tu usuario con la versión de Node.js y añade los comandos en el script de inicio de la shell, para que la nueva versión se establezca cuando se abra una nueva ventana de Terminal. Por ejemplo:

MacOS:

Archivo: `/Users/$USER/.zshrc` o `/Users/$USER/.bashrc`

Linux:

Archivo: `/home/$USER/.bashrc` o `/home/$USER/.profile`

Añade estas líneas:

```sh
# Para establecer la versión de Node.js cuando se abra una nueva ventana de Terminal
if [ -f "./.nvmrc" ]; then
    nvm use
fi
```

Y crea el archivo `.nvmrc` mencionado anteriormente en el directorio home del usuario: `/Users/$USER` o `/home/$USER`.

## Python

Para instalar [Python](https://www.python.org), se recomienda usar [pyenv](https://github.com/pyenv/pyenv) que permite gestionar múltiples versiones de Python.

Existe un script [install_dev_tools.sh](https://github.com/tomkat-cr/genericsuite-be-scripts/blob/main/scripts/install_dev_tools.sh) en el repositorio [genericsuite-be-scripts](https://github.com/tomkat-cr/genericsuite-be-scripts) que facilita la instalación de `pyenv` y otras dependencias necesarias, como [uv](https://docs.astral.sh/uv/getting-started/installation/), [poetry](https://python-poetry.org/docs/), o [pipenv](https://pipenv.pypa.io/en/latest/) para la gestión de dependencias de Python.


## Backend

### Instalar desde PyPi

Pip
```bash
pip install genericsuite
```
```bash
pip install genericsuite-ai
```

Uv
```bash
uv add genericsuite
```
```bash
uv add genericsuite-ai
```

Poetry
```bash
poetry add genericsuite
```
```bash
poetry add genericsuite-ai
```

Pipenv
```bash
pipenv install genericsuite
```
```bash
pipenv install genericsuite-ai
```

Para instalar los scripts del backend de GenericSuite:

```bash
npm install -D genericsuite-be-scripts
```

### Instalar desde repositorios Git

Para instalar cualquiera de las soluciones de backend (Core, AI, etc) desde una rama específica en los repositorios Git, por ejemplo, "branch_x":

Pip
```bash
pip install git+https://github.com/tomkat-cr/genericsuite-be@branch_x
```
```bash
pip install git+https://github.com/tomkat-cr/genericsuite-be-ai@branch_x
```

Uv
```bash
uv add git+https://github.com/tomkat-cr/genericsuite-be@branch_x
```
```bash
uv add git+https://github.com/tomkat-cr/genericsuite-be-ai@branch_x
```

Poetry
```bash
poetry add git+https://github.com/tomkat-cr/genericsuite-be@branch_x
```
```bash
poetry add git+https://github.com/tomkat-cr/genericsuite-be-ai@branch_x
```

Pipenv
```bash
pipenv install git+https://github.com/tomkat-cr/genericsuite-be@branch_x
```
```bash
pipenv install git+https://github.com/tomkat-cr/genericsuite-be-ai@branch_x
```

Para instalar los scripts del backend desde una rama específica en los repos Git, por ejemplo, "branch_x":

```bash
npm install -D tomkat-cr/genericsuite-be-scripts#branch_x
```

### Instalar desde directorio local

Para instalar cualquiera de las soluciones de backend (Core, AI, etc) desde un directorio local:

Pip
```bash
pip install ../genericsuite-be
```
```bash
pip install ../genericsuite-be-ai
```

Uv
```bash
uv add ../genericsuite-be
```
```bash
uv add ../genericsuite-be-ai
```

Poetry
```bash
poetry add ../genericsuite-be
```
```bash
poetry add ../genericsuite-be-ai
```

Pipenv
```bash
pipenv install ../genericsuite-be
```
```bash
pipenv install ../genericsuite-be-ai
```

Para instalar los scripts del backend desde un directorio local:

```bash
npm install -D ../genericsuite-be-scripts
```

## Frontend

### Instalar desde NPMJS

```bash
npm install genericsuite
```
```bash
npm install genericsuite-ai
```
```bash
npm install -D genericsuite-fe-scripts
```

### Instalar desde repositorios Git

Desde la rama `main`:

```bash
npm install tomkat-cr/genericsuite-fe
```
```bash
npm install tomkat-cr/genericsuite-fe-ai
```
```bash
npm install -D tomkat-cr/genericsuite-fe-scripts
```

Desde una rama específica:

```bash
npm uninstall generisuite
npm install tomkat-cr/genericsuite-fe#branch_name
```
```bash
npm uninstall generisuite-ai
npm install tomkat-cr/genericsuite-fe-ai#branch_name
```
```bash
npm uninstall generisuite-fe-scripts
npm install -D tomkat-cr/genericsuite-fe-scripts#branch_name
```

Ej.

```bash
npm uninstall genericsuite && npm install tomkat-cr/genericsuite-fe#develop
```
```bash
npm uninstall genericsuite-ai && npm install tomkat-cr/genericsuite-fe-ai#develop
```
```bash
npm uninstall generisuite-fe-scripts && npm install -D tomkat-cr/genericsuite-fe-scripts#develop
```

O juntos:

```bash
npm uninstall genericsuite genericsuite-ai && npm install tomkat-cr/genericsuite-fe#develop tomkat-cr/genericsuite-fe-ai#develop
```

**IMPORTANTE**:

* Cuando hayas realizado cambios en cualquiera de los paquetes frontend de GenericSuite, realiza un `make pre-publish` para reconstruir los archivos del directorio `dist` antes del `commit` y `push` en Git, ya que esos archivos son necesarios para que `npm install` funcione. Luego vuelve a instalar el paquete cambiado en el proyecto padre (tu aplicación) usando el comando `npm install tomkat-cr/genericsuite-fe` o `npm install tomkat-cr/genericsuite-fe-ai`.