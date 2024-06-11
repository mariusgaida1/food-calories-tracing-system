import re


class User:
    def __init__(
        self,
        user_id,
        username,
        password,
        email,
        age,
        weight,
        height,
        activity_level,
        gender,
    ):
        """
        Initialize a User object with basic information and calculate daily calorie needs.
        """
        self.user_id = int(user_id)
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.gender = gender
        self.daily_calories = self.calculate_calories()

    def calculate_calories(self):
        """
        Calculate the daily calorie needs (BMR * activity level multiplier) based on user's gender, weight, height, age, and activity level.

        Returns:
            int: The calculated daily calorie needs.
        """
        bmr = 0
        if self.gender == "male":
            bmr = round(
                88.362
                + (13.397 * self.weight)
                + (4.799 * self.height)
                - (5.677 * self.age)
            )
        elif self.gender == "female":
            bmr = round(
                447.593
                + (9.247 * self.weight)
                + (3.098 * self.height)
                - (4.330 * self.age)
            )

        activity_multiplier = {
            "sedentary": 1.2,
            "lightly active": 1.375,
            "moderately active": 1.55,
            "very active": 1.725,
            "extra active": 1.9,
        }
        return round(bmr * activity_multiplier[self.activity_level])

    def to_dict(self):
        """
        Convert the User object into a dictionary representation.

        Returns:
            dict: A dictionary containing all attributes of the User object.
        """
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "age": self.age,
            "weight": self.weight,
            "height": self.height,
            "activity_level": self.activity_level,
            "gender": self.gender,
            "daily_calories": self.daily_calories,
        }

    @staticmethod
    def validate_email(email):
        """
        Validate if the provided email address is in a valid format.

        Args:
            email (str): The email address to validate.

        Returns:
            re.Match object or None: A match object if the email is valid, otherwise None.
        """
        regex = r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        return re.match(regex, email)
