import re

# Пример 1
text = "<div>Hello</div><div>World</div>"

greedy = re.findall(r"<.*>", text)  # Жадный
lazy = re.findall(r"<.*?>", text)   # Ленивый

print(greedy)
print(lazy)


# Пример 2 - НЕ ЗАБЫТЬ ПОКАЗАТЬ ПРО КРУГЛЫЕ СКОБКИ
text = "<b>Привет</b>, это <b>Python</b>!"
greedy_pattern = r"<b>.*</b>"
greedy_result = re.findall(greedy_pattern, text)
print(f"Жадный: {greedy_result}")

lazy_pattern = r"<b>.*?</b>"
lazy_result = re.findall(lazy_pattern, text)
print(f"Ленивый: {lazy_result}")
