def function_a():
    print("Начало A")
    function_b()
    print("Конец A")


def function_b():
    print("Начало B")
    function_c()
    print("Конец B")


def function_c():
    print("Начало C")
    print("Конец C")


function_a()
