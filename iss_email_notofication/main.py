import smtplib

import requests
from datetime import datetime

MY_LAT = 37.983160  # Your latitude
MY_LONG = 22.766100  # Your longitude
MY_EMAIL = 'paulospoulos6@gmail.com'
MY_PASSWORD = 'xhgyknjsahpyjaqb'


# Your position is within +5 or -5 degrees of the ISS position.
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if sunrise >= time_now.hour >= sunset:
        print('It is Dark!')
        return True
    else:
        return False


def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude + 5 >= MY_LAT >= iss_latitude - 5:
        if iss_longitude + 5 >= MY_LONG >= iss_longitude - 5:
            return True
        else:
            print('ISS is not above..')
            return False
    else:
        return False


def send_email():
    if is_dark() and is_above():
        print('Sending email...')
        with smtplib.SMTP() as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,
                             password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg='Subject:ISS is Above!!\n\n Look up!! ISS is above your sky!!')
    else:
        print('Iss is not above')


send_email()
