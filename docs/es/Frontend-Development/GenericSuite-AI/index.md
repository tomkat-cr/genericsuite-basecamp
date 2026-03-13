# GenericSuite AI para ReactJS

![gs_ai_logo_circle.png](../../../assets/images/gs_ai_logo_circle.png)

GenericSuite AI (versión frontend) incluye herramientas de ChatBot IA, un editor CRUD personalizable, una interfaz de inicio de sesión y una suite de herramientas para acelerar el desarrollo de tu aplicación de IA.

## Características

- **Herramientas de IA ChatBot:** para implementar conversaciones de chatbot basadas en PLN (Procesamiento del Lenguaje Natural), LLM (Modelos de Lenguaje a Gran Escala) y otras tecnologías de IA como ChatGPT.
- **Editor CRUD personalizable:** código CRUD central (Crear-Leer-Actualizar-Eliminar) que puede parametrizarse y ampliarse mediante archivos de configuración JSON. No es necesario reescribir el código para cada editor de tablas.
- **Menú personalizable:** el menú y endpoints pueden parametrizarse y ampliarse mediante archivos de configuración JSON en el lado del backend. La API proporcionará la estructura del menú y la verificación de seguridad basada en el grupo de seguridad del usuario, y GenericSuite dibujará el menú y las opciones disponibles.
- **Interfaz de inicio de sesión personalizable:** Adapta fácilmente la página de inicio de sesión para que coincida con la identidad de tu marca con el logotipo de la App.
- **Scripts de Desarrollo y Producción:** Comandos rápidos para iniciar el desarrollo o compilar tu aplicación para entornos de QA, staging y producción en AWS.
- **Pruebas con Jest:** Viene preconfigurado con Jest para ejecutar pruebas, incluyendo una prueba inicial para el componente `<App />`.
- **Inclusión de Archivos Esenciales:** `.env.example` para la configuración de variables de entorno, `Makefile` para acortar operaciones frecuentes, `vite.config.mjs`, `webpack.config.js` y `config-overrides.js` para ejecutar la App localmente con `Webpack` o `react-app-rewired`, `scripts` con scripts de desarrollo y de producción, y `CHANGELOG.md` para rastrear cambios entre versiones.

El compañero perfecto para esta solución de frontend es la [versión de backend de The GenericSuite AI](../../Backend-Development/GenericSuite-AI/index.md).

GenericSuite AI (versión frontend) se basa en [The GenericSuite for ReactJS (frontend version)](../GenericSuite-Core/index.md).

## Requisitos previos

Instala las mismas herramientas descritas en [GenericSuite for ReactJS (frontend version)](../GenericSuite-Core/index.md#pre-requisites) en la sección `Requisitos previos`.

## Inicio

Para empezar con GenericSuite AI, sigue estos simples pasos:

### Crear repositorios Git

Los mismos pasos descritos en [GenericSuite for ReactJS (frontend version)](../GenericSuite-Core/index.md#create-the-git-repositories) sección `Getting started > Create Git repositories`.

### Inicia tu proyecto

Los mismos pasos descritos en [GenericSuite for ReactJS (frontend version)](../GenericSuite-Core/index.md#initiate-your-project) sección `Getting started > Initiate your project`.

### Instalar paquetes de GenericSuite AI

```bash
npm install genericsuite genericsuite-ai
```

### Instalar dependencias de desarrollo adicionales

Los mismos pasos descritos en [GenericSuite for ReactJS (frontend version)](../GenericSuite-Core/index.md#install-additional-development-dependencies) sección `Getting started > Install additional development dependencies`.

### Preparar los archivos de configuración

Copiar la plantilla [.env.ejemplo](https://github.com/tomkat-cr/genericsuite-fe-ai/blob/main/.env.example) desde `node_modules/genericsuite-ai` a tu archivo `.env`:

```bash
cp node_modules/genericsuite-ai/.env.example .env
```

Y configure las variables según tus necesidades:

* Asigna las mismas variables descritas en [GenericSuite for ReactJS (frontend version)](../GenericSuite-Core/index.md#prepare-the-configuration-files) sección `Getting started > Prepare the Configuration Files`.

* Asigna los parámetros adicionales `AWS_*` con tus datos de AWS (utilizados por aws_deploy_to_s3.sh y change_env_be_endpoint.sh). Necesitarás una cuenta de AWS.

Para más información, consulta los comentarios de cada variable en el archivo [.env.ejemplo](https://github.com/tomkat-cr/genericsuite-fe-ai/blob/main/.env.example).

#### Otros parámetros

* `REACT_APP_USE_AXIOS`: "1" = uso de axios para enviar archivos, "0" = usar fetch en su lugar. Por defecto es "1".

### Preparar el Makefile

Copiar la plantilla `Makefile` desde `node_modules/genericsuite-ai`:

```bash
cp node_modules/genericsuite-ai/Makefile ./Makefile
```

### Cambiar Scripts en Package.json

Los mismos pasos descritos en [GenericSuite for ReactJS (frontend version)](../GenericSuite-Core/index.md#change-scripts-in-packagejson) sección `Getting started > Change Scripts in Package.json`.

### Crear el archivo de versión

Crear el archivo `version.txt` con la versión de la App:

```bash
vi ./version.txt
# o
# code ./version.txt
```

Añade el número de versión (p. ej. `1.0.0`) y guarda el archivo.

## Estructura de la App

La estructura de repositorio de desarrollo de la App sugerida es la misma descrita en [GenericSuite for ReactJS (frontend version)](../GenericSuite-Core/index.md#app-structure) sección `App structure`.

## Configurar el proyecto

Haz clic [aquí](../../Configuration-Guide/index.md) para obtener más información sobre cómo configurar el proyecto.

## Ejemplos de código y archivos de configuración JSON

El menú principal, los endpoints de API y las configuraciones del editor CRUD se definen en los archivos de configuración JSON.

Puedes encontrar ejemplos sobre configuraciones y cómo crear una App en la [guía de creación y configuración de GenericSuite](../../Configuration-Guide/index.md).

## Uso

### Iniciar el servidor de desarrollo

```bash
make run
```

### Despliegue en QA

Consulta la [Guía de Despliegue](../deployment.md) para más detalles.