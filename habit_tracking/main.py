# HTTP Requests

import requests
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

pixel_config = {
    "date": "20221214",
    "quantity": "3.5",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)