"""
Food moments operations
"""
from typing import Any

from genericsuite.util.jwt import AuthorizedRequest
# from genericsuite.util.app_logger import log_debug

from genericsuite.flasklib.util.blueprint_one import BlueprintOne
from genericsuite.flasklib.util.jwt import token_required

from lib.models.admin_food.food_moments import (
    food_moment_in_user as food_moment_in_user_model,
)

DEBUG = False

bp = BlueprintOne('food_moments', __name__, url_prefix='/food_moments')


@bp.route('/food_moment_in_user', methods=['GET'])
@token_required
def food_moment_in_user(
    request: AuthorizedRequest,
    other_params: dict = None,
) -> Any:
    """
    Fetch the count of food_moment_id in all user's "food_times" array
    """
    return food_moment_in_user_model(
        request=request,
        blueprint=bp,
        other_params=other_params,
    )
