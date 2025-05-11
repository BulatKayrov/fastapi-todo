from pydantic import BaseModel, ConfigDict


class BaseTodo(BaseModel):
    title: str
    description: str
    status: bool


class SToDoCreate(BaseModel):
    title: str
    description: str
    user_pk: int = 1


class SResponseToDo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    pk: int
    title: str
    status: bool
    user_pk: int


class SDetailTODO(SResponseToDo):
    description: str


class SUpdateTODO(BaseModel):
    title: str | None = None
    description: str | None = None
    status: bool | None = None
    user_pk: int
