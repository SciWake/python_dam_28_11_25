import sys

list_comp = [x**2 for x in range(10**6)]  # Списковое включение
gen_expr = (x**2 for x in range(10**6))  # Генераторное выражение

print("Размер списка:", sys.getsizeof(list_comp), "байт")
print("Размер генератора:", sys.getsizeof(gen_expr), "байт")
