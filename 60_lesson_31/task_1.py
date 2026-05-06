"""
Задача 1.
Извлечь всё, что внутри пар одинарных кавычек, не захватывая сами кавычки:
"""

import re

text = "She said 'hello', then 'bye', but not 'hello again hello he d'"

words = re.findall(r"'(\w+(?:\s*\w*)*)'*", text)
print(words)
