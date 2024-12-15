from src.repositories.chats import ChatsRepository
from src.repositories.chats_member import ChatsMemberRepository
from src.repositories.messages import MessageRepository
from src.repositories.users import UsersRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.chats = ChatsRepository(self.session)
        self.chats_member = ChatsMemberRepository(self.session)
        self.message = MessageRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()
