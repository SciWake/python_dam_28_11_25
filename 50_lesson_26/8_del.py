import os

# Удаление файла
file_to_delete = "renamed.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"Файл '{file_to_delete}' удалён.")
else:
    print(f"Файл '{file_to_delete}' не найден, удаление невозможно.")

# Удаление пустой директории
empty_dir_to_delete = "tes"
if os.path.exists(empty_dir_to_delete):
    os.rmdir(empty_dir_to_delete)
    print(f"Пустая директория '{empty_dir_to_delete}' удалена.")
else:
    print(f"Директория '{empty_dir_to_delete}' не найдена или не пуста.")
