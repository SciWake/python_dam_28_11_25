"""
Список файлов и папок

Напишите программу, которая принимает путь к директории через
аргумент командной строки и выводит:
Отдельно список папок
Отдельно список файлов

Пример запуска
python script.py /home/user/documents

Пример вывода
Содержимое директории '/home/user/documents':


Папки:
- folder1
- folder2


Файлы:
- file1.txt
- file2.txt
- notes.docx
"""

import os
import sys

path = sys.argv[1]
items = os.listdir(path)

print(f"Содержимое директории '{path}':")

print("Папки:")
for x in items:
    if os.path.isdir(os.path.join(path, x)):
        print(f"- {x}")

print("Файлы:")
for x in items:
    if not os.path.isdir(os.path.join(path, x)):
        print(f"- {x}")
