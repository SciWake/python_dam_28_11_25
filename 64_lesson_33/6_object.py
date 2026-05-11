class Test:
    # def __str__(self):
    #     print(1)
    #     return 'Вернули содержимое'
    pass


test_1 = Test()
print(dir(test_1))
# print(test_1)
# test_1.


class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working...")

    def __str__(self):
        return f"Employee(name='{self.name}')"


o1 = Employee("Alex")
print(o1)

