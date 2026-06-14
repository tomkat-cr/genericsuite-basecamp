import React, { useContext } from 'react';

import * as gs from "genericsuite";
import daily_meals from "../../configs/frontend/daily_meals.json";
import {
    UserMinimumDailyCalories,
    UserDailyCaloriesAndCondition,
    getUserDataOrCache,
} from '../Health/UserDailyCaloriesAndCondition.jsx';
import {
    DailyMealIngredients,
} from './DailyMealIngredients.jsx';

const useUser = gs.UserContext.useUser;
const getUserData = gs.authenticationService.getUserData;
const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
const MainSectionContext = gs.genericEditorRfcProvider.MainSectionContext;
const genericFuncArrayDefaultValue = gs.genericEditorRfcSpecificFunc.genericFuncArrayDefaultValue;
// const console_debug_log = gs.loggingService.console_debug_log;

export function DailyMeals_EditorData() {
    // console_debug_log("DailyMeals_EditorData");
    const registry = {
        "DailyMeals": DailyMeals, 
        "DailyMealIngredients": DailyMealIngredients,
        "DailyMealsDbListPreRead": DailyMealsDbListPreRead,
        "UserMinimumDailyCalories": UserMinimumDailyCalories,
        "UserDailyCaloriesAndCondition": UserDailyCaloriesAndCondition,
    }
    return GetFormData(daily_meals, registry, 'DailyMeals_EditorData');
}

export const DailyMeals = () => {
// console_debug_log(">>>--> DailyMeals RUN...") // Todo: why 4 times?
    return (<GenericCrudEditor editorConfig={DailyMeals_EditorData()} />)
}

export const DailyMealsDbListPreRead = () => {
    const {
        getCachedData,
        putCachedData,
        typeofCachedData,
    } = useContext(MainSectionContext);
    const { currentUser } = useUser();

    return (data, editor, action) => {
        // Preload user data
        return new Promise((resolve, reject) => {
            let resp = genericFuncArrayDefaultValue(data);
            const setUserData = (error) => {
                reject(error);
            }
            const setErrorMsg = (error) => {
                resolve(resp);
            }
            getUserDataOrCache(
                currentUser,
                typeofCachedData,
                getUserData,
                getCachedData,
                putCachedData,
                setUserData,
                setErrorMsg,
            );
        });
    }
}
