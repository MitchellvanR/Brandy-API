from meal_calorie_counter import MealCalorieCounter
from input_handler import InputHandler
from ui.menus.exceptions import BackException, ExitException
from ui.console.console_operations import ConsoleOperations
from ui.text.color_string import ColorString


class RecipeMenu:
    @staticmethod
    def start_recipe_menu() -> None:
        calorie_counter = MealCalorieCounter()
        while True:
            try:
                ConsoleOperations.clear()
                calorie_counter.display_recipe_ingredients()
                ingredient = InputHandler.prompt_string(
                    ColorString.blue_string("Please enter the name of the ingredient: "))
                weight = InputHandler.prompt_float(
                    ColorString.blue_string("Please enter the weight of the ingredient (in grams): "))
                calories_per_100g = InputHandler.prompt_int(
                    ColorString.blue_string("Please enter the calories per 100g of the ingredient: "))
                print()
                calorie_counter.add_ingredient_to_meal(ingredient, weight, calories_per_100g)
            except BackException:
                ConsoleOperations.clear()
                break
            except ExitException:
                raise
