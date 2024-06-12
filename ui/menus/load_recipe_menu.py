import os

from ui.console.console_operations import ConsoleOperations
from ui.input.input_handler import InputHandler
from ui.menus.exceptions import BackException, ExitException
from ui.text.color_string import ColorString
from ui.text.styler import Styler
from models.meal_calorie_counter import MealCalorieCounter
from datasource.exceptions import FileIOException


class LoadRecipeMenu:
    available_file_names: list = []

    @staticmethod
    def start_load_recipe_menu(calorie_counter: MealCalorieCounter) -> None:
        while True:
            try:
                LoadRecipeMenu.available_file_names = []
                LoadRecipeMenu.display_available_recipes()
                user_input = InputHandler.prompt_string(
                    ColorString.blue_string("Typ de naam van een van de bovenstaande recepten: "))
                if user_input in LoadRecipeMenu.available_file_names:
                    calorie_counter.load_recipe(user_input)
                    raise BackException
                ConsoleOperations.clear()
                Styler.warning("Voer de naam van een van onderstaande recepten in\n")
            except BackException:
                ConsoleOperations.clear()
                break
            except ExitException:
                raise
            except FileIOException:
                raise

    @staticmethod
    def display_available_recipes() -> None:
        Styler.print_white("Welk recept wilt u laden?")
        Styler.print_blue("--={*}=--")
        LoadRecipeMenu.display_recipe_file_names()
        Styler.print_blue("--={*}=--\n")

    @staticmethod
    def display_recipe_file_names() -> None:
        extracted_file_names = os.listdir(os.path.join("datasource", "files", "recipe"))
        for file_name in extracted_file_names:
            formatted_file_name = os.path.splitext(file_name)[0]
            LoadRecipeMenu.available_file_names.append(formatted_file_name)
            Styler.print_cyan(formatted_file_name)
