# import smtplib
#
# my_email = "paulospoulos6@gmail.com"
# password = "xhgyknjsahpyjaqb"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     # Encrypts the email
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="paulospoulos6@yahoo.com",
#         msg="Subject:Hello\n\n This is the body of my email"
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1997 ,month=12, day=15, hour=4)
print(date_of_birth)

