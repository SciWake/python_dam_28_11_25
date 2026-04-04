import os

path = "/subdirectory/example.txt"

# Разделение пути на директорию и файл
directory, file = os.path.split(path)
print(f"Директория: {directory}, Файл: {file}")

# Получение только имени файла
print(f"Имя файла: {os.path.basename(path)}")

# Получение только директории
print(f"Директория: {os.path.dirname(path)}")
