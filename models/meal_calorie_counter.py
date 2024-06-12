from typing import TextIO

from models.meal_ingredient import MealIngredient
from datasource.recipe_dao import RecipeDao
from ui.text.styler import Styler


class MealCalorieCounter:
    recipe_dao: RecipeDao
    ingredients: dict
    total_calories: int

    def __init__(self) -> None:
        self.recipe_dao = RecipeDao()
        self.ingredients = {}
        self.total_calories = 0

    def add_ingredient_to_meal(self, ingredient: str, weight: float, calories_per_100g: int) -> None:
        self.ingredients.update({ingredient: MealIngredient(ingredient, weight, calories_per_100g)})

    def display_recipe_ingredients(self) -> None:
        total_calories = 0
        for key in self.ingredients:
            ingredient = self.ingredients[key]
            Styler.success(f"{ingredient.get_name().capitalize()}: "
                           f"{ingredient.get_calories_in_portion()} kcal voor "
                           f"{ingredient.get_weight()}g")
            total_calories += ingredient.get_calories_in_portion()
        self.total_calories = total_calories
        Styler.success(f"\nTotale calorieën: {self.get_total_calories()}\n")

    def get_total_calories(self):
        return self.total_calories

    def save_recipe(self, file_name: str) -> None:
        self.recipe_dao.save_recipe(file_name, self.ingredients)

    def load_recipe(self, file_name: str) -> None:
        recipe = self.recipe_dao.load_recipe(file_name)
        self.ingredients = recipe
