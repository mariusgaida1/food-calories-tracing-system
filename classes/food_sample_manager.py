import requests
import csv
from .food_item import FoodItem
from .food_sample import FoodSample

EDAMAM_API_URL = "https://api.edamam.com/api/food-database/v2/parser"
APP_ID = "773cbd7d"
APP_KEY = "86da9e9d5ac9e21bd558fc86eed493bb"

class FoodSampleManager:
    def __init__(self, food_file='data/food_samples.csv'):
        self.food_file = food_file
        self.food_samples = self.load_food_samples()

    def fetch_food_item(self, query):
        params = {
            'app_id': APP_ID,
            'app_key': APP_KEY,
            'ingr': query
        }
        response = requests.get(EDAMAM_API_URL, params=params)
        try:    
            if response.status_code == 200:
                result = response.json()
                food_item = FoodItem(
                    name=result['parsed'][0]['food']['label'],
                    calories=result['parsed'][0]['food']['nutrients']['ENERC_KCAL']
                )
                return food_item
            else:
                return None
        except IndexError:
            pass

    def save_food_sample(self, user_id, food_items):
        food_sample = FoodSample(self.get_next_sample_id(), user_id, food_items)
        self.food_samples.append(food_sample)
        self.save_food_samples_to_file()

    def load_food_samples(self):
        food_samples = []
        try:
            with open(self.food_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    food_items = [FoodItem(name=item['name'], calories=float(item['calories'])) for item in eval(row['food_items'])]
                    food_sample = FoodSample(sample_id=row['sample_id'], user_id=row['user_id'], food_items=food_items)
                    food_samples.append(food_sample)
        except FileNotFoundError:
            pass
        return food_samples
    
    def get_next_sample_id(self):
        """Get the next user ID."""
        if not self.food_samples:
            return 1
        max_id = max(food_sample.sample_id for food_sample in self.food_samples)
        return max_id + 1

    def save_food_samples_to_file(self):
        with open(self.food_file, mode='w', newline='') as file:
            fieldnames = ['sample_id','user_id', 'food_items']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for sample in self.food_samples:
                writer.writerow(sample.to_dict())

    def get_user_food_samples(self, user_id):
        return [sample for sample in self.food_samples if int(sample.user_id) == int(user_id)]

    def delete_food_sample_by_id(self, user_id, sample_id):
        sample_id = int(sample_id)
        for sample in self.food_samples:
            if sample.sample_id == sample_id and sample.user_id == user_id:
                self.food_samples.remove(sample)
                self.save_food_samples_to_file()
                return True
        return False
    
    def delete_user_food_samples(self, user_id):
        self.food_samples = [sample for sample in self.food_samples if sample.user_id != user_id]
        self.save_food_samples_to_file()
    
    def reload_food_samples(self):
        self.food_samples = self.load_food_samples()
