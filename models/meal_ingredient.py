class MealIngredient:
    name: str
    weight: float
    calories_per_100g: int
    calories_in_portion: int

    def __init__(self, name: str, weight: float, calories_per_100g: int) -> None:
        self.name = name
        self.weight = weight
        self.calories_per_100g = calories_per_100g
        self.calories_in_portion = int(0.01 * self.calories_per_100g * self.weight)

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_calories_per_100g(self):
        return self.calories_per_100g

    def get_calories_in_portion(self):
        return self.calories_in_portion
