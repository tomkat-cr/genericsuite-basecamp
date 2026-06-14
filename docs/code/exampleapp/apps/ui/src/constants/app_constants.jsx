import constants from "../configs/frontend/app_constants.json";
import * as gs from "genericsuite";

const buildConstant = gs.jsonUtilities.buildConstant;

export const WEIGHT_UNITS = buildConstant(constants.WEIGHT_UNITS);
export const HEIGHT_UNITS = buildConstant(constants.HEIGHT_UNITS);
export const GENDERS = buildConstant(constants.GENDERS);
export const CALORIE_UNITS = buildConstant(constants.CALORIE_UNITS);
export const SERVING_SIZE_UNITS = buildConstant(constants.SERVING_SIZE_UNITS);
export const INGREDIENT_TYPE = buildConstant(constants.INGREDIENT_TYPE);
export const GOAL_CODES = buildConstant(constants.GOAL_CODES);
export const BILLING_PLANS = buildConstant(constants.BILLING_PLANS);
export const ERROR_MESSAGES = constants.ERROR_MESSAGES;
export const APP_EMAILS = constants.APP_EMAILS;
export const APP_VALID_URLS = constants.APP_VALID_URLS;
