from meal_ingredient import MealIngredient
from ui.text.styler import Styler
from ui.text.color_string import ColorString


class MealCalorieCounter:
    ingredients: dict
    total_calories: int

    def __init__(self) -> None:
        self.ingredients = {}
        self.total_calories = 0

    def add_ingredient_to_meal(self, ingredient: str, weight: float, calories_per_100g: int) -> None:
        self.ingredients.update({ingredient: MealIngredient(ingredient, weight, calories_per_100g)})

    def display_recipe_ingredients(self) -> None:
        total_calories = 0
        for key in self.ingredients:
            ingredient = self.ingredients[key]
            Styler.success(f"{ingredient.get_name()}: "
                           f"{ingredient.get_calories_in_portion()} kcal for "
                           f"{ingredient.get_weight()}g")
            total_calories += ingredient.get_calories_in_portion()
        self.total_calories = total_calories
        Styler.success(f"Total calories: {self.get_total_calories()}")

    def get_total_calories(self):
        return self.total_calories
