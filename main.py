from ui.menus.main_menu import MainMenu
from ui.text.styler import Styler
from ui.console.console_operations import ConsoleOperations


def main() -> None:
    ConsoleOperations.clear()
    Styler.warning("Applicatie wordt gestart...\n")
    MainMenu.start_main_menu()
    Styler.warning("Applicatie afgesloten.")


if __name__ == "__main__":
    main()
