def update_user_profile(manager):
    print("Enter new profile data (leave blank to keep current value):")
    age = input(f"Age ({manager.current_user.age}): ")
    weight = input(f"Weight ({manager.current_user.weight} kg): ")
    height = input(f"Height ({manager.current_user.height} cm): ")
    activity_level = input(f"Activity Level ({manager.current_user.activity_level}): ")
    gender = input(f"Gender ({manager.current_user.gender}): ")

    kwargs = {}
    if age:
        kwargs['age'] = int(age)
    if weight:
        kwargs['weight'] = float(weight)
    if height:
        kwargs['height'] = float(height)
    if activity_level:
        kwargs['activity_level'] = activity_level
    if gender:
        kwargs['gender'] = gender

    updated_user = manager.update_user(manager.current_user.user_id, **kwargs)
    if updated_user:
        print("Profile updated successfully.")
    else:
        print("Failed to update profile.")
