def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


# Функции можно хранить в списках, словарях и передавать их динамически
operations = {"+": add, "*": multiply}
choice = input("Выберите операцию (+, *): ")
# Из словаря получена функция и скобки с аргументами запускают её
print(operations[choice](10, 5))
