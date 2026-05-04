import re

# ----------- ПРИМЕР 1 -----------
text = "ID12345 is confirmed. ID23456 is confirmed"

# Проверяем, начинается ли строка с "ID" + цифры
match = re.match(r"ID\d+", text)

if match:
    print("Объект Match:", match)
    print("Само совпадение:", match.group())
    print("Диапазон совпадения:", match.span())
else:
    print("Нет совпадения.")


# ----------- ПРИМЕР 2 -----------
text = "Order ID: 12345, Invoice No: 67890, Ref: ABC9876"

# Найдём первое число в тексте
match = re.search(r"\d+", text)

if match:
    print("Объект Match:", match)
    print("Само совпадение:", match.group())
    print("Индекс начала:", match.start())
    print("Индекс конца:", match.end())
    print("Диапазон совпадения:", match.span())
else:
    print("Нет совпадения.")


# ----------- ПРИМЕР 3 -----------
text = "Python is popular."

# Найдём слово "python" без учёта регистра
match = re.search(r"python", text, re.IGNORECASE)

if match:
    print("Найдено:", match.group())


# ----------- ПРИМЕР 4 -----------
text = "Order ID: 12345, Invoice No: 67890, Ref: ABC9876"

# Найдём все числа в тексте
matches = re.finditer(r"\d+", text)

for match in matches:
    print("Объект Match:", match)
    print("Само совпадение:", match.group())
    print("Диапазон совпадения:", match.span())
    print()


# ----------- ПРИМЕР 5 -----------
text = """Python is popular. It is used in web development, data science, 
and automation. Many developers choose Python for its simplicity."""

# Разделяем строку по запятым, пробелам и точкам
words = re.split(r"[,\s.]+", text)

print("Список слов:", words)


# ----------- ПРИМЕР 6 -----------
text = "apple,   banana ,  orange ,grape"

# Удаляем лишние пробелы перед и после запятых
clean_text = re.sub(r"\s*,\s*", ", ", text)

print("Отформатированный текст:", clean_text)


