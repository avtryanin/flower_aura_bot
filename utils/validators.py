from functools import wraps
from config import ADMIN_IDS
from utils.logger import log_action


def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


def require_admin(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        event = args[0] if args else kwargs.get("event")
        user_id = getattr(event.from_user, "id", None)
        if not is_admin(user_id):
            log_action(
                'User', event.from_user,
                "attempted to execute an admin command"
            )
            return
        return await func(*args, **kwargs)
    return wrapper


def parse_add_command(text: str):
    _, name, price, quantity = text.split()
    return name, float(price), int(quantity)


def parse_edit_command(text: str):
    _, pid, field, value = text.split()
    pid = int(pid)
    if field == 'price':
        value = float(value)
    elif field == 'quantity':
        value = int(value)
    return pid, field, value


def parse_delete_command(text: str):
    _, pid = text.split()
    return int(pid)
