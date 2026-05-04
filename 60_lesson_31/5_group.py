import re

# ----------- ПРИМЕР 1 -----------
m = re.search(r'(\d{4})-(\d{2})-(\d{2})', 'Date: 2024-05-10')
print(m.group(0))  # 2024-05-10
print(m.group(1))  # 2024
print(m.group(2))  # 05
print(m.group(3))  # 10


# ----------- ПРИМЕР 2 -----------
text = "Order ID: 12345, Invoice No: 67890"

# # Найдём ID заказа и счёта
match = re.search(r"Order ID: (\d+), Invoice No: (\d+)", text)
if match:
    print("ID заказа:", match.group(1))
    print("Номер счёта:", match.group(2))


# ----------- ПРИМЕР 3 -----------
print(re.findall(r'(ab)+', 'abd abab ababab x'))
print(re.findall(r'(?:ab)+', 'abd abab ababab x'))


# ----------- ПРИМЕР 4 -----------
text = "USD 100, EUR 200, GBP 300"

# # Найдём суммы, не выделяя валюту
matches = re.findall(r"(?:USD|EUR|GBP) (\d+)", text)
print("Суммы:", matches)

# # Найдём суммы и валюту
matches = re.findall(r"(USD|EUR|GBP) (\d+)", text)
print("Суммы:", matches)

