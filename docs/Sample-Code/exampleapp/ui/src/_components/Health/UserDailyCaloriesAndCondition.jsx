import React, { useEffect, useState, useContext } from 'react';

import * as gs from "genericsuite";

import {
    MinimumDailyCalories,
    getMinimumDailyCalories,
    CalorieCondition,
} from '../Health/MinimumDailyCalories.jsx';

const getUserData = gs.authenticationService.getUserData;
// const authenticationService = gs.authenticationService.authenticationService;

const useUser = gs.UserContext.useUser;
const MainSectionContext = gs.genericEditorRfcProvider.MainSectionContext;
const console_debug_log = gs.loggingService.console_debug_log;

const convertWeight = gs.conversions.convertWeight;
const convertHeight = gs.conversions.convertHeight;
const interpretString = gs.conversions.interpretString;
const timestampToDate = gs.dateTimestamp.timestampToDate;

const ERROR_MSG_CLASS = gs.classNameConstants.ERROR_MSG_CLASS;
const MSG_SELECT_AN_OPTION = gs.generalConstants.MSG_SELECT_AN_OPTION;

const debug = false;
const userDataCacheName = '_currentUserData';

export const prepareUserDataForMDC = (userData) => {
    const height_unit = userData['height_unit'];
    const weight_unit = userData['weight_unit'];
    let height;
    let weight;
    if (height_unit === null || height_unit === '' || height_unit === MSG_SELECT_AN_OPTION) {
        height = 0;
    } else {
        height = convertHeight(
            userData['height'],
            userData['height_unit'],
            'm',
        );
    }
    if (weight_unit === null || weight_unit === '' || weight_unit === MSG_SELECT_AN_OPTION) {
        weight = 0;
    } else {
        weight = convertWeight(
            userData['weight'],
            userData['weight_unit'],
            'kg',
        )
    }

    const data = {
        weight: weight,
        height: height,
        dateOfBirth: (
            typeof userData['birthday'] === "string" ?
                userData['birthday'] : timestampToDate(userData['birthday'])
        ),
        gender: userData['gender'],
        exerciseDays: interpretString(userData['training_days']),
        goal_code: userData['goal_code'],
    }
    return data;
}

export const getUserDataOrCache = (
    currentUser,
    typeofCachedData,
    getUserData,
    getCachedData,
    putCachedData,
    setUserData,
    setErrorMsg,
) => {
    // const { currentUserValue } = authenticationService;
    if (typeofCachedData(userDataCacheName) !== 'undefined') {
        setUserData(getCachedData(userDataCacheName));
    } else {
        // getUserData(currentUserValue.id).then( 
        getUserData(currentUser.id).then( 
            data => {
                const preparedData = prepareUserDataForMDC(data.resultset);
                putCachedData(userDataCacheName, preparedData);
                setUserData(preparedData);
            },
            error => {
                setErrorMsg(error);
            }
        );
    }
}

export const UserDailyCaloriesAndCondition = ( {
    value,
    name,
    className = '',
    showAsField = '0',
} ) => {
    const {
        getCachedData,
        putCachedData,
        typeofCachedData,
    } = useContext(MainSectionContext);
    const { currentUser } = useUser();
    
    const [userData, setUserData] = useState(null);
    const [errorMsg, setErrorMsg] = useState(null);
    
    useEffect(() => {
        if (typeofCachedData(userDataCacheName) !== 'undefined') {
            setUserData(getCachedData(userDataCacheName));
        } else {
            getUserDataOrCache(
                currentUser,
                typeofCachedData,
                getUserData,
                getCachedData,
                putCachedData,
                setUserData,
                setErrorMsg,
            );
        }
    }, [typeofCachedData, getCachedData, putCachedData, currentUser]);

    if (debug) {
        console_debug_log(
            "UserDailyCaloriesAndCondition | userData:", userData,
            "UserDailyCaloriesAndCondition | error:", errorMsg,
            "UserDailyCaloriesAndCondition | value:", value,
            "UserDailyCaloriesAndCondition | name:", name,
        );
    }

    if (userData === null) {
        if (debug) {
            console_debug_log("UserDailyCaloriesAndCondition | NO DATA...");
        }
        return '';
    }

    if (errorMsg !== null) {
        if (debug) {
            console_debug_log("UserDailyCaloriesAndCondition | ERROR MESSAGE...");
        }
        return (
            <>
                <div className={ERROR_MSG_CLASS}>
                    {errorMsg}
                </div>
            </>
        )
    }

    // const totalCalories = parseFloat(document.getElementById("total_calories"));
    const totalCalories = parseFloat(value);
    const minimumDailyCalories = getMinimumDailyCalories(
        userData.weight,
        userData.height,
        userData.dateOfBirth,
        userData.gender,
        userData.exerciseDay,
        userData.goal_code,
    );

    return (
        <>
            <CalorieCondition
                totalCalories={totalCalories}
                minimumDailyCalories={minimumDailyCalories}
                className={className}
                showAsField={showAsField}
            />
        </>
    )

}

export const UserMinimumDailyCalories = ( {
    className,
    showAsField = '1',
} ) => {
    const {
        getCachedData,
        putCachedData,
        typeofCachedData,
    } = useContext(MainSectionContext);
    const { currentUser } = useUser();
    const [userData, setUserData] = useState(null);
    const [errorMsg, setErrorMsg] = useState(null);
    
    useEffect(() => {
        if (debug) console_debug_log("UserMinimumDailyCalories | calls getUserDataOrCache()");
        getUserDataOrCache(
            currentUser,
            typeofCachedData,
            getUserData,
            getCachedData,
            putCachedData,
            setUserData,
            setErrorMsg,
        );
    }, [typeofCachedData, getCachedData, putCachedData, currentUser]);
    
    if (debug) {
        console_debug_log(
            "UserMinimumDailyCalories | userData:", userData,
            "UserMinimumDailyCalories | error:", errorMsg,
        );
    }

    if (userData === null) {
        if (debug) {
            console_debug_log("UserMinimumDailyCalories | NO DATA...");
        }
        return '';
    }

    if (errorMsg !== null) {
        if (debug) {
            console_debug_log("UserMinimumDailyCalories | ERROR MESSAGE...");
        }
        return (
            <>
                <div className={ERROR_MSG_CLASS}>
                    {errorMsg}
                </div>
            </>
        )
    }

    if (debug) {
        console_debug_log("UserMinimumDailyCalories | SHOWING MinimumDailyCalories...");
    }

    let userDataToSend = {...userData};
    const goalCodeElement = document.getElementById('goal_code');
    if (goalCodeElement) {
        userDataToSend["goal_code"] = goalCodeElement.value;
        userDataToSend['weight'] = document.getElementById('weight').value;
        userDataToSend['weight_unit'] = document.getElementById('weight_unit').value;
        userDataToSend['height'] = document.getElementById('height').value;
        userDataToSend['height_unit'] = document.getElementById('height_unit').value;
        userDataToSend['birthday'] = document.getElementById('birthday').value;
        userDataToSend['gender'] = document.getElementById('gender').value;
        userDataToSend['training_days'] = document.getElementById('training_days').value;
        userDataToSend = prepareUserDataForMDC(userDataToSend);
    }

    return (
        <>
            <MinimumDailyCalories
                data={userDataToSend}
                className={className}
                showAsField={showAsField}
            />
        </>
    )
}
