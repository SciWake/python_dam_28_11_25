import os

# ----------------------------
# ========= Пример 1 =========
# ----------------------------
# Рекурсивный обход директории
for root, dirs, files in os.walk("."):
    print(f"Текущая директория: {root}")
    print(f"Поддиректории: {dirs}")
    print(f"Файлы: {files}")
    print("-" * 50)


# ----------------------------
# ========= Пример 2 =========
# ----------------------------
# Поиск всех .txt файлов
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(f"Найден файл: {os.path.join(root, file)}")
