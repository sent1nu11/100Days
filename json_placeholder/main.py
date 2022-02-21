import requests

ENDPOINT = "https://api.github.com/user"
HTTPBIN_ENDPOINT = "https://httpbin.org/get"

jsonPayload = {
    'albumId': 1,
    'title': 'test',
    'url': 'nothing.com'
}

# response = requests.get(url= ENDPOINT)
# print(response.json())

# response = requests.delete(ENDPOINT, json=jsonPayload)
# print(response.json())

ploads = {'things': 2, 'total': 25}

response = requests.get(ENDPOINT)

print(response.json())