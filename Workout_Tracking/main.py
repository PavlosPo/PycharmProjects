import requests
from datetime import datetime


EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/be61e1838b9166a7c340361536e14c49/workoutTracking/workouts"
EXERCISE_HEADERS = {
    "x-app-id": "#############",
    "x-app-key": "#########################",
    "x-remote-user-id": "0"
}

exercise_answer = input("Tell me what exercise you did: ")
EXERCISE_CONFIG = {
    "query": exercise_answer,
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 177,
    "age": 23
}
SHEETY_HEADERS = {
    "Authorization": "Bearer ##########################",
    "Content-Type": "application/json",
}


# TRACK API request
response = requests.post(url=EXERCISE_ENDPOINT, json=EXERCISE_CONFIG, headers=EXERCISE_HEADERS)
data = response.json()
print(response.json())

# response = {"exercises":[{"tag_id":317,"user_input":"ran","duration_min":30.02,"met":9.8,"nf_calories":382.45,"photo":{"highres":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg","thumb":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg","is_user_uploaded":'false'},"compendium_code":12050,"name":"running","description":'null',"benefits":'null'}]}

exercise = data["exercises"][0]['name']
duration = data["exercises"][0]['duration_min']
calories = data["exercises"][0]['nf_calories']
DATE = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%X")

#  Getting the Sheety Google sheet's response.
row_to_add = {
    'workout': {
                "Date": DATE,
                "Time": TIME,
                "Exercise": exercise,
                "Duration": duration,
                "Calories": calories,
            }
    }

# Sheety API HTTP Post request
response = requests.post(url=SHEET_ENDPOINT, json=row_to_add, headers=SHEETY_HEADERS)
response.raise_for_status()
print(response.status_code)

