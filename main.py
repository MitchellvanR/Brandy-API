from ui.menus.main_menu import MainMenu
from ui.text.styler import Styler
from ui.console.console_operations import ConsoleOperations


def main() -> None:
    ConsoleOperations.clear()
    Styler.warning("Starting application...")
    MainMenu.start_main_menu()
    Styler.warning("Application exited.")


if __name__ == "__main__":
    main()
