from models.meal_calorie_counter import MealCalorieCounter
from datasource.exceptions import FileIOException
from ui.menus.display_recipe_menu import DisplayRecipesMenu
from ui.menus.finish_recipe_menu import FinishRecipeMenu
from ui.input.input_handler import InputHandler
from ui.menus.exceptions import BackException, ExitException
from ui.console.console_operations import ConsoleOperations
from ui.text.color_string import ColorString
from ui.text.styler import Styler
from ui.menus.display_recipe_menu_modes import DisplayRecipeMenuModes


class RecipeMenu:
    calorie_counter: MealCalorieCounter = MealCalorieCounter()

    @staticmethod
    def display_options() -> None:
        Styler.print_white("Recept Volgen")
        Styler.print_blue("--={*}=--")
        Styler.print_pink(f"Huidig recept: {RecipeMenu.calorie_counter.get_current_file_name()}")
        Styler.print_blue("--={*}=--")
        Styler.print_gray("Voer de ingrediënten van je recept in, samen")
        Styler.print_gray("met het gewicht van het ingrediënt en de hoeveelheid")
        Styler.print_gray("calorieën per 100g. Het totale aantal")
        Styler.print_gray("calorieën in dit recept wordt weergegeven na")
        Styler.print_gray("het invoeren van je ingrediënt.")
        Styler.print_blue("--={*}=--")
        Styler.print_white("Wat wil je doen?")
        Styler.print_blue("--={*}=--")
        Styler.print_cyan("[1]: Voeg een ingrediënt toe")
        Styler.print_cyan("[2]: Bewaar dit recept")
        Styler.print_cyan("[3]: Bewaar als nieuw recept")
        Styler.print_cyan("[4]: Laad een recept")
        Styler.print_cyan("[5]: Verwijder een recept")
        Styler.print_cyan("[6]: Maak recept leeg")
        Styler.print_cyan("[7]: Recept afronden")

    @staticmethod
    def start_recipe_menu() -> None:
        while True:
            try:
                RecipeMenu.display_options()
                RecipeMenu.calorie_counter.display_recipe_ingredients()
                user_input = InputHandler.prompt_string(
                    ColorString.blue_string("Voer een van de bovenstaande opties in: "))
                RecipeMenu.handle_user_input(user_input)
            except BackException:
                ConsoleOperations.clear()
                break
            except ExitException:
                raise

    @staticmethod
    def handle_user_input(user_input: str) -> None:
        match user_input:
            case "1":
                RecipeMenu.add_ingredient()
            case "2":
                RecipeMenu.evaluate_recipe_saving_mode()
            case "3":
                RecipeMenu.save_as_new_recipe()
            case "4":
                RecipeMenu.start_display_recipe_menu(DisplayRecipeMenuModes.LOAD)
            case "5":
                RecipeMenu.start_display_recipe_menu(DisplayRecipeMenuModes.DELETE)
            case "6":
                RecipeMenu.clear_recipe()
            case "7":
                RecipeMenu.finish_recipe()
            case _:
                ConsoleOperations.clear()
                Styler.warning("Voer een geldige optie in\n")

    @staticmethod
    def add_ingredient() -> None:
        try:
            ingredient = InputHandler.prompt_string(
                ColorString.blue_string("\nVoer de naam van het ingrediënt in: "))
            weight = InputHandler.prompt_float(
                ColorString.blue_string("Voer het gewicht van het ingrediënt in (in gram): "))
            calories_per_100g = InputHandler.prompt_int(
                ColorString.blue_string("Voer het aantal calorieën per 100g van het ingrediënt in: "))
            RecipeMenu.calorie_counter.add_ingredient_to_meal(ingredient, weight, calories_per_100g)
            ConsoleOperations.clear()
        except BackException:
            raise
        except ExitException:
            raise

    @staticmethod
    def evaluate_recipe_saving_mode() -> None:
        file_name = RecipeMenu.calorie_counter.get_current_file_name()
        if file_name == "Nieuw Recept":
            RecipeMenu.save_as_new_recipe()
        else:
            RecipeMenu.save_recipe(file_name)

    @staticmethod
    def save_as_new_recipe() -> None:
        file_name = InputHandler.prompt_string(
            ColorString.blue_string("\nGeef de naam van het bestand waarin u het recept wil opslaan: "))
        RecipeMenu.save_recipe(file_name)

    @staticmethod
    def save_recipe(file_name: str) -> None:
        Styler.warning("Opslaan...")
        RecipeMenu.calorie_counter.save_recipe(file_name)
        ConsoleOperations.clear()
        Styler.success("Recept opgeslagen!\n")

    @staticmethod
    def start_display_recipe_menu(display_mode: str) -> None:
        ConsoleOperations.clear()
        try:
            DisplayRecipesMenu.set_display_mode(display_mode)
            DisplayRecipesMenu.start_display_recipes_menu(RecipeMenu.calorie_counter)
            match display_mode:
                case DisplayRecipeMenuModes.LOAD:
                    Styler.success("Recept geladen!\n")
                case DisplayRecipeMenuModes.DELETE:
                    Styler.success("Recept verwijderd! \n")
        except FileIOException:
            pass

    @staticmethod
    def clear_recipe() -> None:
        ConsoleOperations.clear()
        RecipeMenu.calorie_counter.clear_recipe()

    @staticmethod
    def finish_recipe() -> None:
        ConsoleOperations.clear()
        FinishRecipeMenu.start_finish_recipe_menu(RecipeMenu.calorie_counter)
