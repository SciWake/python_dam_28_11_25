# numbers = [1, 2, 3, 4]
# squared = [num ** 2 for num in numbers]

# # Каждый элемент списка возводится в квадрат
# squared = map(lambda x: x ** 2, numbers)
# print(list(squared)) # [1, 4, 9, 16]


a = [1, 2, 3, 10]
b = [4, 5, 6]
# Каждая пара элементов списков суммируется
result = map(lambda x, y: x + y, a, b)
print(list(result)) # [5, 7, 9]


group_numbers = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# К каждому кортежу применяется функция sum
result = map(sum, group_numbers)
print(list(result)) # [6, 15, 24]