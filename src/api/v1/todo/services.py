from api.v1.todo.repository import ToDoRepository
from api.v1.todo.schemas import SToDoCreate, SUpdateTODO


class ToDoService:

    def __init__(self):
        self.repository = ToDoRepository()

    async def find_all(self):
        return await self.repository.find_all()

    async def create(self, data: SToDoCreate):
        return await self.repository.create_record(new_data=data.model_dump())

    async def delete(self, pk: int):
        await self.repository.delete_record(pk=pk)

    async def find_one_or_none(self, pk: int):
        return await self.repository.find_one_or_none(pk=pk)

    async def update(self, pk: int, data: SUpdateTODO):
        return await self.repository.update_record(
            pk=pk, new_data=data.model_dump(exclude_none=True, exclude_unset=True)
        )


def get_todo_service():
    return ToDoService()
