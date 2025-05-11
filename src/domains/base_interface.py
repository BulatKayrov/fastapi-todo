from abc import ABC, abstractmethod


class AbstractInterface(ABC):
    model = None

    @abstractmethod
    async def find_all(self, *args, **kwargs):
        pass

    @abstractmethod
    async def find_one_or_none(self, *args, **kwargs):
        pass

    @abstractmethod
    async def create_record(self, *args, **kwargs):
        pass

    @abstractmethod
    async def update_record(self, *args, **kwargs):
        pass

    @abstractmethod
    async def delete_record(self, *args, **kwargs):
        pass
