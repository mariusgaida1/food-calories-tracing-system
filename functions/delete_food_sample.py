from classes.food_sample_manager import FoodSampleManager

food_sample_manager = FoodSampleManager()


def delete_food_sample(manager):
    """
    Delete a food sample by its sample_id.

    Args:
        manager (UserManager): An instance of UserManager.
    """
    
    food_sample_manager.reload_food_samples()

    sample_id = input("Enter the ID of the food sample to delete: ")

    # Retrieve the current user's ID from the manager
    user_id = manager.current_user.user_id
    if food_sample_manager.delete_food_sample_by_id(user_id, sample_id):
        print(f"Food sample {sample_id} deleted successfully.")
    else:
        print(f"Failed to delete food sample {sample_id}. Sample not found.")
