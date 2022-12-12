""" It creates emails that are being sended every day, with inspirational quotes """

import smtplib
import datetime as dt
import random
import calendar

emails = ["paulospoulos6@gmail.com", "paulospoulos7@gmail.com"]
receiver_email = "pavlos.poulos@outlook.com"
password = "xhgyknjsahpyjaqb"
now = dt.date.today()
day_of_week = calendar.day_name[now.weekday()]


# It sends the email to every email in list
def send_email(list_of_emails):
    sender_email = "paulospoulos6@gmail.com"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        for email in list_of_emails:
            connection.sendmail(from_addr=receiver_email,
                                to_addrs=email,
                                msg="Subject:Motivational Quote\n\n"
                                    f"Happy {day_of_week}!\n{motivational_quote}")


# Main
with open("quotes.txt", 'r') as quotes:
    lines = quotes.read().splitlines()
    motivational_quote = random.choice(lines)
    send_email(emails)
