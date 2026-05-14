def validate_args(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Проверка длины аргументов
            if len(args) != len(expected_types):
                raise TypeError(
                    f"Ожидалось {len(expected_types)} аргументов, получено {len(args)}"
                )

            # Проверка типов аргументов
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Аргумент {arg} должен быть типа {expected_type.__name__}"
                    )

            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


# Пример использования
try:
    greet(25, "Анна")  # Все аргументы имеют правильные типы
    greet("25", "Анна")  # Возникнет исключение TypeError
except TypeError as e:
    print(e)
