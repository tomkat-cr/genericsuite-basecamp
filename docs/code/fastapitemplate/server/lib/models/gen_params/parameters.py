"""
Food moments operations
"""
from typing import Optional

from genericsuite.util.framework_abs_layer import Response, BlueprintOne

from genericsuite.util.app_logger import log_debug
from genericsuite.util.generic_db_helpers import GenericDbHelper
from genericsuite.util.jwt import AuthorizedRequest
from genericsuite.util.utilities import (
    return_resultset_jsonified_or_exception,
    # get_query_params,
)
from genericsuite.config.config_from_db import app_context_and_set_env

DEBUG = True


def get_param_by_name(
    request: AuthorizedRequest,
    blueprint: BlueprintOne,
    other_params: Optional[dict] = None,
    name: str = None
) -> Response:
    """
    Fetch the general parameter by name
    """
    if not other_params:
        other_params = {}
    if name is None:
        return return_resultset_jsonified_or_exception(
            {"error": True, "error_message": "Parameter name is required"}
        )
    # Set environment variables from the database configurations.
    app_context = app_context_and_set_env(
        request=request, blueprint=blueprint)
    if app_context.has_error():
        return return_resultset_jsonified_or_exception(
            app_context.get_error_resultset()
        )
    # Fetch the parameter by name
    dbo = GenericDbHelper(
        json_file="general_config",
        request=request,
        blueprint=blueprint)
    result = dbo.fetch_row_by_entryname_raw('config_name', name)
    _ = DEBUG and log_debug(
        f"get_param_by_name | name: {name} | result: {result}")
    if result is not None and result['error'] is False and \
       result.get('resultset') is not None and \
       result.get('resultset').get('active') == '1':
        del result['resultset']['_id'], \
            result['resultset']['creation_date'], \
            result['resultset']['update_date'], \
            result['resultset']['active'], \
            result['resultset']['notes']
        return return_resultset_jsonified_or_exception(result)
    else:
        return return_resultset_jsonified_or_exception(
            {"error": True, "error_message": "Parameter not found"}
        )
