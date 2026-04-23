# Пример 1
# def generate_values():
#     print("Начало работы")
#     yield 1  # Приостанавливаем выполнение и возвращаем 1
#     print("Продолжение работы")
#     yield 2  # Приостанавливаем выполнение и возвращаем 2
#     print("Завершение работы")


# gen = generate_values()  # Создаём генератор, но код внутри функции пока не выполняется

# print(next(gen))  # Начало работы → 1
# print(next(gen))  # Продолжение работы → 2
# print(next(gen))  # Завершение работы → StopIteration, так как нет третьего yield


# Пример 2
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Возвращаем текущее значение и "замораживаем" выполнение
        count += 1  # После следующего вызова next() продолжится отсюда


gen = count_up_to(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  # StopIteration

gen = count_up_to(5)
for number in gen:
    print(number)
