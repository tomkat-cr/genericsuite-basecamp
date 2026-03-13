import React from 'react';

import * as gs from "genericsuite";
import * as gsAi from "genericsuite-ai";

import dish_ingredients from "../../configs/frontend/dish_ingredients.json";
import { CalorieTotalSaveDbPostWrite } from './DailyMealIngredients.jsx';
import {
    CALORIE_UNITS,
    SERVING_SIZE_UNITS,
    INGREDIENT_TYPE,
} from '../../_constants/app_constants.jsx';
import { 
    totalCaloriesCalcInDishesIngredients
} from '../Health/MinimumDailyCalories.jsx';

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
const ChatBotButton = gsAi.ChatBotButton;
// const console_debug_log = gs.loggingService.console_debug_log;

export function DishIngredients_EditorData() {
    // console_debug_log("DishIngredients_EditorData");
    const registry = {
        "DishIngredients": DishIngredients, 
        "DishIngredientsDbPostWrite": DishIngredientsDbPostWrite, 
        "CALORIE_UNITS": CALORIE_UNITS,
        "SERVING_SIZE_UNITS": SERVING_SIZE_UNITS,
        "INGREDIENT_TYPE": INGREDIENT_TYPE,
        "ChatBotButton": ChatBotButton,
        "totalCaloriesCalcInDishesIngredients": totalCaloriesCalcInDishesIngredients,
    }
    return GetFormData(dish_ingredients, registry, false);
}

export const DishIngredients = ({parentData, handleFormPageActions}) => (
    <GenericCrudEditor
        editorConfig={DishIngredients_EditorData()}
        parentData={parentData}
        handleFormPageActions={handleFormPageActions}
    />
)

const DishIngredientsDbPostWrite = (data, editor, action) => {
    return CalorieTotalSaveDbPostWrite({
        data: data,
        editor: editor,
        action: action,
        totalCaloriesParentFieldname: "calories_value",
        totalCaloriesChildFieldname: "total_calories",
    });
}
