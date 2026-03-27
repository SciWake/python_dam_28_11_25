"""
Напишите рекурсивную функцию, которая подсчитывает количество вхождений определённого слова во вложенной структуре (список списков строк).
Данные
nested_sentences = [
    ["Python is great", "I love Python"],
    ["Python is powerful", ["Python is everywhere", "Learn Python"]],
    "Coding in Python is fun"
]
word = "Python"
Пример вывода
Количество вхождений: 6
"""


def count_word(structure, word: str) -> int:
    if isinstance(structure, str):
        return structure.count(word)

    if not structure:
        return 0

    return count_word(structure[0], word) + count_word(structure[1:], word)


nested_sentences = [
    ["Python is great", "I love Python"],
    ["Python is powerful", ["Python is everywhere", "Learn Python"]],
    "Coding in Python is fun",
]

word = "Python"

print("Количество вхождений:", count_word(nested_sentences, word))
