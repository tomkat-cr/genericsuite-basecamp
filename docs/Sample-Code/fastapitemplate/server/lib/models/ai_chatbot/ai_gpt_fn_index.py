"""
ChatGPT functions management
"""
from genericsuite.util.app_logger import log_debug
from genericsuite.util.app_context import AppContext

# from genericsuite_ai.lib.ai_gpt_functions import (
#     get_functions_dict,
# )

from lib.config.config import Config

from lib.models.ai_chatbot.ai_gpt_fn_app import (
    cac as cac_app,
)

DEBUG = False
EXTRA_DEBUG = False


def assign_app_specific_gpt_functions(
    app_context: AppContext,
) -> None:
    """
    Assign App-specific GPT functions
    """
    _ = DEBUG and log_debug('ASSIGN_APP_SPECIFIC_GPT_FUNCTIONS |'
                            ' Assigning App-specific GPT functions')
    app_context.set_other_data(
        'additional_function_dict',
        get_additional_functions_dict)
    app_context.set_other_data(
        'additional_func_context',
        additional_gpt_func_appcontexts)
    app_context.set_other_data(
        'additional_run_one_function',
        additional_run_one_function)
    app_context.set_other_data(
        'additional_function_specs',
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
    _ = DEBUG and log_debug('GET_ADDITIONAL_FUNCTIONS_DICT |'
                            ' Assigning App-specific GPT functions dict')
    settings = Config(app_context)
    is_lc = settings.AI_TECHNOLOGY == 'langchain'
    if is_lc:
        # Langchain Tools
        result = {
        }
    else:
        # GPT Functions
        result = {
        }
    if DEBUG and EXTRA_DEBUG:
        log_debug(f"APP-SPECIFIC GET_FUNCTIONS_DICT | is_lc: {is_lc}" +
                  f" result: {result}")
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
        log_debug('ADDITIONAL_GPT_FUNC_APPCONTEXTS |' +
                  ' Assigning App-specific additional GPT function' +
                  ' AppContexts')
    available_func_context = [
        cac_app,
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
    _ = DEBUG and log_debug('ADDITIONAL_RUN_ONE_FUNCTION |' +
                            ' App-specific run_one_function')
    # user_lang = app_context.get_user_data().get('language', 'auto')
    # available_functions = get_functions_dict(app_context)
    # fuction_to_call = available_functions[function_name]
    function_response = None
    _ = DEBUG and \
        log_debug("AI_FA_ROF-1) run_one_function_from_chatgpt" +
                  f" | function_name: {function_name}" +
                  f" | function_args: {function_args}")

    # if function_name == "xxx":
    #     function_response = fuction_to_call(
    #         params={
    #             "name": function_args.get("name"),
    #         }
    #     )

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
    _ = DEBUG and log_debug('GET_ADDITIONAL_FUNCTION_SPECS |' +
                            ' App-specific additional GPT function specs')
    _ = DEBUG and \
        log_debug("AI_FA_GFS-1) get_function_specs")
    result = [{
        #     "name": "xxx",
        #     "description": "xxx" +
        #     "parameters": {
        #         "type": "object",
        #         "properties": {
        #             "name": {
        #                 "type": "string",
        #                 "description": "The name of the xxx",
        #             },
        #         },
        #         "required": [
        #             "name",
        #         ],
        #     },
    }]
    return result
