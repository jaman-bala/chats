from src.models import ChatMemberOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ChatMemberDataMapper


class ChatsMemberRepository(BaseRepository):
    model = ChatMemberOrm
    mapper = ChatMemberDataMapper
