import React from 'react';

import * as gs from "genericsuite";
import users_user_history from "../../configs/frontend/users_user_history.json";
import users_user_history_admin from "../../configs/frontend/users_user_history_admin.json";
import {
    GOAL_CODES,
    WEIGHT_UNITS,
} from '../../constants/app_constants.jsx';

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;

export function UsersUserHistory_EditorData(isSuperUser) {
    // console_debug_log("UsersUserHistory_EditorData");
    const registry = {
        "UsersUserHistory": UsersUserHistory,
        "WEIGHT_UNITS": WEIGHT_UNITS,
        "GOAL_CODES": GOAL_CODES,
    }
    return GetFormData(
        isSuperUser ? users_user_history_admin : users_user_history,
        registry,
        false
    );
}

export function UsersUserHistory() {
    return {
        editorConfig: UsersUserHistory_EditorData(false),
        component: UsersUserHistoryComponent
    };
}

export function UsersUserHistoryAdmin() {
    return {
        editorConfig: UsersUserHistory_EditorData(true),
        component: UsersUserHistoryAdminComponent
    };
}

export const UsersUserHistoryComponent = ({ parentData }) => (
    <GenericCrudEditor
        editorConfig={UsersUserHistory_EditorData(false)}
        parentData={parentData}
    />
)

export const UsersUserHistoryAdminComponent = ({ parentData }) => (
    <GenericCrudEditor
        editorConfig={UsersUserHistory_EditorData(true)}
        parentData={parentData}
    />
)
