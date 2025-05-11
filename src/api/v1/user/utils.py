import logging
from datetime import timedelta, datetime, timezone
from typing import TYPE_CHECKING

import bcrypt
import jwt
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.responses import Response

from api.v1.user.schemas import SUserLogin
from core.config import settings
from models import User

if TYPE_CHECKING:
    from api.v1.user.service import UserService

logger = logging.getLogger(__name__)


def create_token(payload, key, algorithm):
    return jwt.encode(payload=payload, key=key, algorithm=algorithm)


def get_payload(token, key, algorithm):
    return jwt.decode(token, key, algorithms=[algorithm])


def get_hashed_password(password: str) -> str:
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt()).decode()


def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


async def authenticate_user(user_in: SUserLogin, user_service: "UserService") -> "User":
    user = await user_service.find_by(email=user_in.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not check_password(
        password=user_in.password, hashed_password=user.hashed_password
    ):
        raise HTTPException(status_code=404, detail="Incorrect password")

    return user


def create_access_token(payload: dict, expires_delta: timedelta | None = None):
    to_encode = payload.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(seconds=settings.expires_token)
    to_encode.update({"exp": expire})
    return create_token(
        payload=to_encode, key=settings.secret_key, algorithm=settings.algorithm
    )


def set_access_token_in_cookie(user: "User", response: Response):
    token = create_access_token(payload={"user_id": user.pk})
    response.set_cookie(
        key="token", value=token, httponly=True, max_age=settings.expires_token
    )
    return {"token": token}


def get_token(request: Request):
    return request.cookies.get("token", None)
