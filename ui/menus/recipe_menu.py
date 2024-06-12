from models.meal_calorie_counter import MealCalorieCounter
from ui.input.input_handler import InputHandler
from ui.menus.exceptions import BackException, ExitException
from ui.console.console_operations import ConsoleOperations
from ui.text.color_string import ColorString
from ui.text.styler import Styler


class RecipeMenu:
    calorie_counter = MealCalorieCounter()

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
        Styler.print_white("What would you like to do?")
        Styler.print_blue("--={*}=--")
        Styler.print_cyan("[1]: Add an ingredient")
        Styler.print_cyan("[2]: Save this recipe (Not implemented)")
        Styler.print_cyan("[3]: Load a recipe (Not implemented)")
        Styler.print_blue("--={*}=--\n")

    @staticmethod
    def start_recipe_menu() -> None:
        while True:
            try:
                RecipeMenu.display_options()
                RecipeMenu.calorie_counter.display_recipe_ingredients()
                user_input = InputHandler.prompt_string(
                    ColorString.blue_string("Please enter one of the options listed above: "))
                RecipeMenu.handle_user_input(user_input)
            except BackException:
                ConsoleOperations.clear()
                break
            except ExitException:
                raise

    @staticmethod
    def handle_user_input(user_input: str) -> None:
        match user_input:
            case "1":
                RecipeMenu.add_ingredient()
            case "2":
                ConsoleOperations.clear()
                Styler.warning("Not implemented\n")
            case "3":
                ConsoleOperations.clear()
                Styler.warning("Not implemented\n")
            case _:
                ConsoleOperations.clear()
                Styler.warning("Please enter a valid option\n")

    @staticmethod
    def add_ingredient():
        try:
            ingredient = InputHandler.prompt_string(
                ColorString.blue_string("\nPlease enter the name of the ingredient: "))
            weight = InputHandler.prompt_float(
                ColorString.blue_string("Please enter the weight of the ingredient (in grams): "))
            calories_per_100g = InputHandler.prompt_int(
                ColorString.blue_string("Please enter the calories per 100g of the ingredient: "))
            RecipeMenu.calorie_counter.add_ingredient_to_meal(ingredient, weight, calories_per_100g)
            ConsoleOperations.clear()
        except BackException:
            raise
        except ExitException:
            raise
