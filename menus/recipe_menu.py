from meal_calorie_counter import MealCalorieCounter
from input_handler import InputHandler
from menus.exceptions import BackException, ExitException


class RecipeMenu:
    @staticmethod
    def start_recipe_menu() -> None:
        calorie_counter = MealCalorieCounter()
        while True:
            try:
                ingredient = InputHandler.prompt_string("Please enter the name of the ingredient: ")
                weight = InputHandler.prompt_float("Please enter the weight of the ingredient (in grams): ")
                calories_per_100g = InputHandler.prompt_int("Please enter the calories per 100g of the ingredient: ")
                print()
                calorie_counter.add_ingredient_to_meal(ingredient, weight, calories_per_100g)
                calorie_counter.display_recipe_ingredients()
            except BackException:
                break
            except ExitException:
                raise
