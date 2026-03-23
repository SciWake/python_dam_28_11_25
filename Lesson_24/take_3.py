def add(a: int, b: int) -> tuple:
    return (a + b,)

num: int = 10

print(add("10", "10"))


def process_numbers(numbers: list[int]) -> list[int]:
# Список чисел
    return [n ** 2 for n in numbers]


process_numbers(['1', '1'])


def get_info() -> tuple[str, float]:
# Первый элемент str, второй элемент float
    return "Bob", 4.91


def variable_tuple() -> tuple[int, ...]:
# Кортеж произвольной длины, но только целые числа
    return 5, 8, 2


def variable_tuple() -> tuple[int,]:
# Кортеж произвольной длины, но только целые числа
    return (5, 4)