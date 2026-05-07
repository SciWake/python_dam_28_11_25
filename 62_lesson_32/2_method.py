# class User:
#     name = 'Alex'
#     age = 17

#     def method_1(self):
#         print("Я метод 1")
#         print("Self вунтри метода", self)


# u1 = User()

# # Вызываем методы
# u1.method_1() # == User.method_1(u1)
# print("u1 вне метода", u1)


class User:
    counter = 0

    def set_info(self, name, age):
        self.name = name
        self.age = age


u1 = User()
u1.set_info("Alex", 27)
User.counter += 1
u2 = User()
u2.set_info("Jon", 48)
User.counter += 1

print(u1.name, u1.age)
print(u2.name, u2.age)
print(User.counter)
