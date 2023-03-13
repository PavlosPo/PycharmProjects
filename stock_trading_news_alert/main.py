import requests
import datetime as dt
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "####################"
NEWS_API_KEY = "######################"
TWILIO_SID = "######################"
TWILIO_AUTH_TOKEN = "#######################"
TWILIO_PHONE = "+###########"
MY_PHONE = "+#######"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PARAMETERS = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': STOCK,
    'interval': '60min',
    'apikey': STOCK_API_KEY
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_PARAMETERS = {
    'qInTitle': COMPANY_NAME,
    'language': 'en',
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API_KEY
}




stock_data = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)
data = stock_data.json()['Time Series (60min)']
now = dt.datetime.now()


# Returns list with correct stock dates. 0: Yesterday, 1: before Yesterday
def stock_dates() -> list:
    if now.today().weekday() == 7:  # Sunday
        yesterday_date = str(dt.date.today() - dt.timedelta(2))  # Yesterdays stock date
        before_yesterday_date = str(dt.date.today() - dt.timedelta(3))  # Before yesterday stock Date
        yesterday_closed_date = yesterday_date + ' ' + '20:00:00'  # Yesterdays' Closed stock datetime
        before_yesterday_closed_date = before_yesterday_date + ' ' + '20:00:00'  # Before Yesterday's Closed stock datetime
    elif now.today().weekday() == 0:  # Monday
        yesterday_date = str(dt.date.today() - dt.timedelta(3))  # Yesterdays stock date
        before_yesterday_date = str(dt.date.today() - dt.timedelta(4))  # Before yesterday stock Date
        yesterday_closed_date = yesterday_date + ' ' + '20:00:00'  # Yesterdays' Closed stock datetime
        before_yesterday_closed_date = before_yesterday_date + ' ' + '20:00:00'  # Before Yesterday's Closed stock datetime
    elif now.today().weekday() == 1:  # Tuesday
        yesterday_date = str(dt.date.today() - dt.timedelta(1))  # Yesterdays stock date
        before_yesterday_date = str(dt.date.today() - dt.timedelta(4))  # Before yesterday stock Date
        yesterday_closed_date = yesterday_date + ' ' + '20:00:00'  # Yesterdays' Closed stock datetime
        before_yesterday_closed_date = before_yesterday_date + ' ' + '20:00:00'  # Before Yesterday's Closed stock datetime
    else:
        yesterday_date = str(dt.date.today() - dt.timedelta(1))  # Yesterdays stock date
        before_yesterday_date = str(dt.date.today() - dt.timedelta(2))  # Before yesterday stock Date
        yesterday_closed_date = yesterday_date + ' ' + '20:00:00'  # Yesterdays' Closed stock datetime
        before_yesterday_closed_date = before_yesterday_date + ' ' + '20:00:00'  # Before Yesterday's Closed stock datetime

    return [yesterday_closed_date, before_yesterday_closed_date]  # returns a tuple with dates as str


# Returns list with closed prices
def closed_prices() -> list:
    closed_price_yesterday = data[stock_dates()[0]]['4. close']
    closed_price_before_yesterday = data[stock_dates()[1]]['4. close']
    return [float(closed_price_yesterday), float(closed_price_before_yesterday)]


# Difference of closed prices
diff = float(closed_prices()[0]) - float(closed_prices()[1])  # Difference of closed stock prices
prcnt_diff = round((diff / closed_prices()[0]) * 100, 3)  # Percent of difference

if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Making the Alert or not
alert_is_on = False
if abs(prcnt_diff) > 5:
    print("Get News")
    alert_is_on = True

# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Getting the News
if alert_is_on:
    response_data = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    first_3_articles = response_data.json()['articles'][0:4]  # First 3 news articles
    # Creates the messages list for sending it to SMS
    messages = [f""""{COMPANY_NAME}: {up_down} {prcnt_diff}%\nHeadline: {article['title']}\nBrief: {article['description']}""" for article in first_3_articles]
else:
    messages = []
    pass

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article_message in messages:
    message = client.messages.create(
        body=article_message,
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )
