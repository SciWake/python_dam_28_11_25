def gen1():
    yield 1
    yield 2


def gen2():
    yield 10
    yield from gen1()  # подключаем другой генератор
    yield 20


print(list(gen2()))
