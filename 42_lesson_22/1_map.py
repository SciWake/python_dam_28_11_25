"""Использование встроенного map."""

numbers = [1, 2, 3, 4, 5, 4, 16, 2, 24]


# Напишем функцию обработки чисел
def preproc_numbers(x):
    if x % 2 == 0:
        return "чет"
    return "нечет"


# 1. Пройтись циклом
# for i, number in enumerate(numbers):
#     numbers[i] = preproc_numbers(number)
# print(numbers)


# 2. Обработка этой фукнцией через map
# print(list(map(preproc_numbers, numbers)))

# 3. Используем lambda, так лучше
# print(list(map(lambda x: 'чет' if x % 2 == 0 else 'нечет', numbers)))


# -----------------------------------------------------------
# Ещё примеры MAP
data = [int(num) for num in input("Input: ").split(", ")]
print(data)

print(input("Input: ").split(", "))
data = list(map(int, input("Input: ").split(", ")))
print(data)
