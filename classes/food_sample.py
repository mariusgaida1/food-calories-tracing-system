class FoodSample:
    """
    A class to represent a food sample, which consists of multiple food items associated with a user.

    Attributes:
    -----------
    sample_id : int
        The unique identifier for the food sample.
    user_id : int
        The unique identifier for the user associated with the food sample.
    food_items : list of FoodItem
        A list of FoodItem instances included in the food sample.
    """

    def __init__(self, sample_id, user_id, food_items):
        """
        Initializes a new FoodSample instance.

        Parameters:
        -----------
        sample_id : str
            The unique identifier for the food sample. It will be converted to an integer.
        user_id : str
            The unique identifier for the user associated with the food sample. It will be converted to an integer.
        food_items : list of FoodItem
            A list of FoodItem instances included in the food sample.
        """
        self.sample_id = int(sample_id)
        self.user_id = int(user_id)
        self.food_items = food_items

    def total_calories(self):
        """
        Calculates the total calories for all food items in the food sample.

        Returns:
        --------
        int
            The total number of calories for all food items in the food sample.
        """
        return sum(item.calories for item in self.food_items)

    def to_dict(self):
        """
        Converts the FoodSample instance to a dictionary.

        Returns:
        --------
        dict
            A dictionary representation of the FoodSample instance with keys 'sample_id', 'user_id', and 'food_items'.
        """
        return {
            "sample_id": self.sample_id,
            "user_id": self.user_id,
            "food_items": [
                item.to_dict() for item in self.food_items
            ],
        }
