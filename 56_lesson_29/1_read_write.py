import csv

# Пример 1
# with open("56_lesson_29/data_raw/sales.csv", newline="") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# # Пример 2
# with open("output.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["name", "age"])
#     writer.writerow(["Alice", 30])


# # Пример 3
# rows = [["Alice", 30], ["Bob", 25], ["Charlie", 35]]
# with open("output.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["name", "age"])  # заголовок
#     writer.writerows(rows)  # сразу все строки


# # Пример 4
# with open("output.csv", "a", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Orange", "Rainbow", "2025-07-04", "110", "2.00"])
