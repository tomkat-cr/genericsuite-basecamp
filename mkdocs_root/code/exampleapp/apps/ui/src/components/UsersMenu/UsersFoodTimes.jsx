import React from 'react';

import * as gs from "genericsuite";
import users_food_times from "../../configs/frontend/users_food_times.json";
import users_food_times_admin from "../../configs/frontend/users_food_times_admin.json";
import { FoodMomentsSelect, FoodMomentDataPopulator } from '../SuperAdminOptions/FoodMoments.jsx';

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
// const console_debug_log = gs.loggingService.console_debug_log;


export function UsersFoodTimes_EditorData(isSuperUser) {
    // console_debug_log("UsersFoodTimes_EditorData");
    const registry = {
        "UsersFoodTimes": UsersFoodTimes,
        "FoodMomentDataPopulator": FoodMomentDataPopulator,
        "FoodMomentsSelect": FoodMomentsSelect,
    }
    return GetFormData(
        isSuperUser ? users_food_times_admin : users_food_times,
        registry,
        false
    );
}

export function UsersFoodTimes() {
    return {
        editorConfig: UsersFoodTimes_EditorData(false),
        component: UsersFoodTimesComponent
    };
}

export function UsersFoodTimesAdmin() {
    return {
        editorConfig: UsersFoodTimes_EditorData(true),
        component: UsersFoodTimesAdminComponent
    };
}

export const UsersFoodTimesComponent = ({ parentData }) => (
    <GenericCrudEditor
        editorConfig={UsersFoodTimes_EditorData(false)}
        parentData={parentData}
    />
)

export const UsersFoodTimesAdminComponent = ({ parentData }) => (
    <GenericCrudEditor
        editorConfig={UsersFoodTimes_EditorData(true)}
        parentData={parentData}
    />
)
