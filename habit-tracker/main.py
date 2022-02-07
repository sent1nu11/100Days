import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("USER")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

print(TOKEN)

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
   "id": GRAPH_ID,
   "name": "Cycling Graph",
   "unit": "Km",
   "type": "float",
   "color": "sora",
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"

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