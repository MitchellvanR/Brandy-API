from meal_calorie_counter import MealCalorieCounter


class InputHandler:
    valid_menu_inputs = {
        "1": "add",
        "2": "subtract",
        "3": "multiply",
        "4": "divide",
        "exit": "exit"
    }

    main_menu = (
        "\nPlease choose a mathematical operator \n"
        "[1] Add \n"
        "[2] Subtract \n"
        "[3] Multiply \n"
        "[4] Divide \n"
        "Type 'exit' to close the application \n\n"
        "Please enter the number corresponding to the operation: "
    )

    @staticmethod
    def main_menu() -> None:
        while True:
            choice = InputHandler.prompt_string("What can I do for you?")
            if choice == "Enter a recipe":
                break
            print(choice)

    @staticmethod
    def recipe_menu() -> None:
        calorie_counter = MealCalorieCounter()
        while True:
            ingredient = InputHandler.prompt_string("Please enter the name of the ingredient: ")
            if ingredient == "exit":
                break
            weight = InputHandler.prompt_float("Please enter the weight of the ingredient: ")
            if weight == "exit":
                break
            calories_per_100g = InputHandler.prompt_int("Please enter the calories per 100g of the ingredient: ")
            if calories_per_100g == "exit":
                break
            print()
            calorie_counter.add_ingredient_to_meal(ingredient, float(weight), int(calories_per_100g))
            calorie_counter.display_recipe_ingredients()

    @staticmethod
    def prompt_string(prompt: str) -> str:
        return input(prompt).strip().lower()

    @staticmethod
    def prompt_number(prompt: str, conversion_function, error_message: str):
        while True:
            try:
                return conversion_function(input(prompt))
            except ValueError:
                print(f"\n{error_message}\n")

    @staticmethod
    def prompt_int(prompt: str) -> int:
        return InputHandler.prompt_number(prompt, int, "Please enter a whole number.")

    @staticmethod
    def prompt_float(prompt: str) -> float:
        return InputHandler.prompt_number(prompt, float, "Please enter a number (whole or decimal).")
