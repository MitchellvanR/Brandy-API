from input_handler import InputHandler
from menus.recipe_menu import RecipeMenu
from menus.exceptions import ExitException


class MainMenu:
    @staticmethod
    def display() -> None:
        print("What can I do for you today?")
        print("--={*}=--")
        print("[1]: Track a recipe")
        print("[2]: Not implemented")
        print("[3]: Not implemented")
        print("[4]: Not implemented")
        print("--={*}=--")
        print("Type 'exit' at any time to exit the application")

    @staticmethod
    def start_main_menu() -> None:
        while True:
            try:
                MainMenu.display()
                user_input = InputHandler.prompt_user_input("Please enter one of the options listed above: ")
                MainMenu.handle_input(user_input)
            except ExitException:
                print("Exiting application...")
                break

    @staticmethod
    def handle_input(user_input: str) -> None:
        match user_input:
            case "1":
                print()
                RecipeMenu.start_recipe_menu()
                print()
            case "2":
                print()
                print("Not implemented")
                print()
            case "3":
                print()
                print("Not implemented")
                print()
            case "4":
                print()
                print("Not implemented")
                print()
            case _:
                print()
                print("Please enter a valid option")
                print()
