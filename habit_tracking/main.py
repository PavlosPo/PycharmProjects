# HTTP Requests

import requests
from datetime import datetime as dt


USERNAME = "pavlosp"
TOKEN = "hjb32phbobgj"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Creates the user, I allready Created
# response = requests.post(url=pixel_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Creating a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt(year=2022, month=12, day=13)
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# Updating a pixel
day_to_change = dt(year=2022, month=12, day=13).strftime("%Y%m%d")
pixel_update_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_to_change}"
pixel_update_config = {
    "quantity": "3.2",
}

response = requests.put(url=pixel_update_enpoint, json=pixel_update_config, headers=headers)
print(response.text)