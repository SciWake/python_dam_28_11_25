# from functools import reduce

# numbers = [1, 2, 3, 4]
# # Умножение всех элементов списка последовательно
# result = reduce(lambda x, y: x * y, numbers)
# print(result)  # 24


# from functools import reduce

# numbers = [1, 2, 3, 4]
# # Умножение всех элементов списка, начиная с 10
# result = reduce(lambda x, y: x * y, numbers, 10)
# print(result)  # 240


from functools import reduce

numbers = [3, 1, 2, 7, 1, 3, 4, 2]
# Умножение всех элементов списка, начиная с 10
result = reduce(lambda x, y: sum(x + y), numbers, 0)
print(result)  # 240
