from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware

from database.db import get_session
from utils.logger import logger


class DatabaseSessionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Dict[str, Any], Any], Awaitable[Any]],
        event,
        data: Dict[str, Any]
    ) -> Any:
        async with get_session() as session:
            data['session'] = session
            return await handler(event, data)


class ErrorLoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        try:
            return await handler(event, data)
        except Exception as e:
            logger.exception(f"Error while processing event: {event}")
            raise e
