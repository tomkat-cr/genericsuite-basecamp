"""
GPT functions: App Specific
"""
# C0301: | Disable "line-too-long"
# pylint: disable=C0301
# W0718 | broad-exception-caught Catching too general exception Exception
# pylint: disable=W0718

from typing import Any, Optional
# from typing import Union, List
import json
import re
from datetime import datetime
# from uuid import uuid4

from langchain.agents import tool
# from pydantic import BaseModel, Field
from pydantic import BaseModel, Field
# from langchain.schema import Document

from genericsuite.util.app_context import CommonAppContext
from genericsuite.util.app_logger import log_debug
# from genericsuite.util.config_dbdef_helpers import get_json_def_both
# from genericsuite.util.datetime_utilities import interpret_any_date
from genericsuite.util.utilities import (
    get_default_resultset,
    # is_under_test,
)
from genericsuite.util.generic_db_middleware import (
    fetch_all_from_db,
    add_item_to_db,
    # get_item_from_db,
    # modify_item_in_db,
)
# from genericsuite.constants.const_tables import get_constant

from genericsuite_ai.lib.ai_utilities import (
    standard_gpt_func_response,
    get_assistant_you_are,
)
from genericsuite_ai.lib.ai_sub_bots import ask_ai
from genericsuite_ai.lib.ai_langchain_tools import (
    interpret_tool_params,
)
from genericsuite_ai.lib.json_reader import (
    prepare_metadata,
    index_dict,
)

from app.tools.age_utilities import AgeUtilities
# from app.tools.convertion_utilities import ConvertionUtilities
from app.tools.transform_utilities import TransformUtilities


DEBUG = False
cac = CommonAppContext()


# Structures


class Provider(BaseModel):
    """
    Provider (store, maker, business)
    """
    # id: UUID = Field(description="Row ID", default_factory=uuid4)
    name: str = Field(
        description="Name")
    category: str = Field(
        description="Provider category")
    lat: float = Field(
        description="Latitude")
    lng: str = Field(
        description="Longitude")
    address: Optional[str] = Field(default="",
        description="Address")
    city: Optional[str] = Field(default="",
        description="City")
    zipcode: Optional[str] = Field(default="",
        description="Zip code")
    country: Optional[str] = Field(default="",
        description="Country")
    observations: Optional[str] = Field(default="",
        description="Observations")


class Product(BaseModel):
    """
    Products
    """
    # id: UUID = Field(description="Row ID", default_factory=uuid4)
    name: str = Field(
        description="Name")
    bar_code: str = Field(
        description="Barcode")
    category: str = Field(
        description="Product category")
    observations: Optional[str] = Field(default="",
        description="Observations")


class ProductPrices(BaseModel):
    """
    Product prices
    """
    # id: UUID = Field(description="Row ID", default_factory=uuid4)
    user_id: str = Field(
        description="User ID")
    product_id: str = Field(
        description="Product ID")
    provideor_id: str = Field(
        description="Provider ID")
    price: float = Field(
        description="Price")
    currency: str = Field(
        description="Currency")
    price_date: datetime = Field(
        description="Price date")
    observations: Optional[str] = Field(default="",
        description="Observations")
"""

TABLA: prc_medias
Descripción: Media (fotos, videos, documentos)

id - int - Cod. Media (correlativo) [PK]	<<< antes: med_code
prd_code - int - Cod. Producto [IDX]
cli_code - int - Cod. Cliente [IDX]	-> prc_clients.id
med_date - date - Fecha
med_type - int - Tipo. Lista: MEDIA_TYPE
med_fname - varchar(100) - Nombre del Archivo (original)

TABLA: prc_list_encs
Descripción: Listas de productos del usuario (encabezado)

id - int - Cod. Lista (correlativo) [PK]	<<< lse_code
lse_name - varchar(100) - Nombre
cli_code - int - Cod. Cliente [IDX]	-> prc_clients.id

TABLA: prc_list_dets
Descripción: Listas de productos del usuario (detalle)

id - int - Cod. Detalle de Lista (correlativo) [PK]	<<< antes: lsd_code
lse_code - int - Cod. Lista de Productos de Usuario [IDX]
prd_code - int - Cod. Producto [IDX]

TABLA: prc_slst_encs
Descripción: Listas del sistema (encabezado)

id - int - Cod. Lista del Sistema [PK]	<<< sle_code
sle_name - varchar(100) - Nombre Lista
sle_pcode - varchar(20) - Cod. Pnemónico de la Lista
sle_fa_cod - int - Cod. de Lista Padre

TABLA: prc_slst_dets
Descripción: Elementos de listas del sistema (detalle)

id - int - Cod. Elemento de Lista (correlativo) [PK]	<<< sld_code
sle_code - int - Cod. Lista del Sistema [IDX]
sld_pcode - varchar(20) - Cod. Pnemónico del Elemento de Lista
sld_name - varchar(100) - Nombre del elemento de Lista
sld_fa_code - int - Cod. Elemento de Lista Padre [IDX]

...

Lista: SEX
F=Femenino, M=Masculino, ""=No definido

Lista: MEDIA_TYPE
F=Foto, V=Video, D=Documento

Lista: COUNTRY

Lista: CITY

Lista: PROV_CATEG
S=Supermecado, F=Ferretería, TR=Tienda de Ropa, ...

Lista: PROD_CATEG
C=Comida, V=Vestuario, H=Herramientas, ...

"""

class JustName(BaseModel):
    """
    Tool with only a name parameter structure
    """
    name: str = Field(description="Name to process")


# Support Funcions


# Funcions called by ChatGPT


# User's products


@tool
def create_product_price(params: Any) -> str:
    """
Useful when you need to add a new product price to the database.
Args: params (dict): Tool parameters. It must contain:
"name" (str): product name.
"calories_value" (float): product calories.
"calories_unit" (str): product calorie unit. Use only these codes: "kcal" and "kj".
"serving_size" (float): product serving size.
"serving_size_unit" (str): product serving size code. Use only these codes:
g=Grams
u=Unit
tsp=Tea spoon
tablespoon=Table spoon
bowl=Bowl (300 ml)
cup=Cup (200 ml)
scup=Small Cup (150 ml)
ml=Milliliters
mg=Milligrams
ug=Micro grams
oz=Ounce
lb=Pound
iu=International units
mlt=Mass,length,time.
"brand_name" (str): product brand if any.
"observations" (str): additional observations about the product if any.
    """
    return create_product_price_func(params)


def create_product_price_func(params: Any) -> str:
    """
    Add a new product price to the database.
    """
    params = interpret_tool_params(tool_params=params, schema=Product)

    name = params.name
    calories_value = params.calories_value
    calories_unit = params.calories_unit
    serving_size = params.serving_size
    serving_size_unit = params.serving_size_unit
    brand_name = params.brand_name
    observations = params.observations

    new_item = {
        "user_id": cac.app_context.get_user_id(),
        "type": "I",
        "name": name,
        "calories_value": calories_value,
        "calories_unit": calories_unit,
        "serving_size": serving_size,
        "serving_size_unit": serving_size_unit,
        "brand_name": brand_name,
        "observations": observations,
    }
    # filters = {
    #     "user_id": cac.app_context.get_user_id(),
    # }
    if DEBUG:
        log_debug('AI_CUI-1) create_product_price |' +
                  f' new_item: {new_item}')
    result = add_item_to_db(
        app_context=cac.app_context,
        json_file='product_prices',
        data=new_item,
        # filters=filters,
    )
    return standard_gpt_func_response(result, "product price creation")


@tool
def search_product_price(params: Any) -> str:
    """
Useful when you need to search user's products by name.
Args: params (dict): Tool parameters. It must have: name (str): the string to search, contained in the product name.
    """
    return search_product_price_func(params)


def search_product_price_func(params: Any) -> str:
    """
    Search user's products by name.
    """
    params = interpret_tool_params(tool_params=params, schema=JustName)
    name = params.name
    if DEBUG:
        log_debug('AI_SUIBN-1) search_product_price |' +
                  f' name: {name}')
    resultset = fetch_all_from_db(
        app_context=cac.app_context,
        json_file='product_prices',
        like_query_params={"name": name},
        combinator="$or",
    )
    if DEBUG:
        log_debug('AI_SUIBN-2) search_product_price |' +
                  f' resultset: {resultset}')
    return standard_gpt_func_response(
        result=resultset,
        action_description="User's product retrieval",
        include_resultset=True
    )


@tool
def get_product_price_list(params: Any = None) -> str:
    """
Useful when you need to get all user's products.
    """
    return get_product_price_list_func(params)


def get_product_price_list_func(params: Any = None) -> str:
    """
    Get all user's products.
    """
    if params:
        params = interpret_tool_params(tool_params=params)
    else:
        params = {}
    if DEBUG:
        log_debug('AI_GUIL-1) get_product_price_list' +
                  f' params: {params}')
    resultset = get_product_price_list_raw()
    return standard_gpt_func_response(
        result=resultset,
        action_description="User's product list",
        include_resultset=True
    )


def get_product_price_list_raw() -> dict:
    """
    Get all user's products.

    Args:
        None.

    Returns:
        dict: user's products resultset.
    """
    if DEBUG:
        log_debug('AI_GUILR-1) get_product_price_list_raw')
    resultset = fetch_all_from_db(
        app_context=cac.app_context,
        json_file='product_prices',
    )
    if DEBUG:
        log_debug('AI_GUILR-2) get_product_price_list_raw |' +
                  f' resultset: {resultset}')
    return resultset


# User profile


@tool
def get_user_profile(params: Any) -> str:
    """
Useful when you need to get user's summary profile. The summary profile only contains user's data like gender, location (city, state, country).
    """
    return get_user_profile_func(params)


def get_user_profile_func(params: Any) -> str:
    """
    Get user's summary profile.
    """
    if params:
        params = interpret_tool_params(tool_params=params)
    else:
        params = {}
    if DEBUG:
        log_debug('AI_GUP-1) get_user_profile' +
                  f' params: {params}')
    result = get_user_profile_raw()
    return standard_gpt_func_response(
        result=result,
        action_description="User profile",
        include_resultset=True
    )


def get_user_profile_raw() -> dict:
    """
    Get user profile. The profile contains user's data like gender,
    location (city, state, country).

    Args:
        None.

    Returns:
        dict: the user profile resultset.
    """
    if DEBUG:
        log_debug('AI_GUPR-1) get_user_profile_raw')

    user_data = cac.app_context.get_user_data()

    age_lib = AgeUtilities(cac.get())
    # conv_lib = ConvertionUtilities(cac.get())
    transf_lib = TransformUtilities(cac.get())

    # Data calculations
    user_data["age"] = age_lib.calculate_age(
        datetime.utcfromtimestamp(user_data.get("birthday"))
    )

    # # Calculate the minimun daily calories from user data
    # user_data["minimun_daily_calories"] = conv_lib.get_minimum_daily_calories(
    #     weight=conv_lib.convert_weight(user_data.get("weight", 0),
    #         user_data.get("weight_unit", "kg"), "kg"),
    #     height=conv_lib.convert_height(user_data.get("height", 0),
    #         user_data.get("height_unit", "m"), "m"),
    #     age=user_data["age"],
    #     gender=user_data.get("gender", ""),
    #     exercise_days=transf_lib.interpret_string(
    #         user_data.get("training_days", "")),
    #     goal_code=user_data.get("goal_code", ""),
    # )

    # Save elements not in "users" JSON table definition
    saved_elements = {
        "food_times": user_data.get("food_times", []),
        "user_history": user_data.get("user_history", [])
    }

    # Transform data (codes to descriptions)
    user_data = transf_lib.transform_code_desc("users", user_data)

    # Restore elements not in "users" JSON table definition
    user_data["food_times"] = saved_elements["food_times"]
    user_data["user_history"] = saved_elements["user_history"]

    # Removes the goal code from its description
    user_data["general_goal"] = re.sub(r'^[+-]?\d{1,2}%', '',
                                       user_data.get("goal_code", "")
                                       ).strip()

    # Prepare data to avoid send PII
    for attr_name in ["_id", "id", "firstname", "lastname", "email",
                      "birthday", "creation_date",
                      "update_date", "superuser", "passcode",
                      "passcode_repeat", ""]:
        if attr_name in user_data:
            del user_data[attr_name]

    result = get_default_resultset()
    result["resultset"] = user_data.copy()
    user_data = None
    if DEBUG:
        log_debug('AI_GUPR-2) get_user_profile_raw |' +
                  f' result: {result}')
    return result


@tool("get_full_user_profile", return_direct=True)
def get_full_user_profile(params: Any) -> str:
    """
Useful when you need to get an answer to the Human question made over the context of the user's complete profile, that includes: gender, weight, height, age, physical goals, other goals, training days, training hour, food times, historic data (weight, height, physical goals, and other goals), user's preferred food ingredients, user's dishes, and user's historic daily meals.
    """
    return get_full_user_profile_func(params)


def get_full_user_profile_func(params: Any) -> str:
    """
    Get an answer for a question made about the user's complete profile.
    """
    if params:
        params = interpret_tool_params(tool_params=params)
    else:
        params = {}
    if DEBUG:
        log_debug('AI_GFUP-1) get_full_user_profile' +
                  f' params: {params}')
    result = get_default_resultset()
    # Get the question
    question = cac.app_context.get_other_data("question")["content"]

    # Build the prompt
    prompt = f"You are {get_assistant_you_are(cac.app_context)}" + \
             "\n" + \
             f"Answer this question (in english please): {question}"

    # prompt = f"""
    # You are {get_assistant_you_are(cac.app_context)}
    # Please answer this question: {question}"""
    # The user's full profile is in the embeddings. It contains health, diet, nutrition, and training data.
    # The 'user_ingredient_list', 'dishes_list', and 'daily_meal_list' represent the user's food preferences, eating habits, daily calorie consumption, and diet.
    # The 'minimum_daily_calories' is the user's minimum daily calorie consumption. Eating less than or equal to 'minimum_daily_calories' keeps the user in a calorie deficit, otherwise, he/she will be in a calorie surplus.
    # The 'height' and 'height_unit', 'age' and 'gender' represent the user's personal data.
    # The 'weight' and 'weight_unit' indicate the user's current physical health.
    # The 'exercise_days' represent the quantity of days the user is exercising.
    # The 'training_days' represent the weekdays the user uses for physical exercises.
    # The 'general_goal' represents the user's current physical health goal.
    # The 'food_times' indicate the user's mealtimes.
    # The 'user_history' represents the user's weight and goals history by date.
    #"""

    # Get profile data
    result = get_full_user_profile_raw()
    if not result["error"]:
        titles = {
            "user_profile": "user's full profile, containing health, diet, nutrition and training data",
            'user_ingredient_list': "user's food preferences, preferred food ingredients",
            'dishes_list': "user's food preferences, preferred dishes",
            'daily_meal_list': "user's daily meals by date, to have an idea of his/her eating habits, daily calorie consumption and diet",
        }

        # Set the metadata
        json_metadata = prepare_metadata(
            metadata={},    # TODO: enrich the metadata...
            default_element_name="content"
        )

        # Vectorize the profile
        user_id = cac.get().get_user_id()
        json_filename = f"{user_id}_|name|.json"
        documents_list = []
        try:
            for item_name, item_data in result["resultset"].items():
                entries = index_dict(
                    json_content=item_data,
                    json_filename=json_filename.replace('|name|', item_name),
                    json_metadata=json_metadata,
                    title=titles.get(item_name, "User's complete or full profile"),
                )
                documents_list.extend(entries)
        except Exception as err:
            result["error"] = True
            result["error_message"] = \
                "ERROR vectorizing the user's profile [AI-GFUP-E010]:" + \
                f" {str(err)}"

        # Ask the question to the model
        if not result["error"]:
            result = ask_ai(
                app_context=cac.get(),
                documents_list=documents_list,
                question=prompt,
                response_type="answer",
            )
    if DEBUG:
        log_debug('AI_GFUP-2) get_full_user_profile' +
                  f'\nquestion: {question}' +
                  f'\nprompt: {prompt}' +
                  f'\nresult: {result}')
    return standard_gpt_func_response(
        result=result,
        action_description="Thanks for you question. According to your profile data:\n",
        include_resultset=True,
        additional_msg="",
        add_success_msg=False,
        json_result=False,
    )


def get_full_user_profile_raw() -> dict:
    """
    Get the user's full profile, including user's data like gender, weight,
    height, age, physical goals, other goals, training days, training hour,
    food times, historic data (weight, height, physical goals, and other
    goals), user's preferred food ingredients, user's dishes, and
    user's historic daily meals.

    Args:
        params (dict): parameters for the function.

    Returns:
        dict: the user's full profile resultset.
    """
    if DEBUG:
        log_debug('AI_GFUPR-1) get_full_user_profile_raw')
    result = get_default_resultset()
    # Get the full user profile
    result["resultset"] = {
        "user_profile": get_user_profile_raw(),
        # "user_ingredient_list": get_user_ingredient_list_raw(),
        # "dishes_list": get_dishes_list_raw(),
        # "daily_meal_list": get_daily_meal_list_raw(),
    }
    # Reduce each element response unless the element has an error
    for k, val in result["resultset"].items():
        log_debug(f'get_full_user_profile_raw | k: {k} | val: {val}')
        if val["error"]:
            result["error"] = True
            result["error_message"] += ", {k}"
        else:
            result["resultset"][k] = \
                json.loads(val["resultset"]) if isinstance(val["resultset"], str) \
                else val["resultset"]
    # Adjust the eventual error menssage
    if result["error"]:
        result["error_message"] = 'ERROR(s) in: ' + \
            result["error_message"].strip(", ")
    # if DEBUG:
    #     log_debug('AI_GFUPR-2) get_full_user_profile_raw |' +
    #               f' resultset: {result}')
    return result
