# Пример 1
numbers = [10, 20, 30]
iterator = numbers.__iter__()  # Создаём итератор

print(iterator.__next__())  # Получаем нулевой элемент
print(iterator.__next__())  # Получаем первый элемент
print("-" * 30)  # Можно прерваться на другие действия
print(iterator.__next__())  # Получаем второй элемент


# Пример 2
numbers = [1, 2, 3]  # Итерируемый объект
iterator = iter(numbers)  # Вызывает numbers.__iter__()

print(next(iterator))  # Вызывает iterator.__next__()
print(next(iterator))  # Вызывает iterator.__next__()
print(next(iterator))  # Вызывает iterator.__next__()
