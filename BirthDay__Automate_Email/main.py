######### Sending Happy birthdays via Email!!! #########

import datetime as dt
import pandas as pd
import random
import smtplib

# Initial
data = pd.read_csv('birthdays.csv')
my_email = "paulospoulos6@gmail.com"
password = "xhgyknjsahpyjaqb"
# Today
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
today_tuple = (month, day)  # Today
# Birthday CSV data to Dictionary
birthday_dict = {(row['month'], row['day']): row for (index, row) in data.iterrows()}

if today_tuple in birthday_dict:  # If today has anyone birthday
    # Name of Birthday Person
    birthday_person = birthday_dict[today_tuple]
    # Pick Random Letter
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    # Open  the letter
    with open(file_path) as letter_file:
        print('Reading csv file')
        letter = letter_file.read()
        letter = letter.replace('[Name]', f'{birthday_person["name"]}')
        print(letter)
    # Send Email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        print('Sending email...')
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject:Happy Birthday\n\n{letter}")
