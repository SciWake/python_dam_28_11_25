# Часто тот же процесс можно реализовать с помощью цикла:
def countdown_iterative(n: int) -> None:
    while n > 0:
        print(n)
        n -= 1
    print("Конец!")


countdown_iterative(5)


def countdown(n: int) -> None:
    if n <= 0:  # Базовый случай
        print("Конец!")
        return
    print(n)
    countdown(n - 1)  # Рекурсивный случай


countdown(5)


def countdown_recursive(n: int) -> str:
    if n <= 0:
        print("Конец!")
        return

    print(n)
    return countdown_recursive(n - 1)


# countdown_recursive(2: int) "Конец!"
#     return countdown_recursive(1: int) "Конец!"
#         return countdown_recursive(0: int) "Конец!"

result = countdown_recursive(5)
print(result)
