class FoodItem:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def to_dict(self):
        return {
            'name': self.name,
            'calories': self.calories
        }