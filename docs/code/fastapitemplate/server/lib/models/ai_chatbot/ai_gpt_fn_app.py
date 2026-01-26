"""
GPT functions: App specific
"""
# C0301: | Disable "line-too-long"
# pylint: disable=C0301
# W0718 | broad-exception-caught Catching too general exception Exception
# pylint: disable=W0718

# from typing import Union, Any, List, Optional
# import json
# import re
# from datetime import datetime
# from uuid import uuid4

# from langchain.agents import tool
# from pydantic import BaseModel, Field, field_validator
# from pydantic_core import PydanticCustomError

# from langchain.schema import Document

from genericsuite.util.app_context import CommonAppContext
# from genericsuite.util.app_logger import log_debug
# from genericsuite.util.config_dbdef_helpers import get_json_def_both
# from genericsuite.util.datetime_utilities import interpret_any_date
# from genericsuite.util.utilities import (
#     get_default_resultset,
#     is_under_test,
# )
# from genericsuite.util.generic_db_middleware import (
#     fetch_all_from_db,
#     add_item_to_db,
#     get_item_from_db,
#     modify_item_in_db,
# )
# from genericsuite.constants.const_tables import get_constant

# from genericsuite_ai.lib.ai_utilities import (
#     standard_gpt_func_response,
#     get_assistant_you_are,
# )
# from genericsuite_ai.lib.ai_sub_bots import ask_ai
# from genericsuite_ai.lib.ai_langchain_tools import (
#     interpret_tool_params,
# )
# from genericsuite_ai.lib.json_reader import (
#     prepare_metadata,
#     index_dict,
# )

DEBUG = False
cac = CommonAppContext()
