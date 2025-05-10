from pydantic import BaseModel, ConfigDict


class BaseTodo(BaseModel):
    title: str
    description: str
    status: bool


class SToDoCreate(BaseModel):
    title: str
    description: str


class SResponseToDo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    pk: int
    title: str
    status: bool


class SDetailTODO(SResponseToDo):
    description: str


class SUpdateTODO(BaseModel):
    title: str | None = None
    description: str | None = None
    status: bool | None = None
