import os

dir_path = "example_folder"

if not os.path.exists(dir_path):
    # Создание одной директории
    os.mkdir("example_folder")
    print(f"Директория '{dir_path}' создана.")
else:
    print(f"Директория '{dir_path}' существует.")

# Создание вложенных директорий
os.makedirs("parent_folder/child_folder", exist_ok=True)
print("Вложенные директории 'parent_folder/child_folder' созданы.")
