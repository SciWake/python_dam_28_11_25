import re

# ----------- ПРИМЕР 1 -----------
text = "\tPython 171337 19a 211 3.12, Java 17, C++ 14!\n"

print("Цифры:", re.findall(r"\d", text))
print("Двузначные цифры:", re.findall(r"\d\d\d", text))
print("НЕ цифры:", re.findall(r"\D", text))
print("Буквы, цифры, _:", re.findall(r"\w", text))
print("НЕ буквы, цифры, _:", re.findall(r"\W", text))
print("Пробелы:", re.findall(r"\s", text))
print("НЕ пробелы:", re.findall(r"\S", text))
print("Все символы (кроме \\n):", re.findall(r".", text))

# ----------- ПРИМЕР 2 -----------
text = "\nReport, aeport, report2, report10\t"

print("Буквы r или R в слове:", re.findall(r"[rR]eport,", text))
print("Все цифры:", re.findall(r"[0-9]", text))
print("Заглавные буквы:", re.findall(r"[A-Z]", text))
print("Строчные буквы:", re.findall(r"[a-z]", text))
print("Все буквы:", re.findall(r"[a-zA-Z]", text))
print("Все, кроме цифр:", re.findall(r"[^0-9]", text))


# ----------- ПРИМЕР 3 -----------
text = """
Orders: ID123, ID4567, ID89
Numbers: 123-45-67, 321-45-67
Prices: 100$, 199.50$, 99.99€, 0.49€, .99€
File names: report.txt, report2.txt, report10.txt
"""

print("Одна или более цифр:", re.findall(r"\d+", text))
print("Телефонные номера (формата xxx-xx-xx):", re.findall(r"\d{3}-\d{2}-\d{2}", text))
print("Цены (числа с десятичной точкой):", re.findall(r"\d+\.\d+", text))
print("ID-коды:", re.findall(r"ID\d{2,}", text))
print("Имена файлов 0+ цифр:", re.findall(r"report\d*\.txt", text))
print("Имена файлов 0/1 цифр:", re.findall(r"report\d?.txt", text)) 
