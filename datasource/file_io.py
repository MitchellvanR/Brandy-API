from ui.text.styler import Styler


class FileIO:
    @staticmethod
    def get_file_content(path: str) -> str:
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            Styler.error(f"Error: The file at {path} was not found.")
        except IOError as error:
            Styler.error(f"Error reading file at {path}: {error}")

    @staticmethod
    def write_to_file(path: str, content: str) -> None:
        try:
            with open(path, "w") as file:
                file.write(content)
        except IOError as error:
            Styler.error(f"Error writing to file at {path}: {error}")

    @staticmethod
    def append_to_file(path: str, content: str) -> None:
        try:
            with open(path, "a") as file:
                file.write(content)
        except IOError as error:
            Styler.error(f"Error writing to file at {path}: {error}")
