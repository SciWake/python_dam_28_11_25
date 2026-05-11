"""
Анализ курсов студентов
Реализуйте программу, которая должна:
    Прочитать файл student_courses.json, содержащий:
        Имя,
        дату рождения (birth_date) в формате дд.мм.гггг,
        дату поступления (enrollment_date) в том же формате,
        список курсов.
    Вычислить:
        Общее количество студентов.
        Средний возраст на момент поступления.
    Сохранить отчёт в JSON-файл student_courses_report.json.
"""

import json
from datetime import datetime


def read_data(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def save_data(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_age(birth_date, enroll_date):
    birth = datetime.strptime(birth_date, "%d.%m.%Y")
    enroll = datetime.strptime(enroll_date, "%d.%m.%Y")

    age = enroll.year - birth.year
    if (enroll.month, enroll.day) < (birth.month, birth.day):
        age -= 1

    return age


def make_report(students):
    ages = [get_age(s["birth_date"], s["enrollment_date"]) for s in students]

    return {
        "total_students": len(students),
        "average_enrollment_age": round(sum(ages) / len(ages), 1),
    }


report = make_report(read_data("59_summary_15/student_courses.json"))
save_data("59_summary_15/student_courses_report.json", report)
