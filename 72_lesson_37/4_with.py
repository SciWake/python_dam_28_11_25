import pymysql
from config import dbconfig

connection = pymysql.connect(
    **dbconfig,
    charset="utf8mb4",
)

with connection as conn:
    pass

print("После with, open =", connection.open)

with connection.cursor() as cursor:
    cursor.execute("SELECT 1")
    print(cursor.fetchone())
