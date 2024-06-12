from os import system, name


class ConsoleOperations:
    @staticmethod
    def clear() -> None:
        # Windows
        if name == 'nt':
            _ = system('cls')
        # Mac / Linux
        else:
            _ = system('clear')
