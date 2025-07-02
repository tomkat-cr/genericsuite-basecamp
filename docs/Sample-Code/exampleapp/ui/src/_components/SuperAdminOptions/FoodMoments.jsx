import React from 'react';

import * as gs from "genericsuite";
import food_moments from "../../configs/frontend/food_moments.json";

const dbApiService = gs.dbService.dbApiService;
const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
const GenericSelectGenerator = gs.genericEditorRfcSelector.GenericSelectGenerator;
const GenericSelectDataPopulator = gs.genericEditorRfcSelector.GenericSelectDataPopulator;
const genericFuncArrayDefaultValue = gs.genericEditorRfcSpecificFunc.genericFuncArrayDefaultValue;
const convertId = gs.idUtilities.convertId;
const ACTION_DELETE = gs.generalConstants.ACTION_DELETE;

export function FoodMoments_EditorData() {

    const registry = {
        "FoodMoments": FoodMoments, 
        "FoodMomentsValidations": FoodMomentsValidations, 
    }
    return GetFormData(food_moments, registry, 'FoodMoments_EditorData');
}

export const FoodMoments = () => (
    <GenericCrudEditor editorConfig={FoodMoments_EditorData()} />
)

export const FoodMomentsSelect = (props) => (
    <GenericSelectGenerator
        filter={typeof props.filter == 'undefined' ? null : props.filter}
        show_description={typeof props.show_description == 'undefined' ? false : props.show_description}
        editorConfig={FoodMoments_EditorData()}
    />
)

export const FoodMomentDataPopulator = () => (
    <GenericSelectDataPopulator editorConfig={FoodMoments_EditorData()} />
)

const FoodMomentsValidations = (data, editor, action) => {
    // Food_Moments pre-deletion validations
    return new Promise((resolve, reject) => {
        let resp = genericFuncArrayDefaultValue(data);
        switch(action) {
            case ACTION_DELETE:
                const db = new dbApiService({ url: `${editor.dbApiUrl}/food_moment_in_user` });
                const food_moment_id = convertId(data['_id'])
                db.getOne({id: food_moment_id}).then( 
                    data => {
                        if (data['resultset']['rows_count'] > 0) {
                            resp.error = true;
                            resp.errorMsg = (resp.errorMsg === '' ? '' : '<BR/>') + 
                                'Cannot delete because it\'s referenced ' + 
                                data['resultset']['rows_count'] + ' times in ' +
                                ' in User\'s Food Time.';
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
