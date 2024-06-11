from classes.food_sample_manager import FoodSampleManager


food_sample_manager = FoodSampleManager()


def see_food_samples_statistics(manager):
    """
    Display statistics for food samples of the current user.

    Args:
        manager (UserManager): An instance of UserManager.
    """
    # Reload food samples to ensure we have the latest data
    food_sample_manager.reload_food_samples()

    # Get the user ID of the current user from the manager
    user_id = manager.current_user.user_id

    # Retrieve all food samples associated with the current user
    samples = food_sample_manager.get_user_food_samples(user_id)

    # If there are samples found for the user, display their statistics
    if samples:
        for sample in samples:
            # Display each sample's ID and its constituent food items
            print(f"\nSample {sample.sample_id}:")
            for item in sample.food_items:
                print(f"  {item.name} - {item.calories} calories")
            
            # Calculate and display the total calories for the sample
            print(f"Total Calories: {sample.total_calories()}")

            # Retrieve the current user's daily calorie need and compare it with the sample's total calories
            current_user = manager.users.get(user_id)
            if current_user:
                print(f"User's Daily Calories: {round(current_user.daily_calories)}")
            else:
                print("Current user not found.")

            if sample.total_calories() < current_user.daily_calories:
                # Inform the user about the deficit in consumed calories compared to the daily need
                print(
                    f"You need additionally {round(current_user.daily_calories - sample.total_calories())} calories"
                )
            else:
                # Inform the user if they would consumed more calories than their daily need
                print(
                    f"Yours daily calories is over {round(sample.total_calories() - current_user.daily_calories)} calories"
                )

        # manage_food_samples(manager)
    else:
        print("No food samples found.")
