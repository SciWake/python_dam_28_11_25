from pymongo import MongoClient
from config import mongo

client = MongoClient(mongo)

client.admin.command("ping")
print("Connection successful!")

db = client["ich_edit"]
products = db["products"]

# # Пример 1
# doc = products.find_one()
# print(doc)

# # Пример 2
# doc = products.find_one({"price": {"$lt": 5}})
# print(doc)

# $gt (greater than) — строго больше (>)
# $gte (greater than or equal) — больше или равно (>=)
# $lte (less than or equal) — меньше или равно (<=)
# $eq (equal) — равно (==). Хотя для проверки на равенство можно писать проще: {"price": 5}


# Пример 3
# Получить все документы
# docs = products.find()
# print(docs)
# for item in docs:
#     print(item)

# Пример 4
# Получить все документы c условием
# cursor = products.find({"price": {"$gt": 1}})
# print(cursor)
# for doc in cursor:
#     print(doc)

# Пример 5
# for doc in products.find().sort("price", -1).skip(1).limit(2):
#     print(doc)

# Пример 6
# Вернёт только name, price и id (по умолчанию)
for doc in products.find({}, {"name": 1, "price": 1}):
    print(doc)

# # Выбрать продукты с ценой больше 100 и исключить _id:
for doc in products.find({"price": {"$gt": 100}}, {"_id": 0}):
    print(doc)

# # Оставить только name (все остальные исключаются, включая _id)
for doc in products.find({}, {"_id": 0, "name": 1}):
    print(doc)
