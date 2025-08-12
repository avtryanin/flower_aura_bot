import logging
import sys
from logging.handlers import RotatingFileHandler

# Основной логгер
logger = logging.getLogger("flower_aura_bot")
logger.setLevel(logging.INFO)  # INFO — чтобы логировать действия пользователей

# Формат логов
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Логи в консоль
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Логи в файл (ротация — 5 МБ, хранить 5 файлов)
file_handler = RotatingFileHandler(
    "logs/bot.log", maxBytes=5_000_000, backupCount=5, encoding="utf-8"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Отдельный логгер для ошибок
error_file_handler = RotatingFileHandler(
    "logs/errors.log", maxBytes=5_000_000, backupCount=5, encoding="utf-8"
)
error_file_handler.setFormatter(formatter)
error_file_handler.setLevel(logging.ERROR)
logger.addHandler(error_file_handler)


def log_action(role: str, user, action: str):
    logger.info(f"{role} {user.id} ({user.full_name}) {action}")
