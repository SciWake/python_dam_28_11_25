"""
Используя базу данных hr, выведите названия всех департаментов из таблицы departments. Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Administration
2. Marketing
3. Purchasing
...
27. Payroll
"""

import pymysql
from config import dbconfig

connection = pymysql.connect(
    **dbconfig,
    charset="utf8mb4",
)
if connection.open:
    print("Connection successful!")

cursor = connection.cursor()

cursor.execute("USE hr")

cursor.execute("SELECT department_name FROM departments")

print("Список департаментов:")
for i, (department_name,) in enumerate(cursor.fetchall(), start=1):
    print(f"{i}. {department_name}")

cursor.close()
connection.close()
