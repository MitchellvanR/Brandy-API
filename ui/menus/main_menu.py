from input_handler import InputHandler
from ui.menus.recipe_menu import RecipeMenu
from ui.menus.exceptions import ExitException, BackException
from ui.text.styler import Styler
from ui.text.color_string import ColorString
from ui.console.console_operations import ConsoleOperations


class MainMenu:
    @staticmethod
    def display() -> None:
        Styler.print_bold("What can I do for you today?")
        Styler.print_blue(ColorString.bold_string("--={*}=--"))
        Styler.print_cyan("[1]: Track a recipe")
        Styler.print_cyan("[2]: Not implemented")
        Styler.print_cyan("[3]: Not implemented")
        Styler.print_cyan("[4]: Not implemented")
        Styler.print_blue(ColorString.bold_string("--={*}=--"))
        Styler.print_bold("Type 'exit' at any time to exit the application")

    @staticmethod
    def start_main_menu() -> None:
        while True:
            try:
                MainMenu.display()
                user_input = InputHandler.prompt_user_input(
                    ColorString.blue_string("Please enter one of the options listed above: "))
                MainMenu.handle_input(user_input)
            except ExitException:
                ConsoleOperations.clear()
                Styler.warning("Exiting application...")
                break
            except BackException:
                ConsoleOperations.clear()
                Styler.warning("You are already on the main menu.\n")

    @staticmethod
    def handle_input(user_input: str) -> None:
        match user_input:
            case "1":
                RecipeMenu.start_recipe_menu()
            case "2":
                ConsoleOperations.clear()
                Styler.warning("Not implemented\n")
            case "3":
                ConsoleOperations.clear()
                Styler.warning("Not implemented\n")
            case "4":
                ConsoleOperations.clear()
                Styler.warning("Not implemented\n")
            case _:
                ConsoleOperations.clear()
                Styler.warning("Please enter a valid option\n")
