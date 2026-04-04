import os

# Переименование файла
old_file_name = "example.txt"
new_file_name = "renamed.txt"
if os.path.exists(old_file_name):
    os.rename(old_file_name, new_file_name)
    print(f"Файл переименован в '{new_file_name}'.")
else:
    print(f"Файл '{old_file_name}' не найден.")

# Переименование директории
old_dir_name = "example_folder"
new_dir_name = "renamed_folder"
if os.path.exists(old_dir_name):
    os.rename(old_dir_name, new_dir_name)
    print(f"Директория переименована в '{new_dir_name}'.")
else:
    print(f"Директория '{old_dir_name}' не найдена.")
