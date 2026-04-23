# Пример 1
# Генерирует квадраты чисел от 0 до 4
squares = (x**2 for x in range(5))

print(squares)  # Объект генератора

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


# Пример 2
squares = (x**2 for x in range(5))

for num in squares:
    print(num)


# Пример 3
import sys

list_comp = [x**2 for x in range(10**6)]  # Списковое включение
gen_expr = (x**2 for x in range(10**6))  # Генераторное выражение

print("Размер списка:", sys.getsizeof(list_comp), "байт")
print("Размер генератора:", sys.getsizeof(gen_expr), "байт")


# Пример 4
words = ["apple", "Banana", "cherry", "Apricot"]

print(any(word[0].isupper() for word in words))  # Есть слово с заглавной буквы
print(all(len(word) > 3 for word in words))  # Все слова длиннее 3 букв
