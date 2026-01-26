# GenericSuite AI para ReactJS

![gs_ai_logo_circle.png](../../../assets/images/gs_ai_logo_circle.png)

GenericSuite AI (versión frontend) cuenta con herramientas de IA ChatBot, un editor CRUD personalizable, una interfaz de inicio de sesión y una suite de herramientas para iniciar el desarrollo de tu App de IA.

## Características

- **Herramientas de IA ChatBot:** para implementar conversaciones de chatbot basadas en PLN (Procesamiento de Lenguaje Natural), LLM (Modelos de Lenguaje Grande) y otras tecnologías de IA como ChatGPT.
- **Editor CRUD personalizable:** código CRUD básico (Crear-Leer-Actualizar-Eliminar) que puede parametrizarse y ampliarse mediante archivos de configuración JSON. No es necesario reescribir el código para cada editor de tabla.
- **Menú personalizable:** el menú y los endpoints pueden parametrizarse y ampliarse mediante archivos de configuración JSON en el lado del backend. La API proporcionará la estructura del menú y la verificación de seguridad basada en el grupo de seguridad del usuario, y GenericSuite dibujará el menú y las opciones disponibles.
- **Interfaz de inicio de sesión personalizable:** Adapta fácilmente la página de inicio de sesión para que coincida con la identidad de tu marca con el logotipo de la aplicación.
- **Scripts de Desarrollo y Producción:** Comandos rápidos para iniciar el desarrollo o compilar tu aplicación para entornos de QA, staging y producción en AWS.
- **Pruebas con Jest:** Viene preconfigurado con Jest para ejecutar pruebas, incluyendo una prueba inicial para el componente `<App />`.
- **Inclusión de archivos esenciales:** `.env.example` para la configuración de variables de entorno, `Makefile` para acortar operaciones frecuentes, `vite.config.mjs`, `webpack.config.js` y `config-overrides.js` para ejecutar la App localmente con `Webpack` o `react-app-rewired`, `scripts` con scripts de desarrollo y producción, y `CHANGELOG.md` para el seguimiento de cambios entre versiones.

La compañera perfecta para esta solución frontend es la [versión de backend de The GenericSuite AI](../../Backend-Development/GenericSuite-AI/index.md).

GenericSuite AI (versión frontend) se basa en [The GenericSuite para ReactJS (versión frontend)](../GenericSuite-Core/index.md).

## Requisitos previos

Instala las mismas herramientas descritas en [GenericSuite para ReactJS (versión frontend)](../GenericSuite-Core/index.md#pre-requisites) sección `Pre-requisites`.

## Inicio

Para empezar con GenericSuite AI, siga estos pasos simples:

### Crear repositorios Git

Los mismos pasos descritos en [GenericSuite para ReactJS (versión frontend)](../GenericSuite-Core/index.md#create-the-git-repositories) `Getting started > Create Git repositories` sección.

### Iniciar tu proyecto

Los mismos pasos descritos en [GenericSuite para ReactJS (versión frontend)](../GenericSuite-Core/index.md#initiate-your-project) `Getting started > Initiate your project` sección.

### Instalar paquetes de GenericSuite AI

```bash
npm install genericsuite genericsuite-ai
```

### Instalar dependencias de desarrollo adicionales

Los mismos pasos descritos en [GenericSuite para ReactJS (versión frontend)](../GenericSuite-Core/index.md#install-additional-development-dependencies) `Getting started > Install additional development dependencies` sección.

### Preparar los archivos de configuración

Copiar la plantilla desde `node_modules/genericsuite-ai`:

```bash
cp node_modules/genericsuite-ai/.env.example ./.env
```

Y configure las variables según sus necesidades:

* Asigne las mismas variables descritas en la sección `Getting started > Prepare the Configuration Files` del [GenericSuite para ReactJS (versión frontend)](../GenericSuite-Core/index.md#prepare-the-configuration-files).

* Asigne los parámetros adicionales `AWS_*` con sus datos de AWS (utilizados por aws_deploy_to_s3.sh y change_env_be_endpoint.sh). Necesitará una cuenta de AWS.

Para más información, consulte los comentarios de cada variable en el archivo [.env.example](https://github.com/tomkat-cr/genericsuite-fe-ai/blob/main/.env.example).

#### Otros parámetros

* `REACT_APP_USE_AXIOS`: "1" = usar axios para enviar archivos, "0" = usar fetch en su lugar. Por defecto es "1".

### Preparar el Makefile

Copiar la plantilla de `Makefile` desde `node_modules/genericsuite-ai`:

```bash
cp node_modules/genericsuite-ai/Makefile ./Makefile
```

### Cambiar Scripts en Package.json

Los mismos pasos descritos en [GenericSuite para ReactJS (versión frontend)](../GenericSuite-Core/index.md#change-scripts-in-packagejson) `Getting started > Change Scripts in Package.json` sección.


### Crear el archivo de versión

Crear el archivo `version.txt` con la versión de la App:

```bash
vi ./version.txt
# o
# code ./version.txt
```

Añada el número de versión (p. ej. `1.0.0`) y guarde el archivo.


## Estructura de la App

La estructura recomendada del repositorio de desarrollo de la App es la misma descrita en [GenericSuite para ReactJS (versión frontend)](../GenericSuite-Core/index.md#app-structure) sección `App structure`.


## Configurar el proyecto

Haz clic [aquí](../../Configuration-Guide/index.md) para obtener más información sobre cómo configurar el proyecto.

## Ejemplos de código y archivos de configuración JSON

El menú principal, los endpoints de la API y las configuraciones del editor CRUD se definen en los archivos de configuración JSON.

Puede encontrar ejemplos de configuraciones y de cómo crear una App en la guía [Guía de Creación y Configuración de la Aplicación de GenericSuite](../../Configuration-Guide/index.md).

## Uso

### Iniciar el servidor de desarrollo

Para iniciar el servidor de desarrollo:

```bash
make run
```

### Desplegar QA

Consulte la [Guía de Despliegue](../deployment.md) para más detalles.