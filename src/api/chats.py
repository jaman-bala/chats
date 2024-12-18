from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.chats import ChatAddRequest
from src.service.chats import ChatService

router = APIRouter(prefix="/chats", tags=["Чат"])


@router.post("/create")
async def create_chats(db: DBDep, data: ChatAddRequest):
    chats = await ChatService(db).create_chats(data)
    return {"status": "Чат создан", "data": chats}


@router.get("")
async def get_chats(db: DBDep):
    chats = await ChatService(db).get_chats()
    return {"status": "Запрос выполнин", "data": chats}
