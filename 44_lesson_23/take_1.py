# CASE 1 -- Это не кортеж
def get_info() -> tuple[str | float]:
    return "Bob"


def get_info_1() -> tuple[str | float]:
    return (10.2,)


# CASE 2 -- Длина один, если хоим 2 надо исправить | на ,
def get_info_2() -> tuple[str | float]:
    return ("Bob", 10)


def get_info_3() -> tuple[str, float]:
    return ("Bob", 10)


# CASE 3
def get_info_4() -> tuple[str | int, float | list[int]]:
    return ("Bob", [10])


# CASE 4 -- Проблема того, что int подтип float
from typing import NewType

StrictFloat = NewType("StrictFloat", float)


def get_info_5() -> tuple[str, StrictFloat]:
    return ("Bob", 10.2)


def get_info_6() -> tuple[str, StrictFloat]:
    return ("Bob", StrictFloat(10.5))
    # mypy: OK (явное приведение обязательно)


[10.2, 10.3]
[StrictFloat(10.2), StrictFloat(10.3)]

data = [10.2, 10.3]
print(list(map(str, data)))
print(data)


from typing import Any


def test() -> Any:
    return (10,)
