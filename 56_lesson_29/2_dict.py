import csv

# Пример 1
# with open("output.csv") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)

# Пример 2
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"age": 30, "name": "Alice"})


# # Пример 3
new_persons = [
    {"name": "David", "age": 28},
    {"age": 34, "name": "Jane"},
    {"name": "Anna", "city": "Berlin"},
    {"name": "Martin", "age": 20, "city": "London"},
]

with open("output.csv", "a", newline="") as f:
    writer = csv.DictWriter(
        f, fieldnames=["name","city", "age"], extrasaction="ignore"
    )
    writer.writerows(new_persons)


# # Пример 4 - обработка пропущенных строк
with open("output.csv") as f:
    reader = csv.reader(f)
    good_rows = []
    for row in reader:
        # Проверяем, есть ли в строке пропущенные значения
        if any(field == "" for field in row):
            print("Пропущенные значения обнаружены, строка пропущена:", row)
            continue
        good_rows.append(row)

print("\nСтроки с полными данными:")
for row in good_rows:
    print(*row)
