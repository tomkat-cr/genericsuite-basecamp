"""
Transform utilities
"""
from typing import Union
import re

from genericsuite.constants.const_tables import get_constant
from genericsuite.util.app_context import AppContext
from genericsuite.util.config_dbdef_helpers import get_json_def_both
# from genericsuite.util.app_logger import log_debug

from app.config.config import Config

DEBUG = False


class TransformUtilities:
    """
    Transform utilities general class.
    """

    def __init__(self, app_context: AppContext):
        self.app_context = app_context
        self.settings = Config(app_context)


    def transform_code_desc(
        self,
        definition_file: str,
        resultset: dict
    ) -> Union[dict, None]:
        """
        Returns the resultset with the 'select' type columns
        transformed from code to description.

        Args:
            definition_file (str): JSON definition file name
            resultset (dict): resultset where the 'select' type columns
                are transformed from code to description.

        Returns:
            Union[dict, None]: resultset with the 'select' type columns
                transformed from code to description.
        """
        table_def = get_json_def_both(definition_file)
        if not table_def:
            return None
        return {
            item_def["name"]:
            get_constant(item_def["select_elements"],
                        resultset[item_def.get("name", '')])
            if item_def["type"] == "select" and
            item_def.get("select_elements")
            else resultset.get(item_def["name"])
            for item_def in table_def["fieldElements"]
            if item_def["type"] not in ["hr", "label"]
        }

    def interpret_string(self, text: str) -> int:
        """
        Interpret a string by:
            - Returning as number if it's a number
            - Returning letter count if it's a single word
            - Otherwise returning word count (separators: dot and comma)
        """
        if text.isdigit():
            return int(text)

        words = re.sub(r'[.,]', '', text).split()
        if len(words) == 1:
            return len(words[0])

        return len(words)
