from pymongo import MongoClient
from config import mongo

client = MongoClient(mongo)

client.admin.command("ping")
print("Connection successful!")

db = client["ich_edit"]
products = db["products"]

# Пример 1
result = products.update_one(
    {"name": "Notebook"},  # фильтр
    {"$set": {"price": 24.99}},  # изменение
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)

# Пример 2
result = products.update_many(
    {},  # пустой фильтр — все документы
    {"$inc": {"price": 1}},  # увеличить поле price на 1
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)
