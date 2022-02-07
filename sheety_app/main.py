import requests
from dotenv import load_dotenv
import os

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": "5155317e",
    "x-app-key": "5271e3295f34724841bbbbbc4dcd347c",
    "x-remote-user-id": 0
}

user_params = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url=nutritionix_endpoint, json=user_params, headers= headers)
print (response.text)

