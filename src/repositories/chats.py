from src.models import ChatOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ChatDataMapper


class ChatsRepository(BaseRepository):
    model = ChatOrm
    mapper = ChatDataMapper
