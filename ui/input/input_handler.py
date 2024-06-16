from ui.menus.exceptions import BackException, ExitException
from ui.text.styler import Styler


class InputHandler:
    @staticmethod
    def prompt_user_input(prompt: str) -> str:
        user_input = input(prompt).strip().lower()
        if user_input == "terug":
            raise BackException()
        elif user_input == "sluit":
            raise ExitException()
        return user_input

    @staticmethod
    def prompt_string(prompt: str) -> str:
        return InputHandler.prompt_user_input(prompt)

    @staticmethod
    def prompt_number(prompt: str, conversion_function, error_message: str):
        while True:
            try:
                user_input = input(prompt).strip().lower()
                if user_input == "terug":
                    raise BackException()
                elif user_input == "sluit":
                    raise ExitException()
                return conversion_function(user_input)
            except ValueError:
                Styler.warning(f"\n{error_message}\n")

    @staticmethod
    def prompt_int(prompt: str) -> int:
        return InputHandler.prompt_number(prompt, int, "Vul een geheel getal in.")

    @staticmethod
    def prompt_float(prompt: str) -> float:
        return InputHandler.prompt_number(prompt, float, "Vul een getal in.")
