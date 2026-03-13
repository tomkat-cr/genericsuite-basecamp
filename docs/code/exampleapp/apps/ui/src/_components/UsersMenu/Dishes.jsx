import React from 'react';

import * as gs from "genericsuite";
import dishes from "../../configs/frontend/dishes.json";
import {
    CALORIE_UNITS,
    SERVING_SIZE_UNITS,
    INGREDIENT_TYPE,
} from '../../_constants/app_constants.jsx';

import {
    DishIngredients,
} from './DishIngredients.jsx';

import {
    UserIngredientsValidations
} from './UserIngredients.jsx';

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
// const console_debug_log = gs.loggingService.console_debug_log;

export function Dishes_EditorData() {
    // console_debug_log("Dishes_EditorData");
    const registry = {
        "Dishes": Dishes, 
        "DishIngredients": DishIngredients,
        "UserIngredientsValidations": UserIngredientsValidations,
        "CALORIE_UNITS": CALORIE_UNITS,
        "SERVING_SIZE_UNITS": SERVING_SIZE_UNITS,
        "INGREDIENT_TYPE": INGREDIENT_TYPE,
    }
    return GetFormData(dishes, registry, 'Dishes_EditorData');
}

export const Dishes = () => (
    <GenericCrudEditor editorConfig={Dishes_EditorData()} />
)
