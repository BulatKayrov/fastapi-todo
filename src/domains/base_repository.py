from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import connection
from domains.base_interface import AbstractInterface
from exceptions import NotFoundError


class BaseRepository(AbstractInterface):
    model = None

    @connection
    async def find_all(self, session: AsyncSession, **filters):
        stmt = select(self.model).filter_by(**filters)
        result = await session.execute(stmt)
        return result.scalars().all()

    @connection
    async def find_one_or_none(self, session: AsyncSession, **filters):
        stmt = select(self.model).filter_by(**filters)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @connection(commit=True)
    async def create_record(self, session: AsyncSession, new_data: dict, **filters):
        obj = self.model(**new_data)
        session.add(obj)
        return obj

    @connection(commit=True)
    async def update_record(
        self, session: AsyncSession, pk: int, new_data: dict, **filters
    ):
        stmt = select(self.model).filter_by(pk=pk)
        result = await session.execute(stmt)
        instance = result.scalar_one_or_none()

        if instance:
            for k, v in new_data.items():
                setattr(instance, k, v)
            return instance
        raise NotFoundError

    @connection(commit=True)
    async def delete_record(self, session: AsyncSession, **filters):
        stmt = select(self.model).filter_by(**filters)
        result = await session.execute(stmt)
        await session.delete(result.scalar_one_or_none())
        return
