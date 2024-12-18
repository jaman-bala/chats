import uuid
from typing import List
from datetime import datetime
from fastapi import APIRouter, Form, File, UploadFile

from src.api.dependencies import DBDep
from src.service.message import MessageService

router = APIRouter(prefix="/message", tags=["Сообщение"])


@router.post("/create")
async def create_messages(
    db: DBDep,
    chat_id: uuid.UUID = Form(None),
    sender_id: uuid.UUID = Form(None),
    content: str = Form(None),
    send_at: datetime = Form(...),
    is_read: bool = False,
    files: List[UploadFile] = File(None),
):
    await MessageService(db).create_message(
        chat_id=chat_id,
        sender_id=sender_id,
        content=content,
        send_at=send_at,
        is_read=is_read,
        files=files,
    )
    return {"status": "Сообщение создано"}


@router.get("")
async def get_messages(db: DBDep):
    return await MessageService(db).get_message()

