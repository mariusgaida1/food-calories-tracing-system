# Food Calories Tracing System
## Overview
This project is a Food Calories Tracing System that allows users to manage their daily food intake. Users can sign up, sign in, create daily food samples, view food sample statistics, update profile data, and delete food samples. The system also allows sending food sample data via email.

## Features
*User Sign Up, Sign In, and Exit System
>User have unique user ID as well as username, password, email, age, weight, height, activity level, gender attributes. Email is validated with regex, and using Haris-Benedict formula there is generated daily recommended calories amount. Users data is saved and stored in users.csv file.

*View Food Sample Statistics
>Once signed in User can choose to see Food Samples statistics, i.e. Food Samples list.

*Delete Food Samples
>Once signed in User is able to delete Food Sample by entering Food Samples ID.

*Create and Save Daily Food Samples
>Once signed in User can create and save new Daily Food Sample. User is able trough command line enter food item to be search in https://developer.edamam.com/food-database-api. User is able to select item by item for search. If user decided that it is enought should enter "done". Users Food Samples are saved in food_samples.csv file.

*Send Food Data via Email
>Once signed in User is able to send chosen Food Samples information to Users email.

*Update Profile Data
>Once signed in User can edit profile data.

*Sign out from Users profile

*Delete Users Profile
>Once signed in User is able to delete own Users profile with all Users Food Samples.

## Directory Structure

├── README.md\
├── main.py\
├── functions\
│   ├── compose_main_menu.py\
│   ├── compose_profile_menu.py\
│   ├── create_new_food_sample.py\
│   ├── delete_food_sample.py\
│   ├── see_food_samples_statistics.py\
│   ├── send_email.py\
│   └── update_user_profile.py\
├── classes\
│   ├── food_item.py\
│   ├── food_sample.py\
│   ├── food_sample_manager.py\
│   ├── user.py\
│   └── user_manager.py\
└── data\
..  ├── users.csv\
..  └── food_samples.csv
