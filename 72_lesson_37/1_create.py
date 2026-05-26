# pip install pymysql
import pymysql
from config import dbconfig


# connection = pymysql.connect(
# host=dbconfig["host"],
# user=dbconfig['user'],
# password=dbconfig["password"],
# charset="utf8mb4", # кодировка соединения (необязательно, указывать для поддержки русского)
# )

connection = pymysql.connect(
    **dbconfig,
    charset="utf8mb4",
)
if connection.open:
    print("Connection successful!")

cursor = connection.cursor()

# Запрос 1 - Выведем список достпных баз данных
cursor.execute("SHOW DATABASES;")
print("Список баз данных:")
for db in cursor.fetchall():
    print(db)

cursor.execute("CREATE DATABASE IF NOT EXISTS test_257897;")

cursor.execute("SHOW DATABASES;")
databases = [db[0] for db in cursor.fetchall()]

if "test_257897" in databases:
    print("База данных успешно создана")

cursor.execute("DROP DATABASE IF EXISTS test_257897;")

cursor.execute("SHOW DATABASES;")
databases = [db[0] for db in cursor.fetchall()]

if "test_257897" not in databases:
    print("База данных успешно удалена")

cursor.close()
connection.close()
