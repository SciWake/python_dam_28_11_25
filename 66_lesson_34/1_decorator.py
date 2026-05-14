def decorator(func):  # Функция-декоратор, принимает другую функцию
    def wrapper(name):  # Вложенная функция-обертка, добавляющая дополнительное поведение
        print("Логика до выполнения функции")
        func(name)  # Вызываем переданную функцию
        print("Логика после выполнения функции")

    return wrapper  # Возвращаем изменённую функцию


def say_hello(name):
    print(f"Привет! {name}")


say_helldo = decorator(say_hello)
print(say_hello)
say_hello("")
