from functools import wraps

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from core.config import settings

engine = create_async_engine(url=settings.sqlite_url, echo=settings.echo)
async_session = async_sessionmaker(
    bind=engine, expire_on_commit=False, autocommit=False, autoflush=False
)


def connection(_func=None, *, commit=False):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with async_session() as session:
                try:
                    result = await func(session=session, *args, **kwargs)
                    if commit:
                        await session.commit()
                    return result
                except Exception as e:
                    await session.rollback()
                    raise e
                finally:
                    await session.close()

        return wrapper

    if _func is None:
        return decorator

    return decorator(_func)


# def connection(func):
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         async with async_session() as session:
#             try:
#                 result = await func(session=session, *args, **kwargs)
#                 return result
#             except Exception as e:
#                 await session.rollback()
#                 raise e
#             finally:
#                 await session.close()
#
#     return wrapper
