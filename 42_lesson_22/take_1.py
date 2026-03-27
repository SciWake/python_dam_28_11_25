def square(x):
    return x * x


def cube(x):
    return x * x * x


def apply_function(func, value):
    return func(value)  # Вызываем переданную функцию внутри другой функции


# Передаём функцию square без вызова (без скобок)
result_square = apply_function(square, 5)
result_square = apply_function(lambda x: x * x, 5)
# Передаём функцию cube без вызова (без скобок)
result_cube = apply_function(cube, 5)
print(result_square)
print(result_cube)
