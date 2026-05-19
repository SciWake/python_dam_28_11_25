"""
https://docs.github.com/en/rest/users/users?apiVersion=2026-03-10
"""

import requests
import json
import time

BASE_URL = "https://api.github.com/users/"
general_login = "sciwake"
url = BASE_URL + general_login
response = requests.get(url)  # Ответ сервера 200
general_user_data = response.json()  # Получаем данные у объекта response
print(json.dumps(general_user_data, indent=4))

followers_url = general_user_data[
    "followers_url"
]  # https://api.github.com/users/SciWake/followers
response_folowers = requests.get(followers_url)  # Ответ сервера 200
followers_data = response_folowers.json()  # Получаем данные у объекта response_folowers
# print(json.dumps(folowers_data, indent=4))

for follower in followers_data:
    url = BASE_URL + follower["login"]
    finfo = requests.get(url).json()
    print(f"{finfo['login']} | {finfo['name']} count followers = {finfo["followers"]}")
    time.sleep(2)
