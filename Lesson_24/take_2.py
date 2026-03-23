# number = 10
# int number = 10

# vector<int> data = []

# vector<vector<int>> data = [[1, 3], [12, 31]]

def function_name(param1, param2):
    """
    Описание функции.
    :param param1: Описание первого
    параметра.
    :param param2: Описание второго
    параметра.
    :return: Описание возвращаемого
    значения.
    """
    pass


def greet(name):
    """
    Функция принимает имя и возвращает
    строку приветствия.
    :param name: Имя пользователя.
    :return: Приветственное сообщение.
    """
    return f"Hello, {name}!"


def calculate_power(base: int, exponent: int = 2) -> int:
    """Calculates the power of a base to an exponent.

    Args:
        base (int): The number to be raised.
        exponent (int, optional): The power to raise the base to. Defaults to 2.

    Returns:
        int: The result of base raised to the exponent.

    Raises:
        ValueError: If base or exponent are negative.
    """
    if base < 0 or exponent < 0:
        raise ValueError("Inputs must be non-negative.")
    return base ** exponent


print(help(str))