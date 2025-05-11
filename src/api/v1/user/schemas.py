from pydantic import BaseModel, EmailStr, ConfigDict


class BaseUser(BaseModel):
    username: str
    email: EmailStr


class SCreateUser(BaseModel):
    password: str | bytes
    email: EmailStr
    username: str


class SUpdateUser(BaseModel):
    email: EmailStr | None = None
    username: str | None = None


class SResponseUser(BaseUser):
    pk: int
    model_config = ConfigDict(from_attributes=True)


class SUserLogin(BaseModel):
    password: str
    email: EmailStr
