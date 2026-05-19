import requests

API_KEY = "68ce589865ca4b88ae895512261905"
city = "Berlin"
params = {"key": API_KEY, "q": city}
url = "http://api.weatherapi.com/v1/current.json"

response = requests.get(url, params)
data = response.json()

for key, value in data.items():
    print(f"{key}: {value}")
