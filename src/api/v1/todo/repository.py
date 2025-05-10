from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import connection
from exceptions import NotFoundError
from interfacies.base import AbstractInterface
from models import ToDo


class ToDoRepository(AbstractInterface):
    model = ToDo

    @connection
    async def find_all(self, session: AsyncSession):
        stmt = select(self.model).where(self.model.status == False)
        result = await session.execute(stmt)
        return result.scalars().all()

    @connection
    async def find_one_or_none(self, session: AsyncSession, **filters):
        stmt = select(self.model).filter_by(**filters)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @connection(commit=True)
    async def create_record(self, session: AsyncSession, new_data: dict):
        obj = self.model(**new_data)
        session.add(obj)
        return obj

    @connection(commit=True)
    async def update_record(self, session: AsyncSession, pk: int, new_data: dict):
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
