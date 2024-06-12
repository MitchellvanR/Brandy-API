from meal_calorie_counter import MealCalorieCounter
from input_handler import InputHandler
from ui.menus.exceptions import BackException, ExitException
from ui.console.console_operations import ConsoleOperations
from ui.text.color_string import ColorString
from ui.text.styler import Styler


class RecipeMenu:
    @staticmethod
    def display_options() -> None:
        Styler.print_white("Tracking Recipe")
        Styler.print_blue("--={*}=--")
        Styler.print_gray("Please enter the ingredients of your recipe, along")
        Styler.print_gray("with the weight of the ingredient and the amount")
        Styler.print_gray("of calories per 100g. The total amount of")
        Styler.print_gray("calories in this recipe will be printed after")
        Styler.print_gray("entering your ingredient.")
        Styler.print_blue("--={*}=--")
        Styler.print_cyan("Type 'save' to save recipe")
        Styler.print_cyan("or type 'load' to load a saved recipe.\n")

    @staticmethod
    def start_recipe_menu() -> None:
        calorie_counter = MealCalorieCounter()
        while True:
            try:
                ConsoleOperations.clear()
                RecipeMenu.display_options()
                calorie_counter.display_recipe_ingredients()
                ingredient = InputHandler.prompt_string(
                    ColorString.blue_string("Please enter the name of the ingredient: "))
                weight = InputHandler.prompt_float(
                    ColorString.blue_string("Please enter the weight of the ingredient (in grams): "))
                calories_per_100g = InputHandler.prompt_int(
                    ColorString.blue_string("Please enter the calories per 100g of the ingredient: "))
                calorie_counter.add_ingredient_to_meal(ingredient, weight, calories_per_100g)
            except BackException:
                ConsoleOperations.clear()
                break
            except ExitException:
                raise
