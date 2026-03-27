"""
Простое число
Напишите функцию, которая проверяет, является ли число n
простым (делится только на 1 и само себя) и
возвращает булевый результат.
Данные:
n = 17

Пример вывода:
Число 17 является простым
"""


def is_prime_1(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def is_prime_2(n):
    for d in range(2, n + 1):
        if n % d == 0:
            break
    return d == n


is_prime_1(1)

# for num in range(17, 30):
#     print(f"{num} -> {is_prime_1(num)}")
