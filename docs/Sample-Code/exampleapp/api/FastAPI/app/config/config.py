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

        # XXX API credentials and other parameterss
        # self.XXX_API_KEY = self.get_env('XXX_API_KEY', '')
