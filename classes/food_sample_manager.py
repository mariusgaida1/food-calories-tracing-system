import requests
import csv
from .food_item import FoodItem
from .food_sample import FoodSample

EDAMAM_API_URL = "https://api.edamam.com/api/food-database/v2/parser"
APP_ID = "773cbd7d"
APP_KEY = "86da9e9d5ac9e21bd558fc86eed493bb"


class FoodSampleManager:
    """
    A class to manage food samples, including loading from and saving to a CSV file, 
    fetching food item data from an external API.

    Attributes:
    -----------
    food_file : str
        The path to the CSV file storing food samples.
    food_samples : list of FoodSample
        A list of FoodSample instances loaded from the CSV file.
    """
    def __init__(self, food_file="data/food_samples.csv"):
        """
        Initializes a new FoodSampleManager instance and loads food samples from the CSV file.

        Parameters:
        -----------
        food_file : str, optional
            The path to the CSV file storing food samples (default is 'data/food_samples.csv').
        """
        self.food_file = food_file
        self.food_samples = self.load_food_samples()

    def fetch_food_item(self, query):
        """
        Fetches food item data from the Edamam API.

        Parameters:
        -----------
        query : str
            The food item query string.

        Returns:
        --------
        FoodItem or None
            A FoodItem instance if the API call is successful and data is found, otherwise None.
        """
        params = {"app_id": APP_ID, "app_key": APP_KEY, "ingr": query}
        response = requests.get(EDAMAM_API_URL, params=params)
        try:
            if response.status_code == 200:
                result = response.json()
                food_item = FoodItem(
                    name=result["parsed"][0]["food"]["label"],
                    calories=result["parsed"][0]["food"]["nutrients"]["ENERC_KCAL"],
                )
                return food_item
            else:
                return None
        except IndexError:
            pass

    def save_food_sample(self, user_id, food_items):
        """
        Saves a new food sample to the list and writes to the CSV file.

        Parameters:
        -----------
        user_id : int
            The unique identifier for the user.
        food_items : list of FoodItem
            A list of FoodItem instances included in the food sample.
        """
        food_sample = FoodSample(self.get_next_sample_id(), user_id, food_items)
        self.food_samples.append(food_sample)
        self.save_food_samples_to_file()

    def load_food_samples(self):
        """
        Loads food samples from the CSV file.

        Returns:
        --------
        list of FoodSample
            A list of FoodSample instances loaded from the CSV file.
        """
        food_samples = []
        try:
            with open(self.food_file, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    food_items = [
                        FoodItem(name=item["name"], calories=float(item["calories"]))
                        for item in eval(row["food_items"])
                    ]
                    food_sample = FoodSample(
                        sample_id=row["sample_id"],
                        user_id=row["user_id"],
                        food_items=food_items,
                    )
                    food_samples.append(food_sample)
        except FileNotFoundError:
            pass
        return food_samples

    def get_next_sample_id(self):
        """
        Gets the next available sample ID.

        Returns:
        --------
        int
            The next sample ID.
        """
        if not self.food_samples:
            return 1
        max_id = max(food_sample.sample_id for food_sample in self.food_samples)
        return max_id + 1

    def save_food_samples_to_file(self):
        """
        Saves all food samples to the CSV file.
        """
        with open(self.food_file, mode="w", newline="") as file:
            fieldnames = ["sample_id", "user_id", "food_items"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for sample in self.food_samples:
                writer.writerow(sample.to_dict())

    def get_user_food_samples(self, user_id):
        """
        Gets all food samples for a specific user.

        Parameters:
        -----------
        user_id : int
            The unique identifier for the user.

        Returns:
        --------
        list of FoodSample
            A list of FoodSample instances for the specified user.
        """
        return [
            sample
            for sample in self.food_samples
            if int(sample.user_id) == int(user_id)
        ]

    def delete_food_sample_by_id(self, user_id, sample_id):
        """
        Deletes a specific food sample by its ID for a specific user.

        Parameters:
        -----------
        user_id : int
            The unique identifier for the user.
        sample_id : int
            The unique identifier for the food sample.

        Returns:
        --------
        bool
            True if the sample was found and deleted, otherwise False.
        """
        sample_id = int(sample_id)
        for sample in self.food_samples:
            if sample.sample_id == sample_id and sample.user_id == user_id:
                self.food_samples.remove(sample)
                self.save_food_samples_to_file()
                return True
        return False

    def delete_user_food_samples(self, user_id):
        """
        Deletes all food samples for a specific user.

        Parameters:
        -----------
        user_id : int
            The unique identifier for the user.
        """
        self.food_samples = [
            sample for sample in self.food_samples if sample.user_id != user_id
        ]
        self.save_food_samples_to_file()

    def reload_food_samples(self):
        """
        Reloads food samples from the CSV file.
        """
        self.food_samples = self.load_food_samples()
