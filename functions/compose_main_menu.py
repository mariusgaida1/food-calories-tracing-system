from classes.user_manager import UserManager
from .compose_profile_menu import user_profile_menu

user_manager = UserManager()


def main_menu():
    while True:
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (cm): "))
            activity_level = input("Enter activity level (sedentary, lightly active, moderately active, very active, extra active): ")
            gender = input("Enter gender (male/female): ")
    
            try:
                user = user_manager.sign_up(username, password, email, age, weight, height, activity_level, gender)
                print(f"User {user.username} signed up successfully with ID: {user.user_id}")
            except ValueError as e:
                print(e)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_manager.sign_in(username, password):
                print("Sign in successful!")
                user_profile_menu(user_manager)
            else:
                print("Invalid username or password.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")