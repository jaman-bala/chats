from src.models import MessageOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import MessageDataMapper


class MessageRepository(BaseRepository):
    model = MessageOrm
    mapper = MessageDataMapper
