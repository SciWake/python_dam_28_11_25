"""Поиск низких оценок за период
Реализуйте программу, которая должна:
● Прочитать данные из файла grades.json.
● Реализовать функцию filter_low_scores(), которая:
    ○ Принимает минимальный проходной балл (threshold) и диапазон дат (start_date, end_date) в
    формате дд-мм-гггг.
    ○ Возвращает все оценки ниже порога, полученные в заданный период.
    ○ Сохраняет отфильтрованные записи в файл filtered_low_scores.json.
"""

import json
from datetime import datetime


def filter_low_scores(threshold, start_date, end_date):
    date_format = "%d-%m-%Y"

    # Преобразуем строковые границы диапазона в объекты datetime
    start_dt = datetime.strptime(start_date, date_format)
    end_dt = datetime.strptime(end_date, date_format)

    # Читаем исходные данные из файла
    try:
        with open("54_leeson_28/grades.json", "r", encoding="utf-8") as infile:
            data = json.load(infile)
    except FileNotFoundError:
        print("Ошибка: Файл grades.json не найден.")
        return []

    filtered_records = []

    # Фильтруем записи
    for record in data:
        date = datetime.strptime(record["date"], date_format)
        if record["grade"] < threshold and (start_dt <= date <= end_dt):
            filtered_records.append(record)

    # Сохраняем результат в новый JSON-файл
    with open("54_leeson_28/filtered_low_scores.json", "w", encoding="utf-8") as outfile:
        json.dump(filtered_records, outfile, ensure_ascii=False, indent=4)

    return filtered_records


# Пример использования функции:

result = filter_low_scores(70, "01-01-2025", "31-05-2025")

print(f"Найдено записей: {len(result)}, \n")
print(json.dumps(result, ensure_ascii=False, indent=4))
