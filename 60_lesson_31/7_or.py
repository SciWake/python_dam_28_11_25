import re

# ----------- ПРИМЕР 1 -----------
text = "cat dog mouse"
print(re.findall(r"cat|dog", text))


# ----------- ПРИМЕР 2 -----------
text = "Анна Алла Алина"
print(re.findall(r"А(нн|лл|лин)а", text))
print(re.findall(r"А(?:нн|лл|лин)а", text))


# ----------- ПРИМЕР 3 -----------
text = "какока.png photo.jpg archive.zip readme.txt"
print(re.findall(r"\w+\.png|\w+\.jpg|\w+\.zip", text))
print(re.findall(r"\w+\.(png|jpg|zip)", text))
print(re.findall(r"\w+\.(?:png|jpg|zip)", text))
