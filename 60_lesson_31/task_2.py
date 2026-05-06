""" 
Напиши паттерн, который найдёт только домены с нужными зонами:
site.com, api.site.org, start.start.start.docs.python.org, test.net
"""

import re

text = """site.com
ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
api.site.org start.start.start.docs.python.org local test.net
"""

domen = re.findall(r"\w+(?:\.*\w*)*\.(?:org|com|net)", text)
print(domen)

domen = re.findall(r"[\w.]+\.(?:com|org|net)\b", text)
print(domen)
