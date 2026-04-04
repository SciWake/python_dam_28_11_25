import os

# Создание нового пустого файла
file_name = "example.txt"
open(file_name, "w").close()
print(f"Файл '{file_name}' создан или перезаписан.")


file_path = "example.txt"
# Проверяем, существует ли объект
if os.path.exists(file_path):
    # Проверяем, является ли файлом
    if os.path.isfile(file_path):
        print(f"'{file_path}' существует и это файл.")
    else:
        print(f"'{file_path}' существует, но это не файл.")
else:
    print(f"'{file_path}' не существует.")