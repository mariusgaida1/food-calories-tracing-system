from classes.food_sample_manager import FoodSampleManager
from .create_new_food_sample import create_new_daily_food_sample
from .see_food_samples_statistics import see_food_samples_statistics
from .update_user_profile import update_user_profile
from .send_email import send_email
from .delete_food_sample import delete_food_sample


food_sample_manager = FoodSampleManager()

def user_profile_menu(manager):
    while manager.current_user:
        print("\n1. See food samples statistics")
        print("2. Delete food sample by sample_id")
        print("3. Create new daily food sample")
        print("4. Send food data to email")
        print("5. Edit profile data")
        print("6. Sign out")
        print("7. Delete profile")
        choice = input("Enter choice: ")
        if choice == '1':
            see_food_samples_statistics(manager)
        elif choice == '2':
            delete_food_sample(manager)
        elif choice == '3':
            create_new_daily_food_sample(manager)
        elif choice == '4':
            send_email(manager)
        elif choice == '5':
            update_user_profile(manager)
        elif choice == '6':
            manager.sign_out()
            print("Signed out successfully.")
        elif choice == '7':
            user_id = manager.current_user.user_id
            if manager.delete_user(user_id):
                print("Profile deleted successfully.")
            else:
                print("Failed to delete profile.")
            manager.sign_out()

        else:
            print("Invalid choice. Please try again.")