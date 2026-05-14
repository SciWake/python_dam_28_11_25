import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Начало отсчета времени
        result = func(*args, **kwargs)  # Выполнение функции
        end_time = time.time()  # Конец отсчета времени
        print(f"Функция {func.__name__} заняла {end_time - start_time} секунд")
        return result  # Возвращаем результат функции

    return wrapper


@timing_decorator
def algorithm_1():
    time.sleep(2)  # Имитация выполнения функции
    print("Функция выполнена")


@timing_decorator
def algorithm_2():
    time.sleep(1)  # Имитация выполнения функции
    print("Функция выполнена")


# Вызываем функцию
algorithm_1()

# Вызываем функцию
algorithm_2()
