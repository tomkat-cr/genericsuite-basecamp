"""
Convertion utilities
"""
from typing import Union

from genericsuite.util.app_context import AppContext
# from genericsuite.util.app_logger import log_debug

from app.config.config import Config

DEBUG = False


class ConvertionUtilities:
    """
    Convertion utilities general class, to convert weight and height.
    """

    def __init__(self, app_context: AppContext):
        self.app_context = app_context
        self.settings = Config(app_context)

    def convert_height(self, height: float, height_unit: str,
                       target_unit: str) -> Union[float, Exception]:
        """ Convert the give height from one unit to another """
        result = None
        if height_unit == target_unit:
            result = height
        if height_unit == 'cm' and target_unit == 'm':
            result = height / 100
        if height_unit == 'm' and target_unit == 'cm':
            result = height * 100
        if height_unit in ['i', 'in'] and target_unit == 'm':
            result = height * 0.0254
        if height_unit == 'm' and target_unit in ['i', 'in']:
            result = height / 0.0254
        if height_unit in ['i', 'in'] and target_unit == 'cm':
            result = height * 2.54
        if height_unit == 'cm' and target_unit in ['i', 'in']:
            result = height / 2.54
        if result is None:
            raise TypeError(f"Unsupported conversion from {height_unit}" +
                            f" to {target_unit}")
        return result

    def convert_weight(self, weight: float, weight_unit: str,
                       target_unit: str) -> Union[float, Exception]:
        """ Convert the give weight from one unit to another """
        if weight_unit == target_unit:
            return weight
        if weight_unit == 'kg' and target_unit == 'lb':
            return weight * 2.20462
        if weight_unit == 'lb' and target_unit == 'kg':
            return weight / 2.20462
        raise TypeError(f"Unsupported conversion from {weight_unit}" +
                        f" to {target_unit}")
