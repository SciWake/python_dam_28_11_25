class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working...")


class Programmer(Employee):
    pass


class Manager(Employee):
    pass


programmer = Programmer("Alice")
manager = Manager("Bob")

person = [Programmer("Alice"), Manager("Bob")]

programmer.work()
manager.work()
