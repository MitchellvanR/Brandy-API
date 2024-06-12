from ui.text.text_alterations import TextAlterations


class Styler:
    @staticmethod
    def print_green(text: str) -> None:
        print(TextAlterations.GREEN + text + TextAlterations.END)

    @staticmethod
    def print_red(text: str) -> None:
        print(TextAlterations.RED + text + TextAlterations.END)

    @staticmethod
    def print_blue(text: str) -> None:
        print(TextAlterations.BLUE + text + TextAlterations.END)

    @staticmethod
    def print_cyan(text: str) -> None:
        print(TextAlterations.CYAN + text + TextAlterations.END)

    @staticmethod
    def print_pink(text: str) -> None:
        print(TextAlterations.PINK + text + TextAlterations.END)

    @staticmethod
    def print_yellow(text: str) -> None:
        print(TextAlterations.YELLOW + text + TextAlterations.END)

    @staticmethod
    def print_bold(text: str) -> None:
        print(TextAlterations.BOLD + text + TextAlterations.END)

    @staticmethod
    def print_underlined(text: str) -> None:
        print(TextAlterations.UNDERLINE + text + TextAlterations.END)

    @staticmethod
    def warning(text: str) -> None:
        print(TextAlterations.BOLD + TextAlterations.YELLOW + text + TextAlterations.END + TextAlterations.END)

    @staticmethod
    def success(text: str) -> None:
        print(TextAlterations.BOLD + TextAlterations.GREEN + text + TextAlterations.END + TextAlterations.END)

    @staticmethod
    def error(text: str) -> None:
        print(TextAlterations.BOLD + TextAlterations.RED + text + TextAlterations.END + TextAlterations.END)
