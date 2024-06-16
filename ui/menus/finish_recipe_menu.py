from ui.console.console_operations import ConsoleOperations
from ui.text.styler import Styler
from ui.text.color_string import ColorString
from ui.input.input_handler import InputHandler
from models.meal_calorie_counter import MealCalorieCounter


class FinishRecipeMenu:
    @staticmethod
    def display_finish_recipe_menu() -> None:
        Styler.print_white("Recept afronden")
        Styler.print_blue("--={*}=--")
        Styler.print_gray("Weeg het totale gewicht van je gerecht na bereiding.")
        Styler.print_gray("Weeg daarna je portie af en voer dit in.")
        Styler.print_gray("Brandy berekent nu het aantal calorieën in je portie.")
        Styler.print_gray("Indien het gaat om een salade waar het totale gewicht")
        Styler.print_gray("na bereiding niet veel varieert, kun je het eindaantal")
        Styler.print_gray("laten berekenen op basis van de gewichten van de")
        Styler.print_gray("ingevulde ingrediënten.")
        Styler.print_blue("--={*}=--\n")
        Styler.print_white("Typ 'sla over' als u deze stap wil overslaan.")

    @staticmethod
    def start_finish_recipe_menu(calorie_counter: MealCalorieCounter) -> None:
        FinishRecipeMenu.display_finish_recipe_menu()
        total_weight = InputHandler.prompt_string(ColorString.blue_string("Voer het totale gewicht van het recept in: "))
        validated_total_weight = FinishRecipeMenu.evaluate_input(total_weight, calorie_counter)
        portion_weight = InputHandler.prompt_float(ColorString.blue_string("Voer het gewicht van jouw portie in: "))
        calories_in_portion = calorie_counter.calculate_calories_in_portion(validated_total_weight, portion_weight)
        ConsoleOperations.clear()
        Styler.success(f"Calorieën in jouw portie: {calories_in_portion}\n")

    @staticmethod
    def evaluate_input(user_input: str, calorie_counter: MealCalorieCounter) -> float:
        while True:
            try:
                if user_input == "sla over":
                    return calorie_counter.calculate_total_meal_weight()
                return float(user_input)
            except ValueError:
                Styler.warning("Vul een getal in.")
