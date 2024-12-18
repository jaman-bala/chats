import uuid
from datetime import datetime
from fastapi import UploadFile, Form, File

from src.connectors.websocket import active_connections
from src.schemas.message import MessageAdd
from src.service.base import BaseService


class MessageService(BaseService):
    async def create_message(
        self,
        chat_id: uuid.UUID = Form(None),
        sender_id: uuid.UUID = Form(None),
        content: str = Form(None),
        send_at: datetime = Form(...),
        is_read: bool = False,
        files: list[UploadFile] = File(None),
    ):
        uploaded_files = []
        if files:
            for file in files:
                saved_filename = await self.db.message.file_upload(file)
                uploaded_files.append(saved_filename)

        new_message_data = MessageAdd(
            chat_id=chat_id,
            sender_id=sender_id,
            content=content,
            send_at=send_at,
            is_read=is_read,
            files=uploaded_files,
        )
        await self.db.message.add(new_message_data)
        await self.db.commit()
        if chat_id in active_connections:
            message = {
                "sender_id": sender_id,
                "content": content,
                "send_at": send_at,
                "file": uploaded_files,
                "is_read": is_read,
            }
            # Отправляем сообщение всем подключенным пользователям
            for websocket in active_connections[chat_id]:
                await websocket.send_text(str(message))

    async def get_message(self):
        get_messages = await self.db.message.get_all()
        return get_messages
