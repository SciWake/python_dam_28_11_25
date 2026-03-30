"""
## Задание

Напишите программу, которая на вход принимает два числа
A и B, и возводит число А в целую степень B с помощью рекурсии.
"""


def my_pow(a, b):
    if b == 0:
        return 1
    return my_pow(a, b - 1) * a


def my_pow_ternary(a, b):
    return 1 if b == 0 else my_pow(a, b - 1) * a


print(my_pow_ternary(10, 2))


# Реешние через хвостовую рекурсию
def tail_recursive_pow(a, b, acc=1):
    if b == 0:
        return acc
    return tail_recursive_pow(a, b - 1, acc * a)


print(tail_recursive_pow(10, 2))
