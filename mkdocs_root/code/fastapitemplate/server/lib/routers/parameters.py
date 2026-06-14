"""
Chalice Food moments operations
"""
from fastapi import Depends, Request as FaRequest, Path, Response
from fastapi.security import HTTPBasic

from genericsuite.fastapilib.framework_abstraction import (
    BlueprintOne,
)
# from genericsuite.util.app_logger import log_debug

from genericsuite.fastapilib.util.dependencies import (
    get_current_user,
    get_default_fa_request,
)

from lib.models.gen_params.parameters import get_param_by_name

DEBUG = False

# Set FastAPI router
router = BlueprintOne()

# Set up Basic Authentication
security = HTTPBasic()


@router.get('/{name}', tags='get_parameter')
async def get_parameter(
    request: FaRequest,
    current_user: str = Depends(get_current_user),
    name: str = Path(..., description="The name of the parameter to fetch"),
) -> Response:
    """
    Fetch the general parameter by name
    """
    gs_request, other_params = get_default_fa_request(
        current_user=current_user)
    router.set_current_request(request, gs_request)
    return get_param_by_name(
        request=gs_request,
        blueprint=router,
        other_params=other_params,
        name=name
    )
