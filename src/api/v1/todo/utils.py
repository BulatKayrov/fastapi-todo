from functools import wraps

from fastapi import HTTPException

from functools import wraps
from fastapi import HTTPException


def try_except(_func=None, *, logger=None, message_un_args=None):
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
                if logger and message_un_args:
                    logger.info(message_un_args)
                return result

            except Exception as e:
                if logger:
                    logger.error(f"Ошибка: {str(e)}", exc_info=True)
                if isinstance(e, HTTPException):
                    raise HTTPException(status_code=e.status_code, detail="Кастомное сообщение")
                raise HTTPException(status_code=500, detail="Ошибка сервера")

        return async_wrapper

    return decorator(_func) if _func else decorator