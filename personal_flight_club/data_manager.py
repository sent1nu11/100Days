class DataManager:
    #This class is responsible for talking to the Google Sheet.
    import requests
    from pprint import pprint

    response = requests.get(url="https://api.sheety.co/ad8d11e0d75ff57d00d6d5660e56066b/flightDeals2/prices")
    data = response.json()

    pprint(data)