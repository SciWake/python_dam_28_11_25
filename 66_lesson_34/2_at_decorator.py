def decorator(func):
    def wrapper(*args, **kwargs):
        print("Логика до выполнения функции")
        result = func(*args, **kwargs)
        print("Логика после выполнения функции")
        return result

    return wrapper

@decorator
def say_hello(name, age):
    print("Я say_hello отработала")
    return f"Функция example_function {name} {age} выполнена"


# Вызываем функцию
# say_hello()

# say_hello = decorator(say_hello)
print(say_hello("Алексей", 17))
