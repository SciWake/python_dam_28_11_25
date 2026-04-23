numbers = [10, 20, 30]  # Итерируемый объект
iterator = iter(numbers)  # Создание итератора

while True:
    try:
        num = next(iterator)  # Получаем следующий элемент
        print(num)
    except StopIteration:
        break  # Завершаем цикл при окончании элементов
