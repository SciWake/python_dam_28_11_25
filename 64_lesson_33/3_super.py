class Employee:
    def __init__(self, name, age):
        self.name = name
        if not (0 < age < 100):
            print("Возраст должен быть от 0 до 100")
            self.age = None
        else:
            self.age = age


class Programmer(Employee):
    def __init__(self, name, age, language):
        # Employee.__init__(self, name, age)
        super().__init__(name, age)  # вызываем родительский __init__
        self.language = language


class Manager(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age)  # вызываем родительский __init__
        self.department = department


p = Programmer("Alice", 170, "Python")
print(p.name)
print(p.language)


