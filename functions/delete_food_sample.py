from classes.food_sample_manager import FoodSampleManager

food_sample_manager = FoodSampleManager()


def delete_food_sample(manager):
    sample_id = input("Enter the ID of the food sample to delete: ")
    user_id = manager.current_user.user_id
    if food_sample_manager.delete_food_sample_by_id(user_id, sample_id):
        print(f"Food sample {sample_id} deleted successfully.")
    else:
        print(f"Failed to delete food sample {sample_id}. Sample not found.")
