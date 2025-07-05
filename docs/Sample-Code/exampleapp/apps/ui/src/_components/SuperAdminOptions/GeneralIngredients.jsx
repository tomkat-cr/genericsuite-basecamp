import React from 'react';

import * as gs from "genericsuite";
import general_ingredients from "../../configs/frontend/general_ingredients.json";
import { CALORIE_UNITS, SERVING_SIZE_UNITS } from '../../_constants/app_constants.jsx';

const dbApiService = gs.dbService.dbApiService;
const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
const GenericSelectGenerator = gs.genericEditorRfcSelector.GenericSelectGenerator;
const GenericSelectDataPopulator = gs.genericEditorRfcSelector.GenericSelectDataPopulator;
const genericFuncArrayDefaultValue = gs.genericEditorRfcSpecificFunc.genericFuncArrayDefaultValue;
const convertId = gs.idUtilities.convertId;
const ACTION_DELETE = gs.generalConstants.ACTION_DELETE;

export function GeneralIngredients_EditorData() {
    // console_debug_log("GeneralIngredients_EditorData");
    const registry = {
        "GeneralIngredients": GeneralIngredients, 
        "GeneralIngredientsValidations": GeneralIngredientsValidations,
        "CALORIE_UNITS": CALORIE_UNITS,
        "SERVING_SIZE_UNITS": SERVING_SIZE_UNITS,
    }
    return GetFormData(general_ingredients, registry, 'GeneralIngredients_EditorData');
}

export const GeneralIngredients = () => (
    <GenericCrudEditor editorConfig={GeneralIngredients_EditorData()} />
)

export const GeneralIngredientsSelect = (props) => (
    <GenericSelectGenerator
        filter={typeof props.filter == 'undefined' ? null : props.filter}
        show_description={typeof props.show_description == 'undefined' ? false : props.show_description}
        editorConfig={GeneralIngredients_EditorData()}
    />
)

export const GeneralIngredientsDataPopulator = () => (
    <GenericSelectDataPopulator editorConfig={GeneralIngredients_EditorData()} />
)

const GeneralIngredientsValidations = (data, editor, action) => {
    // general_ingredients pre-deletion validations
    return new Promise((resolve, reject) => {
        let resp = genericFuncArrayDefaultValue(data);
        switch(action) {
            case ACTION_DELETE:
                const db = new dbApiService({ url: `${editor.dbApiUrl}/general_ingredients_in_user` });
                const users_ingredient_id = convertId(data['_id'])
                db.getOne({id: users_ingredient_id}).then( 
                    data => {
                        if (data['resultset']['rows_count'] > 0) {
                            resp.error = true;
                            resp.errorMsg = (resp.errorMsg === '' ? '' : '<BR/>') + 
                                'Cannot delete because it\'s referenced ' + 
                                data['resultset']['rows_count'] + ' times in ' +
                                ' in User\'s Ingredients.';
                        }
                        if (resp.error) {
                            reject(resp);
                        } else {
                            resolve(resp);
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
