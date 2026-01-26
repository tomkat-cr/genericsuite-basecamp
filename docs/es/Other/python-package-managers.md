# Gestores de paquetes de Python

# De pipenv a uv o poetry

Las versiones antiguas de GenericSuite usaban "pipenv" como la herramienta de gestión de paquetes y dependencias de Python. Ahora, estamos migrando a "uv" como la herramienta predeterminada. Poetry también es compatible.

Para convertir una aplicación de **pipenv** a **uv** o **poetry**, siga estos pasos:

1. Vaya al directorio raíz del proyecto, inicialice "uv" o "poetry" y agregue las dependencias de GenericSuite:

Para `uv`:

```bash
# Inicializar "uv" y agregar dependencias de GenericSuite

uv init

# NOTA: modifique el archivo pyproject.toml para añadir los campos "name", "version" y "description".
nano pyproject.toml

# Añadir las dependencias de backend y AI de GenericSuite

uv add genericsuite-be genericsuite-be-ai

# Añadir las dependencias del framework de backend

uv add chalice
#      o
uv add fastapi fastapi-cors mangum "uvicorn[standard]" python-multipart
#      o
uv add flask flask-cors gunicorn python-multipart

# Añadir las dependencias de desarrollo

uv add --dev pytest coverage cfn-lint
```

Para `poetry`:

```bash
# Inicializar "poetry" y añadir dependencias de GenericSuite

poetry init

# NOTA: modifique el archivo pyproject.toml para añadir los campos "name", "version" y "description".
nano pyproject.toml

# Añadir las dependencias de backend y AI de GenericSuite

poetry add genericsuite-be genericsuite-be-ai

# Añadir las dependencias del framework de backend

poetry add chalice
#      o
poetry add fastapi fastapi-cors mangum "uvicorn[standard]" python-multipart
#      o
poetry add flask flask-cors gunicorn python-multipart

# Añadir las dependencias de desarrollo

poetry add --dev pytest coverage cfn-lint
```

2. Reinstale GS BE Scripts

```bash
npm install genericsuite-be-scripts@latest
```

3. Actualice el archivo `Makefile` cambiando cada referencia a `pipenv` por `bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh` + la etiqueta de Makefile:

Por ejemplo:

Reemplace:
    ```
    npm install
    ```

Con:
    ```
    bash node_modules/genericsuite-be-scripts/scripts/run_pem.sh install
    ```

Aquí tienes el ejemplo completo:

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

4. Busque todas las referencias no implementadas a `pipenv` en el archivo `Makefile` y reemplácelas por `uv` o `poetry`. Las referencias no implementadas son aquellas diferentes de: `install`, `install_dev`, `update`, `update_dev`, `locked_dev`, `locked_install`, `lock`, `requirements`, `clean_rm`, `lint`, `types`, `coverage`, `format`, `format_check`, 

5. Busque todas las referencias a "pipenv" en los archivos *.sh y reemplácelas por:

```bash
PEM_TOOL=uv
    .
    .
# Reemplace "pipenv" por "${PEM_TOOL}"
```

6. Busque todas las referencias a `pipenv` en el archivo `package.json` y reemplácelas por `uv` o `poetry`.

7. Actualice los archivos `.env` y `.env.example` añadiendo la referencia a la variable `PEM_TOOL` y eliminando el comentario `#` de la línea que contiene la herramienta de gestión de dependencias que desea usar:

```env
# Python package and dependency management tool (uv, pipenv, and poetry), default to "uv"
# PEM_TOOL=pipenv
# PEM_TOOL=uv
# PEM_TOOL=poetry
```