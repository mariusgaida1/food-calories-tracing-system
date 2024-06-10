from classes.food_sample_manager import FoodSampleManager

food_sample_manager = FoodSampleManager()

def create_new_daily_food_sample(manager):
    print("Enter food items (type 'done' when finished):")
    food_items = []
    while True:
        item_name = input("Enter food item: ")
        if item_name.lower() == 'done':
            break
        food_item = food_sample_manager.fetch_food_item(item_name)
        if food_item:
            food_items.append(food_item)
            print(f"Added {item_name} - {food_item.calories} calories")
        else:
            print(f"Could not find data for {item_name}")
    
    if food_items:
        food_sample_manager.save_food_sample(manager.current_user.user_id, food_items)
        print("Daily food sample saved.")