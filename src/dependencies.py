from typing import TYPE_CHECKING

import jwt
from fastapi import Depends, HTTPException

from api.v1.user.service import get_user_service
from api.v1.user.utils import get_token, get_payload
from core.config import settings

if TYPE_CHECKING:
    from models import User


async def get_current_user(
    token: str = Depends(get_token), user_service=Depends(get_user_service)
) -> "User":

    try:
        payload = get_payload(token, settings.secret_key, settings.algorithm)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=404, detail="Expired token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=404, detail="Invalid token")

    user_id = payload["user_id"]
    user = await user_service.find_by(pk=user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
