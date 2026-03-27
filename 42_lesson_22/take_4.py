def apply_func(func, numbers):
    return [func(num) for num in numbers]


result = apply_func(lambda x: x + 10, [5, 8, 3])
print(result)