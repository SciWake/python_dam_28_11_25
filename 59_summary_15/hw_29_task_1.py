"""
Работа с CSV-файлами

На лекции при выполнении практического задания 2 был получен файл grades.csv.

Напишите программу, которая:
    -- Читает этот файл.
    -- Создает на его основе три новых файла: grades-Science.csv,
    grades-Math.csv, grades-Physics.csv. В каждом из этих файлов
    только два столбца - имя и количество баллов по тому предмету,
    который указан в названии файла.
    -- Создает четвертый файл grades-info.csv.
    В этом файле три строки (по названиям предметов)
    и столбцы со статистическими характеристиками оценок:
    среднее арифметическое, минимум, максимум, медиана,
    стандартное отклонение.
"""

import csv
import statistics
from collections import defaultdict

BASE_PATH = "59_summary_15"

buckets = defaultdict(list)
with open(f"{BASE_PATH}/grades.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        if row["subject"] in ["Science", "Math", "Physics"]:
            buckets[row["subject"]].append((row["name"], int(row["grade"])))

stats_rows = []

for subject, rows in buckets.items():
    with open(f"{BASE_PATH}/grades-{subject}.csv", "w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows([["name", "grade"]] + rows)

    grades = [g for _, g in rows]
    stats_rows.append(
        {
            "subject": subject,
            "avg": round(statistics.mean(grades), 2),
            "min": min(grades),
            "max": max(grades),
            "median": statistics.median(grades),
            "stdev": round(statistics.stdev(grades), 2),
        }
    )

with open(f"{BASE_PATH}/grades-info.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["subject", "avg", "min", "max", "median", "stdev"])
    writer.writeheader()
    writer.writerows(stats_rows)
