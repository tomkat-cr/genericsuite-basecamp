"""
Food specific utilities
"""
from datetime import date

from genericsuite.util.app_context import AppContext
# from genericsuite.util.app_logger import log_debug

from app.config.config import Config

DEBUG = False


class AgeUtilities:
    """
    Age utilities general class, to calculate age related calculations.
    """

    def __init__(self, app_context: AppContext):
        self.app_context = app_context
        self.settings = Config(app_context)

    def calculate_age(self, birth_date: date) -> int:
        """
        Calculates the age today for a given date

        Args:
            birth_date (date): date of birth

        Returns:
            int: age in years
        """
        today = date.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or \
           (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age
