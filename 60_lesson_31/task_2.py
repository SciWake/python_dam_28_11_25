""" 
Задача 2.
Написать шаблон, который:

матчит "Иванов Иван" и "Иванов Иван Иванович",
- в group(1) — фамилия,
- в group(2) — имя,
- в group(3) — отчество или None.
"""

import re

text = "Иванов Иван, Петров Пётр Петрович, Сидоров Сидор"

pattern = r'...'  # допиши сам
for m in re.finditer(pattern, text):
    print(m.group(1), m.group(2), m.group(3))