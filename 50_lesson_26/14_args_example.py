import os
import sys

# Проверяем, передан ли аргумент
if len(sys.argv) != 2:
    print("Использование: python script.py <директория>")
    sys.exit(1)

directory = sys.argv[1]

# Проверяем существование директории
if not os.path.isdir(directory):
    print(f"Директория '{directory}' не существует.")
    sys.exit(1)

# Выводим содержимое директории
print(f"Содержимое директории '{directory}':")
for item in os.listdir(directory):
    print(f"- {item}")
