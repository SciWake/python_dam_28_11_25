"""
Добавьте к предыдущей программе возможность выбора департамента.
Пусть пользователь введёт название из списка.
Далее выведите всех сотрудников этого департамента, указав имя, фамилию и должность.
Пример вывода:
    Enter department: Marketing
    Michael Hartstein — Marketing Manager
    Pat Fay — Marketing Representative
...
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
cursor.execute("SELECT department_name FROM departments ORDER BY department_name")
departments = cursor.fetchall()

print("Список департаментов:")
for i, (department_name,) in enumerate(departments, start=1):
    print(f"{i}. {department_name}")

department = input("Enter department: ")

query = """
    SELECT e.first_name, e.last_name, j.job_title
    FROM employees e
        JOIN departments d 
            ON e.department_id = d.department_id
        JOIN jobs j 
            ON e.job_id = j.job_id
    WHERE d.department_name = %s
    ORDER BY e.first_name, e.last_name
"""

cursor.execute(query, (department,))
employees = cursor.fetchall()

for first_name, last_name, job_title in employees:
    print(f"{first_name} {last_name} — {job_title}")

cursor.close()
connection.close()
