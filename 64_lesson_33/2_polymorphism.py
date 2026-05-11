class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working...")


class Programmer(Employee):
    def work(self):
        print(f"{self.name} writing code...")


class Manager(Employee):
    def work(self):
        print(f"{self.name} managing team...")


staff = [Programmer("Alice"), Manager("Bob"), Programmer("Bill")]

for person in staff:
    person.work()  # Поведение зависит от конкретного типа
