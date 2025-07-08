"""
Chalice Food moments operations
"""
from typing import Optional

from genericsuite.util.framework_abs_layer import Response, BlueprintOne
from genericsuite.util.jwt import (
    request_authentication,
    AuthorizedRequest
)

from lib.models.admin_food.food_moments import (
    food_moment_in_user as food_moment_in_user_model,
)

bp = BlueprintOne(__name__)


@bp.route(
    'food_moment_in_user',
    methods=['GET'],
    authorizor=request_authentication(),
)
def food_moment_in_user(
    request: AuthorizedRequest,
    other_params: Optional[dict] = None
) -> Response:
    """
    Fetch the count of food_moment_id in all user's "food_times" array
    """
    return food_moment_in_user_model(
        request=request, blueprint=bp,
        other_params=other_params)
