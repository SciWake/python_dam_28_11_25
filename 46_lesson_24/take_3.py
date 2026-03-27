"""## Задание 1

Факториал числа
"""


def fact_for(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


fact_for(5)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


fact(5)
# return 5 * fact(5 - 1) -> 5 * 4 * 3 * 2 * 1
#     return 4 * fact(4 - 1) -> 4 * (3 * (2 * 1))
#         return 3 * fact(3 - 1) -> 3 * (2 * 1)
#             return 2 * fact(2 - 1) -> (2 * 1)
#                 fact(1) -> 1
