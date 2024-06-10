import csv
from .user import User
from .food_sample_manager import FoodSampleManager
import bcrypt

class UserManager:
    def __init__(self, user_file='data/users.csv'):
        self.user_file = user_file
        self.users = self.load_users()
        self.current_user = None
        self.food_sample_manager = FoodSampleManager()

    def load_users(self):
        users = {}
        try:
            with open(self.user_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(
                        username=row['username'],
                        password=row['password'],
                        user_id=row['user_id'],
                        email=row['email'],
                        age=int(row['age']),
                        weight=float(row['weight']),
                        height=float(row['height']),
                        activity_level=row['activity_level'],
                        gender=row['gender']
                    )
                    #user.user_id = row['user_id']
                    user.daily_calories = float(row['daily_calories'])
                    users[user.user_id] = user
        except FileNotFoundError:
            pass
        return users

    def get_next_user_id(self):
        """Get the next user ID."""
        if not self.users:
            return 1
        max_id = max(user.user_id for user in self.users.values())
        return max_id + 1

    def save_users(self):
        with open(self.user_file, mode='w', newline='') as file:
            fieldnames = ['username', 'password', 'user_id', 'email', 'age', 'weight', 'height', 'activity_level', 'gender', 'daily_calories']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.users.values():
                writer.writerow(user.to_dict())

    def sign_up(self, username, password, email, age, weight, height, activity_level, gender):
        if not User.validate_email(email):
            raise ValueError("Invalid email address.")
        for user in self.users.values():
            if user.username == username:
                raise ValueError("Username already exists.")
        new_user_id = self.get_next_user_id()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User(new_user_id, username, hashed_password.decode('utf-8'), email, age, weight, height, activity_level, gender)
        self.users[user.user_id] = user
        self.save_users()
        return user

    def sign_in(self, username, password):
        for user in self.users.values():
            if user.username == username and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                self.current_user = user
                return True
        return False
    
    def sign_out(self):
        self.current_user = None

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            self.food_sample_manager.delete_user_food_samples(user_id)
            self.save_users()
            return True
        return False

    def update_user(self, user_id, **kwargs):
        if user_id not in self.users:
            return False
        user = self.users[user_id]
        if 'age' in kwargs:
            user.age = kwargs['age']
        if 'weight' in kwargs:
            user.weight = kwargs['weight']
        if 'height' in kwargs:
            user.height = kwargs['height']
        if 'activity_level' in kwargs:
            user.activity_level = kwargs['activity_level']
        if 'gender' in kwargs:
            user.gender = kwargs['gender']
        user.daily_calories = user.calculate_calories()
        self.save_users()
        return user