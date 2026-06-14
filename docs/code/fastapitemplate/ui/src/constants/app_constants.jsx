import constants from "../configs/frontend/app_constants.json";
import * as gs from "genericsuite";

const buildConstant = gs.jsonUtilities.buildConstant;

export const GENDERS = buildConstant(constants.GENDERS);
export const BILLING_PLANS = buildConstant(constants.BILLING_PLANS);
export const ERROR_MESSAGES = constants.ERROR_MESSAGES;
export const APP_EMAILS = constants.APP_EMAILS;
export const APP_VALID_URLS = constants.APP_VALID_URLS;
