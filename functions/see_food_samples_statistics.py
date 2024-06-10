from classes.food_sample_manager import FoodSampleManager


food_sample_manager = FoodSampleManager()

def see_food_samples_statistics(manager):
    food_sample_manager.reload_food_samples()
    user_id = manager.current_user.user_id
    samples = food_sample_manager.get_user_food_samples(user_id)
    if samples:
        for sample in samples:
            print(f"\nSample {sample.sample_id}:")
            for item in sample.food_items:
                print(f"  {item.name} - {item.calories} calories")
            print(f"Total Calories: {sample.total_calories()}")

            current_user = manager.users.get(user_id)
            if current_user:
                print(f"User's Daily Calories: {round(current_user.daily_calories)}")
            else:
                print("Current user not found.")

            if sample.total_calories() < current_user.daily_calories:
                print(f"You need additionally {round(current_user.daily_calories - sample.total_calories())} calories")
            else:
                print(f"Yours daily calories is over {round(sample.total_calories() - current_user.daily_calories)} calories")

        #manage_food_samples(manager)
    else:
        print("No food samples found.")
