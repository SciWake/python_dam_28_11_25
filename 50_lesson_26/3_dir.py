import os

# ----------------------------
# ========= Пример 1 =========
# ----------------------------
# Проверка существования файла
# print(os.getcwd())
# file_path = "2_os.py"
# # или
# # file_path = "example_folder/example.txt"
# if os.path.exists(file_path):
#     print(f"Файл '{file_path}' существует.")
# else:
#     print(f"Файл '{file_path}' не найден.")

# Проверка существования директории
# directory_path = "example_folder"
# # или
# # directory_path = "parent_folder/child_folder"
# if os.path.exists(directory_path):
#     print(f"Директория '{directory_path}' существует.")
# else:
#     print(f"Директория '{directory_path}' не найдена.")


# ----------------------------
# ========= Пример 2 =========
# ----------------------------
# Список содержимого текущей директории
contents = os.listdir(".")
print("Содержимое текущей директории:", contents)

# Список содержимого указанной директории
specific_dir = "parent_folder"
if os.path.exists(specific_dir):
    print(f"Содержимое директории '{specific_dir}':", os.listdir(specific_dir))
