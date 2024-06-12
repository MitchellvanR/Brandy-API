from ui.text.text_alterations import TextAlterations


class ColorString:
    @staticmethod
    def green_string(text: str) -> str:
        return TextAlterations.GREEN + text + TextAlterations.END

    @staticmethod
    def red_string(text: str) -> str:
        return TextAlterations.RED + text + TextAlterations.END

    @staticmethod
    def blue_string(text: str) -> str:
        return TextAlterations.BLUE + text + TextAlterations.END

    @staticmethod
    def cyan_string(text: str) -> str:
        return TextAlterations.CYAN + text + TextAlterations.END

    @staticmethod
    def pink_string(text: str) -> str:
        return TextAlterations.PINK + text + TextAlterations.END

    @staticmethod
    def yellow_string(text: str) -> str:
        return TextAlterations.YELLOW + text + TextAlterations.END

    @staticmethod
    def bold_string(text: str) -> str:
        return TextAlterations.BOLD + text + TextAlterations.END

    @staticmethod
    def underlined_string(text: str) -> str:
        return TextAlterations.UNDERLINE + text + TextAlterations.END

    @staticmethod
    def warning_string(text: str) -> str:
        return TextAlterations.BOLD + TextAlterations.YELLOW + text + TextAlterations.END + TextAlterations.END

    @staticmethod
    def success_string(text: str) -> str:
        return TextAlterations.BOLD + TextAlterations.GREEN + text + TextAlterations.END + TextAlterations.END

    @staticmethod
    def error_string(text: str) -> str:
        return TextAlterations.BOLD + TextAlterations.RED + text + TextAlterations.END + TextAlterations.END
