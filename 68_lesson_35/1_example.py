import requests

# ---- Пример 1 ----
# response = requests.get("https://example.com")
# print(response.status_code)  # Выводит код состояния ответа
# print(response.headers)  # Выводит заголовки ответа
# print(response.text)  # Выводит данные, полученные от сервера


# ---- Пример 2 ----
# Пример GET-запроса с параметрами
url = "https://httpbin.org/get"  # Сервис для тестирования HTTP-запросов
params = {"course": "Python", "lang": "ru"}

response = requests.get(url, params=params)

# Вывод результата
if response.status_code == 200:
    print(response.json())  # Тело ответа в формате JSON
else:
    print(f"Status code: {response.status_code}")
