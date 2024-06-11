class FoodItem:
    """
    A class to represent a food item with a name and calorie count.

    Attributes:
    -----------
    name : str
        The name of the food item.
    calories : int
        The calorie count of the food item.
    """

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def to_dict(self):
        """
        Converts the FoodItem instance to a dictionary.

        Returns:
        --------
        dict
            A dictionary representation of the FoodItem instance with keys 'name' and 'calories'.
        """
        return {"name": self.name, "calories": self.calories}
