import requests
from dotenv import load_dotenv
import os

load_dotenv()

X_APP_ID = os.getenv("APP_ID")
X_APP_KEY = os.getenv("APP_KEY")

GENDER = "female"
WEIGHT_KG = 72.5
HEIGHT_CM = 167.64
AGE = 30

print(X_APP_ID)

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": X_APP_KEY
}

user_params = {
    "query": "ran 3 miles",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
#
# response = requests.get(url=nutritionix_endpoint)
# print(response)

response = requests.post(url=nutritionix_endpoint, json=user_params, headers=headers)
result = response.json()
print(result)

