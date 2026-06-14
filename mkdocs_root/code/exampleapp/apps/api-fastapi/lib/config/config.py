"""
General configuration module
"""
# C0103 | Disable "name doesn't conform to naming rules..." (snake_case)
# pylint: disable=C0103

from typing import Any

from genericsuite_ai.config.config import Config as ConfigSuperClass


class Config(ConfigSuperClass):
    """
    General configuration parameters read from environment variables
    """

    def __init__(self, app_context: Any = None) -> None:
        super().__init__(app_context)

        # FDA API credentials and other parameters
        self.FDA_API_KEY = self.get_env('FDA_API_KEY', '')

        # Minimun kcal formula method
        # Options: "hb", "msj", "ck"
        # "hb" = Harris-Benedict formula
        # "msj" = Mifflin - St Jeor formula
        # "ck" = Christian Kosmos formula
        self.MIN_KCAL_FORMULA = self.get_env('MIN_KCAL_FORMULA', "ck")
