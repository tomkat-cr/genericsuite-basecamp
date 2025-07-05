import React from 'react';

import * as gs from "genericsuite";
import users_user_history from "../../configs/frontend/users_user_history.json";
import {
    WEIGHT_UNITS,
    GOAL_CODES,
} from '../../_constants/app_constants.jsx';

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;

export function UsersUserHistory_EditorData() {
    // console_debug_log("UsersUserHistory_EditorData");
    const registry = {
        "UsersUserHistory": UsersUserHistory, 
        "WEIGHT_UNITS": WEIGHT_UNITS,
        "GOAL_CODES": GOAL_CODES,
    }
    return GetFormData(users_user_history, registry, false);
}

export function UsersUserHistory() {
    return {
        editorConfig: UsersUserHistory_EditorData(),
        component: UsersUserHistoryComponent
    };
}

export const UsersUserHistoryComponent = ({parentData}) => (
    <GenericCrudEditor
        editorConfig={UsersUserHistory_EditorData()}
        parentData={parentData}
    />
)
