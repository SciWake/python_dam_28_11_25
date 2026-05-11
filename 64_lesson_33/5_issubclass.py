class Employee:
    pass


class Programmer(Employee):
    pass


class Manager(Employee):
    pass


class BackendDeveloper(Programmer):
    pass


print(issubclass(Programmer, Employee))  # Прямой потомок
print(issubclass(BackendDeveloper, Programmer))  # Прямой потомок
print(issubclass(BackendDeveloper, Employee))  # Потомок через цепочку
print(issubclass(Manager, Programmer))  # Разные ветки иерархии
print(issubclass(Employee, object))  # Все классы наследуют от object
