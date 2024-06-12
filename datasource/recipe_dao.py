from datasource.file_io import FileIO
from ui.text.styler import Styler
from models.meal_ingredient import MealIngredient
import os


class RecipeDao:
    recipe_root_directory: str

    def __init__(self):
        self.recipe_root_directory = os.path.join("datasource", "files", "recipe")
        os.makedirs(self.recipe_root_directory, exist_ok=True)

    def save_recipe(self, file_name: str, content: dict) -> None:
        formatted_content = self.__format_recipe_to_string(content)
        file_path = os.path.join(self.recipe_root_directory, file_name)
        FileIO.write_to_file(file_path, formatted_content)

    def load_recipe(self, file_name: str) -> dict:
        file_path = os.path.join(self.recipe_root_directory, file_name)
        content = FileIO.get_file_content(file_path)
        return self.__format_recipe_to_dictionary(content)

    # Method is not static due to it being a private helper method. Hence, the warning suppression below.
    # noinspection PyMethodMayBeStatic
    def __format_recipe_to_string(self, content: dict) -> str:
        formatted_content = ""
        for key, ingredient in content.items():
            try:
                formatted_content += (f"{ingredient.get_name()},"
                                      f"{ingredient.get_weight()},"
                                      f"{ingredient.get_calories_per_100g()}\n")
            except AttributeError as e:
                Styler.error(f"Error formatting ingredient {key}: {e}")
        return formatted_content

    # Method is not static due to it being a private helper method. Hence, the warning suppression below.
    # noinspection PyMethodMayBeStatic
    def __format_recipe_to_dictionary(self, content: str) -> dict:
        ingredient_strings = content.strip().split("\n")
        recipe = {}
        for ingredient_string in ingredient_strings:
            attributes = ingredient_string.split(",")
            ingredient = MealIngredient(
                attributes[0],
                float(attributes[1]),
                int(attributes[2])
            )
            recipe[attributes[0]] = ingredient
        return recipe
