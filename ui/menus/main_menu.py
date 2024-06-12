from ui.input.input_handler import InputHandler
from ui.menus.recipe_menu import RecipeMenu
from ui.menus.exceptions import ExitException, BackException
from ui.text.styler import Styler
from ui.text.color_string import ColorString
from ui.console.console_operations import ConsoleOperations


class MainMenu:
    @staticmethod
    def display() -> None:
        Styler.print_white("Wat kan ik vandaag voor je doen?")
        Styler.print_blue("--={*}=--")
        Styler.print_cyan("[1]: Volg een recept")
        Styler.print_cyan("[2]: Beheer ingrediënten en voedselproducten (Niet geïmplementeerd)")
        Styler.print_cyan("[3]: Volg dagelijkse calorie-inname (Niet geïmplementeerd)")
        Styler.print_cyan("[4]: Log uit (Niet geïmplementeerd)")
        Styler.print_blue("--={*}=--")
        Styler.print_white("Typ 'exit' op elk moment om de applicatie af te sluiten")

    @staticmethod
    def start_main_menu() -> None:
        while True:
            try:
                MainMenu.display()
                user_input = InputHandler.prompt_user_input(
                    ColorString.blue_string("Voer een van de bovenstaande opties in: "))
                MainMenu.handle_input(user_input)
            except ExitException:
                ConsoleOperations.clear()
                Styler.warning("Applicatie wordt afgesloten...")
                break
            except BackException:
                ConsoleOperations.clear()
                Styler.warning("Je bevindt je al in het hoofdmenu.\n")

    @staticmethod
    def handle_input(user_input: str) -> None:
        match user_input:
            case "1":
                ConsoleOperations.clear()
                RecipeMenu.start_recipe_menu()
            case "2":
                ConsoleOperations.clear()
                Styler.warning("Niet geïmplementeerd\n")
            case "3":
                ConsoleOperations.clear()
                Styler.warning("Niet geïmplementeerd\n")
            case "4":
                ConsoleOperations.clear()
                Styler.warning("Niet geïmplementeerd\n")
            case _:
                ConsoleOperations.clear()
                Styler.warning("Voer een geldige optie in\n")
