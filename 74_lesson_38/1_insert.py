from pymongo import MongoClient
from config import mongo

client = MongoClient(mongo)

client.admin.command("ping")
print("Connection successful!")


db = client["ich_edit"]
products = db["products"]

# Пример 1
# product = {"name": "Notebook", "price": 5.99, "stock": 120}

# result = products.insert_one(product)
# print("Inserted ID:", result.inserted_id)

# # Пример 2
items = [
    {"name": "Pen", "price": 1.50, "stock": 300},
    {"name": "Pencil", "price": 0.99, "stock": 500},
    {"name": "Eraser", "price": 0.75, "stock": 200},
]

result = products.insert_many(items)
print("Inserted IDs:", result.inserted_ids)
client.close()
