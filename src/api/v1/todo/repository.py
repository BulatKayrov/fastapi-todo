from domains.base_repository import BaseRepository
from models import ToDo


class ToDoRepository(BaseRepository):
    model = ToDo

    # async def create_record(self, new_data: dict, **filters):
    #     await super().create_record(new_data=new_data, **filters)
