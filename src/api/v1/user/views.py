import logging

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from starlette import status
from starlette.responses import Response

from api.v1.user.schemas import SResponseUser, SCreateUser, SUpdateUser, SUserLogin
from api.v1.user.service import get_user_service
from api.v1.user.utils import (
    authenticate_user,
    set_access_token_in_cookie,
)
from dependencies import get_current_user

router = APIRouter(prefix="/user", tags=["USER"])
user_service = get_user_service()
log = logging.getLogger(__name__)


@router.get("/me", response_model=SResponseUser)
async def get_me(user=Depends(get_current_user)):
    log.info("Пользователь (почта = %s) зашел в профиль", user.email)
    return user


@router.post("/create", response_model=SResponseUser)
async def create_user(user: SCreateUser):
    user = await user_service.create_user(user=user)
    log.info("Пользователь (почта = %s) создан", user.email)
    return user


@router.put("/update/{pk}", response_model=SResponseUser)
async def update_user(user: SUpdateUser, pk: int):
    user = await user_service.update_user(user=user, pk=pk)
    log.info("Пользователь (почта = %s) обновил профиль", user.email)
    return user


@router.delete("/delete/{pk}")
async def delete_user(pk: int):
    await user_service.delete_user(pk=pk)
    log.info("User deleted")
    return {"success": True}


@router.post("/login")
async def login_user(user_in: SUserLogin, response: Response):
    user = await authenticate_user(user_in=user_in, user_service=user_service)
    if user:
        log.info("User login success")
        return set_access_token_in_cookie(user=user, response=response)
    log.info("User login failed")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
    )


@router.get("/logout")
async def logout_user(response: Response):
    log.info("User logout success")
    return response.delete_cookie("token")
