import os

from ui.console.console_operations import ConsoleOperations
from ui.input.input_handler import InputHandler
from ui.menus.exceptions import BackException, ExitException
from ui.text.color_string import ColorString
from ui.text.styler import Styler
from ui.menus.display_recipe_menu_modes import DisplayRecipeMenuModes
from models.meal_calorie_counter import MealCalorieCounter
from datasource.exceptions import FileIOException


class DisplayRecipesMenu:
    available_file_names: list = []
    current_mode: str

    @staticmethod
    def start_display_recipes_menu(calorie_counter: MealCalorieCounter) -> None:
        while True:
            try:
                DisplayRecipesMenu.available_file_names = []
                DisplayRecipesMenu.display_available_recipes()
                user_input = InputHandler.prompt_string(
                    ColorString.blue_string(
                        f"Voer de naam in van een van de bovenstaande recepten om te "
                        f"{DisplayRecipesMenu.current_mode}: "))
                if user_input in DisplayRecipesMenu.available_file_names:
                    DisplayRecipesMenu.handle_menu_action(user_input, calorie_counter)
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
    def handle_menu_action(user_input: str, calorie_counter: MealCalorieCounter):
        match DisplayRecipesMenu.current_mode:
            case DisplayRecipeMenuModes.LOAD:
                calorie_counter.load_recipe(user_input)
            case DisplayRecipeMenuModes.DELETE:
                calorie_counter.delete_recipe(user_input)

    @staticmethod
    def set_display_mode(mode: str):
        DisplayRecipesMenu.current_mode = mode

    @staticmethod
    def display_available_recipes() -> None:
        Styler.print_white(f"Welk recept wilt u {DisplayRecipesMenu.current_mode}?")
        Styler.print_blue("--={*}=--")
        DisplayRecipesMenu.display_recipe_file_names()
        Styler.print_blue("--={*}=--\n")

    @staticmethod
    def display_recipe_file_names() -> None:
        extracted_file_names = os.listdir(os.path.join("datasource", "files", "recipe"))
        for file_name in extracted_file_names:
            formatted_file_name = os.path.splitext(file_name)[0]
            DisplayRecipesMenu.available_file_names.append(formatted_file_name)
            Styler.print_cyan(formatted_file_name)
