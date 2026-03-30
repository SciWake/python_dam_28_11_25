import logging

# force=True удалит старые обработчики среды и применит твои
logging.basicConfig(level=logging.CRITICAL, force=True)


# Вывод различных сообщений
logging.debug("Отладочное сообщение")
logging.info("Информационное сообщение")
logging.warning("Предупреждение!")
logging.error("Ошибка!")
logging.critical("Критическая ошибка!")