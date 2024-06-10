import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from classes.food_sample_manager import FoodSampleManager
food_sample_manager = FoodSampleManager()

def send_email(manager):
    food_sample_manager.reload_food_samples()
    if not manager.current_user:
        print("No user is currently signed in.")
        return



    sample_ids = input("Enter the food sample IDs to send (comma-separated): ").split(',')
    sample_ids = [id.strip() for id in sample_ids]

    user_id = manager.current_user.user_id
    samples = food_sample_manager.get_user_food_samples(user_id)




    selected_samples = [sample for sample in samples if str(sample.sample_id) in sample_ids]

    if not selected_samples:
        print("No matching food samples found.")
        return
    
    email_content = ""
    for sample in selected_samples:
        email_content += f"Sample ID: {sample.sample_id}\n"
        for item in sample.food_items:
            email_content += f"  {item.name} - {item.calories} calories\n"
        email_content += f"Total Calories: {sample.total_calories()}\n"


        current_user = manager.users.get(user_id)
        if current_user:
            email_content += f"User's Daily Calories: {round(current_user.daily_calories)}\n"
        else:
            print("Current user not found.")

        if sample.total_calories() < current_user.daily_calories:
            email_content += f"You need additionally {round(current_user.daily_calories - sample.total_calories())} calories\n\n"
        else:
            email_content += f"Yours daily calories is over {round(sample.total_calories() - current_user.daily_calories)} calories\n\n"

    # Email setup
    sender_email = "mariusmeska0@gmail.com"
    receiver_email = manager.current_user.email
    subject = "Your Food Samples Information"
    body = email_content

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        gmail_password = "klut fmkz layn mxtx"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, gmail_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Email sent successfully to {receiver_email}.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")