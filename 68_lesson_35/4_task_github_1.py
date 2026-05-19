"""
https://docs.github.com/en/rest/users/users?apiVersion=2026-03-10
"""

import requests
import json


url = "https://api.github.com/users/sciwake"

response = requests.get(url)  # Ответ сервера 200
general_user_data = response.json()  # Получаем данные у объекта response

folowers_url = general_user_data[
    "followers_url"
]  # https://api.github.com/users/SciWake/followers
response_folowers = requests.get(folowers_url)  # Ответ сервера 200
folowers_data = response_folowers.json()  # Получаем данные у объекта response_folowers
print(json.dumps(folowers_data, indent=4))
# print(len(folowers_data))
