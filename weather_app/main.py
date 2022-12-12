import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ['API_KEY']
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

weather_params = {
    'lat': 38.246683654246965,
    'lon': 21.733417384813052,
    'appid': api_key,
    'exclude': "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()
data_sliced = data['list'][:12]

will_rain = True
for hourly_data in data_sliced:
    condition_code = hourly_data['weather'][0]['id']
    if condition_code <= 700:
        will_rain = True

if will_rain:
    print('it will rain!')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+306940820115",
        from_="+12058557218",
        body="It's going to rain today. Remember to bring on ☂️")
    print(message.status)
