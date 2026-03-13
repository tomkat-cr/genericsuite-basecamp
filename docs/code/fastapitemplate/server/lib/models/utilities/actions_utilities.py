"""
Food specific utilities
"""
from lib.config.config import Config
from genericsuite.util.app_context import AppContext
# from genericsuite.util.app_logger import log_debug

DEBUG = False


class ActionsUtilities:
    """
    Actions utilities general class, to calculate actions related
    data, interpret exercise days string, convertions, et al.
    """

    def __init__(self, app_context: AppContext):
        self.app_context = app_context
        self.settings = Config(app_context)
