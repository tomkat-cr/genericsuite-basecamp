import React from 'react';

import * as gs from "genericsuite";
import * as gsAi from "genericsuite-ai";

import daily_meal_ingredients from "../../configs/frontend/daily_meal_ingredients.json";
import { FoodMomentsSelect, FoodMomentDataPopulator } from '../SuperAdminOptions/FoodMoments.jsx';
import { UserIngredientsDataPopulator, UserIngredientsSelect } from './UserIngredients.jsx';
import {
    CALORIE_UNITS,
    SERVING_SIZE_UNITS,
} from '../../_constants/app_constants.jsx';
import { 
    totalCaloriesCalcInDailyMealIngredients,
} from '../Health/MinimumDailyCalories.jsx';

const dbApiService = gs.dbService.dbApiService;
const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
const genericFuncArrayDefaultValue = gs.genericEditorRfcSpecificFunc.genericFuncArrayDefaultValue;
const console_debug_log = gs.loggingService.console_debug_log;
const convertCaloriesToUnit = gs.conversions.convertCaloriesToUnit;
const ACTION_DELETE = gs.generalConstants.ACTION_DELETE;
const ACTION_CREATE = gs.generalConstants.ACTION_CREATE;
const ACTION_UPDATE = gs.generalConstants.ACTION_UPDATE;
const ChatBotButton = gsAi.ChatBotButton;

export function DailyMealIngredients_EditorData() {
    // console_debug_log("DailyMealIngredients_EditorData");
    const registry = {
        "DailyMealIngredients": DailyMealIngredients, 
        "FoodMomentDataPopulator": FoodMomentDataPopulator,
        "FoodMomentsSelect": FoodMomentsSelect,
        "UserIngredientsDataPopulator": UserIngredientsDataPopulator,
        "UserIngredientsSelect": UserIngredientsSelect,
        "DailyMealIngredientsDbPostWrite": DailyMealIngredientsDbPostWrite,
        "CALORIE_UNITS": CALORIE_UNITS,
        "SERVING_SIZE_UNITS": SERVING_SIZE_UNITS,
        "ChatBotButton": ChatBotButton,
        "totalCaloriesCalcInDailyMealIngredients": totalCaloriesCalcInDailyMealIngredients,
    }
    return GetFormData(daily_meal_ingredients, registry, false);
}

export function DailyMealIngredients() {
    return {
        editorConfig: DailyMealIngredients_EditorData(),
        component: DailyMealIngredientsComponent
    };
}

export const DailyMealIngredientsComponent = ({parentData, handleFormPageActions}) => (
    <GenericCrudEditor
        editorConfig={DailyMealIngredients_EditorData()}
        parentData={parentData}
        handleFormPageActions={handleFormPageActions}
    />
)

const DailyMealIngredientsDbPostWrite = (data, editor, action) => {
    return CalorieTotalSaveDbPostWrite({
        data: data,
        editor: editor,
        action: action,
        totalCaloriesParentFieldname: "total_calories",
        totalCaloriesChildFieldname: "total_calories",
    });
}

export const CalorieTotalSaveDbPostWrite = ({
    data,
    editor,
    action,
    totalCaloriesParentFieldname,
    totalCaloriesChildFieldname,
}) => {
    const debug = false;
    return new Promise((resolve, reject) => {
        let resp = genericFuncArrayDefaultValue(data);
        let total_calories = 0;
        if (debug) {
            console_debug_log("CalorieTotalSaveDbPostWrite - editor.parentData");
            console_debug_log(editor.parentData);
        }
        // const daily_meal_id = editor.parentData["id"]
        const parentId = editor.parentData[editor.parentKeyNames[0].parentElementName];
        let childFilter = {};
        childFilter[editor.parentKeyNames[0].parameterName] = parentId;
        switch(action) {
            case ACTION_CREATE:
            case ACTION_UPDATE:
            case ACTION_DELETE:
                const db = new dbApiService({ url: editor.parentUrl });
                // db.getOne({id: daily_meal_id}).then( 
                db.getOne({id: parentId}).then( 
                    data => {
                        if (!data['resultset']) {
                            resp.error = true;
                            resp.errorMsg = (resp.errorMsg === '' ? '' : '<BR/>') + 
                                // `Cannot read Parent Table ID: ${daily_meal_id}`;
                                `Cannot read Parent Table ID: ${parentId}`;
                        }
                        if (resp.error) {
                            reject(resp);
                        } else {
                            // const db2 = new dbApiService({ url: `daily_meal_ingredients` });
                            const db2 = new dbApiService({ url: editor.dbApiUrl });
                            // db2.getAll({daily_meal_id: daily_meal_id}).then( 
                            db2.getAll(childFilter).then( 
                                data2 => {
                                    total_calories = data2['resultset'].reduce( (total, row) => {
                                        total += convertCaloriesToUnit(
                                            row[totalCaloriesChildFieldname],
                                            row['calories_unit'],
                                            data['resultset']['calories_unit'],
                                        );
                                        return total;
                                    }, 0)
                                    let itemToSave = (data['resultset']);
                                    itemToSave[totalCaloriesParentFieldname] = total_calories.toFixed(2);
                                    delete itemToSave["_id"];
                                    if (debug) {
                                        console_debug_log("CalorieTotalSaveDbPostWrite - itemToSave:");
                                        console_debug_log(itemToSave);
                                    }
                                    // db.updateRow(daily_meal_id, itemToSave).then(
                                    db.updateRow(parentId, itemToSave).then(
                                        _ => {
                                            // To refresh parent component and show the new calorie total
                                            resp['otherData']['refresh'] = true;
                                            if (debug) {
                                                console_debug_log(`CalorieTotalSaveDbPostWrite | resp:`, resp);
                                            }
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
