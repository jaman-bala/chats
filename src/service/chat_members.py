from src.schemas.chat_members import ChatMemberAddRequest
from src.service.base import BaseService


class ChatMemberService(BaseService):
    async def create_chat_member(self, data: ChatMemberAddRequest):
        new_chat_member = await self.db.chats_member.add(data)
        await self.db.commit()
        return new_chat_member

    async def get_chat_member(self):
        chat_member = await self.db.chats_member.get_all()
        return chat_member
