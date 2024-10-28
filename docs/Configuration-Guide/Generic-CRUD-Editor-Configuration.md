# Generic CRUD Editor Configuration Documentation

This documentation provides configuration specifications for the Generic CRUD Editor JSON files.

## Configuration directory

Here's where the Generic CRUD Editor JSON files are stored. The directory structure is:

```
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

## Frontend Configuration

This configuration section defines the overall behavior of the CRUD editor and is used by both the frontend and backend.

### General Configuration

The general configuration section defines the overall behavior of the CRUD editor.

* **baseUrl**: The ReactJS router URL for the CRUD editor.
	+ Example: `ai_chatbot_conversations`

* **title**: The title of the CRUD editor, used in the listing page.
	+ Example: "AI Assistant Conversations"

* **name**: The name of the CRUD editor component, used as a title in the form submission page.
	+ Example: "AI Assistant Conversation"

* **component**: The ReactJS component name used by the CRUD editor. This component is the glue with the .json file and the registry of dependencies (or related components).
	+ Example: `AiChatBotConversations`

* **dbApiUrl**: The API endpoint URL that the CRUD editor interacts with.
	+ Example: `ai_chatbot_conversations`

* **primaryKeyName**: Primary Key parameter name for API calls
    + Example: `id`

* **defaultOrder**: The default order specifies the sorting criteria for data retrieved from the database in the listing page.
	+ Example: `defaultOrder": "update_date|desc` sorts data by `update_date` in descending order.

* **mandatoryFilters**: Mandatory filters are used to restrict access to certain fields or data. If it's specified, `mandatoryFiltersDbListPreRead` will be added to `dbListPreRead` and `mandatoryFiltersDbPreRead` will be added to `dbPreRead` specific functions.
	+ Example: to specify the ID of the current user who should be authorized to access the filtered data.
```json
"mandatoryFilters": {
    "user_id": "{CurrentUserId}"
},
```

* **userIdFilter**: Whether the current user ID filter should be added to the listing page. It's an alternative to the previous example given to the `mandatoryFilters` attribute.
    + Example: `true` or `false`

* **fieldElements**: List of field elements to be used in the child listing editor. More details in the [Field Elements](#field-elements) section.

### 1 to N Relationships

* **childComponents**: List of child components related to the main table.
    + Example: to have child listings with the `Users History` and `Users Configuration` components related to the `Users` main table:
```json
"childComponents": [
    "UsersUserHistory",
    "UsersConfig"
],
```

* **type**: editor type. Use `child_listing` for the child editors (1-to-many relationship), of `master_listing` for the main editor. Defaults to `master_listing`.
    + Example: `child_listing` or `master_listing`

* **subType**: tells the backend how to store the 1-to-many relationship. Use `array` for relationship items stored in the same parent table as an array element. Use `table` for relationship items stored in a different table.
    + Example: `array` or `table`

* **array_name**: attribute name for the `array` type child listing. For example, if the parent table is "table_x_header" and the child table is "table_x_lines", the `array_name` could be "table_x_lines".
    + Example: `table_x_lines`

* **parentKeyNames**: Parent Key Names, to stabllish the relationship between the parent and child tables. It's used for the child editors (1-to-many relationship). It must have the following attributes:
    + `parentUrl`: the parent table URL to be used in the backend API call.
    + `parameterName`: the name of the parameter to be used in the backend API call to identify the parent table Primary Key.
    + `parentElementName`: the name of the parent table's primary key column/attribute.<BR/><BR/>
    + Example:
```json
"type": "child_listing",
"subType": "array",
"array_name": "users_config",
"parentKeyNames": [
{
    "parentUrl": "users",
    "parameterName": "user_id",
    "parentElementName": "id"
}
],
```

* **allow_duplicates**: Allow duplicates in the child listing items creation. Defaults to `false`.
    + Example: `true` or `false`

### Field Elements

Field elements define the individual fields used in the CRUD editor.

* **name**: The name of the field element.

* **label**: The label displayed for the field.

* **type**: The data type of the field. Check [Field data types](#field-data-types) for more details.

* **required**: Whether the field is required for submission.
	+ Example: `true`, `false`

* **listing**: Whether the field should be displayed in the listing page.
	+ Example: `true`, `false`

* **readonly**: Whether the field should be read-only.
	+ Example: `true`, `false`

* **default_value**: The default value to use for the field when the form data page is loaded.
	+ Example: `0` or `current_timestamp`. `current_timestamp` will be replaced by the current date/time.

* **hidden**: Whether the field should be hidden from display.
	+ Example: `true`, `false`

* **formula**: to get the fields's value from a ReactJS component. Check the [Formulas](#formulas) section for more details.

#### Field data types

* **text**: generates a text input field (single line).

* **textarea**: generates a textarea input field (multi line).

* **number**: generates a number input field (float).

* **integer**: generates a integer input field (no decimals).

* **date**: generates a date input field (date only).

* **datetime-local**: generates a datetime-local input field (date and time).

* **email**: generates an email input field (and validates it during the input).

* **label**: generates a label with no input field.

* **hr**: generates a horizontal rule.

* **_id**: generates a hidden input field with the current object's primary key value.

* **select**: generates a select input field from a list of options.

* **select_component**: generates a select input field with a ReactJS component that populates the options from the database.

* **suggestion_dropdown**: generates a input field with a suggestion dropdown from the database or a API call. Check the [Suggestion Dropdowns](#suggestion-dropdowns) section for more details.

* **component**: shows a value generated from a ReactJS component.

#### Special buttons definitions

There are special buttons that can be used in the field elements. These buttoms will appear in the form data page only at the right side of the field.

The buttons are enabled by the `chatbot_popup` and `google_popup` attributes of the field element, and the `chatbot_prompt` and `google_prompt` attributes are used to define the text that will be used when calling the corresponding button ReacTJS component.

The special buttons definitions are optional.

* **chatbot_popup**: generates a button that uses the `ChatBotButton` ReactJS component which opens a popup to interact with the AI Assistant. Defaults to `false`.
    + Example: `chatbot_popup: true`.

* **chatbot_prompt**: defines the text that will be used when calling the `ChatBotButton` ReactJS component.
    + Example: `chatbot_prompt: "Give me all the information for the %s topic"`. __NOTE__: `%s` will be replaced by the field value.

* **google_popup**: generates a button that will call the `SearchEngineButton` ReactJS component. Defaults to `false`.
    + Example: `google_popup: true`

* **google_prompt**: defines the text that will be used when calling the `SearchEngineButton` ReactJS component.
    + Example: `google_prompt: "%s calories in KCAL, serving size amount and serving size unit"`. __NOTE__: `%s` will be replaced by the field value.

### Suggestion Dropdowns

Suggestion dropdowns are used to fill the input field value with suggestions shown in a dropdown list populated by a database or API call while the user is typing.

The suggestions are populated from a API URL defined in the `filter_api_url` attribute, and the `filter_api_request_method` attribute defines the HTTP method to be used to call the API.

The `suggestion_id_fieldname` attribute defines the field name in the API response that will be used to identify the selected item Key in the dropdown.

The `suggestion_desc_fieldname` attribute defines the field name in the API response that will be used to display the selected item Name in the dropdown.

The `filter_search_param_name` attribute defines the parameter name to be used in the API call to identify the search term.

The `filter_search_other_param` attribute is a dictionary that defines the other parameters to be used in the API call to identify the search term.

The `autocomplete_fields` attribute is a dictionary that defines the fields to be populated from the selected item in the dropdown. The key is the field name in form, and the value is the field name from the API call response.

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
    "chatbot_prompt": "Give me the %s calories in KCAL including the serving size amount and serving size unit. Look first in my ingredients, if it's not there, look for it with the web_search Tool.",
    "google_popup": true,
    "google_prompt": "%s calories KCAL"
},
```

### Specific functions

Functions that extend the generic CRUD editor functionality from the frontend perspective. They're intended to be used before and after the database operations: read, write, delete, and validations.

Each specific function value is a lists (arrays) of ReactJS functions that will be executed in the order they are listed.

All the specific functions are all optional.

* **dbListPreRead**: Before read data from database in the listing. Good place for hidden filters.
    + Example:
```json
"dbListPreRead": [
    "UsersDbListPreRead"
],
```

* **dbListPostRead**: After read data from database in the listing. At the end of the list, the `timestampDbListPostRead` will be always appended to perform the Timestamp to Date convertion of `date` and `datetime-local` type fields.

* **dbPreRead**: Before read data from database in formData. If any error, shows the error message.

* **dbPostRead**: After read data from database in formData. If any error, shows the error message. At the end of the list, the `timestampDbPostRead` will be always appended to perform the Timestamp to Date convertion of `date` and `datetime-local` type fields.

* **dbPreValidations**: FormData field values validation before doing a Delete operation. If any error, prevents the database row to be deleted.
    + Example:
```json
"dbPreValidations": [
    "UsersValidations"
],
```

* **validations**: FormData field values validation before write to the database. If any error, prevents the database write and stays in FormData.
    + Example:
```json
"validations": [
    "UsersPasswordValidations"
]
```

* **dbPreWrite**: Before write to database, after a successfull validation. If any error, shows the error message, prevents the database write and stays in FormData.
    + Example:
```json
"dbPreWrite": [
    "UsersDbPreWrite"
],
```
At the end of the list, the `timestampDbPreWrite` will be appended by default to handle the timestamp assignment to `date` and `datetime-local` type fields. If `update_date` doesn't exist in the form, the current timestamp will be assigned to it.

* **dbPostWrite**: After a successful write to database. If any error, shows the error message and stays in FormData.
    + Example:
```json
"dbPostWrite": [
    "UsersDbPostWrite"
],
```

### Formulas

Formulas are used to calculate the fields' values from other fields.

Example: in a Order form with a 1 to many relationship with Order Lines, the `total` field could have the `totalCalcInOrderLine` in the **formula** attribute and the corresponding ReactJS component could be:
```jsx
export const totalCalcInOrderLine = () => {
    // Calculate the total price of the order lines by multiplying the price by the quantity
    const response = (parseFloat(document.getElementsByName('price')[0].value) * parseFloat(document.getElementsByName('quantity')[0].value)).toFixed(2);
    return response;
}
```
To calculate the form data page's `grand_total`, there must be a `dbPostWrite` specific function in the Order Lines child component, e.g.  `granTotalFromOrderLines` and the ReactJS componet could be: 
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
        const parentId = editor.parentData[editor.parentKeyNames[0].parentElementName];
        let childFilter = {};
        childFilter[editor.parentKeyNames[0].parameterName] = parentId;
        switch(action) {
            case ACTION_CREATE:
            case ACTION_UPDATE:
            case ACTION_DELETE:
                const db = new dbApiService({ url: editor.parentUrl });
                // Get the parent item data
                db.getOne({id: parentId}).then( 
                    data => {
                        if (!data['resultset']) {
                            resp.error = true;
                            resp.errorMsg = (resp.errorMsg === '' ? '' : '<BR/>') + 
                                `Cannot read Parent Table ID: ${parentId}`;
                        }
                        if (resp.error) {
                            reject(resp);
                        } else {
                            // Get the child items data
                            const db2 = new dbApiService({ url: editor.dbApiUrl });
                            db2.getAll(childFilter).then( 
                                data2 => {
                                    // Calculate the grand total summing the child items
                                    grand_total = data2['resultset'].reduce( (total, row) => {
                                        total += (row["quantity"] * row["price"]);
                                        return total;
                                    }, 0)
                                    // Update the parent item with the grand total
                                    let itemToSave = (data['resultset']);
                                    itemToSave["grand_total"] = grand_total.toFixed(2);
                                    delete itemToSave["_id"];
                                    db.updateRow(parentId, itemToSave).then(
                                        _ => {
                                            // Refresh the parent (main table) form data once the child items are updated in the database
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

## Backend Configuration

This configuration is used by the backend exclusively.

* **table_name**: physical table name in the database.
    + Example:
```json
    "table_name": "users",
```

* **creation_pk_name**: column/attribute name in the database used as the primary key for the table during the creation process.
    + Example:
```json
    "creation_pk_name": "email",
```

* **projection_exclusion**: list of attributes to exclude from the projection.
    + Example:
```json
    "projection_exclusion": [
        "passcode"
    ],
```

* **email_verification**: list of attributes to be validated as email addresses.
    + Example:
```json
    "email_verification": [
        "email"
    ],
```

* **passwords**: list of attributes to be validated as passwords.
    + Example:
```json
    "passwords": [
        "passcode"
    ],
```

* **mandatory_fields**: list of attributes that must be present in the table.
    + Example:
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

* **additional_query_params**: list of attributes to be used in the query operations other than the primary key.
    + Example:
```json
    "additional_query_params": [
        "email"
    ],
```

* **specific_function**: specific function to be executed before and after  database operations.
    + Example:
```json
    "specific_function": "delete_params_file"
```
