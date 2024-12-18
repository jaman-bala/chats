from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.chats import ChatMemberAddRequest
from src.service.chat_members import ChatMemberService

router = APIRouter(prefix="/chat_members", tags=["Информация о пользователе"])


@router.post("/create")
async def create_chat_members(db: DBDep, data: ChatMemberAddRequest):
    chat_members = await ChatMemberService(db).create_chat_member(data)
    return {"status": "OK", "data": chat_members}


@router.get("")
async def get_members(db: DBDep):
    members = await ChatMemberService(db).get_chat_member()
    return {"status": "Запрос выполнин", "data": members}
