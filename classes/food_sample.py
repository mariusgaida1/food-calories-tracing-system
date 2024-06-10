class FoodSample:
    def __init__(self, sample_id, user_id, food_items):
        self.sample_id = int(sample_id)
        self.user_id = int(user_id)
        self.food_items = food_items

    def total_calories(self):
        return sum(item.calories for item in self.food_items)

    def to_dict(self):
        return {
            'sample_id': self.sample_id,
            'user_id': self.user_id,
            'food_items': [item.to_dict() for item in self.food_items]
        }