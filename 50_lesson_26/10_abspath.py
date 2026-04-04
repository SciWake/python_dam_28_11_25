import os

# ----------------------------
# ========= Пример 1 =========
# ----------------------------
# Относительный путь
relative_path = "example.txt"

# Преобразование в абсолютный путь
absolute_path = os.path.abspath(relative_path)
print(f"Абсолютный путь: {absolute_path}")


# ----------------------------
# ========= Пример 2 =========
# ----------------------------
# Объединение нескольких компонентов
current_dir = os.getcwd()
sub_dir = "docs"
file_name = "data.txt"
full_path = os.path.join(current_dir, sub_dir, file_name)
print(f"Путь: {full_path}")
