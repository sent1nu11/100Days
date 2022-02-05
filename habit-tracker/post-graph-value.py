import requests

USERNAME = "sent1nu11"
TOKEN = "sdfieru38flvcsdf"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

data_params = {
    "date": "20220204",
    "quantity": "33.5"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

graph_config = {
   "id": "graph1",
   "name": "Cycling Graph",
   "unit": "Km",
   "type": "float",
   "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=data_endpoint, json=data_params, headers=headers)
print(response.text)