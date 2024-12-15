from src.repositories.mappers.base import DataMapper
from src.models import UserOrm, ChatOrm, ChatMemberOrm, MessageOrm
from src.schemas.chats import Chat, ChatMember, Message
from src.schemas.users import User


class UserDataMapper(DataMapper):
    db_model = UserOrm
    schema = User


class ChatDataMapper(DataMapper):
    db_model = ChatOrm
    schema = Chat


class ChatMemberDataMapper(DataMapper):
    db_model = ChatMemberOrm
    schema = ChatMember


class MessageDataMapper(DataMapper):
    db_model = MessageOrm
    schema = Message
