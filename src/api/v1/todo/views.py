import logging

from fastapi import APIRouter

from api.v1.todo.schemas import SToDoCreate, SResponseToDo, SDetailTODO, SUpdateTODO
from api.v1.todo.services import get_todo_service

router = APIRouter(prefix="/todo", tags=["TODO"])
todo_service = get_todo_service()
log = logging.getLogger(__name__)


@router.get("/list", response_model=list[SResponseToDo])
async def list_todos():
    log.info("Получены все записи")
    return await todo_service.find_all()


@router.post("/create", response_model=SResponseToDo)
async def create_todo(todo: SToDoCreate):
    log.info("Запись создана")
    return await todo_service.create(todo)


@router.delete("/delete/{pk}")
async def delete_todo(pk: int):
    await todo_service.delete(pk=pk)
    log.info("Todo deleted")
    return {"success": True}


@router.get("/details/{pk}", response_model=SDetailTODO)
async def detail_todo(pk: int):
    log.info("Get details")
    return await todo_service.find_one_or_none(pk=pk)


@router.put("/update/{pk}", response_model=SResponseToDo)
async def update_todo(pk: int, new_todo: SUpdateTODO):
    log.info("Update todo")
    return await todo_service.update(pk=pk, data=new_todo)
