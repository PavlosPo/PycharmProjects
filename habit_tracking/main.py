# HTTP Requests

import requests
USERNAME = "pavlosp"
TOKEN = "hjb32phbobgj"


pixel_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Creates the user, I allready Created
# response = requests.post(url=pixel_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
