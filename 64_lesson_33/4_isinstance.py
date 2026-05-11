class Employee:
    pass


class Programmer(Employee):
    pass


class Manager(Employee):
    pass


e = Employee()
p = Programmer()
m = Manager()

print(isinstance(p, Programmer))  # экземпляр класса
print(isinstance(p, Employee))  # экземпляр наследника
print(isinstance(p, Manager))  # Manager не находится выше в иерархии
print(isinstance(p, object))  # True — все классы наследуют от object


class Employee:
    def work(self):
        print("Выполняет общие задачи")


class Programmer(Employee):
    def write_code(self):
        print("Пишет код")


class BackendDeveloper(Programmer):
    def write_code(self):
        print("Пишет серверный код")


class FrontendDeveloper(Programmer):
    def write_code(self):
        print("Пишет интерфейс")


class Manager(Employee):
    def work(self):
        print("Проводит собрание")


staff = [Programmer(), BackendDeveloper(), FrontendDeveloper(), Manager(), Employee()]

for person in staff:
    if isinstance(person, Programmer):
        person.write_code()
    else:
        person.work()
