import re

# ----------- ПРИМЕР 1 -----------
text = "\tPython 3.12, Java 17, C++ 14!\n"

print("Цифры:", re.findall(r"\d", text))