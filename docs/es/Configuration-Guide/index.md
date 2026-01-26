# Guía de creación y configuración de la aplicación GenericSuite

![gs_logo_circle.png](../../assets/images/gs_logo_circle.png)

Esta documentación muestra cómo crear las configuraciones de la App frontend/backend y las estructuras de datos.

## Configuración del Editor Genérico CRUD

Siga las instrucciones para construir los archivos `.json` en la [Documentación de Configuración del Editor CRUD Genérico](./Generic-CRUD-Editor-Configuration.md).

## App de ejemplo

La [ExampleApp](../../code/exampleapp/README.md) es una aplicación de ejemplo de pila completa que demuestra cómo crear una App usando GenericSuite. Es una arquitectura de aplicación web con un frontend basado en React y servicios de backend implementados en FastAPI, Flask y Chalice.

Haz clic [aquí](../../code/exampleapp/README.md) para saber más sobre ello.

## Creación de la App

Cada App debería tener una parte de frontend y una de backend.<br>

El frontend es el elemento con el que el usuario interactúa, la parte visible. Puede ser un sitio web hecho con React.JS o una App móvil hecha con Flutter o React Native.<br>

El backend es la API que interactúa con la Base de Datos y otros elementos invisibles para el usuario. Puede hacerse en Python o GoLang.<br>

En el contexto de GenericSuite hay un tercer elemento, el "Directorio de configuración".

## Directorio de configuración

El Directorio de configuración almacena la configuración de la App, permitiendo definir estructuras de tablas, formularios de entrada, estructura de menús, configuración de seguridad, parámetros de configuración, etc.

La estructura sugerida es:

```
src/configs
├── CHANGELOG.md
├── README.md
├── backend
│   ├── app_main_menu.json
│   ├── endpoints.json
│   ├── general_config.json
│   ├── users.json
│   └── users_config.json
└── frontend
    ├── app_constants.json
    ├── general_config.json
    ├── general_constants.json
    ├── users.json
    ├── users_config.json
    └── users_profile.json
```

## Directorio frontend

El directorio `frontend` contiene configuraciones utilizadas tanto por la App frontend como por la API backend.

- **app_constants.json**<br><br>
  Constantes específicas de la App. Estas constantes deben copiarse al directorio de la App objetivo para cambiar valores específicos por ejemplo `BILLING_PLANS`, dirección de correo en `ERROR_MESSAGES`, `APP_EMAILS` y `APP_VALID_URLS` (ver `includesAppValidLinks()` y `dangerouslySetInnerHTML`).<br><br>

- **general_constants.json**<br><br>
  Constantes generales de la App, principalmente para desplegados `<select/>`. Por ejemplo `TRUE_FALSE`, `YES_NO`, `LANGUAGES`.<br><br>

- **general_config.json**<br><br>
  Definiciones del editor de Parámetros de Configuración generales de la App.<br>
  Todos los parámetros en la clase backend Config() que pueden leerse desde variables de entorno pueden sobrescribirse dinámicamente mediante los Parámetros de Configuración.<br>
  Esto se usa para la opción de menú frontend `Admin > Configuration Parameters`.<br><br>

- **users.json**<br><br>
  Definiciones del editor CRUD de Usuarios y de la tabla. Esto se usa para la opción de menú frontend `Admin > Users`.<br><br>

- **users_config.json**<br><br>
  Parámetros de configuración específicos de usuarios (CRUD) y definiciones de la tabla.<br>
  Esto se usa para `Configuration parameters` en la opción de menú frontend `Admin > Users`.<br><br>

- **users_profile.json**<br><br>
  Configuración del perfil de usuarios. Esto se usa para la opción de menú frontend `Hamburger Menu > Profile`.

## Directorio Backend

El directorio `backend` contiene configuraciones visibles únicamente en la API backend.

Esto es principalmente para opciones de la estructura del menú y seguridad que no queremos que estén disponibles en el frontend.

- **app_main_menu.json**<br><br>
  Estructura del menú y configuraciones de seguridad.<br><br>

- **endpoints.json**<br><br>
  Definición y configuración de Endpoints.<br><br>

- **general_config.json**<br><br>
  Definiciones del editor de Parámetros de Configuración Generales de la App.<br><br>

- **users.json**<br><br>
  Definiciones del editor de Usuarios.<br><br>

- **users_config.json**<br><br>
  Definiciones del editor de parámetros de configuración específicos de usuario.<br>
  Estos parámetros de configuración sobrescriben los Parámetros Generales de Configuración, por usuario.

## Compartir archivos JSON entre los repositorios de desarrollo

Para compartir los archivos JSON entre los repositorios de desarrollo de frontend y backend, se puede crear un repositorio separado y enlazar a ambos repos con un Submódulo de Git:

### Crear un repositorio solo para los archivos JSON

  Crear el repositorio de archivos JSON en tu plataforma Git favorita ([GitHub](https://github.com/), [GitLab](https://gitlab.com/), [Bitbucket](https://bitbucket.org/)).

  Una vez creado, abre una ventana de Terminal y cambia al directorio raíz de tus repos.

  Luego clona los repos:

  E.g. para el repositorio de configs llamado `exampleapp_configs` creado en Github:

```bash
git clone https://github.com/tomkat-cr/exampleapp_configs.git
```

### Crear esta estructura de directorios

```
.
├── CHANGELOG.md
├── README.md
├── backend
└── frontend
```

### Definir parámetros del submódulo de Git

- Define los parámetros `GIT_SUBMODULE_LOCAL_PATH_FRONTEND` y `GIT_SUBMODULE_URL` en el archivo frontend [.env](https://github.com/tomkat-cr/genericsuite-fe/blob/main/.env.example).

- Define los parámetros `GIT_SUBMODULE_LOCAL_PATH` y `GIT_SUBMODULE_URL` en el archivo backend [.env](https://github.com/tomkat-cr/genericsuite-be/blob/main/.env.example).

- En el directorio frontend ejecuta esto para inicializar el submódulo de Git:

```bash
make add_submodules
```

- En el directorio backend, ejecuta esto para inicializar el submódulo de Git:

```bash
make add_submodules
```

- En el directorio backend, ejecuta esto para copiar los archivos básicos de configuración JSON:

```bash
make init_submodules
```

- Haz commit y push de los cambios para hacerlos disponibles para el frontend:

```bash
# FastAPI
cd app/config_dbdef
# Flask
# cd flaskr/config_dbdef
# Chalice
# cd lib/config_dbdef
```
```bash
git commit -m "Initial JSON config files"
```
```bash
git push
```

## Cómo crear tablas de base de datos

Para crear una nueva tabla de base de datos, debe existir un archivo `.json` en el directorio `backend/` con la definición de la tabla (p. ej. `table_name`, `mandatory_fields`, `projection_exclusion`, `email_verification`, `passwords`,  `additional_query_params`, etc., y las funciones específicas del backend `specific_function`), y un archivo `.json` en el directorio `frontend/` con la estructura de la tabla (p. ej. con columnas/atributos definidos en `fieldElements`).

Por ejemplo, la tabla **users** tiene los siguientes archivos:

* [backend/users.json](../../code/genericsuite-configs/backend/users.json)
* [frontend/users.json](../../code/genericsuite-configs/frontend/users.json)

La tabla **users** puede tener más de un archivo `.json` en los directorios `backend/` y `frontend/`, cada uno con vistas diferentes o con propiedades adicionales (o columnas) para una tabla.

Por ejemplo:

1. El **perfil de usuario** tiene una vista diferente a la de los **usuarios** con menos atributos, porque no es un formulario para editar al usuario (solo los usuarios administradores pueden editar usuarios), sino una vista de perfil (destinada a que el usuario vea su propio perfil):

* [backend/users_profile.json](../../code/genericsuite-configs/backend/users_profile.json)
* [frontend/users_profile.json](../../code/genericsuite-configs/frontend/users_profile.json)

2. Para definir una relación 1 a muchos entre dos tablas, por ejemplo entre las tablas **usuarios** y **users_api_keys**:

* [backend/users_api_keys.json](../../code/genericsuite-configs/backend/users_api_keys.json), donde `table_name` es "users_api_keys" definiendo el nombre físico de la tabla relacionada en la base de datos
* [frontend/users_api_keys.json](../../code/genericsuite-configs/frontend/users_api_keys.json), donde `type` es "child_listing" (lo que significa que es una relación 1 a muchos), `subType` es "table" (lo que significa que la propiedad es otra tabla), `endpointKeyNames` es un array con uno o más objetos con `parameterName` como "user_id" (el parámetro que se enviará al backend para recuperar los ítems de la tabla hija), y `parentElementName` como "user_id" (el nombre de la propiedad de la tabla padre para establecer la relación con la tabla hija)

3. Para definir una relación 1 a muchos en la misma tabla, por ejemplo la tabla **users** con una propiedad tipo array (o columna tipo JSON) llamada `users_config`:

* [backend/users_config.json](../../code/genericsuite-configs/backend/users_config.json), donde `table_name` es "users" definiendo la tabla padre físico en la base de datos
* [frontend/users_config.json](../../code/genericsuite-configs/frontend/users_config.json), donde `type` es "child_listing" (lo que significa que es una relación 1 a muchos), `subType` es "array" (lo que significa que la propiedad es un array en la tabla), `array_name` es "users_config" (el nombre de la propiedad de array), `primaryKeyName` es "id" (la clave primaria de la tabla de array), `parentUrl` es "users" (el nombre del endpoint para recuperar el elemento de la tabla padre -ó fila-), `endpointKeyNames` tiene: `parameterName` como "user_id" (el parámetro que se enviará al backend para recuperar el ítem de la tabla padre), y `parentElementName` como "id" (el nombre de la clave primaria de la tabla padre)

Siga las instrucciones para construir los archivos `.json` en la [Documentación de Configuración del Editor CRUD Genérico](./Generic-CRUD-Editor-Configuration.md).

## Cómo crear formularios

Los formularios comparten los mismos archivos `.json` de frontend y backend que las tablas de la base de datos, dando la posibilidad de crear formularios con diferentes vistas.

Para cada formulario debe haber un par de archivos: uno para el frontend y otro para el backend.

Para crear un nuevo formulario, debe existir un archivo `.json` en el directorio `frontend/` con la estructura del formulario (por ejemplo con campos de entrada definidos en `fieldElements`, y los atributos del formulario en `baseUrl`, `title`, `name`, `component`, `dbApiUrl`,  relaciones 1 a muchos en `childComponents`, funciones específicas en `dbListPreRead`, `dbPreWrite`, `dbPreValidations`, `validations`, etc.), y un archivo `.json` en el directorio `backend/` con la tabla utilizada por el formulario (para especificar `table_name`).

Por ejemplo, la tabla **users** puede tener un formulario para editar al usuario, y otro formulario para editar el perfil del usuario:

* [frontend/users.json](../../code/genericsuite-configs/frontend/users.json)
* [backend/users.json](../../code/genericsuite-configs/backend/users.json)
* [frontend/users_profile.json](../../code/genericsuite-configs/frontend/users_profile.json)
* [backend/users_profile.json](../../code/genericsuite-configs/backend/users_profile.json)

Siga las instrucciones para construir los archivos `.json` en la [Documentación de Configuración del Editor CRUD Genérico](./Generic-CRUD-Editor-Configuration.md).

## Cómo construir los archivos de configuración JSON

Siga las instrucciones para construir los archivos de configuración JSON en la [Documentación de Configuración del Editor CRUD Genérico](./Generic-CRUD-Editor-Configuration.md).


## App frontend

Siga las instrucciones para crear el frontend de la App en ReactJS [aquí](../Configuration-Guide/index.md).

Si la App incluirá funciones de IA, haga clic [aquí](../Frontend-Development/GenericSuite-AI/index.md).<br>

### Crear el código inicial

En el directorio `src`:

- `index.jsx` ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe-ai/blob/main/src/index.jsx))<br>
Punto de inicio de la App.
```js
import React from 'react';
import { createRoot } from 'react-dom/client';
import { HashRouter } from 'react-router-dom';

import { App } from './components/App/App';

const root = createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <App/>
  </React.StrictMode>
);
```

- `input.css` ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe/blob/main/src/input.css))<br>
Configuración general de CSS y Tailwind.
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

- `d.ts` ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe/blob/main/src/d.ts))<br>
Para permitir la importación de archivos JSON.

```ts
declare module "*.json"
```

### Crear componentes iniciales

- Crear el directorio `src/components`.

- Crear los directorios `src/components/About`, `src/components/App`, `src/components/HomePage`:

- Crear el directorio `src.constants`.

- `About/About.jsx` componente ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe-ai/blob/main/src/lib/components/About/About.jsx)).<br>

   En el pop-up Acerca de estará la descripción de tu App :
```js
import React from 'react'
import * as gs from "genericsuite";
const GsAboutBody = gs.AboutBody;
export const AboutBody = () => {
    return (
        <GsAboutBody>
            <p>
                ExampeApp is an application to ...
            </p>
        </GsAboutBody>
    )
}
```

- `App/App.jsx` componente ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe-ai/blob/main/src/lib/components/App/App.jsx)).<br>

   Configura el logo de la App (p. ej. `app_logo_circle.svg`) y los componentes del menú principal (p. ej. `ExampleMainElement` y `ExampleChildElement`).

```js
import React from 'react';
import * as gs from "genericsuite";

import { HomePage } from '../HomePage/HomePage.jsx';
import { AboutBody } from '../About/About.jsx';

import { ExampleMainElement } from '../ExampleMenu/ExampleMainElement.jsx';
import { ExampleChildElement } from '../ExampleMenu/ExampleChildElement.jsx';

const componentMap = {
    "AboutBody": AboutBody,
    "HomePage": HomePage,
    "ExampleMainElement": ExampleMainElement,
    "ExampleChildElement": ExampleChildElement,
    "exampleChildElementFormula": () => ( parseFloat(document.getElementsByName('yes_no')[0].value) == '0' ? 0 : ( parseFloat(document.getElementsByName('float_value')[01].value) * parseFloat(document.getElementsByName('quantity')[0].value) ).toFixed(2) ),
};

export const App = () => {
    return (
        <gs.App
            // Logo for login page (circled)
            appLogo="app_logo_circle.svg"
            // Logo for the header (landscape)
            // appLogoHeader={"app_logo_landscape.svg"}
            componentMap={componentMap}
        />
    );
}
```

Para cambiar los colores del tema por defecto:

```js
export const defaultTheme = {
  light: {
    primary: 'bg-blue-600 defaultThemeLightPrimary',
    secondary: 'bg-gray-200 defaultThemeLightSecondary',
    text: 'text-gray-800 defaultThemeLightText',
    textHoverTop: 'hover:bg-blue-400 defaultThemeLightTextHoverTop',
    textHoverTopSubMenu: 'hover:bg-gray-200 defaultThemeLightTextHoverTopSubMenu',
    textHoverSide: 'hover:bg-gray-300 defaultThemeLightTextHoverSide',
    background: 'bg-gray-100 defaultThemeLightBackground',
    contentBg: 'bg-gray-300 defaultThemeLightContentBg',
  },
  dark: {
    primary: 'bg-blue-800 defaultThemeDarkPrimary',
    secondary: 'bg-gray-700 defaultThemeDarkSecondary',
    text: 'text-gray-200 defaultThemeDarkText',
    textHoverTop: 'hover:bg-blue-400 defaultThemeDarkTextHoverTop',
    textHoverTopSubMenu: 'hover:bg-gray-200 defaultThemeDarkTextHoverTopSubMenu',
    textHoverSide: 'hover:bg-gray-400 defaultThemeDarkTextHoverSide',
    background: 'bg-gray-900 defaultThemeDarkBackground',
    contentBg: 'bg-slate-500 defaultThemeDarkContentBg',
  }
}

const componentMap = {
        .
        .
    "defaultTheme": defaultTheme,
}
```

Para reemplazar el pie de página de la App por un componente personalizado <AppFooter />:

```js
// import * as gs from "genericsuite";
import * as gsAi from "genericsuite-ai";

import { HomePage } from '../HomePage/HomePage.jsx';
import { AboutBody } from '../About/About.jsx';
import { AppFooter } from '../AppFooter/AppFooter.jsx';

const AppLogo = 'app_logo_square.svg';

const componentMap = {
    "AboutBody": AboutBody,
    "HomePage": HomePage,
    "AppFooter": AppFooter,
};

const GsAiApp = gsAi.App;

export const App = () => {
    return (
        <GsAiApp
            appLogo={AppLogo}
            componentMap={componentMap}
        />
    );
}
```

Y...

Archivo: `src/components/AppFooter/AppFooter.jsx`

```js
import React from "react";
import * as gs from "genericsuite";
const GsAppFooter = gs.AppFooter;

export const AppFooter = () => {
    return (
        <GsAppFooter>
            year={`2020-${new Date().getFullYear()}`}
            url="https://www.exampleapp.com"
            otherLine={"Made by https://www.examplecompany.com"}
        </>
    );
}
```

- **`HomePage/HomePage.jsx`** componente ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe-ai/blob/main/src/lib/components/HomePage/HomePage.jsx)).<br>

   Define el contenido de la Página de Inicio.
```js
import React from 'react';
import * as gs from "genericsuite";

const useUser = gs.UserContext.useUser;

export const HomePage = () => {
    const { currentUser } = useUser();
    return (
        <gs.HomePage>
            <>
                <h2>Hi {currentUser.firstName}!</h2>
                <p>Here you can add your custom content, widgets or other components for the Home Page</p>
            </>
        </gs.HomePage>
    );
}
```

### Definir constantes específicas de la App

- `src/configs/frontend/app_constants.json` ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe/blob/main/src/configs/frontend/app_constants.json))

```json
{
    "BILLING_PLANS": {
        "free": "Free",
        "basic": "Basic",
        "premium": "Premium"
    },
    "GENDERS": {
        "m": "Male",
        "f": "Female",
        "nb": "Non-binary",
        "o": "Other"
    },
    "ERROR_MESSAGES": {
        "ACCOUNT_INACTIVE": "User account inactive [L5]. To activate your account, please contact support@exampleapp.com"
    },
    "APP_EMAILS": {
        "SUPPORT_EMAIL": "support@exampleapp.com",
        "INFO_EMAIL": "info@exampleapp.com"
    },
    "APP_VALID_URLS": {
        "APP_DOMAIN": "exampleapp.com",
        "APP_WEBSITE": "https://www.exampleapp.com"
    }
}
```
NOTA: reemplace `exampleapp.com`, `info@exampleapp.com` y `support@exampleapp.com` con los dominios y correos de su App.

- `src/constants/app_constants.jsx` ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe/blob/main/src/lib/constants/app_constants.jsx))

```js
import constants from "../configs/frontend/app_constants.json";
import * as gs from "genericsuite";

const buildConstant = gs.jsonUtilities.buildConstant;

export const GENDERS = buildConstant(constants.GENDERS);
export const BILLING_PLANS = buildConstant(constants.BILLING_PLANS);
export const ERROR_MESSAGES = constants.ERROR_MESSAGES;
export const APP_EMAILS = constants.APP_EMAILS;
export const APP_VALID_URLS = constants.APP_VALID_URLS;
```

### Definir editores CRUD

Ahora definiremos dos componentes: `ExampleMainElement`, que es el componente principal accesible desde el menú principal y permitirá realizar las operaciones CRUD (crear, leer, actualizar, eliminar) sobre una `example_table`.

El `ExampleMainElement` tendrá un componente hijo `ExampleChildElement` con una relación `1 a N` y se almacenará en la misma `example_table` como un elemento de la lista.

- Crea estos directorios:
```
src/components/ExampleMenu
src/images
src/configs
src/configs/backend
src/configs/frontend
```

- En el directorio `src/components/ExampleMenu` crea estos archivos:
```
src/components/ExampleMenu/ExampleMainElement.jsx
src/components/ExampleMenu/ExampleChildElement.jsx
```

- En el directorio `src/configs` crea estos archivos:
```
src/configs/backend/example_main_element.json
src/configs/backend/example_child_element.json
src/configs/frontend/example_main_element.json
src/configs/frontend/example_child_element.json
```

Tendrás una estructura de directorios/archivos como la siguiente:
```
.
└── src
    ├── components
    │   ├── ExampleMenu
    │   │   ├── ExampleMainElement.jsx
    │   │   └── ExampleChildElement.jsx
    ├── configs
    │   ├── backend
    │   │   ├── example_main_element.json
    │   │   └── example_child_element.json
    │   └── frontend
    │       ├── example_main_element.json
    │       └── example_child_element.json
    └── images
        └── app_logo_circle.svg
```

- `src/components/ExampleMenu/ExampleMainElement.jsx` archivo:<br>
Tendrá el componente principal que permite operaciones CRUD sobre la `example_table`.<br>
```js
import React from 'react';

import * as gs from "genericsuite";
import exampleMainElementConfig from "../../configs/frontend/example_main_element.json";
import {
    GENDERS,
    BILLING_PLANS
} from '../../constants/app_constants.jsx';

import {
    ExampleChildElement,
} from './ExampleChildElement.jsx';

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;

// To show debug data in the Browser's developer tools console
const console_debug_log = gs.loggingService.console_debug_log;

export function ExampleMainElement_EditorData() {
    console_debug_log("ExampleMainElement_EditorData");
    const registry = {
        "ExampleMainElement": ExampleMainElement, 
        "ExampleChildElement": ExampleChildElement,
        "GENDERS": GENDERS,
        "BILLING_PLANS": BILLING_PLANS,
    }
    return GetFormData(exampleMainElementConfig, registry, 'ExampleMainElement_EditorData');
}

export const ExampleMainElement = () => (
    <GenericCrudEditor editorConfig={ExampleMainElement_EditorData()} />
)
```

- `src/configs/frontend/example_main_element.json` archivo:<br>
Tendrá la configuración del componente principal para backend y frontend.<br>
```json
{
    "baseUrl": "example_table",
    "title": "Example Main Element",
    "name": "Dish",
    "component": "ExampleMainElement",
    "dbApiUrl": "example_table_endpoint",
    "mandatoryFilters": {
        "user_id": "{CurrentUserId}",
        "type": "D"
    },
    "fieldElements": [
        {
            "name": "id",
            "required": true,
            "label": "ID",
            "type": "_id",
            "readonly": true,
            "hidden": true
        },
        {
            "name": "user_id",
            "required": true,
            "label": "User ID",
            "type": "text",
            "readonly": true,
            "hidden": true
        },
        {
            "name": "gender",
            "required": true,
            "label": "Gender",
            "type": "select",
            "select_elements": "GENDERS",
            "readonly": true,
            "hidden": false,
            "default_value": "m"
        },
        {
            "name": "name",
            "required": true,
            "label": "Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "billing_plan",
            "required": true,
            "label": "Billing Plan",
            "type": "select",
            "select_elements": "BILLING_PLANS",
            "readonly": false,
            "listing": true,
            "default_value": "free"
        },
        {
            "name": "creation_date",
            "required": true,
            "label": "Created",
            "type": "datetime-local",
            "readonly": true,
            "hidden": false,
            "default_value": "current_timestamp",
            "listing": true
        },
        {
            "name": "update_date",
            "required": true,
            "label": "Last update",
            "type": "datetime-local",
            "readonly": true,
            "hidden": false,
            "default_value": "current_timestamp",
            "listing": false
        }
    ],
    "childComponents": [
        "ExampleChildElement"
    ]
}
```

- `src/configs/backend/example_main_element.json` archivo:<br>
Tendrá la configuración backend del componente principal.<br>
`creation_pk_name` define el nombre del atributo utilizado para verificar duplicados en la creación. En este caso, no permitirá nombres repetidos.<br>
`additional_query_params` permite tener consultas de claves secundarias.<br><br>
```json
{
    "table_name": "example_table",
    "notes": "Example table main table",
    "creation_pk_name": "name",
    "additional_query_params": [
        "name"
    ]
}
```

- `src/components/ExampleMenu/ExampleChildElement.jsx` archivo:<br>
Tendrá el componente hijo que permite operaciones CRUD sobre el atributo `child_array` en la `example_table`.<br>
```js
import React from 'react';

import * as gs from "genericsuite";
import exampleChildElementConfig from "../../configs/frontend/example_child_element.json";

const TRUE_FALSE = gs.generalConstants.TRUE_FALSE;

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;

export function ExampleChildElement_EditorData() {
    const registry = {
        "ExampleChildElement": ExampleChildElement, 
        "TRUE_FALSE": TRUE_FALSE,
    }
    return GetFormData(exampleChildElementConfig, registry, false);
}

export const ExampleChildElement = ({parentData, handleFormPageActions}) => (
    <GenericCrudEditor
        editorConfig={ExampleChildElement_EditorData()}
        parentData={parentData}
        handleFormPageActions={handleFormPageActions}
    />
)
```

- `src/configs/frontend/example_child_element.json` archivo:<br>
Tendrá la configuración del componente hijo para backend y frontend.<br>
```json
{
    "baseUrl": "example_table_child",
    "title": "Example Child Elements",
    "name": "Example Child Element",
    "dbApiUrl": "example_table_child_endpoint",
    "component": "ExampleChildElement",
    "type": "child_listing",
    "subType": "array",
    "array_name": "child_array",
    "parentUrl": "example_table",
    "endpointKeyNames": [
        {
            "parameterName": "child_id",
            "parentElementName": "id"
        }
    ],
    "primaryKeyName": "id",
    "allow_duplicates": true,
    "fieldElements": [
        {
            "name": "id",
            "required": false,
            "label": "ID",
            "type": "text",
            "readonly": true,
            "hidden": true,
            "listing": false,
            "uuid_generator": true
        },
        {
            "name": "float_value",
            "required": true,
            "label": "Float Value",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "yes_no",
            "required": true,
            "label": "Yes or No",
            "type": "select",
            "select_elements": "TRUE_FALSE",
            "readonly": false,
            "listing": true,
            "default_value": "1"
        },
        {
            "name": "quantity",
            "required": true,
            "label": "Qty.",
            "type": "number",
            "min": "0",
            "max": "9999",
            "readonly": false,
            "listing": true
        },
        {
            "name": "float_by_quantity",
            "label": "Total",
            "type": "number",
            "readonly": true,
            "listing": true,
            "formula": "exampleChildElementFormula"
        }
    ]
}
```

- `src/configs/backend/example_child_element.json` archivo:<br>
Tendrá la configuración backend del componente hijo.<br>
```json
{
    "table_name": "example_table",
    "notes": "Example table array attribute with 1-to-many relationship in the same table",
}
```

### Usa la librería de iconos de GenericSuite: <GsIcons>

Hay una lista de Iconos incluidos o integrados en el archivo `node_modules/genericsuite/src/lib/helpers/IconsLib.jsx`.

Para usarlos, importa el componente `GsIcons` y usa la propiedad `icon` para seleccionar el icono a mostrar.

```js
import * as gs from "genericsuite";
const GsIcons = gs.IconsLib.GsIcons;

      .
      .
  <GsIcons
      icon="google-logo"
      alt="Open Google Search"
  />
```

Para definir un conjunto específico de iconos:

- Crea un nuevo directorio Helpers, por ejemplo `src/helpers`, y crea un nuevo archivo para los nuevos Iconos. Por ejemplo `src/helpers/iconsLibAiExtras.jsx`

- Importa los iconos que quieres usar en el archivo. Por ejemplo

```js
import { iconsLibAiExtras } from '../../helpers/iconsLibAiExtras.jsx';
```

- Usa los iconos en el archivo. Por ejemplo

```js
<GsIcons
    icon={isRecording ? 'stop' : 'microphone'}
    size='lg'
    additionalIconsFn={iconsLibAiExtras}
/>
```

### Crear imágenes

- Crea el directorio `src/images` y copia las imágenes de la App allí.

- Para referenciar las imágenes, usa el nombre de la imagen en una etiqueta `<img src="..." />`. Revisa un ejemplo [aquí](https://github.com/tomkat-cr/genericsuite-fe/blob/main/src/lib/services/generic.editor.rfc.service.jsx#L333). Por ejemplo,

```js
import React from 'react';
import * as gs from "genericsuite";
const imageDirectory = gs.generalConstants.imageDirectory;
const exampleButton = () => {
   return (
      <>
         <img src={imageDirectory + "eample_button.svg"}
            alt="Example Button"
            className={"text-white fill-white"}
         />
      </>
   );
}
```

IMPORTANTE: todas las imágenes se copiarán al directorio `build/static/media` durante la ejecución de desarrollo local y la implementación en QA/staging/producción.

Hay algunas imágenes precargadas utilizadas por la biblioteca GenericSuite. Consulta [aquí](https://github.com/tomkat-cr/genericsuite-fe/tree/main/src/lib/images) para más detalles.

### Definir opciones de menú para los editores CRUD

- `src/configs/backend/app_main_menu.json` archivo ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe/blob/main/src/configs/backend/app_main_menu.json)):

```json
[
    {
        "title": "Home",
        "location": "top_menu",
        "type": "nav_link",
        "path": "/",
        "element": "HomePage",
        "hard_prefix": false,
        "reload": true
    },
    {
        "title": "Admin Menu",
        "location": "top_menu",
        "type": "nav_dropdown",
        "sec_group": "admin",
        "sub_menu_options": [
            {
                "type": "editor",
                "sec_group": "admin",
                "title": "Users",
                "element": "Users_EditorData"
            },
            {
                "type": "editor",
                "sec_group": "admin",
                "title": "General Config",
                "element": "GeneralConfig_EditorData"
            }
        ]
    },
    {
        "title": "Example Menu",
        "location": "top_menu",
        "type": "nav_dropdown",
        "sec_group": "users",
        "sub_menu_options": [
            {
                "type": "editor",
                "sec_group": "users",
                "title": "Example Main Element",
                "element": "ExampleMainElement_EditorData"
            }
        ]
    },
    {
        "title": "Hamburger Menu",
        "location": "hamburger",
        "sub_menu_options": [
            {
                "title": "Profile",
                "path": "/profile",
                "element": "UserProfileEditor"
            },
            {
                "title": "Preferences",
                "path": "#preferences",
                "element": "PreferencesEditor"
            },
            {
                "title": "About",
                "on_click": "|about|"
            },
            {
                "title": "Logout",
                "path": "/login",
                "on_click": "logout"
            }
        ]
    },
    {
        "title": "Other Routes",
        "sub_menu_options": [
            {
                "title": "Absolut Home",
                "path": "/",
                "element": "HomePage",
                "get_prefix": false
            },
            {
                "title": "About body",
                "path": "/about_body",
                "element": "AboutBody",
                "get_prefix": false
            }
        ]
    }
]
```

### Definir editores CRUD de API endpoints

- `src/configs/backend/endpoints.json` archivo ([ejemplo](https://github.com/tomkat-cr/genericsuite-fe/blob/main/src/configs/backend/endpoints.json))

```json
[
    {
        "name": "general_config",
        "url_prefix": "general_config",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "general_config"
                }
            }
        ]
    },
    {
        "name": "example_table_endpoint",
        "url_prefix": "example_table_endpoint",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "example_table"
                }
            }
        ]
    },
    {
        "name": "example_table_child_endpoint",
        "url_prefix": "example_table_child_endpoint",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "example_table_child"
                }
            }
        ]
    }
]
```

### Usa el User Context

Existen algunos casos en los que se requiere obtener datos del usuario actual. Por ello, se proporciona el `UserContext`. Este contexto se usa para obtener los datos del usuario actualmente conectado.

Para usar el `UserContext`, importa el hook `useUser` desde el `UserContext` y úsalo en tu componente:

```js
// Componente de ejemplo que usa el UserContext para obtener el nombre de pila del usuario
import React, { useState, useEffect } from 'react';
import * as gs from "genericsuite";
const useUser = gs.UserContext.useUser;
export const HomePage = () => {
    // Obtener los datos del usuario actualmente conectado
    const { currentUser } = useUser();
    return (
        <gs.HomePage>
            <h1>Hi {currentUser.firstName}!</h1>
            <OtherComponents ... />
        </gs.HomePage>
    );
}
```

La lista completa de atributos disponibles del UserContext se puede encontrar en la documentación de [GenericSuite UserContext].(https://github.com/tomkat-cr/genericsuite-fe/blob/master/src/lib/helpers/UserContext.jsx)

### Usar el App Context

El App Context se usa para compartir atributos, variables y funciones entre los componentes de la App. Por ejemplo:

- `appLogo`
- `appLogoHeader`
- `componentMap`
- `state` (para almacenar los posibles mensajes de error en el componente principal de la App)
- `menuOptions`
- `sideMenu` (bandera que indica si el menú lateral izquierdo está activo)
- `isDarkMode`
- `isMobileMenuOpen`
- `expandedMenus` (contiene una lista de submenús expandidos)
- `isWide` (verdadero si la ventana tiene más de 640 píxeles de ancho)
- `theme` (atributos de color para modos claro y oscuro, dependiendo de cuál esté activo)
- `toggleDarkMode()`
- `toggleSideMenu()`
- `toggleMobileMenu()`
- `toggleSubmenu()`
- `isComponent()` (para comprobar si un objeto es un componente de React)
- `setExpanded()`

Por ejemplo, para usar el App Context, el directorio de imágenes, constantes de clases y elementos NavLib (como el ToggleSideBar, GsButton y CenteredBoxContainer):

```js
import React, { useState, useEffect } from 'react';

import * as gs from "genericsuite";

const useAppContext = gs.AppContext.useAppContext;

const imageDirectory = gs.generalConstants.imageDirectory;

const LOGIN_PAGE_APP_LOGO_CLASS = gs.classNameConstants.LOGIN_PAGE_APP_LOGO_CLASS;
const MAIN_CONTAINER_FOR_SIDE_MENU_CLASS = gs.classNameConstants.MAIN_CONTAINER_FOR_SIDE_MENU_CLASS;
const MAIN_CONTAINER_FOR_TOP_MENU_CLASS = gs.classNameConstants.MAIN_CONTAINER_FOR_TOP_MENU_CLASS;
const HIDDEN_CLASS = gs.classNameConstants.HIDDEN_CLASS;

const NavLib = gs.NavLib;
const ToggleSideBar = gs.NavLib.ToggleSideBar;

const alternativeAppLogo = "app_logo_square.svg";

export const SomeComponent = () => {
    const { theme, appLogo, appLogoHeader } = useAppContext();

    const [hideBar, setHideBar] = useState(false);
    const handleBarVisibility = () => {
        setHideBar(!hideBar);
    }
    const barClassName = () = (hideBar ? HIDDEN_CLASS : "");

    return (
        <NavLib.CenteredBoxContainer>
          <div
            className={`${sideMenu ? MAIN_CONTAINER_FOR_SIDE_MENU_CLASS : MAIN_CONTAINER_FOR_TOP_MENU_CLASS} ${theme.background} ${theme.text}`}
          >
            <div
              className={barClassName()}
            >
              <img
                src={imageDirectory + (appLogo || alternativeAppLogo)}
                width="150"
                height="150"
                className={LOGIN_PAGE_APP_LOGO_CLASS}
                alt="App Logo"
              />
              <GsButton
                variant={"secondary"}
                onClick={handleBarVisibility}
              >
                Toggle Side Menu
              </GsButton>
            </div>
          </div>
          <ToggleSideBar
            onClick={handleBarVisibility}
          />
        </NavLib.CenteredBoxContainer>
    );
}
```

La lista completa de atributos disponibles del AppContext se puede encontrar en la documentación de [GenericSuite AppContext](https://github.com/tomkat-cr/genericsuite-fe/blob/master/src/lib/helpers/AppContext.jsx).

## App backend

Siga las instrucciones para crear el backend de la App en Python [aquí](https://github.com/tomkat-cr/genericsuite-be/blob/main/README.md).<br>
Si la App incluirá funciones de IA, haga clic [aquí](https://github.com/tomkat-cr/genericsuite-be-ai/blob/main/README.md)<br>

### Crear el código inicial de la API

Para un proyecto Chalice:

1. `app.py` en el directorio raíz del proyecto.

```python
"""
Exampleapp main
"""
from genericsuite.chalicelib.util.create_app import create_app

from lib.config.config import Config

# exampleapp specific endpoint definition
# from chalicelib.endpoints import exampleapp_specific_endpoint

# Only for API Apps using GenericSuite AI backend version
# https://github.com/tomkat-cr/genericsuite-be-ai
# from chalicelib.endpoints import ai_exampleapp_bot as ai_chatbot_endpoint

settings = Config()
app = create_app(app_name=f'{settings.APP_NAME.lower()}-backend',
    settings=settings)

# Register application specific endpoints
# app.register_blueprint(food_moments.bp, url_prefix='/exampleapp_specific_endpoint')

# Register AI endpoints
# app.register_blueprint(ai_chatbot_endpoint.bp, url_prefix='/ai')
```

2. `lib/config/config.py`

```python
"""
General configuration module
"""
# C0103 | Disable "name doesn't conform to naming rules..." (snake_case)
# pylint: disable=C0103

from typing import Any

# For GenericSuite for backend project
from genericsuite_ai.config.config import Config as ConfigSuperClass
# For GenericSuite AI for backend project
# from genericsuite_ai.config.config import Config as ConfigSuperClass


class Config(ConfigSuperClass):
    """
    General configuration parameters read from environment variables
    """

    def __init__(self, app_context: Any = None) -> None:
        super().__init__(app_context)

        # Specific API credentials and other parameters
        # self.OTHER_API_KEY = self.get_env('OTHER_API_KEY', '')
```

## Elementos de IA

Los elementos de IA están disponibles en la versión frontend de GenericSuite AI y en la versión backend de GenericSuite AI.

### Elementos de IA: la opción de menú ChatBot

Para implementar un Asistente ChaBot similar a ChatGPT en tu App:

1. Opción de menú ChatBot `src/configs/backend/app_main_menu.json`

```json
    {
        "title": "ChatBot",
        "location": "top_menu",
        "type": "nav_link",
        "sec_group": "users",
        "path": "/chatbot",
        "element": "Chatbot"
    },
```

2. Código frontend `App.jsx`

```js
import React from 'react';

import * as gsAi from "genericsuite-ai";

import { HomePage } from '../HomePage/HomePage.jsx';
import { AboutBody } from '../About/About.jsx';

const AppLogo = 'app_logo_square.svg';

const componentMap = {
    "AboutBody": AboutBody,
    "HomePage": HomePage,
};

const GsAiApp = gsAi.App;

export const App = () => {
    return (
        <GsAiApp
            appLogo={AppLogo}
            componentMap={componentMap}
        />
    );
}
```

3. Código backend `app.py`

```python
"""
ExampleApp main
"""
from genericsuite.chalicelib.util.create_app import create_app

from lib.config.config import Config

from chalicelib.endpoints import ai_chatbot as ai_chatbot_endpoint

settings = Config()
app = create_app(app_name=f'{settings.APP_NAME.lower()}-backend',
    settings=settings)

# Register AI endpoints
app.register_blueprint(ai_chatbot_endpoint.bp, url_prefix='/ai')
```

4. Endpoint API de ChatBot `chalicelib/endpoints/ai_chatbot.py`
```python
"""
AI Endpoints
"""
from typing import Optional

from genericsuite.util.framework_abs_layer import Response

from genericsuite.util.blueprint_one import BlueprintOne
from genericsuite.util.jwt import (
    request_authentication,
    AuthorizedRequest
)
from genericsuite_ai.lib.ai_chatbot_endpoint import (
    ai_chatbot_endpoint as ai_chatbot_endpoint_model,
    vision_image_analyzer_endpoint as vision_image_analyzer_endpoint_model,
    transcribe_audio_endpoint as transcribe_audio_endpoint_model,
)

from lib.models.ai_chatbot.ai_gpt_fn_index import (
    assign_example_app_gpt_functions
)

DEBUG = False
bp = BlueprintOne(__name__)


@bp.route(
    '/chatbot',
    methods=['POST'],
    authorizor=request_authentication(),
)
def ai_chatbot_endpoint(
    request: AuthorizedRequest,
    other_params: Optional[dict] = None
) -> Response:
    """
    This function is the endpoint for the AI chatbot.
    It takes in a request and other parameters,
    logs the request, retrieves the user data, and runs the
    conversation with the AI chatbot.
    It then returns the AI chatbot's response.

    :param request: The request from the user.
    :param other_params: Other parameters that may be needed.
    :return: The response from the AI chatbot.
    """
    return ai_chatbot_endpoint_model(
        request=request,
        other_params=other_params,
        additional_callable=assign_example_app_gpt_functions,
    )


@bp.route(
    '/image_to_text',
    methods=['POST'],
    authorizor=request_authentication(),
    content_types=['multipart/form-data']
)
def vision_image_analyzer_endpoint(
    request: AuthorizedRequest,
    other_params: Optional[dict] = None
) -> Response:
    """
    This endpoint receives an image file, saves it to a temporary directory
    with a uuid4 .jpg | .png filename, calls @vision_image_analyzer with
    the file path, and returns the result.

    :param request: The request containing the image file.
    :return: The text with the image analysis.
    """
    return vision_image_analyzer_endpoint_model(
        request=request,
        other_params=other_params,
        additional_callable=assign_example_app_gpt_functions,
    )


@bp.route(
    '/voice_to_text',
    methods=['POST'],
    authorizor=request_authentication(),
    content_types=['multipart/form-data']
)
def transcribe_audio_endpoint(
    request: AuthorizedRequest,
    other_params: Optional[dict] = None
) -> Response:
    """
    This endpoint receives an audio file, saves it to a temporary directory
    with a uuid4 .mp3 filename, calls @audio_to_text_transcript with
    the file path, and returns the result.

    :param request: The request containing the audio file.
    :return: The transcription result.
    """
    return transcribe_audio_endpoint_model(
        request=request,
        other_params=other_params,
        additional_callable=assign_example_app_gpt_functions,
    )
```

5. GPT functions/tools específicas de IA ChatBot `lib/models/ai_chatbot/ai_gpt_fn_app.py`<br>(solo si la App tiene funciones GPT específicas)
```python
"""
GPT functions: App specific
"""
# C0301: | Disable "line-too-long"
# pylint: disable=C0301
# W0718 | broad-exception-caught Catching too general exception Exception
# pylint: disable=W0718

from typing import Union, Any, List, Optional
import json
import re
from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field
from langchain.tools import tool
from langchain_classic.schema import Document

from genericsuite.util.app_context import CommonAppContext
from genericsuite.util.app_logger import log_debug
from genericsuite.util.config_dbdef_helpers import get_json_def_both
from genericsuite.util.datetime_utilities import interpret_any_date
from genericsuite.util.utilities import (
    get_default_resultset,
    is_under_test,
)
from genericsuite.util.generic_db_middleware import (
    fetch_all_from_db,
    add_item_to_db,
    get_item_from_db,
    modify_item_in_db,
)
from genericsuite.constants.const_tables import get_constant

from genericsuite_ai.lib.ai_utilities import (
    standard_gpt_func_response,
    get_assistant_you_are,
)
from genericsuite_ai.lib.ai_sub_bots import ask_ai
from genericsuite_ai.lib.ai_langchain_tools import (
    interpret_tool_params,
)
from genericsuite_ai.lib.json_reader import (
    prepare_metadata,
    index_dict,
)

DEBUG = False
cac = CommonAppContext()

# Structures


class ExampleFuncElement(BaseModel):
    """
    example_element parameter structure class
    """
    name: str = Field(
        description="example_element name")
    #      .
    #      .
    observations: Optional[str] = Field(default="",
        description="example_element observations if any. Defaults to None")

# Funcions called by ChatGPT


@tool
def create_example_element(params: Any) -> str:
    """
Useful when you need to add a new example_element to the database.
Args: params (dict): Tool parameters. It must contain:
"name" (str): ingredient name.
    .
    .
"observations" (str): additional observations about the ingredient if any.
    """
    return create_example_element_func(params)


def create_example_element_func(params: Any) -> str:
    """
    Add a example_element to the database.
    """
    params = interpret_tool_params(tool_params=params, schema=ExampleFuncElement)

    name = params.name
    observations = params.observations

    new_item = {
        "user_id": cac.app_context.get_user_id(),
        "name": name,
        #      .
        #      .
        "observations": observations,
    }
    result = add_item_to_db(
        app_context=cac.app_context,
        json_file='example_element',
        data=new_item,
    )
    return standard_gpt_func_response(result, "example_element creation")
#      .
#      .
#      .
```

6. Gestión de funciones/herramientas GPT específicas de IA ChatBot `lib/models/ai_chatbot/ai_gpt_fn_index.py`<br>(solo si la App tiene funciones GPT específicas)

```python
"""
ChatGPT functions management
"""
from genericsuite.util.app_logger import log_debug
from genericsuite.util.app_context import AppContext

from genericsuite_ai.lib.ai_gpt_functions import (
    get_functions_dict,
)

from lib.config.config import Config
from lib.models.ai_chatbot.ai_gpt_fn_fda import (
    cac as cac_fda,
    get_fda_food_query,
    get_fda_food_query_func,
)

from lib.models.ai_chatbot.ai_gpt_fn_app import (
    cac as cac_app,
    create_example_element,
    create_example_element_func,
)

DEBUG = False
EXTRA_DEBUG = False


def assign_example_app_gpt_functions(
    app_context: AppContext,
) -> None:
    """
    Assign specific example_app GPT functions
    """
    _ = DEBUG and log_debug('ASSIGN_EXAMPLE_APP_GPT_FUNCTIONS | Assigning example_app GPT functions')
    app_context.set_other_data('additional_function_dict', get_additional_functions_dict)
    app_context.set_other_data('additional_func_context', additional_gpt_func_appcontexts)
    app_context.set_other_data('additional_run_one_function', additional_run_one_function)
    app_context.set_other_data('additional_function_specs', get_additional_function_specs)


def get_additional_functions_dict(
    app_context: AppContext,
) -> dict:
    """
    Get the available ChatGPT functions and its callables (app-specific).

    Returns:
        dict: A dictionary containing the available ChatGPT functions
        and its callable.
    """
    _ = DEBUG and log_debug('GET_ADDITIONAL_FUNCTIONS_DICT | Assigning example_app GPT functions dict')
    settings = Config(app_context)
    is_lc = settings.AI_TECHNOLOGY == 'langchain'
    if is_lc:
        # Langchain Tools
        result = {
            "create_example_element": create_example_element,
        }
    else:
        # GPT Functions
        result = {
            "create_example_element": create_example_element_func,
        }
    if DEBUG and EXTRA_DEBUG:
        log_debug(f"example_app GET_FUNCTIONS_DICT | is_lc: {is_lc} result: {result}")
    return result


def additional_gpt_func_appcontexts(
    app_context: AppContext,
) -> list:
    """
    Assign the app_context to the ChatGPT functions.

    Args:
        app_context (AppContext): GPT Context
    """
    _ = DEBUG and \
        log_debug('ADDITIONAL_GPT_FUNC_APPCONTEXTS | Assigning' + \
        ' example_app additional GPT function AppContexts')
    available_func_context = [
        cac_example_app,
    ]
    return available_func_context


def additional_run_one_function(
    app_context: AppContext,
    function_name: str,
    function_args: dict,
) -> dict:
    """
    Execute a function based on the given function_name
    and function_args.

    Args:
        app_context (AppContext): GPT Context
        function_name (str): function name
        function_args (dict): function args

    Returns:
        The result of the function execution.
    """
    _ = DEBUG and log_debug('ADDITIONAL_RUN_ONE_FUNCTION | example_app-specific run_one_function')
    user_lang = app_context.get_user_data().get('language', 'auto')
    # question = app_context.get_other_data("question")["content"]
    available_functions = get_functions_dict(app_context)
    fuction_to_call = available_functions[function_name]
    function_response = None
    _ = DEBUG and \
        log_debug("AI_FA_ROF-1) run_one_function_from_chatgpt" +
                  f" | function_name: {function_name}" +
                  f" | function_args: {function_args}")

    if function_name == "create_example_element":
        function_response = fuction_to_call(
            params={
                "name": function_args.get("name"),
                #     .
                #     .
                "observations": function_args.get("observations"),
            }
        )
    elif function_name == "...":
        function_response = fuction_to_call(
            params={
                "...": function_args.get("..."),
            }
        )

    result = {
        "function_response": function_response,
        "function_name": function_name,
        "function_args": function_args,
    }
    _ = DEBUG and \
        log_debug('AI_FA_ROF-2) run_one_function_from_chatgpt' +
                  f' | result: {result}')
    return result


def get_additional_function_specs(
    app_context: AppContext,
) -> list:
    """
    Get the ChatGPT function specifications (parameters, documentation).

    Returns:
        list[dict]: A list of dictionaries containing the available
        ChatGPT functions.
    """
    _ = DEBUG and log_debug('GET_ADDITIONAL_FUNCTION_SPECS | example_app additional GPT function specs')
    _ = DEBUG and \
        log_debug("AI_FA_GFS-1) get_function_specs")
    result = [{
        "name": "create_example_element",
        "description": "Add a example_element",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the" +
                    " example_element",
                },
                "observations": {
                    "type": "string",
                    "description": "Any observations about" +
                    " the example_element (value can be blank)",
                },
            },
            "required": [
                "name",
                "observations",
            ],
        },
    }, {
        "name": "...",
        "description": "...",
        "parameters": {
            "type": "object",
            "properties": {
                "...": {
                    "description": "...",
                    "type": "string",
                }
            }
        },
        "required": ["..."],
    }]

    return result

```

### Elementos de IA: el botón de ChatBot

Para implementar un botón que abra un pop-up de ChaBot:

1. Configuración del editor CRUD `src/configs/frontend/example_element.json`

```json
{
    "baseUrl": "example_element",
    "title": "Example Elements",
    "name": "Example element",
    "component": "ExampleElement",
    "dbApiUrl": "example_element",
    "mandatoryFilters": {
        "user_id": "{CurrentUserId}",
        "type": "I"
    },
    "defaultOrder": "name",
    "fieldElements": [
        {
            "name": "id",
            "required": true,
            "label": "ID",
            "type": "_id",
            "readonly": true,
            "hidden": true
        },
        {
            "name": "user_id",
            "required": true,
            "label": "User ID",
            "type": "text",
            "readonly": true,
            "hidden": true
        },
        {
            "name": "name",
            "required": true,
            "label": "Name",
            "type": "text",
            "readonly": false,
            "listing": true,
            "chatbot_popup": true,
            "aux_component": "ChatBotButton",
            "chatbot_prompt": "Give me all the information you have about %s. If you don't have it in your model, look for it with the web_search Tool.",
            "google_popup": true,
            "google_prompt": "information about %s"
        }
    ]
}
```

2. Frontend CRUD editor component `src/components/UsersMenu/ExampleElement.jsx`

```js
import React from 'react';

import * as gs from "genericsuite";
import * as gsAi from "genericsuite-ai";

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;

const ChatBotButton = gsAi.ChatBotButton;

export function ExampleElement_EditorData() {
    const registry = {
        "ExampleElement": ExampleElement, 
        "ChatBotButton": ChatBotButton,
    }
    return GetFormData(user_ingredients, registry, 'ExampleElement_EditorData');
}

export const ExampleElement = () => (
    <GenericCrudEditor editorConfig={ExampleElement_EditorData()} />
)
```

## Crear la base de datos MongoDB

Puedes crear una base de datos MongoDB en MongoDB Atlas:

1. Ve a [mongodb.com/](https://www.mongodb.com/)

2. Crea una cuenta [aquí](https://account.mongodb.com/account/register) si aún no tienes una, o [inicia sesión](https://account.mongodb.com/account/login) en tu cuenta existente.

3. Crea un nuevo Proyecto.

4. Crea una nueva Base de Datos / Despliegue.

5. Asigna un usuario y una contraseña de base de datos.

6. Copia o anota la contraseña del usuario.

7. Haz clic en el botón `Connect`.

8. Haz clic en la opción `Drivers`.

9. En la sección `3. Add your connection string into your application code`: copia la cadena de conexión.

10. Reemplaza `<password>` con la contraseña del usuario copiada en los pasos anteriores. Asegúrate de que cualquier parámetro de opción esté URL codificado ([ver la documentación aquí](https://www.mongodb.com/docs/atlas/troubleshoot-connection/#special-characters-in-connection-string-password)).

11. Asigna la cadena de conexión en las variables `.env` `APP_DB_URI_QA`, `APP_DB_URI_STAGING`, `APP_DB_URI_PROD` y `APP_DB_URI_DEMO`.

## Crear el usuario Super Admin

Para crear el Usuario de Administración, ejecuta esto:

```bash
# Run the backend API with the QA Database
make run_qa
# Or using the local Docker MongoDB
# make run
```

Cuando se te solicite, elige `1` para la opción `http`.

Usando [Postman](https://www.postman.com/home) (o tu aplicación favorita para enviar solicitudes API):

1. Crea una nueva pestaña de Solicitud.

2. En el campo `URL`, selecciona `POST` y asigna la URL `http://127.0.0.1:5001/users/supad-create`

3. Ve a la pestaña `Authorization`.

4. Selecciona `Type: Basic Auth`.

5. En el campo `Username`, coloca el valor asignado en la variable `APP_SUPERADMIN_EMAIL` del [.env](https://github.com/tomkat-cr/genericsuite-be/blob/main/.env.example).

6. En el campo `Password`, coloca el valor asignado en la variable `APP_SECRET_KEY` del [.env](https://github.com/tomkat-cr/genericsuite-be/blob/main/.env.example).

7. Envía la Solicitud.

8. Si la respuesta se parece al siguiente JSON, el usuario Super Admin fue creado con éxito:

```json
{
  "error": false,
  "error_message": "",
  "resultset": { ... },
  "rows_affected": "1"
}
```

9. Si la respuesta se parece al siguiente JSON, las credenciales son incorrectas. Verifica que los valores de los campos `Username` y `Password` deben ser iguales a las variables `APP_SUPERADMIN_EMAIL` y `APP_SUPERADMIN_EMAIL` del [.env](https://github.com/tomkat-cr/genericsuite-be/blob/main/.env.example):

```json
{
  "body": "Could not verify [SAC2]",
    "status_code": 400,
    "headers": {
      "WWW.Authentication": "Basic realm: \"login required\""
    }
}
```

10. Si la respuesta se parece al siguiente JSON, el usuario Super Admin ya fue creado:

```json
{
    "body": "User already exists [SAC4]",
    "status_code": 400,
    "headers": {
        "WWW.Authentication": "Basic realm: \"login required\""
    }
}
```

## Backend de AWS App

Este apéndice es para el Backend de la App que usa AWS Lambda Function, API Gateway, buckets S3, DynamoDB y Chalice.

### Definir el rol de la función Lambda

Ve a AWS Console > IAM > Roles y crea el `<exampleapp>-api_handler-role-<stage>` para cada etapa:

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Action": [
				"logs:CreateLogGroup",
				"logs:CreateLogStream",
				"logs:PutLogEvents"
			],
			"Resource": "arn:aws:logs:*:*:*",
			"Effect": "Allow"
		},
		{
			"Action": [
				"dynamodb:PutItem",
				"dynamodb:DeleteItem",
				"dynamodb:UpdateItem",
				"dynamodb:GetItem",
				"dynamodb:Scan",
				"dynamodb:Query"
			],
			"Resource": [
				"arn:aws:dynamodb:*:*:table/users",
				"arn:aws:dynamodb:*:*:table/general_config"
			],
			"Effect": "Allow"
		},
		{
			"Action": [
				"s3:PutObject",
				"s3:PutObjectAcl",
				"s3:GetObject",
				"s3:GetObjectAcl",
				"s3:DeleteObject"
			],
			"Resource": [
				"arn:aws:s3:::*/*",
				"arn:aws:s3:::*",
				"arn:aws:s3:::example-chatbot-attachments-<stage>/*"
			],
			"Effect": "Allow"
		}
	]
}
```

### Definir plantilla de configuración Chalice

1. Crea el directorio `.chalice` en el directorio raíz del proyecto.

```bash
mkdir -p .chalice
```

2. Crea el archivo `.chalice/config-example.json`.

```json
{
  "version": "2.0",
  "app_name": "APP_NAME_LOWERCASE_placeholder-backend",
  "lambda_memory_size": 256,
  "environment_variables": {
    "APP_NAME": "APP_NAME_placeholder",
    "AI_ASSISTANT_NAME": "AI_ASSISTANT_NAME_placeholder",
    "APP_VERSION": "APP_VERSION_placeholder",
    "APP_SECRET_KEY": "APP_SECRET_KEY_placeholder",
    "APP_SUPERADMIN_EMAIL": "APP_SUPERADMIN_EMAIL_placeholder",
    "GIT_SUBMODULE_URL": "GIT_SUBMODULE_URL_placeholder",
    "GIT_SUBMODULE_LOCAL_PATH": "GIT_SUBMODULE_LOCAL_PATH_placeholder",
    "CURRENT_FRAMEWORK": "CURRENT_FRAMEWORK_placeholder",
    "DEFAULT_LANG": "DEFAULT_LANG_placeholder",
    "FDA_API_KEY": "FDA_API_KEY_placeholder",
    "OPENAI_API_KEY": "OPENAI_API_KEY_placeholder",
    "OPENAI_MODEL": "OPENAI_MODEL_placeholder",
    "OPENAI_TEMPERATURE": "OPENAI_TEMPERATURE_placeholder",
    "GOOGLE_API_KEY": "GOOGLE_API_KEY_placeholder",
    "GOOGLE_CSE_ID": "GOOGLE_CSE_ID_placeholder",
    "LANGCHAIN_API_KEY": "LANGCHAIN_API_KEY_placeholder",
    "LANGCHAIN_PROJECT": "LANGCHAIN_PROJECT_placeholder",
    "HUGGINGFACE_API_KEY": "HUGGINGFACE_API_KEY_placeholder",
    "HUGGINGFACE_DEFAULT_CHAT_MODEL": "HUGGINGFACE_DEFAULT_CHAT_MODEL_placeholder",
    "SMTP_SERVER": "SMTP_SERVER_placeholder",
    "SMTP_PORT": "SMTP_PORT_placeholder",
    "SMTP_USER": "SMTP_USER_placeholder",
    "SMTP_PASSWORD": "SMTP_PASSWORD_placeholder",
    "SMTP_DEFAULT_SENDER": "SMTP_DEFAULT_SENDER_placeholder",
    "FLASK_APP": "FLASK_APP_placeholder"
  },
  "stages": {
    "dev": {
      "api_gateway_stage": "dev",
      "environment_variables": {
        "APP_DEBUG": "APP_DEBUG_placeholder",
        "APP_STAGE": "dev",
        "APP_DB_ENGINE": "APP_DB_ENGINE_DEV_placeholder",
        "APP_DB_NAME": "APP_DB_NAME_DEV_placeholder",
        "APP_DB_URI": "APP_DB_URI_DEV_placeholder",
        "APP_FRONTEND_AUDIENCE": "APP_FRONTEND_AUDIENCE_DEV_placeholder",
        "APP_CORS_ORIGIN": "APP_CORS_ORIGIN_DEV_placeholder",
        "AWS_S3_CHATBOT_ATTACHMENTS_BUCKET": "AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_DEV_placeholder"
      }
    },
    "qa": {
      "api_gateway_stage": "qa",
      "autogen_policy": false,
      "environment_variables": {
        "PORT": "5001",
        "APP_DEBUG": "APP_DEBUG_placeholder",
        "APP_STAGE": "qa",
        "APP_DB_ENGINE": "APP_DB_ENGINE_QA_placeholder",
        "APP_DB_NAME": "APP_DB_NAME_QA_placeholder",
        "APP_DB_URI": "APP_DB_URI_QA_placeholder",
        "APP_FRONTEND_AUDIENCE": "APP_FRONTEND_AUDIENCE_QA_placeholder",
        "APP_CORS_ORIGIN": "APP_CORS_ORIGIN_QA_placeholder",
        "AWS_S3_CHATBOT_ATTACHMENTS_BUCKET": "AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_QA_placeholder"
      }
    },
    "prod": {
      "api_gateway_stage": "prod",
      "environment_variables": {
        "APP_DEBUG": "0",
        "APP_STAGE": "prod",
        "APP_DB_ENGINE": "APP_DB_ENGINE_PROD_placeholder",
        "APP_DB_NAME": "APP_DB_NAME_PROD_placeholder",
        "APP_DB_URI": "APP_DB_URI_PROD_placeholder",
        "APP_FRONTEND_AUDIENCE": "APP_FRONTEND_AUDIENCE_PROD_placeholder",
        "APP_CORS_ORIGIN": "APP_CORS_ORIGIN_PROD_placeholder",
        "AWS_S3_CHATBOT_ATTACHMENTS_BUCKET": "AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_PROD_placeholder"
      }
    }
  }
}
```

### Define plantilla para tablas DynamoDB

Si planeas usar DynamoDB como tecnología de base de datos, necesitarás crear las tablas.

Este es un archivo inicial de ejemplo de `dynamodb_cf_template.yaml` para automatizar el proceso:

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  UsersTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: users
      AttributeDefinitions:
        - AttributeName: "email"
          AttributeType: "S"
        # - AttributeName: "username"
        #   AttributeType: "S"
      KeySchema:
        - AttributeName: "email"
          KeyType: "HASH"
        # - AttributeName: "username"
        #   KeyType: "HASH"
      ProvisionedThroughput:
        ReadCapacityUnits: "5"
        WriteCapacityUnits: "5"

  GeneralConfigTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: general_config
      AttributeDefinitions:
        - AttributeName: "id"
          AttributeType: "S"
        # - AttributeName: "config_name"
        #   AttributeType: "S"
      KeySchema:
        - AttributeName: "id"
          KeyType: "HASH"
        # - AttributeName: "config_name"
        #   KeyType: "RANGE"
      ProvisionedThroughput:
        ReadCapacityUnits: "5"
        WriteCapacityUnits: "5"

Outputs:
  Users:
    Description: Users
    Value: !Ref "UsersTable"
  Sessions:
    Description: General Config
    Value: !Ref "GeneralConfigTable"
```

### Definir plantilla SAM

1. `scripts/aws_big_lambda/template-sam.yml`

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Outputs:
  RestAPIId:
    Value:
      Ref: RestAPI
  APIHandlerName:
    Value:
      Ref: APIHandler
  APIHandlerArn:
    Value:
      Fn::GetAtt:
      - APIHandler
      - Arn
  EndpointURL:
    Value:
      Fn::Sub: https://${RestAPI}.execute-api.${AWS::Region}.${AWS::URLSuffix}/api/
Resources:
  LambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties: 
      AssumeRolePolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - Effect: Allow
            Principal: 
              Service: 
                - lambda.amazonaws.com
            Action: sts:AssumeRole
      Policies: 
        - PolicyName: LambdaS3Access 
          PolicyDocument:
            Version: "2012-10-17"
            Statement: 
              - Effect: Allow 
                Action: 
                - s3:PutObject
                - s3:PutObjectAcl
                - s3:GetObject
                - s3:GetObjectAcl
                - s3:DeleteObject
                Resource: "arn:aws:s3:::AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_placeholder/*"
        - PolicyName: DefaultRolePolicy
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
            - Effect: Allow
              Action:
              - logs:CreateLogGroup
              - logs:CreateLogStream
              - logs:PutLogEvents
              Resource: arn:*:logs:*:*:*

  RestAPI:
    Type: AWS::Serverless::Api
    Properties:
      StageName: api
      EndpointConfiguration: EDGE
      Domain: 
        DomainName: api.example.com
        CertificateArn: CertificateArn_placeholder
      BinaryMediaTypes:
      - audio/mpeg
      - application/octet-stream
      DefinitionBody:
        swagger: '2.0'
        info:
          version: '1.0'
          title: APP_NAME_LOWERCASE_placeholder-backend
        schemes:
        - https
        paths:
          /menu_options:
            get:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: 'Get authorized menu options '
            options:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
                  headers:
                    Access-Control-Allow-Methods:
                      type: string
                    Access-Control-Allow-Origin:
                      type: string
                    Access-Control-Allow-Headers:
                      type: string
                    Access-Control-Allow-Headers:
                      type: string
                    Access-Control-Expose-Headers:
                      type: string
                    Access-Control-Max-Age:
                      type: string
                    Access-Control-Allow-Credentials:
                      type: string
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                    responseParameters:
                      method.response.header.Access-Control-Allow-Methods: '''GET,OPTIONS'''
                      method.response.header.Access-Control-Allow-Origin: '''http://localhost:3000'''
                      method.response.header.Access-Control-Allow-Headers: '''Access-Control-Allow-Origin,Authorization,Content-Type,X-Amz-Date,X-Amz-Security-Token,X-Api-Key'''
                      method.response.header.Access-Control-Expose-Headers: '''Authorization,Access-Control-Allow-Origin,Content-Type,Content-Disposition,Content-Length'''
                      method.response.header.Access-Control-Max-Age: '''600'''
                      method.response.header.Access-Control-Allow-Credentials: '''true'''
                requestTemplates:
                  application/json: '{"statusCode": 200}'
                passthroughBehavior: when_no_match
                type: mock
                contentHandling: CONVERT_TO_TEXT

          /menu_options/element:
            post:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: 'Get menu element configuration '
            options:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
                  headers:
                    Access-Control-Allow-Methods:
                      type: string
                    Access-Control-Allow-Origin:
                      type: string
                    Access-Control-Allow-Headers:
                      type: string
                    Access-Control-Expose-Headers:
                      type: string
                    Access-Control-Max-Age:
                      type: string
                    Access-Control-Allow-Credentials:
                      type: string
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                    responseParameters:
                      method.response.header.Access-Control-Allow-Methods: '''POST,OPTIONS'''
                      method.response.header.Access-Control-Allow-Origin: '''http://localhost:3000'''
                      method.response.header.Access-Control-Allow-Headers: '''Access-Control-Allow-Origin,Authorization,Content-Type,X-Amz-Date,X-Amz-Security-Token,X-Api-Key'''
                      method.response.header.Access-Control-Expose-Headers: '''Authorization,Access-Control-Allow-Origin,Content-Type,Content-Disposition,Content-Length'''
                      method.response.header.Access-Control-Max-Age: '''600'''
                      method.response.header.Access-Control-Allow-Credentials: '''true'''
                requestTemplates:
                  application/json: '{"statusCode": 200}'
                passthroughBehavior: when_no_match
                type: mock
                contentHandling: CONVERT_TO_TEXT

          /users:
            get:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: User's CRUD operations (create, read, update, delete)
            post:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: User's CRUD operations (create, read, update, delete)
            put:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: User's CRUD operations (create, read, update, delete)
            delete:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: User's CRUD operations (create, read, update, delete)
            options:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
                  headers:
                    Access-Control-Allow-Methods:
                      type: string
                    Access-Control-Allow-Origin:
                      type: string
                    Access-Control-Allow-Headers:
                      type: string
                    Access-Control-Allow-Headers:
                      type: string
                    Access-Control-Max-Age:
                      type: string
                    Access-Control-Allow-Credentials:
                      type: string
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                    responseParameters:
                      method.response.header.Access-Control-Allow-Methods: '''GET,POST,PUT,DELETE,OPTIONS'''
                      method.response.header.Access-Control-Allow-Origin: '''http://localhost:3000'''
                      method.response.header.Access-Control-Allow-Headers: '''Access-Control-Allow-Origin,Authorization,Content-Type,X-Amz-Date,X-Amz-Security-Token,X-Api-Key'''
                      method.response.header.Access-Control-Expose-Headers: '''Authorization,Access-Control-Allow-Origin,Content-Type,Content-Disposition,Content-Length'''
                      method.response.header.Access-Control-Max-Age: '''600'''
                      method.response.header.Access-Control-Allow-Credentials: '''true'''
                requestTemplates:
                  application/json: '{"statusCode": 200}'
                passthroughBehavior: when_no_match
                type: mock

          /general_config:
            get:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: Handles generic route requests and delegates to the appropriate
              description: "CRUD operation based on the request parameters.\n\nArgs:\n\
                \    request (AuthorizedRequest): The authorized request object.\n\
                \    kwargs (dict): Additional keyword arguments.\n\nReturns:\n  \
                \  Response: The response from the CRUD operation."
            post:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: Handles generic route requests and delegates to the appropriate
              description: "CRUD operation based on the request parameters.\n\nArgs:\n\
                \    request (AuthorizedRequest): The authorized request object.\n\
                \    kwargs (dict): Additional keyword arguments.\n\nReturns:\n  \
                \  Response: The response from the CRUD operation."
            put:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: Handles generic route requests and delegates to the appropriate
              description: "CRUD operation based on the request parameters.\n\nArgs:\n\
                \    request (AuthorizedRequest): The authorized request object.\n\
                \    kwargs (dict): Additional keyword arguments.\n\nReturns:\n  \
                \  Response: The response from the CRUD operation."
            delete:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                uri:
                  Fn::Sub: arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${APIHandler.Arn}/invocations
                passthroughBehavior: when_no_match
                httpMethod: POST
                contentHandling: CONVERT_TO_TEXT
                type: aws_proxy
              summary: Handles generic route requests and delegates to the appropriate
              description: "CRUD operation based on the request parameters.\n\nArgs:\n\
                \    request (AuthorizedRequest): The authorized request object.\n\
                \    kwargs (dict): Additional keyword arguments.\n\nReturns:\n  \
                \  Response: The response from the CRUD operation."
            options:
              consumes:
              - application/json
              produces:
              - application/json
              responses:
                '200':
                  description: 200 response
                  schema:
                    $ref: '#/definitions/Empty'
                  headers:
                    Access-Control-Allow-Methods:
                      type: string
                    Access-Control-Allow-Origin:
                      type: string
                    Access-Control-Allow-Headers:
                      type: string
                    Access-Control-Expose-Headers:
                      type: string
                    Access-Control-Max-Age:
                      type: string
                    Access-Control-Allow-Credentials:
                      type: string
              x-amazon-apigateway-integration:
                responses:
                  default:
                    statusCode: '200'
                    responseParameters:
                      method.response.header.Access-Control-Allow-Methods: '''GET,POST,PUT,DELETE,OPTIONS'''
                      method.response.header.Access-Control-Allow-Origin: '''http://localhost:3000'''
                      method.response.header.Access-Control-Allow-Headers: '''Access-Control-Allow-Origin,Authorization,Content-Type,X-Amz-Date,X-Amz-Security-Token,X-Api-Key'''
                      method.response.header.Access-Control-Expose-Headers: '''Authorization,Access-Control-Allow-Origin,Content-Type,Content-Disposition,Content-Length'''
                      method.response.header.Access-Control-Max-Age: '''600'''
                      method.response.header.Access-Control-Allow-Credentials: '''true'''
                requestTemplates:
                  application/json: '{"statusCode": 200}'
                passthroughBehavior: when_no_match
                type: mock

        definitions:
          Empty:
            type: object
            title: Empty Schema
        x-amazon-apigateway-binary-media-types:
        - multipart/form-data
        - application/octet-stream
        - application/x-tar
        - application/zip
        - audio/basic
        - audio/ogg
        - audio/mp4
        - audio/mpeg
        - audio/wav
        - audio/webm
        - image/png
        - image/jpg
        - image/jpeg
        - image/gif
        - video/ogg
        - video/mpeg
        - video/webm



  APIHandler:
    Type: AWS::Serverless::Function
    Properties:
      # Runtime: python3.12
      Runtime: python3.11
      Handler: app.app
      CodeUri: ./deployment.zip
      Tags:
        aws-chalice: version=1.30.0:stage=APP_STAGE_placeholder:app=APP_NAME_LOWERCASE_placeholder-backend
      Tracing: PassThrough
      Timeout: 60
      MemorySize: 256
      Environment:
        Variables:
          APP_NAME: APP_NAME_placeholder
          AI_ASSISTANT_NAME: AI_ASSISTANT_NAME_placeholder
          APP_VERSION: APP_VERSION_placeholder
          FLASK_APP: FLASK_APP_placeholder
          APP_DEBUG: APP_DEBUG_placeholder
          APP_STAGE: APP_STAGE_placeholder
          APP_SECRET_KEY: APP_SECRET_KEY_placeholder
          APP_SUPERADMIN_EMAIL: APP_SUPERADMIN_EMAIL_placeholder
          APP_FRONTEND_AUDIENCE: APP_FRONTEND_AUDIENCE_placeholder
          APP_CORS_ORIGIN: APP_CORS_ORIGIN_placeholder
          APP_DB_ENGINE: APP_DB_ENGINE_placeholder
          APP_DB_NAME: APP_DB_NAME_placeholder
          APP_DB_URI: APP_DB_URI_placeholder
          CURRENT_FRAMEWORK: CURRENT_FRAMEWORK_placeholder
          DEFAULT_LANG: DEFAULT_LANG_placeholder
          GIT_SUBMODULE_URL: GIT_SUBMODULE_URL_placeholder
          GIT_SUBMODULE_LOCAL_PATH: GIT_SUBMODULE_LOCAL_PATH_placeholder
          AWS_S3_CHATBOT_ATTACHMENTS_BUCKET: AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_placeholder
          SMTP_SERVER: SMTP_SERVER_placeholder
          SMTP_PORT: SMTP_PORT_placeholder
          SMTP_USER: SMTP_USER_placeholder
          SMTP_PASSWORD: SMTP_PASSWORD_placeholder
          SMTP_DEFAULT_SENDER: SMTP_DEFAULT_SENDER_placeholder
          FDA_API_KEY: FDA_API_KEY_placeholder
          OPENAI_API_KEY: OPENAI_API_KEY_placeholder
          OPENAI_MODEL: OPENAI_MODEL_placeholder
          OPENAI_TEMPERATURE: OPENAI_TEMPERATURE_placeholder
          GOOGLE_API_KEY: GOOGLE_API_KEY_placeholder
          GOOGLE_CSE_ID: GOOGLE_CSE_ID_placeholder
          LANGCHAIN_API_KEY: LANGCHAIN_API_KEY_placeholder
          LANGCHAIN_PROJECT: LANGCHAIN_PROJECT_placeholder
          HUGGINGFACE_API_KEY: HUGGINGFACE_API_KEY_placeholder
          HUGGINGFACE_DEFAULT_CHAT_MODEL: HUGGINGFACE_DEFAULT_CHAT_MODEL_placeholder
      Role:
        Fn::GetAtt:
        - LambdaExecutionRole
        # - DefaultRole
        - Arn
  APIHandlerInvokePermission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName:
        Ref: APIHandler
      Action: lambda:InvokeFunction
      Principal: apigateway.amazonaws.com
      SourceArn:
        Fn::Sub:
        - arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestAPIId}/*
        - RestAPIId:
            Ref: RestAPI
```

2. `scripts/aws_big_lambda/template-samconfig.toml`

```toml
# samconfig.toml

# More information about the configuration file can be found here:
# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html
version = 0.1

[default]
[default.global.parameters]
stack_name = "APP_NAME_LOWERCASE_placeholder-backend"

[default.build.parameters]
cached = true
parallel = true

[default.validate.parameters]
lint = true

[default.deploy.parameters]
capabilities = ["CAPABILITY_IAM"]
confirm_changeset = false
resolve_s3 = true
s3_prefix = "APP_NAME_LOWERCASE_placeholder-backend"
region = "us-east-1"
image_repositories = []
disable_rollback = false
force_upload = true
resolve_image_repos = true

[default.package.parameters]
resolve_s3 = true

[default.sync.parameters]
watch = true

[default.local_start_api.parameters]
warm_containers = "EAGER"

[default.local_start_lambda.parameters]
warm_containers = "EAGER"
```