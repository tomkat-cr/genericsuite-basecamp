# Instalación de GenericSuite

## Versión global de Node

Para establecer la versión predeterminada de `Node` que será utilizada por `nvm`:

1. Ejecute el siguiente comando en su terminal, sustituyendo `<version>` por el número de versión de Node que desea establecer como predeterminado: `nvm alias default <version>`. Por ejemplo, para usar `Node 20`:

```sh
nvm alias default 20
```

2. Cree un archivo `.nvmrc` en la raíz de su proyecto con la versión de Node en su contenido, para que la nueva versión se establezca cuando ejecute `nvm use` o cuando se abra una Terminal en su editor de código favorito (p. ej. Visual Studio Code o Cursor.sh). Por ejemplo:

Archivo: `.nvmrc`

```
20
```

3. Cree un archivo `.nvmrc` en el directorio home del usuario con la versión de Node y agregue los comandos en el script de inicio de la shell, para que la nueva versión se establezca cuando se abra una nueva ventana de Terminal. Por ejemplo:

macOS:

Archivo: `/Users/$USER/.zshrc` o `/Users/$USER/.bashrc`

Linux:

Archivo: `/home/$USER/.bashrc` o `/home/$USER/.profile`

Agregue estas líneas:

```sh
# To set the Node version when new Terminal window is opened
if [ -f "./.nvmrc" ]; then
    nvm use
fi
```

Y cree el archivo `.nvmrc` mencionado anteriormente en el directorio home del usuario: `/Users/$USER` o `/home/$USER`.


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

Para instalar los scripts de backend de GenericSuite:

```bash
npm install genericsuite-be-scripts
```

### Instalar desde repositorios Git

Para instalar cualquiera de las soluciones de backend (Core, AI, etc) desde una rama específica en los repositorios Git, p. ej. "branch_x":

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

Para instalar los scripts de backend desde una rama en los repositorios Git, p. ej. "branch_x":

```bash
npm install tomkat-cr/genericsuite-be-scripts#branch_x
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

Para instalar los scripts de backend desde un directorio local:

```bash
npm install ../genericsuite-be-scripts
```

## Frontend

### Instalar desde NPMJS

```bash
npm install genericsuite
```
```bash
npm install genericsuite-ai
```

### Instalar desde repositorios Git

Desde la rama `main`:

```bash
npm install tomkat-cr/genericsuite-fe
```
```bash
npm install tomkat-cr/genericsuite-fe-ai
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

Ej.

```bash
npm uninstall genericsuite && npm install tomkat-cr/genericsuite-fe#develop
```
```bash
npm uninstall genericsuite-ai && npm install tomkat-cr/genericsuite-fe-ai#develop
```

O todo junto:

```bash
npm uninstall genericsuite genericsuite-ai && npm install tomkat-cr/genericsuite-fe#develop tomkat-cr/genericsuite-fe-ai#develop
```

**IMPORTANTE**:

* Cuando haya realizado cambios en cualquiera de los paquetes frontend de GenericSuite, ejecute `make pre-publish` para reconstruir los archivos del directorio `dist` antes del `commit` y `push` en Git, ya que esos archivos son necesarios para que `npm install` funcione. Luego vuelva a instalar el paquete modificado en el proyecto padre (su aplicación) usando el comando `npm install tomkat-cr/genericsuite-fe` o `npm install tomkat-cr/genericsuite-fe-ai`.