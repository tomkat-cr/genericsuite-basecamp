import React from 'react';

import * as gs from "genericsuite";
import users_food_times from "../../configs/frontend/users_food_times.json";
import { FoodMomentsSelect, FoodMomentDataPopulator } from '../SuperAdminOptions/FoodMoments.jsx';

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
// const console_debug_log = gs.loggingService.console_debug_log;


export function UsersFoodTimes_EditorData() {
    // console_debug_log("UsersFoodTimes_EditorData");
    const registry = {
        "UsersFoodTimes": UsersFoodTimes, 
        "FoodMomentDataPopulator": FoodMomentDataPopulator,
        "FoodMomentsSelect": FoodMomentsSelect,
    }
    return GetFormData(users_food_times, registry, false);
}

export function UsersFoodTimes() {
    return {
        editorConfig: UsersFoodTimes_EditorData(),
        component: UsersFoodTimesComponent
    };
}

export const UsersFoodTimesComponent = ({parentData}) => (
    <GenericCrudEditor
        editorConfig={UsersFoodTimes_EditorData()}
        parentData={parentData}
    />
)
