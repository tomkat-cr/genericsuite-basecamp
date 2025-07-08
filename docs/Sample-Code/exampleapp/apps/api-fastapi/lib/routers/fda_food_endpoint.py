"""
FastAPI FDA food API endpoint
"""
from typing import Any

from fastapi import Depends, Request as FaRequest
from fastapi.security import HTTPBasic

from genericsuite.fastapilib.framework_abstraction import (
    BlueprintOne,
)
# from genericsuite.util.app_logger import log_debug

from genericsuite.fastapilib.util.dependencies import (
    get_current_user,
    get_default_fa_request,
)

from lib.models.external_apis.fda_food_endpoint import (
    fda_food_endpoint as fda_food_endpoint_model
)

DEBUG = False

# Set FastAPI router
router = BlueprintOne()

# Set up Basic Authentication
security = HTTPBasic()


@router.post('/', tags='fda_food_endpoint')
async def fda_food_endpoint(
    request: FaRequest,
    current_user: str = Depends(get_current_user),
) -> Any:
    """
    This endpoint is used to fetch food data from the FDA API.
    It takes in a request and other parameters and returns a response.

    :param request: The request object containing the request data.
    :param other_params: Any other parameters that may be needed.
    :return: A response object containing the response data.
    """
    gs_request, other_params = get_default_fa_request(
        current_user=current_user)
    router.set_current_request(request, gs_request)
    return fda_food_endpoint_model(
        request=gs_request,
        blueprint=router,
        other_params=other_params
    )
