"""Handle FDA API calls to get food and food nutrients calorie data
"""
import requests

from lib.config.config import Config
from genericsuite.util.app_context import AppContext
from genericsuite.util.app_logger import log_debug
from genericsuite.util.utilities import get_default_resultset

DEBUG = False


def call_fda_api(
    app_context: AppContext,
    food_name: str
) -> dict:
    """
    Calls the FDA API to get food data.

    :param food_name: The name of the food to search for.
    :return: A dictionary containing the response from the FDA API.
    """
    settings = Config(app_context)
    fda_response = get_default_resultset()
    api_key = settings.FDA_API_KEY
    url = "https://api.nal.usda.gov/fdc/v1/foods/search?" + \
        f"api_key={api_key}"
    headers = {
        "Content-Type": "application/json",
    }
    food_name = food_name.strip().lower().capitalize()
    data = {
        "query": food_name,
    }
    if DEBUG:
        log_debug(f"FDA_API - url: {url} | data: {data} | headers: {headers}")
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        # Raises an exception if the status code indicates an error
        response.raise_for_status()

        # Successful response
        fda_response["response"] = response.json()

        # Error simulation:
        # return {"error": False, "error_message": None,
        # "resultset": response.json()}

    except requests.exceptions.RequestException as err:
        # Error occurred during the API call
        fda_response["error"] = True
        fda_response["error_message"] = str(err)

        # Error simulation:
        # return {"error": True, "error_message": str(e), "resultset": None}

    except Exception as err:
        # Other unexpected errors
        fda_response["error"] = True
        fda_response["error_message"] = str(err)

        # Error simulation:
        # return {"error": True, "error_message": str(e), "resultset": None}

    if DEBUG:
        log_debug(f"FDA_API - fda_response: {fda_response}")
    return fda_response


def convert_serving_size_unit(ss_unit: str) -> str:
    """
    Converts the serving size unit to a standard format.

    :param ss_unit: The serving size unit to convert.
    :return: The converted serving size unit.
    """
    if not ss_unit:
        return ''
    ss_unit = {
        'GRM': 'g',
    }.get(ss_unit, ss_unit.lower())
    return ss_unit


def convert_calorie_unit(cal_unit: str) -> str:
    """
    Converts the calorie unit to a standard format.

    :param cal_unit: The calorie unit to convert.
    :return: The converted calorie unit.
    """
    if not cal_unit:
        return ''
    cal_unit = {
        'KCAL': 'kcal',
        'Kilo Calories': 'kcal',
    }.get(cal_unit, cal_unit.lower())
    return cal_unit


def get_calories(
    api_response: dict,
    only_first: bool = False,
    detailed: bool = False,
    mandatory_serving_size: bool = False,
) -> list:
    """
    Get the calories for all records found from the FDA API response.

    :param api_response: The response from the FDA API.
    :param only_first: If True, only the first record will be returned.
    :param detailed: If True, detailed information will be included in the
    response.
    :return: A list of dictionaries containing calorie information.
    """
    calories_response = []
    foods = api_response["foods"]
    for food in foods:
        # "nutrientName": "Energy",
        # "unitName": "KCAL",
        # "derivationCode": "LCCS",
        # "derivationDescription": "Calculated from value per serving
        #  size measure",
        # "value": 393,
        calories_entry = {"calories_data": v for v
                          in food.get("foodNutrients", [])
                          if v.get("nutrientName", '') == "Energy"}
        if len(calories_entry) == 0:
            continue

        calories = {
            "nutrientId": str(calories_entry["calories_data"]["nutrientId"]),
            "value": str(calories_entry["calories_data"]["value"]),
            "unit": str(calories_entry["calories_data"]["unitName"]),
        }

        # "description": "CHEDDAR CHEESE",
        # "servingSizeUnit": "g",
        # "servingSize": 28.0,
        food_id = food.get("fdcId", "N/A")
        nutrient_id = calories['nutrientId']
        food_name = food.get("description", "N/A")
        brand_name = food.get("brandName")
        serving_size = food.get("servingSize")
        ss_unit = food.get("servingSizeUnit")

        if mandatory_serving_size and not serving_size:
            continue

        description = F"{food_name} has " + \
            f"{calories['value']} {calories['unit']}" + \
            f"{', serving size: '+str(serving_size) if serving_size else ''}" \
            + \
            f"{' '+str(ss_unit) if ss_unit and serving_size else ''}" + \
            f"{' ('+brand_name+' brand)' if brand_name else ''}"

        element = {}
        element["description"] = description
        if detailed:
            element["id"] = food_id
            element["nutrient_id"] = nutrient_id
            element["food_name"] = food_name
            element["brand_name"] = brand_name
            element["serving_size"] = serving_size
            element["serving_size_unit"] = convert_serving_size_unit(ss_unit)
            # element["calories"] = calories
            element['calories_value'] = calories['value']
            element['calories_unit'] = convert_calorie_unit(calories['unit'])
        calories_response.append(element)

    if only_first and len(calories_response) > 0:
        calories_response = [calories_response[0]]

    return calories_response
