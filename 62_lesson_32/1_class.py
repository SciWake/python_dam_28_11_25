class User:
    name = 'Alex'
    age = 17

# Обращение к атрибутам класса
print(User.age)
print(User.name)

# Изменение/создание атрибутов класса
User.age = 20
User.gender = 'мужчина'


# Создание объектов (экземпляр класса)
u1 = User()
u2 = User()

# Обращение к атрибутам объектов
print(u1.age)
print(u2.name)

# Изменение/создание атрибутов объекта
u1.age = 79
u2.gender = 'жен'


print(u1.age)
print(u2.gender)
