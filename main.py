from ui.menus.main_menu import MainMenu
from ui.text.styler import Styler


def main() -> None:
    Styler.warning("Starting application...")
    MainMenu.start_main_menu()
    Styler.warning("Application exited.")


if __name__ == "__main__":
    main()
