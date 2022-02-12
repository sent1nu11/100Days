#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
import data_manager
from pprint import pprint

response = requests.get(url="https://api.sheety.co/ad8d11e0d75ff57d00d6d5660e56066b/flightDeals2/prices")
data = response.json()

pprint(data)
