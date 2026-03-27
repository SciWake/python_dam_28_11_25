from collections.abc import Iterable
from typing import Callable


def is_even(number: int) -> bool:
    """Проверка на четность числа
    Args:
        number (int): любое целое число
    Returns:
        bool: явл ли оно четным
    """
    return number % 2 == 0


def filter(func: Callable, numbers: Iterable[int]) -> list[int]:
    """Фильтр чисел по условию предиката
    Args:
        func (Callable): предикат
        numbers (list[int] | tuple[int] | set[int]): любая коллекция с целыми числами
    Returns:
        list: список чисел соответствующие условию предиката
    """
    return [num for num in numbers if func(num)]


numbers = [1, 2, 3, 4, 5, 6, 26, 3]
print(filter(is_even, numbers))


from functools import reduce

print(
    list(
        reduce(
            lambda a, b: a + b,
            map(lambda num: num**2, filter(lambda num: num % 2 == 0, [1, 2, 3, 4])),
        )
    )
)
