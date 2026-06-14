import React from 'react';

import * as gs from "genericsuite";
import users_profile from "../../configs/frontend/users_profile.json";
import {
    GENDERS,
    GOAL_CODES,
    HEIGHT_UNITS,
    WEIGHT_UNITS,
} from '../../constants/app_constants.jsx';
import { UserMinimumDailyCalories } from '../Health/UserDailyCaloriesAndCondition.jsx';
import { UsersDbPostWrite } from '../SuperAdminOptions/Users.jsx';
import { UsersFoodTimes } from './UsersFoodTimes.jsx';
import { UsersUserHistory } from './UsersUserHistory.jsx';

// const authenticationService = gs.authenticationService.authenticationService;
const useUser = gs.UserContext.useUser;
const GenericSinglePageEditor = gs.genericEditorSinglepage.GenericSinglePageEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
// const console_debug_log = gs.loggingService.console_debug_log;
const BILLING_PLANS = gs.appConstants.BILLING_PLANS;
const LANGUAGES = gs.generalConstants.LANGUAGES;
const TRUE_FALSE = gs.generalConstants.TRUE_FALSE;

const UsersConfig = gs.UsersConfig;
// const UsersDbPostWrite = gs.UsersDbPostWrite;
const UsersDbListPreRead = gs.UsersDbListPreRead;
const UsersDbPreWrite = gs.UsersDbPreWrite;
const UsersValidations = gs.UsersValidations;
const UsersPasswordValidations = gs.UsersPasswordValidations;
const UsersApiKey = gs.UsersApiKey;

export function UsersProfile_EditorData() {
    const registry = {
        // User's Profile
        "WEIGHT_UNITS": WEIGHT_UNITS,
        "HEIGHT_UNITS": HEIGHT_UNITS,
        "GENDERS": GENDERS,
        "GOAL_CODES": GOAL_CODES,
        "LANGUAGES": LANGUAGES,
        "TRUE_FALSE": TRUE_FALSE,
        "BILLING_PLANS": BILLING_PLANS,
        "UserMinimumDailyCalories": UserMinimumDailyCalories,
        "UsersFoodTimes": UsersFoodTimes,
        "UsersUserHistory": UsersUserHistory,
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
    // const { currentUserValue } = authenticationService;
    const { currentUser } = useUser();
    return (
        <>
            <GenericSinglePageEditor
                // id={currentUserValue.id}
                id={currentUser.id}
                editorConfig={UsersProfile_EditorData()}
            />
        </>
    );
}
