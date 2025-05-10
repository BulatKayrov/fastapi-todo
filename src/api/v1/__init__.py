from fastapi import APIRouter

from .todo.views import router as todo_router

router = APIRouter(prefix="/v1")
router.include_router(todo_router)
