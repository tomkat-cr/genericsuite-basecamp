"""
Food specific utilities
"""
from typing import Union
from datetime import date
import re

from lib.config.config import Config
from genericsuite.util.app_context import AppContext
from genericsuite.util.app_logger import log_debug

DEBUG = False


class FoodUtilities:
    """
    Food utilities general class, to calculate calories related
    data, interpret exercise days string, convertions, et al.
    """

    def __init__(self, app_context: AppContext):
        self.app_context = app_context
        self.settings = Config(app_context)

    def total_calories(
        self,
        calories_value: float,
        serving_size: float,
        quantity: float,
    ) -> float:
        """
        Calculate the total calories for a daily meal or dish
        ingredient.

        Args:
            calories_value (float): ingredient calories
            serving_size (float): ingredient serving size for the given calories
            quantity (float): ingredient quantity

        Returns:
            dict: The updated daily meal with the total calories and
            converted calories unit.
        """
        return round(
            ((calories_value * quantity) /
              serving_size)
            if serving_size > 0 else 0,
            2
        )

    def sum_total_calories(self, item: dict, array_name: str) -> dict:
        """
        Calculate the total calories for a daily meal or dish
        and convert the calories to the desired unit.

        Args:
            item (dict): The daily meal containing the
                ingredients with calories, calories unit, serving size,
                serving size unit and quantity.

        Returns:
            dict: The updated daily meal with the total calories and
            converted calories unit.
        """
        if DEBUG:
            log_debug('AI_AITD-1) sum_total_calories' +
                      f' array_nname: {array_name} | BEFORE item: {item}')
        total_calories = 0
        for ingredient in item.get(array_name, []):
            if ingredient.get("total_calories", 0) <= 0:
                ingredient["total_calories"] = (
                    0 if ingredient['serving_size'] <= 0
                    else (
                        ingredient['calories_value'] * ingredient['quantity']
                    )
                    / ingredient['serving_size']
                )
            total_calories += self.convert_calories_to_unit(
                ingredient["total_calories"],
                ingredient["calories_unit"],
                item.get("calories_unit", 'kcal')
            )
        item["total_calories"] = total_calories
        if DEBUG:
            log_debug('AI_AITD-1) sum_total_calories' +
                      f' | AFTER item: {item}')
        return item

    def calculate_quantity(
        self,
        serving_size: float,
        total_calories: float,
        calories_value: float,
    ):
        """
        Calculate the ingredient quantity given the serving size, total calories
        and calories value.
        Formula: quantity = (serving_size * total_calories) / calories_value
        """
        if calories_value > 0:
            quantity = (serving_size * total_calories) / calories_value
        else:
            quantity = 0
        return quantity

    # def convert_calories_to_unit(
    #     calories: float, from_unit: str, to_unit: str
    # ) -> float:
    #     """
    #     Convert calories from one unit to another.

    #     Args:
    #         calories (float): The calories value to be converted.
    #         from_unit (str): The unit of the calories value.
    #         to_unit (str): The desired unit to convert the calories value to.

    #     Returns:
    #         float: The converted calories value.
    #     """
    #     if from_unit == "kcal" and to_unit == "kj":
    #         result = calories * 4.184
    #     elif from_unit == "kj" and to_unit == "kcal":
    #         result = calories / 4.184
    #     else:
    #         result = calories
    #     if DEBUG:
    #         log_debug('AI_CCTU-1) convert_calories_to_unit' +
    #                   f' | result: {result}')
    #     return result

    def convert_calories_to_unit(self, calories: float, from_unit: str,
                                 to_unit: str = "kcal") -> float:
        """
        Convert calories from one unit to another.

        Args:
            calories (float): The calories value to be converted.
            from_unit (str): The unit of the calories value.
            to_unit (str): The desired unit to convert the calories value to.

        Returns:
            float: The converted calories value.
        """
        units = {"kcal": 1, "kj": 0.239006}
        result = calories * (units[from_unit] / units[to_unit])
        if DEBUG:
            log_debug('AI_CCTU-1) convert_calories_to_unit' +
                      f' | result: {result}')
        return result

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

    def get_bmr(
        self,
        weight: float,
        height: float,
        gender: str,
        age: int,
    ) -> float:
        """
        Get the BMR (Basal Methabolic Rate).

        MIN_KCAL_FORMULA options:
        "hb" = Harris-Benedict formula
        "msj" = Mifflin - St Jeor formula
        "ck" = Christian Kosmos formula
        """
        if gender.lower() in ['male', 'm']:
            if self.settings.MIN_KCAL_FORMULA == "hb":
                bmr = 88.362 + (13.397 * weight) + (4.799 * height) - \
                    (5.677 * age)
            elif self.settings.MIN_KCAL_FORMULA == "msj":
                bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
            else:
                bmr = 22 * weight
        else:
            if self.settings.MIN_KCAL_FORMULA == "hb":
                bmr = 447.593 + (9.247 * weight) + (3.098 * height) - \
                    (4.330 * age)
            elif self.settings.MIN_KCAL_FORMULA == "msj":
                bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
            else:
                bmr = 22 * weight

        if DEBUG:
            log_debug(f"get_bmr: {gender}, age: {age}, bmr: {bmr}")

        return bmr

    def get_minimum_daily_calories(
        self,
        weight: float,
        height: float,
        age: int,
        gender: str,
        exercise_days: int,
        goal_code: str = "-20"
    ) -> float:
        """
        Calculates the minimum daily calories required based on weight, height,
        age, gender, exercise days, and goal code.

        Args:
            weight (float): weight in kg
            height (float): height in meters
            age (int): age in years
            gender (str): gender. Valid options: 'm', 'f'
            exercise_days (int): number of exercise days
            goal_code (str): Goal code, Defaults to "-20"

        Returns:
            float: minimum daily calories
        """
        bmr = self.get_bmr(weight, height, gender, age)

        if exercise_days <= 1:
            calories = bmr * 1.2
        elif exercise_days <= 3:
            calories = bmr * 1.375
        elif exercise_days <= 5:
            calories = bmr * 1.55
        elif exercise_days <= 6:
            calories = bmr * 1.725
        else:
            calories = bmr * 1.9

        calories_final = self.apply_goal(calories, goal_code)

        if DEBUG:
            log_debug(f"get_minimum_daily_calories: weight={weight}" +
                      f", height={height}, age={age}" +
                      f", gender={gender}, exercise_days={exercise_days}" +
                      f", goal_code={goal_code}" +
                      f"\nbmr: {bmr}" +
                      f"\ncalories: {calories}" +
                      f"\nfinal: {calories_final}")

        return calories_final

    def apply_goal(self, calories: float, goal_code: str = None) -> float:
        """
        Apply a goal to the given calories based on the goal code.

        Args:
            calories (float): calories
            goal_code (str): goal code. Check GOAL_CODES in the
            "app_constants.json" file.

        Returns:
            float: the calories plus/minus the calories percent
            according to the goal.
        """
        perc = float(goal_code) if goal_code else -20
        result = calories + ((calories * perc) / 100)
        if DEBUG:
            log_debug(f"apply_goal: calories={calories}, goal_code={goal_code}," +
                  f" perc={perc}, result={result}")
        return result

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
