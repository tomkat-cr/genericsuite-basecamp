# Documentación de Configuración del Editor Genérico CRUD

Esta documentación proporciona especificaciones de configuración para los archivos JSON del Editor Genérico CRUD.

## Directorio de configuración

El directorio de configuración es donde se almacenan los archivos JSON del Editor Genérico CRUD. La estructura de directorio sugerida es:

```text
.
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

## Configuración del Frontend

La configuración del frontend define el comportamiento general del editor CRUD y es utilizada tanto por el frontend como por el backend.

La configuración del frontend se encuentra en el directorio `frontend`.

En el directorio de configuración del frontend, hay varios archivos JSON, la mayoría son configuraciones del editor CRUD, y hay tres archivos especiales:

* `app_constants.json`
* `general_constants.json`
* `general_config.json`

Consulta la sección [Directorio Frontend](./index.md#frontend-directory) en la guía [Generación y Configuración de GenericSuite App](./index.md) para más detalles.

### Validación

La configuración de validación define las reglas de validación para el editor CRUD.

Las interfaces de TypeScript para validar las configuraciones JSON del frontend se definen en el archivo [CrudEditorConfigInterface.ts](https://github.com/tomkat-cr/genericsuite-basecamp/blob/main/docs/code/configuration-guide/CrudEditorConfigInterface.ts) (`FrontendCrudEditorConfig`, `ParentKeyName`, `FieldElement`, `FieldType`).

Las clases de Python para validar las configuraciones JSON del frontend se definen en el archivo [crud_editor_config_classes.py](https://github.com/tomkat-cr/genericsuite-basecamp/blob/main/docs/code/configuration-guide/crud_editor_config_classes.py) (`FrontendCrudEditorConfig`, `ParentKeyName`, `FieldElement`, `FieldType`).

### Configuración General

Los archivos JSON para cada tabla o editor CRUD en el ejemplo son `users.json`, `users_config.json` y `users_profile.json`.

Para esos archivos, la sección de configuración general define el comportamiento global del editor CRUD.

Los siguientes atributos se utilizan en la sección de configuración general:

* **baseUrl**: La URL del enrutador de ReactJS para el editor CRUD.
	+ Ejemplo: `ai_chatbot_conversations`

* **title**: El título del editor CRUD, utilizado en la página de listado.
	+ Ejemplo: "AI Assistant Conversations" → "Conversaciones del Asistente AI"

* **name**: El nombre del componente del editor CRUD, utilizado como título en la página de envío del formulario.
	+ Ejemplo: "AI Assistant Conversation" → "Conversación del Asistente AI"

* **component**: El nombre del componente de ReactJS utilizado por el editor CRUD. Este componente es el pegamento entre el archivo .json y el registro de dependencias (o componentes relacionados).
	+ Ejemplo: `AiChatBotConversations`

* **dbApiUrl**: La URL del endpoint de la API con la que interactúa el editor CRUD.
	+ Ejemplo: `ai_chatbot_conversations`

* **primaryKeyName**: Nombre del parámetro de clave primaria para las llamadas a la API
    + Ejemplo: `id`

* **defaultOrder**: El orden predeterminado especifica los criterios de clasificación de los datos obtenidos de la base de datos en la página de listado.
	+ Ejemplo: `defaultOrder": "update_date|desc` ordena los datos por `update_date` en orden descendente.

* **mandatoryFilters**: Los filtros obligatorios se utilizan para restringir el acceso a ciertos campos o datos. Si se especifica, `mandatoryFiltersDbListPreRead` se añadirá a `dbListPreRead` y `mandatoryFiltersDbPreRead` se añadirá a las funciones específicas de `dbPreRead`.
	+ Ejemplo:
```json
"mandatoryFilters": {
    "user_id": "{CurrentUserId}"
},
```

* **userIdFilter**: Si se debe añadir el filtro de ID de usuario actual a la página de listado. Es una alternativa al ejemplo anterior dado para el atributo `mandatoryFilters`.
	+ Ejemplo: `true` o `false`

* **fieldElements**: Lista de elementos de campo a utilizar en el editor de listado secundario. Más detalles en la sección [Field Elements](#field-elements).

### Relaciones 1 a N

* **childComponents**: Lista de componentes secundarios relacionados con la tabla principal.
	+ Ejemplo: para tener listados secundarios con los componentes `Users History` y `Users Configuration` relacionados con la tabla principal `Users`:
```json
"childComponents": [
    "UsersUserHistory",
    "UsersConfig"
],
```

* **type**: tipo de editor. Use `child_listing` para los editores secundarios (relación 1 a muchos), o `master_listing` para el editor principal. Por defecto es `master_listing`.
	+ Ejemplo: `child_listing` o `master_listing`

* **subType**: indica al backend cómo almacenar la relación 1 a muchos. Use `array` para ítems de relación almacenados en la misma tabla padre como un elemento de arreglo. Use `table` para ítems de relación almacenados en una tabla diferente.
	+ Ejemplo: `array` o `table`

* **array_name**: nombre de atributo para el listado hijo tipo `array`. Por ejemplo, si la tabla padre es "table_x_header" y la tabla hija es "table_x_lines", el `array_name` podría ser "table_x_lines".
	+ Ejemplo: `table_x_lines`

* **parentUrl**: la URL de la tabla padre que se utilizará en ciertas funciones específicas (porque el nombre de la tabla padre está definido en el archivo JSON de backend como atributo `table_name` y el frontend no tiene acceso a él).
	+ Ejemplo: `users` para el endpoint `/v1/users`.

* **endpointKeyNames**: Arreglo de nombres de claves utilizado al hacer llamadas a la API al backend para obtener los ítems del listado hijo. Esto se usa para establecer la relación entre las tablas padre e hijo (relación 1 a muchos). Cada elemento del arreglo debe tener los siguientes atributos:
	+ `parameterName`: el nombre del parámetro que se utilizará en la llamada a la API del backend (endpoint) para identificar la clave primaria/clave de clasificación de la tabla padre.
	+ `parentElementName`: el nombre del atributo de la tabla padre cuyo valor se utilizará para identificar la clave primaria/clave de clasificación de la tabla padre.
	+ Ejemplo:
```json
"type": "child_listing",
"subType": "array",
"array_name": "users_config",
"parentUrl": "users",
"endpointKeyNames": [
    {
        "parameterName": "user_id",
        "parentElementName": "id"
    }
],
```

* **allow_duplicates**: Permitir duplicados en la creación de ítems del listado hijo. Por defecto es `false`.
	+ Ejemplo: `true` o `false`

### Elementos de Campo

Los elementos de campo definen los campos individuales utilizados en el editor CRUD.

* **name**: El nombre del elemento de campo.

* **label**: La etiqueta mostrada para el campo.

* **type**: El tipo de dato del campo o `field type` para el elemento de campo. Consulta [Field data types](#field-data-types) para más detalles.

* **required**: Si el campo es obligatorio para el envío.
	+ Ejemplo: `true`, `false`

* **listing**: Si el campo debe mostrarse en la página de listado.
	+ Ejemplo: `true`, `false`

* **readonly**: Si el campo debe ser de solo lectura.
	+ Ejemplo: `true`, `false`

* **primaryKey**: Si el campo es la clave primaria de la tabla.
	+ Ejemplo: `true`, `false`

* **default_value**: El valor por defecto a usar para el campo cuando se carga la página de datos del formulario.
	+ Ejemplo: `0` o `current_timestamp`. `current_timestamp` será reemplazado por la fecha/hora actuales.

* **hidden**: Si el campo debe estar oculto de la visualización.
	+ Ejemplo: `true`, `false`

* **formula**: para obtener el valor del campo desde un componente ReactJS. Consulta la sección [Formulas](#formulas) para más detalles.

#### Tipos de datos de campo

* **text**: genera un campo de entrada de texto (una sola línea).

* **textarea**: genera un campo de entrada de textarea (multilínea).

* **number**: genera un campo de entrada numérica (flotante).

* **integer**: genera un campo de entrada entero (sin decimales).

* **date**: genera un campo de entrada de fecha (solo fecha).

* **datetime-local**: genera un campo de entrada datetime-local (fecha y hora).

* **array**: genera un campo de arreglo multidimensional, como el tipo `dict` en Python.
    + Ejemplos: 
```json
"array": [
    {
        "key1": "value1",
        "key2": "value2"
    }
]
```
```json
"array": {
    "key1": {
        "key2": "value2"
    }
}
```

* **email**: genera un campo de entrada de correo electrónico (y lo valida durante la entrada).

* **label**: genera una etiqueta sin campo de entrada.

* **h1, h2, h3, h4, h5, h6**: generan un encabezado con el nivel especificado.

* **hr**: genera una regla horizontal.

* **_id**: genera un campo oculto con el valor de la clave primaria del objeto actual.

* **select**: genera un campo de entrada de selección a partir de una lista de opciones.

* **select_table**: genera un campo de entrada de selección a partir de una lista de ítems en una tabla relacionada.

* **select_component**: genera un campo de entrada de selección con un componente ReactJS que rellena las opciones desde la base de datos.

* **suggestion_dropdown**: genera un campo de entrada con un desplegable de sugerencias desde la base de datos o una llamada a API. Consulta la sección [Suggestion Dropdowns](#suggestion-dropdowns) para más detalles.

* **component**: muestra un valor generado por un componente ReactJS.

#### Definiciones de botones especiales

Hay botones especiales que pueden usarse en los elementos de campo. Estos botones aparecerán en la página de datos del formulario solo en el lado derecho del campo.

Los botones se habilitan mediante los atributos `chatbot_popup` y `google_popup` del elemento de campo, y los atributos `chatbot_prompt` y `google_prompt` se utilizan para definir el texto que se utilizará al llamar al correspondiente componente ReactJS.

Las definiciones de botones especiales son opcionales.

* **chatbot_popup**: genera un botón que utiliza el componente ReactJS `ChatBotButton` que abre un popup para interactuar con el AI Assistant. Por defecto es `false`.
	+ Ejemplo: `chatbot_popup: true`.

* **chatbot_prompt**: define el texto que se utilizará al llamar al componente ReactJS `ChatBotButton`.
	+ Ejemplo: `chatbot_prompt: "Dame toda la información para el tema %s"`. __NOTA__: `%s` será reemplazado por el valor del campo.

* **google_popup**: genera un botón que llamará al componente ReactJS `SearchEngineButton`. Por defecto es `false`.
	+ Ejemplo: `google_popup: true`

* **google_prompt**: define el texto que se utilizará al llamar al componente ReactJS `SearchEngineButton`.
	+ Ejemplo: `google_prompt: "%s calories en KCAL, cantidad de porción y unidad de porción"`. __NOTA__: `%s` será reemplazado por el valor del campo.

### Desplegables de sugerencias

Los desplegables de sugerencias se utilizan para rellenar el valor del campo de entrada con sugerencias mostradas en una lista desplegable poblada por una base de datos o una llamada a API mientras el usuario escribe.

Las sugerencias se rellenan desde una URL de API definida en el atributo `filter_api_url`, y el atributo `filter_api_request_method` define el método HTTP a utilizar para llamar a la API.

El atributo `suggestion_id_fieldname` define el nombre del campo en la respuesta de la API que se utilizará para identificar la clave del elemento seleccionado en el desplegable.

El atributo `suggestion_desc_fieldname` define el nombre del campo en la respuesta de la API que se utilizará para mostrar el nombre del elemento seleccionado en el desplegable.

El atributo `filter_search_param_name` define el nombre del parámetro que se utilizará en la llamada a la API para identificar el término de búsqueda.

El atributo `filter_search_other_param` es un diccionario que define los otros parámetros a usar en la llamada a la API para identificar el término de búsqueda.

El atributo `autocomplete_fields` es un diccionario que define los campos que se completarán desde el elemento seleccionado en el desplegable. La clave es el nombre del campo en el formulario, y el valor es el nombre del campo de la respuesta de la API.

```json
{
    "name": "name",
    "required": true,
    "label": "Name",
    "readonly": false,
    "listing": true,
    "type": "suggestion_dropdown",
    "suggestion_id_fieldname": "_id",
    "suggestion_desc_fieldname": "name",
    "filter_api_url": "user_ingredients",
    "filter_api_request_method": "GET",
    "filter_search_param_name": "name",
    "filter_search_other_param": {
        "like": "1",
        "user_id": "{CurrentUserId}"
    },
    "autocomplete_fields": {
        "calories_value": "calories_value",
        "calories_unit": "calories_unit",
        "serving_size": "serving_size",
        "serving_size_unit": "serving_size_unit",
        "brand_name": "brand_name",
        "observations": "observations"
    },
    "chatbot_popup": true,
    "aux_component": "ChatBotButton",
    "chatbot_prompt": "Dame las %s calorías en KCAL incluyendo la cantidad de porción y la unidad de porción. Busca primero en mis ingredientes, si no está, busca con la herramienta web_search.",
    "google_popup": true,
    "google_prompt": "%s calorías KCAL"
},
```

### Funciones específicas

Funciones que amplían la funcionalidad del editor CRUD desde la perspectiva del frontend. Están destinadas a usarse antes y después de las operaciones de base de datos: leer, escribir, eliminar y validaciones.

Cada valor de función específica es una lista (arrays) de funciones ReactJS que se ejecutarán en el orden en que aparecen.

Todas las funciones específicas son opcionales.

* **dbListPreRead**: Antes de leer datos desde la base de datos en la página de listado. Un buen lugar para filtros ocultos.
	+ Ejemplo:
```json
"dbListPreRead": [
    "UsersDbListPreRead"
],
```

* **dbListPostRead**: Después de leer datos desde la base de datos en la página de listado. Al final de la lista, `timestampDbListPostRead` siempre se añadirá para realizar la conversión de Timestamp a Date de los campos de tipo `date` y `datetime-local`.

* **dbPreRead**: Antes de leer datos desde la base de datos en formData. Si hay algún error, muestra el mensaje de error.

* **dbPostRead**: Después de leer datos desde la base de datos en formData. Si hay algún error, muestra el mensaje de error. Al final de la lista, `timestampDbPostRead` siempre se añadirá para realizar la conversión de Timestamp a Date de los campos de tipo `date` y `datetime-local`.

* **dbPreValidations**: Validación de valores de campos de FormData antes de realizar una operación de Delete. Si hay algún error, impide que se elimine la fila de la base de datos.
	+ Ejemplo:
```json
"dbPreValidations": [
    "UsersValidations"
],
```

* **validations**: Validación de valores de campos de FormData antes de escribir en la base de datos. Si hay algún error, impide la escritura en la base de datos y se mantiene en FormData.
	+ Ejemplo:
```json
"validations": [
    "UsersPasswordValidations"
]
```

* **dbPreWrite**: Antes de escribir en la base de datos, tras una validación exitosa. Si hay algún error, muestra el mensaje de error, impide la escritura en la base de datos y se mantiene en FormData.
	+ Ejemplo:
```json
"dbPreWrite": [
    "UsersDbPreWrite"
],
```
Al final de la lista, por defecto se añadirá `timestampDbPreWrite` para manejar la asignación de timestamp a los campos de tipo `date` y `datetime-local`. Si `update_date` no existe en el formulario, se asignará el timestamp actual.

* **dbPostWrite**: Después de una escritura exitosa en la base de datos. Si hay algún error, muestra el mensaje de error y se mantiene en FormData.
	+ Ejemplo:
```json
"dbPostWrite": [
    "UsersDbPostWrite"
],
```

### Formulas

Las Formulas se utilizan para calcular los valores de los campos a partir de otros campos.

Ejemplo: en un formulario de Pedido con una relación de 1 a muchos con las Líneas de Pedido, el campo `total` podría tener `totalCalcInOrderLine` en el atributo **formula** y el correspondiente componente ReactJS podría ser:

```jsx
export const totalCalcInOrderLine = () => {
    // Calcula el precio total de las líneas de pedido multiplicando el precio por la cantidad
    const response = (parseFloat(document.getElementsByName('price')[0].value) * parseFloat(document.getElementsByName('quantity')[0].value)).toFixed(2);
    return response;
}
```

Para calcular el `grand_total` de la página de datos del formulario, debe existir una función específica de `dbPostWrite` en el componente hijo de Líneas de Pedido, por ej. `granTotalFromOrderLines` y el componente ReactJS podría ser:

```jsx
const dbApiService = gs.dbService.dbApiService;
const genericFuncArrayDefaultValue = gs.genericEditorRfcSpecificFunc.genericFuncArrayDefaultValue;
const ACTION_DELETE = gs.generalConstants.ACTION_DELETE;
const ACTION_CREATE = gs.generalConstants.ACTION_CREATE;
const ACTION_UPDATE = gs.generalConstants.ACTION_UPDATE;

export const granTotalFromOrderLines = ({
    data,
    editor,
    action,
}) => {
    return new Promise((resolve, reject) => {
        let resp = genericFuncArrayDefaultValue(data);
        let grand_total = 0;
        const parentId = editor.parentData[editor.endpointKeyNames[0].parentElementName];
        let childFilter = {};
        childFilter[editor.endpointKeyNames[0].parameterName] = parentId;
        switch(action) {
            case ACTION_CREATE:
            case ACTION_UPDATE:
            case ACTION_DELETE:
                const db = new dbApiService({ url: editor.parentUrl });
                // Obtener los datos del ítem padre
                db.getOne({id: parentId}).then( 
                    data => {
                        if (!data['resultset']) {
                            resp.error = true;
                            resp.errorMsg = (resp.errorMsg === '' ? '' : '<br>') + 
                                `Cannot read Parent Table ID: ${parentId}`;
                        }
                        if (resp.error) {
                            reject(resp);
                        } else {
                            // Obtener los datos de los ítems hijos
                            const db2 = new dbApiService({ url: editor.dbApiUrl });
                            db2.getAll(childFilter).then( 
                                data2 => {
                                    // Calcular el total general sumando los ítems hijos
                                    grand_total = data2['resultset'].reduce( (total, row) => {
                                        total += (row["quantity"] * row["price"]);
                                        return total;
                                    }, 0)
                                    // Actualizar el ítem padre con el grand total
                                    let itemToSave = (data['resultset']);
                                    itemToSave["grand_total"] = grand_total.toFixed(2);
                                    delete itemToSave["_id"];
                                    db.updateRow(parentId, itemToSave).then(
                                        _ => {
                                            // Refrescar el padre (tabla principal) form data una vez que los ítems hijos se actualicen en la base de datos
                                            resp['otherData']['refresh'] = true;
                                            resolve(resp);
                                        },
                                        error => {
                                            resp.error = true;
                                            resp.errorMsg = error;
                                            reject(resp)
                                        }
                                    );
                                },
                                error => {
                                    resp.error = true;
                                    resp.errorMsg = error;
                                    reject(resp)
                                }
                            );
                        }
                    },
                    error => {
                        resp.error = true;
                        resp.errorMsg = error;
                        reject(resp)
                    }
                );
                break;
            default:
                resolve(resp);
        }
    });
}
```

## Configuración Backend

Esta configuración es utilizada exclusivamente por el backend.

### Validación

Las interfaces de TypeScript para validar las configuraciones JSON del backend se definen en el archivo [CrudEditorConfigInterface.ts](https://github.com/tomkat-cr/genericsuite-basecamp/blob/main/docs/code/configuration-guide/CrudEditorConfigInterface.ts) (`BackendCrudEditorConfig`).

Las clases de Python para validar las configuraciones JSON del backend se definen en el archivo [crud_editor_config_classes.py](https://github.com/tomkat-cr/genericsuite-basecamp/blob/main/docs/code/configuration-guide/crud_editor_config_classes.py) (`BackendCrudEditorConfig`).

### Atributos de la Configuración Backend

* **table_name**: nombre físico de la tabla en la base de datos.
	+ Ejemplo:
```json
    "table_name": "users",
```

* **creation_pk_name**: nombre de la columna/atributo en la base de datos utilizado como clave primaria para la tabla durante el proceso de creación.
	+ Ejemplo:
```json
    "creation_pk_name": "email",
```

* **projection_exclusion**: lista de atributos a excluir de la proyección.
	+ Ejemplo:
```json
    "projection_exclusion": [
        "passcode"
    ],
```

* **email_verification**: lista de atributos que deben validarse como direcciones de correo.
	+ Ejemplo:
```json
    "email_verification": [
        "email"
    ],
```

* **passwords**: lista de atributos que deben validarse como contraseñas.
	+ Ejemplo:
```json
    "passwords": [
        "passcode"
    ],
```

* **mandatory_fields**: lista de atributos que deben estar presentes en la tabla.
	+ Ejemplo:
```json
    "mandatory_fields": [
        "firstname",
        "lastname",
        "creation_date",
        "gender",
        "birthday",
        "email"
    ],
```

* **additional_query_params**: lista de atributos que se deben usar en las operaciones de consulta distintas de la clave primaria.
	+ Ejemplo:
```json
    "additional_query_params": [
        "email"
    ],
```

* **specific_function**: función específica a ejecutar antes y después de las operaciones de base de datos.
	+ Ejemplos:
```json
    "specific_function": "delete_params_file"
```
```json
    "specific_function": "app_other_specific_function"
```

**IMPORTANTE**: para funciones específicas no estándar como "delete_params_file", la función debe estar implementada en el backend:

```python
from genericsuite_ai.fastapilib.util.create_app import (
    create_app,
    create_handler
)

from app.config.config import Config

# Importa la función específica
from app.specific_functions import app_other_specific_function


settings = Config()
app = create_app(
    app_name=f"{settings.APP_NAME.lower()}-backend", settings=settings)

# Registra la función específica
app.custom_data['app_other_specific_function'] = app_other_specific_function

handler = create_handler(app)
```

## Ejemplos

Veamos algunos ejemplos de archivos de configuración usando una App hipotética [GenericSuite Example App](../../code/exampleapp/README.md) para seguir calorías y crear planes de comidas. Los archivos de configuración se encuentran en el directorio [exampleapp/apps/config_dbdef](../../code/exampleapp/apps/config_dbdef/README.md).

### Estructura de Directorios

```
exampleapp/apps/config_dbdef/
├── backend/
|   ├── ai_chatbot_conversations.json           # Conversaciones de IA Chatbot para la interfaz de Chatbot
|   ├── app_main_menu.json                      # Configuración del menú principal de la App
|   ├── clarifai_models.json                    # Modelos de IA de Clarifai
|   ├── daily_meal_ingredients.json             # Ingredientes de comidas diarias del usuario
|   ├── daily_meals.json                        # Lista de comidas diarias del usuario
|   ├── dish_ingredients.json                   # Ingredientes de los platos del usuario
|   ├── dishes.json                             # Lista de platos del usuario
|   ├── endpoints.json                          # Configuración de endpoints de la API backend de la App
|   ├── food_moments.json                       # Tipos de comida generales (o momentos)
|   ├── general_config.json                     # Parámetros de configuración dinámica de la App
|   ├── general_ingredients.json                # Ingredientes globales
|   ├── user_ingredients_all.json               # Todos los ingredientes del usuario
|   ├── user_ingredients.json                   # Ingredientes del usuario
|   ├── users_api_keys.json                     # Claves API del usuario
|   ├── users_config.json                       # Parámetros de configuración del usuario
|   ├── users_food_times.json                   # Tiempos típicos de ingesta de comidas del usuario
|   ├── users_profile.json                      # Página de perfil del usuario
|   ├── users_user_history.json                 # Historial de datos del usuario (objetivos, peso, etc.)
|   ├── users.json                              # Usuarios
├── frontend/
|   ├── ai_chatbot_conversations_complete.json  # Conversaciones de IA Chatbot para un editor CRUD
|   ├── ai_chatbot_conversations.json           # Conversaciones de IA Chatbot para la interfaz de Chatbot
|   ├── app_constants.json                      # Constantes generales de la App (planes de facturación, unidades, tipos, códigos, género, correos, URLs, etc.)
|   ├── clarifai_models.json                    # Modelos de IA de Clarifai
|   ├── daily_meal_ingredients.json             # Ingredientes de comidas diarias del usuario
|   ├── daily_meals.json                        # Lista de comidas diarias del usuario
|   ├── dish_ingredients.json                   # Ingredientes de los platos del usuario
|   ├── dishes.json                             # Lista de platos del usuario
|   ├── food_moments.json                       # Tipos de comida generales (o momentos)
|   ├── general_config.json                     # Parámetros de configuración dinámica de la App
|   ├── general_constants.json                  # Constantes generales de la App (true/false, yes/no, idiomas, géneros, etc.)
|   ├── general_ingredients.json                # Ingredientes globales
|   ├── user_ingredients_all.json               # Todos los ingredientes del usuario
|   ├── user_ingredients.json                   # Ingredientes del usuario
|   ├── users_api_keys.json                     # Claves API del usuario
|   ├── users_config.json                       # Parámetros de configuración del usuario
|   ├── users_food_times.json                   # Tiempos típicos de ingesta de comidas del usuario
|   ├── users_profile.json                      # Página de perfil del usuario
|   ├── users_user_history.json                 # Historial de datos del usuario (objetivos, peso, etc.)
|   ├── users.json                              # Usuarios
├── .gitignore
├── CHANGELOG.md
├── package.json
├── README.md
```

### backend/ai_chatbot_conversations.json

Conversaciones de IA Chatbot para la interfaz de Chatbot

```json
{
    "table_name": "ai_chatbot_conversations",
    "creation_pk_name": "_id",
    "additional_query_params": [
        "_id"
    ]
}
```

### backend/app_main_menu.json

Configuración del menú principal de la App

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
        "title": "Admin",
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
                "title": "Meal Types",
                "element": "FoodMoments_EditorData"
            },
            {
                "type": "editor",
                "sec_group": "admin",
                "title": "General Ingredients",
                "element": "GeneralIngredients_EditorData"
            },
            {
                "type": "editor",
                "sec_group": "admin",
                "title": "General Config",
                "element": "GeneralConfig_EditorData"
            },
            {
                "type": "editor",
                "sec_group": "admin",
                "title": "Clarifai Models",
                "element": "ClarifaiModels_EditorData"
            }
        ]
    },
    {
        "title": "Foods",
        "location": "top_menu",
        "type": "nav_dropdown",
        "sec_group": "users",
        "sub_menu_options": [
            {
                "type": "editor",
                "sec_group": "users",
                "title": "Ingredients",
                "element": "UserIngredients_EditorData"
            },
            {
                "type": "editor",
                "sec_group": "users",
                "title": "Dishes",
                "element": "Dishes_EditorData"
            },
            {
                "type": "editor",
                "sec_group": "users",
                "title": "Daily Meals",
                "element": "DailyMeals_EditorData"
            }
        ]
    },
    {
        "title": "ExampleApp Bot",
        "location": "top_menu",
        "type": "nav_link",
        "sec_group": "users",
        "path": "/chatbot",
        "element": "Chatbot"
    },
    {
        "title": "User Menu",
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
                "path": "/logout",
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

### backend/clarifai_models.json

Modelos de IA de Clarifai

```json
{
    "table_name": "clarifai_models",
    "creation_pk_name": "model_name",
    "additional_query_params": [
        "model_name"
    ]
}
```

### backend/daily_meal_ingredients.json

Ingredientes de comidas diarias del usuario

```json
{
    "table_name": "daily_meals"
}
```

### backend/daily_meals.json

Lista de comidas diarias del usuario

```json
{
    "table_name": "daily_meals"
}
```

### backend/dish_ingredients.json

Ingredientes de los platos del usuario

```json
{
    "table_name": "user_ingredients",
    "notes": "'dishes' are 'user_ingredients' with type 'D'"
}
```

### backend/dishes.json

Lista de platos del usuario

```json
{
    "table_name": "user_ingredients",
    "notes": "'dishes' are 'user_ingredients' with type 'D'",
    "creation_pk_name": "name",
    "additional_query_params": [
        "name"
    ]
}
```

### backend/endpoints.json

Configuración de endpoints de la API backend de la App

```json
[
    {
        "name": "food_moments",
        "url_prefix": "food_moments",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "food_moments"
                }
            }
        ]
    },
    {
        "name": "general_ingredients",
        "url_prefix": "general_ingredients",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "general_ingredients"
                }
            }
        ]
    },
    {
        "name": "user_ingredients",
        "url_prefix": "user_ingredients",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "user_ingredients"
                }
            }
        ]
    },
    {
        "name": "user_ingredients_all",
        "url_prefix": "user_ingredients_all",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "user_ingredients_all"
                }
            }
        ]
    },
    {
        "name": "dishes",
        "url_prefix": "dishes",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "dishes"
                }
            }
        ]
    },
    {
        "name": "dish_ingredients",
        "url_prefix": "dish_ingredients",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "dish_ingredients"
                }
            }
        ]
    },
    {
        "name": "daily_meals",
        "url_prefix": "daily_meals",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "daily_meals"
                }
            }
        ]
    },
    {
        "name": "daily_meal_ingredients",
        "url_prefix": "daily_meal_ingredients",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "daily_meal_ingredients"
                }
            }
        ]
    },
    {
        "name": "ai_chatbot_conversations",
        "url_prefix": "ai_chatbot_conversations",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "ai_chatbot_conversations"
                }
            }
        ]
    },
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
        "name": "users",
        "url_prefix": "users",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "users"
                }
            }
        ]
    },
    {
        "name": "users_config",
        "url_prefix": "users_config",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "users_config"
                }
            }
        ]
    },
    {
        "name": "users_food_times",
        "url_prefix": "users_food_times",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "users_food_times"
                }
            }
        ]
    },
    {
        "name": "users_user_history",
        "url_prefix": "users_user_history",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "users_user_history"
                }
            }
        ]
    },
    {
        "name": "users_api_keys",
        "url_prefix": "users_api_keys",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "users_api_keys"
                }
            }
        ]
    }, 
    {
        "name": "clarifai_models",
        "url_prefix": "clarifai_models",
        "routes": [
            {
                "endpoint": "/",
                "methods": ["GET", "POST", "PUT", "DELETE"],
                "handler_type": "GenericEndpointHelper",
                "view_func": "lib.util.generic_endpoint_builder.generic_route_handler",
                "params": {
                    "json_file": "clarifai_models"
                }
            }
        ]
    }
]
```

### backend/food_moments.json

Lista general de tipos de comida (o momentos)

```json
{
    "table_name": "food_moments",
    "creation_pk_name": "name",
    "additional_query_params": [
        "name"
    ]
}
```

### backend/general_config.json

Parámetros de configuración dinámica de la App

```json
{
    "table_name": "general_config",
    "creation_pk_name": "config_name",
    "additional_query_params": [
        "config_name"
    ],
    "specific_function": "delete_params_file"
}
```

### backend/general_ingredients.json

Ingredientes globales

```json
{
    "table_name": "general_ingredients",
    "creation_pk_name": "name",
    "additional_query_params": [
        "name"
    ]
}
```

### backend/user_ingredients_all.json

Todos los ingredientes del usuario

```json
{
    "table_name": "user_ingredients",
    "creation_pk_name": "name",
    "additional_query_params": [
        "name"
    ]
}
```

### backend/user_ingredients.json

Ingredientes del usuario

```json
{
    "table_name": "user_ingredients",
    "creation_pk_name": "name",
    "additional_query_params": [
        "name"
    ]
}
```

### backend/users_api_keys.json

Claves API del usuario

```json
{
    "table_name": "users_api_keys",
    "specific_function": "delete_params_file"
}
```

### backend/users_config.json

Parámetros de configuración del usuario

```json
{
    "table_name": "users",
    "specific_function": "delete_params_file"
}
```

### backend/users_food_times.json

Tiempos típicos de ingesta de comidas del usuario

```json
{
    "table_name": "users"
}
```

### backend/users_profile.json

Página de perfil del usuario

```json
{
    "table_name": "users",
    "creation_pk_name": "email",
    "projection_exclusion": [
        "passcode"
    ],
    "email_verification": [
        "email"
    ],
    "passwords": [
        "passcode"
    ],
    "mandatory_fields": [
        "firstname",
        "lastname",
        "creation_date",
        "gender",
        "birthday",
        "email",
        "height",
        "height_unit",
        "weight",
        "weight_unit",
        "training_days",
        "training_hour"
    ],
    "additional_query_params": [
        "email"
    ],
    "specific_function": "delete_params_file"
}
```

### backend/users_user_history.json

Historial de datos del usuario (objetivos, peso, etc.)

```json
{
    "table_name": "users"
}
```

### backend/users.json

Usuarios

```json
{
    "table_name": "users",
    "creation_pk_name": "email",
    "projection_exclusion": [
        "passcode"
    ],
    "email_verification": [
        "email"
    ],
    "passwords": [
        "passcode"
    ],
    "mandatory_fields": [
        "firstname",
        "lastname",
        "creation_date",
        "gender",
        "birthday",
        "email"
    ],
    "additional_query_params": [
        "email"
    ]
}
```

### frontend/ai_chatbot_conversations_complete.json

Conversaciones de IA Chatbot para un editor CRUD

```json
{
    "table_name": "ai_chatbot_conversations",
    "creation_pk_name": "_id",
    "additional_query_params": [
        "_id"
    ],
    "baseUrl": "ai_chatbot_conversations",
    "title": "ExampleApp Bot Conversations",
    "name": "ExampleApp Bot Conversation",
    "component": "ExampleApp Bot Conversations",
    "dbApiUrl": "ai_chatbot_conversations",
    "mandatoryFilters": {
        "user_id": "{CurrentUserId}"
    },
    "defaultOrder": "update_date|desc",
    "fieldElements": [
        {
            "name": "id",
            "label": "ID",
            "type": "_id",
            "listing": true,
            "required": true
        },
        {
            "name": "user_id",
            "label": "User ID",
            "type": "text",
            "listing": true,
            "required": true
        },
        {
            "name": "title",
            "label": "Title",
            "type": "text",
            "listing": true,
            "required": true
        },
        {
            "name": "creation_date",
            "required": true,
            "label": "Created",
            "type": "datetime-local",
            "listing": true
        },
        {
            "name": "update_date",
            "required": true,
            "label": "Last update",
            "type": "datetime-local",
            "listing": true
        },
        {
            "name": "messages",
            "required": true,
            "label": "Messages",
            "type": "array",
            "listing": true
        }
    ]
}
```

### frontend/ai_chatbot_conversations.json

Conversaciones de IA Chatbot para la interfaz de Chatbot

```json
{
    "baseUrl": "ai_chatbot_conversations",
    "title": "ExampleApp Bot Conversations",
    "name": "ExampleApp Bot Conversation",
    "component": "ExampleApp Bot Conversations",
    "dbApiUrl": "ai_chatbot_conversations",
    "mandatoryFilters": {
        "user_id": "{CurrentUserId}"
    },
    "defaultOrder": "update_date|desc",
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
            "name": "title",
            "required": true,
            "label": "Title",
            "type": "text",
            "readonly": true,
            "listing": true
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
            "listing": true
        },
        {
            "name": "messages",
            "required": true,
            "label": "Messages",
            "type": "array",
            "readonly": true,
            "listing": false
        }
    ]
}
```

### frontend/app_constants.json

Constantes generales de la App (planes de facturación, unidades, tipos, códigos, género, correos, URLs, etc.)

```json
{
    "WEIGHT_UNITS": {
        "kg": "Kg",
        "lb": "Libras"
    },
    "HEIGHT_UNITS": {
        "m": "Metros",
        "i": "Pulgadas"
    },
    "GENDERS": {
        "m": "Masculino",
        "f": "Femenino"
    },
    "CALORIE_UNITS": {
        "kcal": "Calorías (KCAL)",
        "kj": "KJoules (kj)"
    },
    "SERVING_SIZE_UNITS": {
        "g": "Gramos (g)",
        "u": "Unidad",
        "tsp": "Cucharadita",
        "tablespoon": "Cucharada",
        "bowl": "Cuenco (300 ml)",
        "cup": "Taza (200 ml)",
        "scup": "Taza pequeña (150 ml)",
        "ml": "Mililitros (ml)",
        "mg": "Miligramos (mg)",
        "ug": "Microgramos (ug)",
        "oz": "Onza (oz)",
        "lb": "Libra (lb)",
        "iu": "Unidades internacionales (iu)",
        "mlt": " Masa, longitud, tiempo (mlt)"
    },
    "INGREDIENT_TYPE": {
        "I": "Ingrediente",
        "D": "Plato"
    },
    "GOAL_CODES": {
        "-20-DEFAULT": "Perder peso:",
        "-10": "-10% descenso más lento pero más seguro (recomendado para conservar masa muscular y rendimiento)",
        "-20": "-20% quiere perder peso para que sea algo más rápido",
        "-30": "-30% urgencia para perder peso rápidamente o sufrir de obesidad",
        "+20-DEFAULT": "Ganar peso:",
        "+10": "+10% tiende a aumentar de peso o ha estado entrenando mucho tiempo y quiere ganar masa muscular",
        "+15": "+15% quiere ganar un poco más de peso",
        "+20": "+20% para ectomorfos o dificiles de ganar"
    },
    "BILLING_PLANS": {
        "free": "Gratis",
        "basic": "Básico",
        "premium": "Premium"
    },
    "ERROR_MESSAGES": {
        "ACCOUNT_INACTIVE": "Cuenta de usuario inactiva [L5]. Para activar su cuenta, póngase en contacto con support@exampleapp.com"
    },
    "APP_EMAILS": {
        "SUPPORT_EMAIL": "support@exampleapp.com",
        "INFO_EMAIL": "info@exampleapp.com"
    },
    "APP_VALID_URLS": {
        "APP_DOMAIN": "exampleapp.com",
        "APP_WEBSITE": "https://www.exampleapp.com"
    },
    "AI_PROMPT_TEMPLATES": {
        "ASSISTANT_YOU_ARE": "{assistant_name}. Usted es parte de ExampleApp, una App que permite a las personas registrar sus ingredientes de comida favoritos, recetas y comidas diarias, rastrear el consumo de calorías y crear menús con déficit calórico basados en ingredientes y recetas asequibles y preferidos. Proporciona experiencias potenciadas por IA a las personas usando grandes modelos de lenguaje, reconocimiento de voz, texto a imagen y imagen a texto, permitiéndoles interactuar por voz, texto o carga de imágenes.",
        "BOTTOM_LINE": "Si la información calórica no pudo recuperarse de la base de datos de la FDA, búscala en Internet y, si tampoco funciona, dedúcela de tu modelo."
    }
}
```

### frontend/clarifai_models.json

Modelos de IA de Clarifai

```json
{
    "baseUrl": "clarifai_models",
    "title": "Clarifai Models",
    "name": "Clarifai Model Configuration",
    "component": "ClarifaiModels",
    "dbApiUrl": "clarifai_models",
    "defaultOrder": "model_name|asc",
    "fieldElements": [
        {
            "name": "id",
            "required": true,
            "label": "ID",
            "type": "_id",
            "readonly": true
        },
        {
            "name": "model_name",
            "required": true,
            "label": "Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "active",
            "required": true,
            "label": "Active",
            "type": "select",
            "select_elements": "TRUE_FALSE",
            "readonly": false,
            "hidden": false,
            "default_value": "1",
            "listing": true
        },
        {
            "name": "user_id",
            "required": true,
            "label": "User ID",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "app_id",
            "required": true,
            "label": "App ID",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "model_id",
            "required": true,
            "label": "Model ID",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "model_version_id",
            "required": true,
            "label": "Model Version ID",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "model_url",
            "required": false,
            "label": "Model URL",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "notes",
            "required": false,
            "label": "Notes",
            "type": "text",
            "readonly": false,
            "listing": true
        }
    ]
}
```

### frontend/daily_meal_ingredients.json

Ingredientes de comidas diarias del usuario

```json
{
    "baseUrl": "daily_meal_ingredients",
    "title": "Meal Ingredients",
    "name": "Meal Ingredient",
    "dbApiUrl": "daily_meal_ingredients",
    "component": "DailyMealIngredients",
    "type": "child_listing",
    "subType": "array",
    "array_name": "meal_ingredients",
    "parentUrl": "daily_meals",
    "endpointKeyNames": [
        {
            "parameterName": "daily_meal_id",
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
            "name": "meal_type",
            "label": "Type",
            "required": true,
            "listing": true,
            "type": "suggestion_dropdown",
            "suggestion_id_fieldname": "_id",
            "suggestion_desc_fieldname": "name",
            "filter_api_url": "food_moments",
            "filter_api_request_method": "GET",
            "filter_search_param_name": "name",
            "filter_search_other_param": {
                "like": "1"
            }
        },            
        {
            "name": "name",
            "required": true,
            "label": "Name",
            "readonly": false,
            "listing": true,
            "type": "suggestion_dropdown",
            "suggestion_id_fieldname": "_id",
            "suggestion_desc_fieldname": "name",
            "filter_api_url": "user_ingredients_all",
            "filter_api_request_method": "GET",
            "filter_search_param_name": "name",
            "filter_search_other_param": {
                "like": "1",
                "user_id": "{CurrentUserId}"
            },
            "autocomplete_fields": {
                "calories_value": "calories_value",
                "calories_unit": "calories_unit",
                "serving_size": "serving_size",
                "serving_size_unit": "serving_size_unit",
                "brand_name": "brand_name",
                "observations": "observations"
            },
            "chatbot_popup": true,
            "aux_component": "ChatBotButton",
            "chatbot_prompt": "Dame las %s calorías en KCAL incluyendo la cantidad de porción y la unidad de porción. Busca primero en mis ingredientes, si no está, busca con la herramienta web_search.",
            "google_popup": true,
            "google_prompt": "%s calorías KCAL"
        },
        {
            "name": "calories_value",
            "required": true,
            "label": "Calories",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "calories_unit",
            "required": true,
            "label": "Calories Unit",
            "type": "select",
            "select_elements": "CALORIE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "kcal"
        },
        {
            "name": "serving_size",
            "required": true,
            "label": "Serving size",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "serving_size_unit",
            "required": true,
            "label": "Serving size unit",
            "type": "select",
            "select_elements": "SERVING_SIZE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "g"
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
            "name": "total_calories",
            "label": "Total",
            "type": "number",
            "readonly": true,
            "listing": true,
            "formula": "totalCaloriesCalcInDailyMealIngredients"
        },
        {
            "name": "brand_name",
            "required": false,
            "label": "Brand Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "observations",
            "required": false,
            "label": "Observations",
            "type": "textarea",
            "readonly": false,
            "listing": true
        }
    ],
    "dbPostWrite": [
        "DailyMealIngredientsDbPostWrite"
    ]
}
```

### frontend/daily_meals.json

Lista de comidas diarias del usuario

```json
{
    "baseUrl": "daily_meals",
    "title": "Daily Meals",
    "name": "Daily Meal",
    "component": "DailyMeals",
    "dbApiUrl": "daily_meals",
    "mandatoryFilters": {
        "user_id": "{CurrentUserId}"
    },
    "createReenter": true,
    "defaultOrder": "meal_date|desc",
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
            "name": "meal_date",
            "required": true,
            "label": "Date",
            "type": "date",
            "readonly": false,
            "listing": true
        },
        {
            "name": "total_calories",
            "label": "Total Calories",
            "type": "number",
            "readonly": true,
            "listing": true,
            "component": "UserDailyCaloriesAndCondition"
        },
        {
            "name": "minimun_daily_calories",
            "label": "Daily Calorie Goal",
            "type": "component",
            "component": "UserMinimumDailyCalories",
            "readonly": true,
            "listing": false
        },
        {
            "name": "observations",
            "required": false,
            "label": "Observations",
            "type": "textarea",
            "readonly": false,
            "listing": true
        }
    ],
    "childComponents": [
        "DailyMealIngredients"
    ]
}
```

### frontend/dish_ingredients.json

Ingredientes de los platos del usuario

```json
{
    "baseUrl": "dish_ingredients",
    "title": "Dish Ingredients",
    "name": "Dish Ingredient",
    "dbApiUrl": "dish_ingredients",
    "component": "DishIngredients",
    "type": "child_listing",
    "subType": "array",
    "array_name": "dish_ingredients",
    "parentUrl": "dishes",
    "endpointKeyNames": [
        {
            "parameterName": "dish_id",
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
            "name": "name",
            "required": true,
            "label": "Name",
            "readonly": false,
            "listing": true,
            "type": "suggestion_dropdown",
            "suggestion_id_fieldname": "_id",
            "suggestion_desc_fieldname": "name",
            "filter_api_url": "user_ingredients",
            "filter_api_request_method": "GET",
            "filter_search_param_name": "name",
            "filter_search_other_param": {
                "like": "1",
                "user_id": "{CurrentUserId}"
            },
            "autocomplete_fields": {
                "calories_value": "calories_value",
                "calories_unit": "calories_unit",
                "serving_size": "serving_size",
                "serving_size_unit": "serving_size_unit",
                "brand_name": "brand_name",
                "observations": "observations"
            },
            "chatbot_popup": true,
            "aux_component": "ChatBotButton",
            "chatbot_prompt": "Dame las %s calorías en KCAL incluyendo la cantidad de porción y la unidad de porción. Busca primero en mis ingredientes, si no está, busca con la herramienta web_search.",
            "google_popup": true,
            "google_prompt": "%s calorías KCAL"
        },
        {
            "name": "calories_value",
            "required": true,
            "label": "Calories",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "calories_unit",
            "required": true,
            "label": "Calories Unit",
            "type": "select",
            "select_elements": "CALORIE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "kcal"
        },
        {
            "name": "serving_size",
            "required": true,
            "label": "Serving size",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "serving_size_unit",
            "required": true,
            "label": "Serving size unit",
            "type": "select",
            "select_elements": "SERVING_SIZE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "g"
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
            "name": "total_calories",
            "label": "Total",
            "type": "number",
            "readonly": true,
            "listing": true,
            "formula": "totalCaloriesCalcInDishesIngredients"
        },
        {
            "name": "brand_name",
            "required": false,
            "label": "Brand Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "observations",
            "required": false,
            "label": "Observations",
            "type": "textarea",
            "readonly": false,
            "listing": true
        }
    ],
    "dbPostWrite": [
        "DishIngredientsDbPostWrite"
    ]
}
```

### frontend/dishes.json

Lista de platos del usuario

```json
{
    "baseUrl": "dishes",
    "title": "Dishes",
    "name": "Dish",
    "component": "Dishes",
    "dbApiUrl": "dishes",
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
            "name": "type",
            "required": true,
            "label": "Type",
            "type": "select",
            "select_elements": "INGREDIENT_TYPE",
            "readonly": true,
            "hidden": false,
            "default_value": "D"
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
            "name": "calories_value",
            "required": true,
            "label": "Calories",
            "type": "number",
            "readonly": false,
            "listing": true,
            "default_value": "0"
        },
        {
            "name": "calories_unit",
            "required": true,
            "label": "Calories Unit",
            "type": "select",
            "select_elements": "CALORIE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "kcal"
        },
        {
            "name": "serving_size",
            "required": true,
            "label": "Serving size",
            "type": "number",
            "readonly": false,
            "listing": true,
            "default_value": "1"
        },
        {
            "name": "serving_size_unit",
            "required": true,
            "label": "Serving size unit",
            "type": "select",
            "select_elements": "SERVING_SIZE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "u" 
        },
        {
            "name": "brand_name",
            "required": false,
            "label": "Brand Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "observations",
            "required": false,
            "label": "Observations",
            "type": "textarea",
            "readonly": false,
            "listing": true
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
        "DishIngredients"
    ],
    "dbPreValidations": [
        "UserIngredientsValidations"
    ]
}
```

### frontend/food_moments.json

Tipos de comida generales (o momentos)

```json
{
    "baseUrl": "food_moments",
    "title": "Food Moments",
    "name": "Food Moment",
    "component": "FoodMoments",
    "dbApiUrl": "food_moments",
    "fieldElements": [
        {
            "name": "id",
            "required": true,
            "label": "ID",
            "type": "_id",
            "readonly": true
        },
        {
            "name": "name",
            "required": true,
            "label": "Name",
            "type": "text",
            "readonly": false,
            "listing": true
        }
    ],
    "dbPreValidations": [
        "FoodMomentsValidations"
    ]
}
```

### frontend/general_config.json

Parámetros de configuración dinámica de la App

```json
{
    "baseUrl": "general_config",
    "title": "Configuration Parameters",
    "name": "Configuration Parameter",
    "component": "GeneralConfig",
    "dbApiUrl": "general_config",
    "defaultOrder": "config_name|asc",
    "fieldElements": [
        {
            "name": "id",
            "required": true,
            "label": "ID",
            "type": "_id",
            "readonly": true
        },
        {
            "name": "config_name",
            "required": true,
            "label": "Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "active",
            "required": true,
            "label": "Active",
            "type": "select",
            "select_elements": "TRUE_FALSE",
            "readonly": false,
            "hidden": false,
            "default_value": "1",
            "listing": true
        },
        {
            "name": "config_value",
            "required": true,
            "label": "Value",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "notes",
            "required": true,
            "label": "Notes",
            "type": "text",
            "readonly": false,
            "listing": true
        }
    ]
}
```

### frontend/general_constants.json

Constantes generales de la App (verdadero/falso, sí/no, idiomas, géneros, etc.)

```json
{
    "TRUE_FALSE": {
        "1": "Sí",
        "0": "No"
    },
    "YES_NO": {
        "y": "Sí",
        "n": "No"
    },
    "LANGUAGES": {
        "en": "Inglés",
        "es": "Español"
    },
    "GENDERS": {
        "m": "Masculino",
        "f": "Femenino"
    }
}
```

### frontend/general_ingredients.json

Ingredientes globales

```json
{
    "baseUrl": "general_ingredients",
    "title": "Ingredients (general)",
    "name": "Ingredient",
    "component": "GeneralIngredients",
    "dbApiUrl": "general_ingredients",
    "fieldElements": [
        {
            "name": "id",
            "required": true,
            "label": "ID",
            "type": "_id",
            "readonly": true
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
            "name": "calories_value",
            "required": true,
            "label": "Calories",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "calories_unit",
            "required": true,
            "label": "Calories Unit",
            "type": "select",
            "select_elements": "CALORIE_UNITS",
            "readonly": false,
            "listing": true
        },
        {
            "name": "serving_size",
            "required": true,
            "label": "Serving size",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "serving_size_unit",
            "required": true,
            "label": "Serving size unit",
            "type": "select",
            "select_elements": "SERVING_SIZE_UNITS",
            "readonly": false,
            "listing": true
        },
        {
            "name": "brand_name",
            "required": false,
            "label": "Brand Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "other_names",
            "required": false,
            "label": "Other Names",
            "type": "text",
            "readonly": false,
            "listing": true
        }
    ],
    "dbPreValidations": [
        "GeneralIngredientsValidations"
    ]
}
```

### frontend/user_ingredients_all.json

Todos los ingredientes del usuario

```json
{
    "baseUrl": "user_ingredients",
    "title": "Ingredients for Suggestions",
    "name": "Ingredient",
    "component": "UserIngredients",
    "dbApiUrl": "user_ingredients",
    "mandatoryFilters": {
        "user_id": "{CurrentUserId}"
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
            "name": "name",
            "required": true,
            "label": "Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "calories_value",
            "required": true,
            "label": "Calories",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "calories_unit",
            "required": true,
            "label": "Calories Unit",
            "type": "select",
            "select_elements": "CALORIE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "kcal" 
        },
        {
            "name": "serving_size",
            "required": true,
            "label": "Serving size",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "serving_size_unit",
            "required": true,
            "label": "Serving size unit",
            "type": "select",
            "select_elements": "SERVING_SIZE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "g" 
        },
        {
            "name": "brand_name",
            "required": false,
            "label": "Brand Name",
            "type": "text",
            "readonly": false,
            "listing": true
        }
    ]
}
```

### frontend/user_ingredients.json

Ingredientes del usuario

```json
{
    "baseUrl": "user_ingredients",
    "title": "Ingredients",
    "name": "Ingredient",
    "component": "UserIngredients",
    "dbApiUrl": "user_ingredients",
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
            "name": "type",
            "required": true,
            "label": "Type",
            "type": "select",
            "select_elements": "INGREDIENT_TYPE",
            "readonly": true,
            "hidden": false,
            "default_value": "I"
        },
        {
            "name": "name",
            "required": true,
            "label": "Name",
            "type": "suggestion_dropdown",
            "readonly": false,
            "listing": true,
            "suggestion_id_fieldname": "id",
            "suggestion_desc_fieldname": "description",
            "suggestion_name_fieldname": "food_name",
            "filter_api_url": "fda_food_query",
            "filter_search_param_name": "food_name",
            "filter_search_other_param": {
                "autocomplete": "1"
            },
            "autocomplete_fields": {
                "calories_value": "calories_value",
                "calories_unit": "calories_unit",
                "serving_size": "serving_size",
                "serving_size_unit": "serving_size_unit",
                "brand_name": "brand_name"
            },
            "chatbot_popup": true,
            "aux_component": "ChatBotButton",
            "chatbot_prompt": "Dame las %s calorías en KCAL incluyendo la cantidad de porción y la unidad de porción. Busca primero en la API FDA, si no está, busca con la herramienta web_search.",
            "google_popup": true,
            "google_prompt": "%s calorías KCAL"
        },
        {
            "name": "calories_value",
            "required": true,
            "label": "Calories",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "calories_unit",
            "required": true,
            "label": "Calories Unit",
            "type": "select",
            "select_elements": "CALORIE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "kcal" 
        },
        {
            "name": "serving_size",
            "required": true,
            "label": "Serving size",
            "type": "number",
            "readonly": false,
            "listing": true
        },
        {
            "name": "serving_size_unit",
            "required": true,
            "label": "Serving size unit",
            "type": "select",
            "select_elements": "SERVING_SIZE_UNITS",
            "readonly": false,
            "listing": true,
            "default_value": "g" 
        },
        {
            "name": "brand_name",
            "required": false,
            "label": "Brand Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "observations",
            "required": false,
            "label": "Observations",
            "type": "textarea",
            "readonly": false,
            "listing": true
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
    "dbPreValidations": [
        "UserIngredientsValidations"
    ]
}
```

### frontend/users_api_keys.json

Claves API del usuario

```json
{
    "baseUrl": "users_api_keys",
    "title": "User API Keys",
    "name": "User's API Key",
    "dbApiUrl": "users_api_keys",
    "component": "UsersApiKey",
    "type": "child_listing",
    "subType": "table",
    "endpointKeyNames": [
        {
            "parameterName": "user_id",
            "parentElementName": "id"
        }
    ],
    "primaryKeyName": "id",
    "defaultOrder": "access_token",
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
            "name": "access_token",
            "required": true,
            "label": "Access Token",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "active",
            "required": true,
            "label": "Active",
            "type": "select",
            "select_elements": "TRUE_FALSE",
            "default_value": "1",
            "readonly": false,
            "listing": true
        }
    ],
    "dbPreRead": [
        "UsersApiKeyDbPreRead"
    ]
}
```

### frontend/users_config.json

Parámetros de configuración del usuario

```json
{
  "baseUrl": "users_config",
  "title": "User Configurations",
  "name": "User's Configuration",
  "dbApiUrl": "users_config",
  "component": "UsersConfig",
  "type": "child_listing",
  "subType": "array",
  "array_name": "users_config",
  "parentUrl": "users",
  "endpointKeyNames": [
    {
      "parameterName": "user_id",
      "parentElementName": "id"
    }
  ],
  "primaryKeyName": "id",
  "defaultOrder": "config_name",
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
      "name": "config_name",
      "required": true,
      "label": "Name",
      "type": "text",
      "readonly": false,
      "listing": true
    },
    {
        "name": "config_value",
        "required": true,
        "label": "Value",
        "type": "text",
        "readonly": false,
        "listing": true
    }
  ]
}
```

### frontend/users_food_times.json

Tiempos típicos de ingesta de comidas del usuario

```json
{
  "baseUrl": "food_times",
  "title": "Food Times",
  "name": "Food Time",
  "dbApiUrl": "users_food_times",
  "component": "UsersFoodTimes",
  "type": "child_listing",
  "subType": "array",
  "array_name": "food_times",
  "parentUrl": "users",
  "endpointKeyNames": [
    {
      "parameterName": "user_id",
      "parentElementName": "id"
    }
  ],
  "primaryKeyName": "food_moment_id",
  "fieldElements": [
    {
      "name": "meal_type",
      "label": "Type",
      "required": true,
      "listing": true,
      "type": "suggestion_dropdown",
      "suggestion_id_fieldname": "_id",
      "suggestion_desc_fieldname": "name",
      "filter_api_url": "food_moments",
      "filter_api_request_method": "GET",
      "filter_search_param_name": "name",
      "filter_search_other_param": {
          "like": "1"
      }
    },
    {
      "name": "meal_time",
      "required": true,
      "label": "Time",
      "type": "text",
      "readonly": false,
      "listing": true
    }
  ]
}
```

### frontend/users_profile.json

Página de perfil del usuario

```json
{
    "baseUrl": "users",
    "title": "User Profiles",
    "name": "User Profile",
    "component": "Users",
    "dbApiUrl": "users",
    "updateItem": "1",
    "fieldElements": [
        {
            "name": "id",
            "required": true,
            "label": "ID",
            "type": "_id",
            "hidden": true,
            "readonly": true
        },
        {
            "name": "firstname",
            "required": true,
            "label": "First Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "lastname",
            "required": true,
            "label": "Last Name",
            "type": "text",
            "readonly": false,
            "listing": true
        },
        {
            "name": "email",
            "required": true,
            "label": "Email",
            "type": "email",
            "readonly": false,
            "listing": true
        },
        {
            "name": "birthday",
            "required": true,
            "label": "Birthday",
            "type": "date",
            "readonly": false
        },
        {
            "name": "gender",
            "required": true,
            "label": "Gender",
            "type": "select",
            "select_elements": "GENDERS",
            "readonly": false,
            "listing": false
        },
        {
            "name": "training_days",
            "required": true,
            "label": "Training Days",
            "type": "text",
            "readonly": false
        },
        {
            "name": "training_hour",
            "required": true,
            "label": "Training Hour",
            "type": "text",
            "readonly": false
        },
        {
            "name": "height",
            "required": true,
            "label": "Height",
            "type": "number",
            "readonly": false,
            "listing": false
        },
        {
            "name": "height_unit",
            "required": true,
            "label": "Height Unit",
            "type": "select",
            "select_elements": "HEIGHT_UNITS",
            "readonly": false,
            "listing": false
        },
        {
            "name": "weight",
            "required": true,
            "label": "Weight",
            "type": "number",
            "readonly": false
        },
        {
            "name": "weight_unit",
            "required": true,
            "label": "Weight Unit",
            "type": "select",
            "select_elements": "WEIGHT_UNITS",
            "readonly": false
        },
        {
            "name": "minimun_daily_calories",
            "label": "Daily Calorie Goal",
            "type": "component",
            "component": "UserMinimumDailyCalories",
            "readonly": true,
            "listing": false
        },
        {
            "name": "goal_code",
            "required": true,
            "label": "Goal",
            "type": "select",
            "select_elements": "GOAL_CODES",
            "readonly": false,
            "listing": false
        }, 
        {
            "name": "goals",
            "required": true,
            "label": "Goal Observation",
            "type": "textarea",
            "readonly": false,
            "listing": false
        }, 
        {
            "name": "language",
            "required": true,
            "label": "Preferred Language",
            "type": "select",
            "select_elements": "LANGUAGES",
            "readonly": false,
            "listing": false
        }, 
        {
            "name": "plan",
            "required": true,
            "label": "Billing Plan",
            "type": "select",
            "select_elements": "BILLING_PLANS",
            "default_value": "free",
            "readonly": true,
            "listing": true
        }, 
        {
            "name": "status",
            "required": true,
            "label": "Active",
            "type": "select",
            "select_elements": "TRUE_FALSE",
            "default_value": "1",
            "readonly": true
        },
        {
            "name": "openai_api_key",
            "required": false,
            "label": "OpenAI API Key",
            "type": "text"
        }, 
        {
            "name": "openai_model",
            "required": false,
            "label": "OpenAI Model (defaults to gpt-4o-mini)",
            "type": "text"
        }, 
        {
            "name": "creation_date",
            "required": true,
            "label": "Client Since",
            "type": "datetime-local",
            "readonly": true,
            "hidden": false,
            "default_value": "current_timestamp",
            "listing": true
        },
        {
            "name": "label0",
            "type": "hr"
        },
        {
            "name": "label1",
            "label": "PASWORD CHANGE",
            "type": "label"
        },
        {
            "name": "passcode",
            "required": false,
            "label": "New password",
            "type": "password",
            "force_value": ""
        },
        {
            "name": "passcode_repeat",
            "required": false,
            "label": "Repeat new password",
            "type": "password",
            "force_value": ""
        }
    ],
    "childComponents": [
        "UsersFoodTimes",
        "UsersUserHistory",
        "UsersApiKey"
    ],
    "dbListPreRead": [
        "UsersDbListPreRead"
    ],
    "dbPreWrite": [
        "UsersDbPreWrite"
    ],
    "dbPostWrite": [
        "UsersDbPostWrite"
    ],
    "dbPreValidations": [
        "UsersValidations"
    ],
    "validations": [
        "UsersPasswordValidations"
    ]
}
```

