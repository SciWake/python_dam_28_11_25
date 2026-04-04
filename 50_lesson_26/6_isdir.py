import os

path = "example.txt"
# path = "parent_folder"

# Проверяем, является ли файлом
if os.path.isfile(path):
    print(f"'{path}' существует и это файл.")
# Проверяем, является ли директорией
elif os.path.isdir(path):
    print(f"'{path}' существует и это директория.")
