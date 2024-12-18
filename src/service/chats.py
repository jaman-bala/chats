from src.schemas.chats import ChatAddRequest
from src.service.base import BaseService


class ChatService(BaseService):
    async def create_chats(self, data: ChatAddRequest):
        new_chats = await self.db.chats.add(data)
        await self.db.commit()
        return new_chats

    async def get_chats(self):
        chats = await self.db.chats.get_all()
        return chats
