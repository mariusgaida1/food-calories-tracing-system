from classes.food_sample_manager import FoodSampleManager

food_sample_manager = FoodSampleManager()


def create_new_daily_food_sample(manager):
    """
    Create a new daily food sample by adding food items.

    Args:
        manager (UserManager): An instance of UserManager.
    """
    print("Enter food items (type 'done' when finished):")
    food_items = []

    # Loop to continuously accept food items from the user
    while True:
        item_name = input("Enter food item: ")
        if item_name.lower() == "done":
            break

        # Fetch the food item data from the food_sample_manager
        food_item = food_sample_manager.fetch_food_item(item_name)
        if food_item:
            # If the food item is found, add it to the list and display the calories
            food_items.append(food_item)
            print(f"Added {item_name} - {food_item.calories} calories")
        else:
            print(f"Could not find data for {item_name}")

    # After exiting the loop, check if any food items were added
    if food_items:
        # Save the list of food items as a new daily food sample for the current user
        food_sample_manager.save_food_sample(manager.current_user.user_id, food_items)
        print("Daily food sample saved.")
