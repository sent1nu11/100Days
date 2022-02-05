import requests
from datetime import datetime

USERNAME = "sent1nu11"
TOKEN = "sdfieru38flvcsdf"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
   "id": GRAPH_ID,
   "name": "Cycling Graph",
   "unit": "Km",
   "type": "float",
   "color": "sora",
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": "20220129",
    "quantity": "30"
}

headers = {
    "X-USER-TOKEN": TOKEN
}



response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)