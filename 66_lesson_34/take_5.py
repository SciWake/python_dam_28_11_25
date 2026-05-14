# ПРИМЕР 1: Проверяет, авторизован ли пользователь, прежде чем выполнить функцию.
def auth_decorator(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") == required_role:
                return func(user, *args, **kwargs)
            else:
                return f"Доступ запрещен для пользователя с ролью {user.get('role')}"

        return wrapper

    return decorator


@auth_decorator("admin")
def sensitive_function(user):
    return "Конфиденциальная информация"


# Пример использования
user1 = {"name": "Alice", "role": "admin"}
user2 = {"name": "Bob", "role": "user"}

print(sensitive_function(user1))  # Доступ разрешен
print(sensitive_function(user2))  # Доступ запрещен
