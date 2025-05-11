from api.v1.user.repository import UserRepository
from api.v1.user.schemas import SCreateUser, SUpdateUser
from api.v1.user.utils import get_hashed_password


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def find_by(self, **filters):
        return await self.repository.find_one_or_none(**filters)

    async def create_user(self, user: SCreateUser):
        data_in = user.model_dump()
        data_in["hashed_password"] = get_hashed_password(
            password=data_in.pop("password")
        )
        return await self.repository.create_record(new_data=data_in)

    async def update_user(self, user: SUpdateUser, pk: int):
        return await self.repository.update_record(
            pk=pk, new_data=user.model_dump(exclude_none=True, exclude_unset=True)
        )

    async def delete_user(self, pk: int):
        return await self.repository.delete_record(pk=pk)


def get_user_service() -> UserService:
    return UserService(UserRepository())
