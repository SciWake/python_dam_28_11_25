import logging
import time

# ----------------------------
# ========= Пример 1 =========
# ----------------------------
# logging.basicConfig(filename="app.log", level=logging.ERROR, force=True)

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     logging.error(f"Ошибка: {e}")


# ----------------------------
# ========= Пример 2 =========
# ----------------------------
# Настройка формата логов
# logging.basicConfig(
#     filename="app.log",
#     format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s",
#     level=logging.DEBUG,
#     force=True,
# )

# logging.debug("Это отладочное сообщение")
# logging.info("Информационное сообщение")
# logging.warning("Предупреждение")
# logging.error("Ошибка")
# logging.critical("Критическая ошибка")


# ----------------------------
# ========= Пример 2 =========
# ----------------------------
# Настраиваем формат логов
# log_format = "[%(asctime)s] | %(levelname)-8s | Строка: %(lineno)04d | %(message)s"

# logging.basicConfig(
#     level=logging.DEBUG,
#     force=True,
#     format=log_format,
#     datefmt="%Y-%m-%d %H:%M:%S",
# )


# def process_data():
#     logging.debug("Подключение к базе данных...")

#     user_id = 42
#     logging.info(f"Пользователь с ID {user_id} начал сессию")

#     # Имитация ошибки
#     try:
#         10 / 0
#     except ZeroDivisionError:
#         logging.error("Сбой вычислений: деление на ноль!")


# process_data()

# ----------------------------
# ========= Пример 3 =========
# ----------------------------
# Настраиваем формат логов
log_format = "[%(asctime)s] | %(levelname)-8s | Строка: %(lineno)04d | %(message)s"

logging.basicConfig(
    level=logging.DEBUG,
    force=True,
    format=log_format,
    datefmt="%Y-%m-%d %H:%M:%S",
)


def fetch_data(url, retries=3):
    for attempt in range(retries):
        try:
            # Имитация успешного подключения только на 3-й раз
            if attempt < 2:
                raise ConnectionError("Timeout")
            logging.info(f"Данные успешно скачаны с {url}")
            return {"status": "success"}

        except ConnectionError as e:
            logging.warning(f"Попытка {attempt + 1} провалилась: {e}. Повторяем...")
            time.sleep(1)

    logging.error("Не удалось скачать данные после 3 попыток.")
    return None


fetch_data("https://api.example.com")
