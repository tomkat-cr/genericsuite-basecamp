import React from 'react';

import * as gs from "genericsuite";
import users_profile from "../../configs/frontend/users_profile.json";
import { UsersDbPostWrite } from '../SuperAdminOptions/Users';

// App-specific GS GENDERS:
import {
    GENDERS,
} from '../../constants/app_constants.jsx';
// // Standad GS GENDERS:
// const GENDERS = gs.generalConstants.GENDERS;

// // App - specific GS BILLING_PLANS:
import {
    BILLING_PLANS,
} from '../../constants/app_constants.jsx';
// // Standad GS BILLING_PLANS:
// const BILLING_PLANS = gs.appConstants.BILLING_PLANS;

const useUser = gs.UserContext.useUser;
const GenericSinglePageEditor = gs.genericEditorSinglepage.GenericSinglePageEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
const LANGUAGES = gs.generalConstants.LANGUAGES;
const TRUE_FALSE = gs.generalConstants.TRUE_FALSE;

const UsersConfig = gs.UsersConfig;
const UsersDbListPreRead = gs.UsersDbListPreRead;
const UsersDbPreWrite = gs.UsersDbPreWrite;
const UsersValidations = gs.UsersValidations;
const UsersPasswordValidations = gs.UsersPasswordValidations;
const UsersApiKey = gs.UsersApiKey;

export function UsersProfile_EditorData() {
    const registry = {
        // User's Profile
        "GENDERS": GENDERS,
        "LANGUAGES": LANGUAGES,
        "TRUE_FALSE": TRUE_FALSE,
        "BILLING_PLANS": BILLING_PLANS,
        "UsersDbPostWrite": UsersDbPostWrite,
        "UsersConfig": UsersConfig,
        "UserProfileEditor": UserProfileEditor,
        "UsersDbListPreRead": UsersDbListPreRead,
        "UsersDbPreWrite": UsersDbPreWrite,
        "UsersValidations": UsersValidations,
        "UsersPasswordValidations": UsersPasswordValidations,
        "UsersApiKey": UsersApiKey,
    }
    return GetFormData(users_profile, registry, 'UserProfileEditor');
}

export const UserProfileEditor = (props) => {
    const { currentUser } = useUser();
    return (
        <>
            <GenericSinglePageEditor
                id={currentUser.id}
                editorConfig={UsersProfile_EditorData()}
            />
        </>
    );
}
