class User:
    counter = 0
    MIN_AGE, MAX_AGE = 1, 120

    def __init__(self, name, age):
        self.name = name
        self.set_age(age)
        User.counter += 1
        self.id = "#" + str(User.counter)

    def set_age(self, age):
        if not (User.MIN_AGE <= age <= User.MAX_AGE):
            raise ValueError("Возраст должен быть в диапозоне от 1 до 120")
        self.age = age

    def get_id(self):
        return self.id

    def get_info(self):
        return f"Name: {self.name} Age: {self.age}"


u1 = User("Alex", 120)
u2 = User("Jon", 48)
u1.name = "Alex3"
print(u1.get_info(), u1.get_id())
print(u2.get_info(), u2.get_id())
print(User.counter)
