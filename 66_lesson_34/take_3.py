# def decorator(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(3):
#             result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @decorator
# def example_function():
#     print("Функция выполнена")
#
# # Вызываем функцию
# example_function()


def repeat_decorator(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


repeat_input = int(input("Enter a number to repeat: "))


@repeat_decorator(repeat_input)
def example_function():
    print("Функция выполнена")


# Вызываем функцию
example_function()
