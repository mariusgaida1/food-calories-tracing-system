def update_user_profile(manager):
    """
    Update the profile data of the current user.

    Args:
        manager (UserManager): An instance of UserManager.
    """
    print("Enter new profile data (leave blank to keep current value):")

    # Ask for age input, defaulting to current user's age if blank
    age = input(f"Age ({manager.current_user.age}): ")
    weight = input(f"Weight ({manager.current_user.weight} kg): ")
    height = input(f"Height ({manager.current_user.height} cm): ")
    activity_level = input(f"Activity Level ({manager.current_user.activity_level}): ")
    gender = input(f"Gender ({manager.current_user.gender}): ")

    # Initialize an empty dictionary to store updated profile data
    kwargs = {}
    if age:
        kwargs["age"] = int(age)
    if weight:
        kwargs["weight"] = float(weight)
    if height:
        kwargs["height"] = float(height)
    if activity_level:
        kwargs["activity_level"] = activity_level
    if gender:
        kwargs["gender"] = gender

    # Call UserManager's update_user method with user ID and kwargs
    updated_user = manager.update_user(manager.current_user.user_id, **kwargs)
    if updated_user:
        print("Profile updated successfully.")
    else:
        print("Failed to update profile.")
