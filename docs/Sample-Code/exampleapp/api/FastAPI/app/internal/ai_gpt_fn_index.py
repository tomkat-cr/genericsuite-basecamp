"""
ChatGPT functions management
"""
# from typing import Union
# import json

from genericsuite.util.app_logger import log_debug
from genericsuite.util.app_context import AppContext

from genericsuite_ai.lib.ai_gpt_functions import (
    get_functions_dict,
)

from app.config.config import Config

from app.internal.ai_gpt_fn_app_specific import (
    cac as cac_app_specific,
    create_product_price,
    create_product_price_func,
    search_product_price,
    search_product_price_func,
    get_product_price_list,
    get_product_price_list_func,
)

DEBUG = False
EXTRA_DEBUG = False


def assign_app_gpt_functions(
    app_context: AppContext,
) -> None:
    """
    Assign App Specific GPT functions
    """
    _ = DEBUG and log_debug(
        'ASSIGN_APP_SPECIFIC_GPT_FUNCTIONS | ' +
        'Assigning App Specific GPT functions')
    app_context.set_other_data('additional_function_dict',
                               get_additional_functions_dict)
    app_context.set_other_data('additional_func_context',
                               additional_gpt_func_appcontexts)
    app_context.set_other_data('additional_run_one_function',
                               additional_run_one_function)
    app_context.set_other_data('additional_function_specs',
                               get_additional_function_specs)


def get_additional_functions_dict(
    app_context: AppContext,
) -> dict:
    """
    Get the available ChatGPT functions and its callables (app-specific).

    Returns:
        dict: A dictionary containing the available ChatGPT functions
        and its callable.
    """
    _ = DEBUG and log_debug(
        "GET_ADDITIONAL_FUNCTIONS_DICT | " +
        'Assigning App Specific GPT functions dict')
    settings = Config(app_context)
    is_lc = settings.AI_TECHNOLOGY == 'langchain'
    if is_lc:
        # Langchain Tools
        result = {
            # "create_product_price": create_product_price,
            # "search_product_price": search_product_price,
            # "get_product_price_list": get_product_price_list,
        }
    else:
        # GPT Functions
        result = {
            # "create_product_price": create_product_price_func,
            # "search_product_price": search_product_price_func,
            # "get_product_price_list": get_product_price_list_func,
        }
    if DEBUG and EXTRA_DEBUG:
        log_debug("App Specific GET_FUNCTIONS_DICT" +
                  f" | is_lc: {is_lc} result: {result}")
    return result


def additional_gpt_func_appcontexts(
    app_context: AppContext,
) -> list:
    """
    Assign the app_context to the ChatGPT functions.

    Args:
        app_context (AppContext): GPT Context
    """
    _ = DEBUG and \
        log_debug(
            'ADDITIONAL_GPT_FUNC_APPCONTEXTS | Assigning' +
            ' App Specific additional GPT function AppContexts')
    available_func_context = [
        cac_app_specific,
    ]
    return available_func_context


def additional_run_one_function(
    app_context: AppContext,
    function_name: str,
    function_args: dict,
) -> dict:
    """
    Execute a function based on the given function_name
    and function_args.

    Args:
        app_context (AppContext): GPT Context
        function_name (str): function name
        function_args (dict): function args

    Returns:
        The result of the function execution.
    """
    _ = DEBUG and log_debug(
        'ADDITIONAL_RUN_ONE_FUNCTION | ' +
        'App Specific run_one_function')
    user_lang = app_context.get_user_data().get('language', 'auto')
    # question = app_context.get_other_data("question")["content"]
    available_functions = get_functions_dict(app_context)
    fuction_to_call = available_functions[function_name]
    function_response = None
    _ = DEBUG and \
        log_debug("AI_FA_ROF-1) run_one_function_from_chatgpt" +
                  f" | function_name: {function_name}" +
                  f" | function_args: {function_args}")

    if function_name == "get_fda_food_query":
        function_response = fuction_to_call(
            params={
                "food_name": function_args.get("food_name"),
                "source_lang": user_lang,
            }
        )
    elif function_name == "create_product_price":
        function_response = fuction_to_call(
            params={
                "name": function_args.get("name"),
                "calories_value": function_args.get("calories_value"),
                "calories_unit": function_args.get("calories_unit"),
                "serving_size": function_args.get("serving_size"),
                "serving_size_unit": function_args.get("serving_size_unit"),
                "brand_name": function_args.get("brand_name"),
                "observations": function_args.get("observations"),
            }
        )
    elif function_name == "search_product_price":
        function_response = fuction_to_call(
            params={
                "name": function_args.get("name"),
            }
        )
    elif function_name == "get_product_price_list":
        function_response = fuction_to_call(
            params={}
        )

    result = {
        "function_response": function_response,
        "function_name": function_name,
        "function_args": function_args,
    }
    _ = DEBUG and \
        log_debug('AI_FA_ROF-2) run_one_function_from_chatgpt' +
                  f' | result: {result}')
    return result


def get_additional_function_specs(
    app_context: AppContext,
) -> list:
    """
    Get the ChatGPT function specifications (parameters, documentation).

    Returns:
        list[dict]: A list of dictionaries containing the available
        ChatGPT functions.
    """
    _ = DEBUG and log_debug(
        'GET_ADDITIONAL_FUNCTION_SPECS | ' +
        'App Specific additional GPT function specs')
    _ = DEBUG and \
        log_debug("AI_FA_GFS-1) get_function_specs")
    result = [{
        "name": "get_fda_food_query",
        "description": "Get the name, description, calories, serving size" +
        " amount and serving size unit in a given food product.",
        "parameters": {
            "type": "object",
            "properties": {
                "food_name": {
                    "type": "string",
                    "description": "The name of the food product,"
                    " e.g. brocoli",
                },
                "source_lang": {
                    "type": "string",
                    "description": "The original language of the food " +
                    "product, e.g. es, fr, en",
                },
            },
            "required": ["food_name"],
        },
    }, {
        "name": "create_product_price",
        "description": "Add a new product price without a quantity" +
        ". e.g.: add brocoli to my products",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the" +
                    " product",
                },
                "calories_value": {
                    "type": "number",
                    "description": "The calories value of" +
                    " the product",
                },
                "calories_unit": {
                    "type": "string",
                    "description": "The calories unit code" +
                    " of the product." +
                    " Preferred value: kcal",
                },
                "serving_size": {
                    "type": "number",
                    "description": "The serving size of the" +
                    " product",
                },
                "serving_size_unit": {
                    "type": "string",
                    "description": "The serving size unit" +
                    " code of the product. It could be: " +
                    "Grams (g), " +
                    "Unit (u), " +
                    "Tea spoon (tsp), " +
                    "Table spoon (tablespoon), " +
                    "Bowl (bowl), " +
                    "Cup (cup), " +
                    "Small Cup (scup), " +
                    "Milliliters (ml), " +
                    "Milligrams (mg), " +
                    "Micro grams (ug), " +
                    "Ounce (oz), " +
                    "Pound (lb), " +
                    "International units (iu), " +
                    "Mass, length, time (mlt), " +
                    "Note: codes are between parenthesis"
                },
                "brand_name": {
                    "type": "string",
                    "description": "The brand name of"
                    " the product (value can be blank)",
                },
                "observations": {
                    "type": "string",
                    "description": "Any observations about" +
                    " the product (value can be blank)",
                },
            },
            "required": [
                "name",
                "calories_value",
                "calories_unit",
                "serving_size",
                "serving_size_unit",
                "brand_name",
                "observations",
            ],
        },
    }, {
        "name": "search_product_price",
        "description": "Search for user's products by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "description": "the string to search, contained in the" +
                    " product name",
                    "type": "string",
                }
            }
        },
        "required": ["name"],
    }]

    # _ = DEBUG and \
    #     log_debug('AI_FA_GFS-2) get_function_specs' +
    #               f' | section: {section}' +
    #               f' | result: {result}')
    return result
