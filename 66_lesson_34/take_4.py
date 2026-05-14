# ПРИМЕР 1: Добавляет префикс и суффикс к результату выполнения функции.
def add_prefix_suffix_decorator(prefix, suffix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}{result}{suffix}"

        return wrapper

    return decorator


@add_prefix_suffix_decorator("<<", ">>")
def example_function(name):
    return f"Hello, {name}!"


# Вызываем функцию
print(example_function("World"))
print([1, 2, 3, 4])
print((1, 2, 3, 4))
