"""
Flask FDA food API endpoint
"""
from typing import Any

from genericsuite.util.jwt import AuthorizedRequest
# from genericsuite.util.app_logger import log_debug

from genericsuite.flasklib.util.blueprint_one import BlueprintOne
from genericsuite.flasklib.util.jwt import token_required

from lib.models.external_apis.fda_food_endpoint import (
    fda_food_endpoint as fda_food_endpoint_model
)

DEBUG = False

bp = BlueprintOne('fda_food_query', __name__, url_prefix='/fda_food_query')


@bp.route('/', methods=['POST'])
@token_required
def fda_food_endpoint(
    request: AuthorizedRequest,
    other_params: dict = None,
) -> Any:
    """
    This endpoint is used to fetch food data from the FDA API.
    It takes in a request and other parameters and returns a response.

    :param request: The request object containing the request data.
    :param other_params: Any other parameters that may be needed.
    :return: A response object containing the response data.
    """
    return fda_food_endpoint_model(
        request=request,
        blueprint=bp,
        other_params=other_params,
    )
