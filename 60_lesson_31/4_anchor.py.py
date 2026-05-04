import re

# ----------- ПРИМЕР 1 -----------
# ^ Начало строки
text = "hello world"
# # Найти 'hello' только если оно стоит в начале строки
print(re.findall(r"^hello", text))  # ['hello']
print(re.findall(r"world", text))  # ['world']
print(re.findall(r"^world", text))  # [] — 'world' не в начале


# ----------- ПРИМЕР 2 -----------
# ^ Начало строки + MULTILINE
text = "first line\nsecond line"
print(re.findall(r"^.+", text))  # ['first line']
print(re.findall(r"^.+", text, re.MULTILINE))  # ['first line', 'second line']


# ----------- ПРИМЕР 3 -----------
# $ Конец строки
text = "hello world"
# Найти 'world' только если оно в конце строки
print(re.findall(r"world$", text))  # ['world']
print(re.findall(r"hello$", text))  # [] — 'hello' не в конце


# ----------- ПРИМЕР 4 -----------
# $ Конец строки + MULTILINE
text = "error: not found\nok: done"
print(re.findall(r".+$", text))  # ['ok: done']
print(re.findall(r".+$", text, re.MULTILINE))  # ['error: not found', 'ok: done']


# ----------- ПРИМЕР 5 -----------
# \b Граница слова
# “Слово” — последовательность word-символов: буквы, цифры, подчёркивание;

# \b — это позиция между символами, где слева \w,
# а справа \W, или наоборот; плюс начало/конец строки,
# если рядом стоит \w.
text = "category wildcat education _cat_ catalog"
print("Слова с 'cat' внутри:", re.findall(r"\w+cat\w+", text))
print("Слова с 'cat' в начале слов:", re.findall(r"\bcat\w*", text))
print("Слова с 'cat' в конце слов:", re.findall(r"\w*cat\b", text))


# ----------- ПРИМЕР 6 -----------
# \b НЕ граница слова
# \B — противоположность \b.
# \B совпадает там, где нет такой границы:
# либо с двух сторон \w, либо с двух сторон \W
text3 = "X123X 234 4567X X999"
print("Числа внутри строк:", re.findall(r"\B\d+\B", text3))
