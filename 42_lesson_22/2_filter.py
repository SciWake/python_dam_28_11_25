"""Использование встроенного filter.
Функция filter() принимает два параметра.
Первый — имя созданной пользователем функции,
а второй — итерируемый объект
(список, строка, множество, кортеж и так далее)."""


def my_filter(function, numbers):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


numbers = [1, 2, 3, 4, 5, 4, 16, 2, 24]
# Напишем фильтр через lambda и подставим внуть функции фильтрации
print(my_filter(lambda x: x >= 10, numbers))


# filter(функци, последовательность)
print(list(filter(lambda x: x >= 10, numbers)))
