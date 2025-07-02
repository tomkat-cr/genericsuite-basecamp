"""
FDA food API endpoint
"""
from typing import Optional

# from chalice.app import Response
# from genericsuite.util.blueprint_one import BlueprintOne
from genericsuite.util.framework_abs_layer import Response, BlueprintOne
from genericsuite.util.jwt import (
    request_authentication,
    AuthorizedRequest
)

from lib.models.external_apis.fda_food_endpoint import (
    fda_food_endpoint as fda_food_endpoint_model
)

bp = BlueprintOne(__name__)


@bp.route(
    '/',
    methods=['POST'],
    authorizor=request_authentication(),
)
def fda_food_endpoint(
    request: AuthorizedRequest,
    other_params: Optional[dict] = None
) -> Response:
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
        other_params=other_params
    )
