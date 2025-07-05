import React from 'react';

import * as gs from "genericsuite";
import {
    CALORIE_DEFICIT_CLASS,
    CALORIE_SURPLUS_CLASS
} from '../../_constants/class_name_constants';

const console_debug_log = gs.loggingService.console_debug_log;
const ShowAsDisabledField = gs.genericEditorRfcUi.ShowAsDisabledField;
const calculateAge = gs.conversions.calculateAge;

const debug = false;    

export const getCalorieCondition = (minimumDailyCalories, totalCalories) => {
    const calorieDeficit = (minimumDailyCalories > totalCalories);
    const conditionDescription = (calorieDeficit ? 'Deficit' : 'Surplus');
    const message = (
        totalCalories === null ? '' : 
        `Calorie ${conditionDescription}`
    );
    const result = {
        calorieDeficit: calorieDeficit,
        message: message,
    };
    if (debug) {
        console_debug_log(
            `getCalorieCondition | minimumDailyCalories: ${minimumDailyCalories}, totalCalories: ${totalCalories}, result: ${result}`,
        )
    }
    return result;
}

/*
Understanding TDEE (Total Daily Energy Expenditure)
https://www.acko.com/calculators/tdee-calculator/

How to calculate TDEE
Calculating TDEE using the formula TDEE = BMR x Activity Factor involves two steps:

Step 1: Calculate your BMR using the following formula.

BMR = 10 x weight (kg) + 6.25 x height (cm) - 5 x age (years) + 5

For example, let's say you are a 30-year-old female who weighs 65 kg and is 165 cm tall. To calculate your BMR, you would plug in the numbers like this:
BMR = 10 x 65 + 6.25 x 165 - 5 x 30 + 5
BMR = 650 + 1031.25 - 150 + 5
BMR = 1536.25
So your BMR is 1536.25 calories per day.

Step 2: Multiply your BMR by your activity factor to calculate your TDEE. 

Your activity factor depends on how active you are. Here are the different activity factors and their corresponding activity levels:

Sedentary: 1.2
Lightly active: 1.375
Moderately active: 1.55
Very active: 1.725
Super active: 1.9

Let's say you are lightly active, so your activity factor is 1.375. To calculate your TDEE, you would plug in your BMR and activity factor like this:
TDEE = BMR x Activity Factor
TDEE = 1536.25 x 1.375
TDEE = 2111.33
*/

// const formulaMethod = "hb"; // Harris-Benedict formula
// const formulaMethod = "msj"; // Mifflin - St Jeor formula
const formulaMethod = "ck"; // Christian Kosmos formula

export const getBMR = (weight, height, gender, dateOfBirth) => {
    const age = calculateAge(dateOfBirth);
    let BMR;
        if (['male', 'm', 'M'].includes(gender)) {
            switch(formulaMethod) {
                case "hb":
                    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age); // Harris-Benedict formula
                    break;
                case "msj":
                    BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5; // Mifflin - St Jeor formula
                    break;
                case "ck":
                default:
                    BMR = (22 * weight); // Christian Kosmos
                    break;
            }
        if (debug) {
            console_debug_log(`getBMR - male (${gender}), age: ${age}, BMR: ${BMR}`);
        }
    } else {
        switch(formulaMethod) {
            case "hb":
                BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age); // Harris-Benedict formula
                break;
            case "msj":
                BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161; // Mifflin - St Jeor formula
                break;
            case "ck":
            default:
                BMR = (22 * weight); // Christian Kosmos
                break;
        }
        if (debug) {
            console_debug_log(`getBMR - female & other (${gender}), age: ${age}, BMR: ${BMR}`);
        }
    }
    return BMR;
}

export const getMinimumDailyCalories = (weight, height, dateOfBirth, gender, exerciseDays, goal_code) => {
    /*
    * weight: float in kg
    * height: float in meters
    * dateOfBirth: date string
    * gender: 'm', 'f'
    * exerciseDays: int
    */

    const BMR = getBMR(weight, height, gender, dateOfBirth);

    let calories;
    if (exerciseDays <= 1) {
        calories = BMR * 1.2;
    } else if (exerciseDays <= 3) {
        calories = BMR * 1.375;
    } else if (exerciseDays <= 5) {
        calories = BMR * 1.55;
    } else if (exerciseDays <= 6) {
        calories = BMR * 1.725;
    } else {
        calories = BMR * 1.9;
    }

    const caloriesFinal = applyGoal(calories, goal_code);

    if (debug) {
        console_debug_log(
            `getMinimumDailyCalories | Parameters | weight: ${weight}, height: ${height}, dateOfBirth: ${dateOfBirth}, gender: ${gender}, exerciseDays: ${exerciseDays}`,
            "getMinimumDailyCalories | BMR: ", BMR,
            "getMinimumDailyCalories | calories: ", calories,
            "getMinimumDailyCalories | caloriesFinal: ", caloriesFinal,
        );
    }

    return caloriesFinal;
}


export const applyGoal = (calories, goal_code) => {
    const perc = (
        typeof goal_code !== "undefined" && goal_code ?
            parseFloat(goal_code) : -20
    );
    const result = calories + ((calories * perc)/100);
    if (debug) {
        console_debug_log(
            `applyGoal | calories: ${calories}, goal_code: ${goal_code}, perc: ${perc} | result = ${result}`,
        );
    }
    return result;
}


// Minimun daily calories according to Mifflin - St Jeor formula.
// Parameters `data` with JSON structure: weight in kg, height in cm, age, gender, and number of days exercised.
export const MinimumDailyCalories = ( {
    data,
    className = '',
    showAsField = '1',
} ) => {
    const { weight, height, dateOfBirth, gender, exerciseDays, goal_code } = data;
    const minimumDailyCalories = getMinimumDailyCalories(
        weight, height, dateOfBirth, gender, exerciseDays, goal_code
    );

    if (showAsField === '1') {
        return (
            <>
                <ShowAsDisabledField className={className}>
                    {minimumDailyCalories.toFixed(2)}
                </ShowAsDisabledField>
            </>
        );
    }
    // {Math.round(minimumDailyCalories)}
    return (
        <>
            {minimumDailyCalories.toFixed(2)}
        </>
    );
};

export const CalorieCondition = ({
    minimumDailyCalories,
    totalCalories,
    className = '',
    showAsField = '0',
}) => {
    const calorieCondition = getCalorieCondition(minimumDailyCalories, totalCalories);
    const output = (
        <>
            <span 
                className={calorieCondition.calorieDeficit ? CALORIE_DEFICIT_CLASS : CALORIE_SURPLUS_CLASS}
            >
                {calorieCondition.message}
            </span>
            &nbsp;&nbsp;
            {totalCalories}
        </>
    );
    if (showAsField === '1') {
        return (
            <>
                <ShowAsDisabledField
                    className={className}
                >
                    {output}
                </ShowAsDisabledField>
            </>
        );
    }
    return (
        <>
            {output}
        </>
    );
}

export const totalCaloriesCalcInDailyMealIngredients = () => {
    const debug = true;
    const response = (parseFloat(document.getElementsByName('serving_size')[0].value) <= 0 ? 0 : ((parseFloat(document.getElementsByName('calories_value')[0].value) * parseFloat(document.getElementsByName('quantity')[0].value)) / parseFloat(document.getElementsByName('serving_size')[0].value)).toFixed(2));
    if (debug) console_debug_log('totalCaloriesCalcInDailyMealIngredients | response:', response);
    return response;
}

export const totalCaloriesCalcInDishesIngredients = () => {
    const debug = true;
    const response = (parseFloat(document.getElementsByName('serving_size')[1].value) <= 0 ? 0 : ((parseFloat(document.getElementsByName('calories_value')[1].value) * parseFloat(document.getElementsByName('quantity')[0].value)) / parseFloat(document.getElementsByName('serving_size')[1].value)).toFixed(2));
    if (debug) console_debug_log('totalCaloriesCalcInDishesIngredients | response:', response);
    return response;
}
