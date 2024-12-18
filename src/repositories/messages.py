import os
import uuid
import aiofiles
from fastapi import UploadFile

from src.config import settings
from src.models import MessageOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import MessageDataMapper


class MessageRepository(BaseRepository):
    model = MessageOrm
    mapper = MessageDataMapper

    async def file_upload(self, file: UploadFile) -> str:
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = f"{settings.LINK_UPLOAD_FILES}/{unique_filename}"
        os.makedirs(settings.LINK_UPLOAD_FILES, exist_ok=True)
        async with aiofiles.open(file_path, "wb") as buffer:
            content = await file.read()
            await buffer.write(content)
        return f"{settings.LINK_UPLOAD_FILES}/{unique_filename}"
