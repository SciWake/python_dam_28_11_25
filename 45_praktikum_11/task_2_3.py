# 2.3. Фильтрация списка строк по критерию
# Доработайте функцию так, чтобы можно было в виде лямбда-функции
# передавать критерии отбора слов, которые нужно оставить.
# Например:
# слова, начинаются с заглавной буевы
# слова из одного символа
# слова начинаются и заканчиваются одной буквой, независимо от регистра

words = ["hi", "Hello", "a", "python", "Ok", "Radar"]
# Пример вывода:
# ['Hello', 'Ok', 'Radar']
# ['a']
# ['a', 'Radar']


def my_sum(a, b, c):
    return a + b + c


# print(my_sum(10, 12, 3)) -> 22


def filter_words(func, words: list[str]) -> list[str]:
    return list(filter(func, words))


print(filter_words(lambda word: word[0].isupper(), words))
print(filter_words(lambda word: len(word) == 1, words))
print(filter_words(lambda word: word[0].lower() == word[-1].lower(), words))

# predicates = [
#     lambda word: word[0].isupper(),
#     lambda word: len(word) == 1,
#     lambda word: word[0].lower() == word[-1].lower(),
# ]

# for item in predicates:
#     print(filter_words(item, words))


map()
