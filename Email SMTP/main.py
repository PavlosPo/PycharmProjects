""" It creates emails that are being sended every day, with inspirational quotes """

import smtplib
import datetime as dt
import random
import calendar

my_email = "paulospoulos6@gmail.com"
receiver_email = "pavlos.poulos@outlook.com"
password = "xhgyknjsahpyjaqb"
now = dt.date.today()
day_of_week = calendar.day_name[now.weekday()]

with open("quotes.txt", 'r') as quotes:
    lines = quotes.read().splitlines()
    motivational_quote = random.choice(lines)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg="Subject:Motivational Quote\n\n"
                            f"Happy {day_of_week}!\n{motivational_quote}")