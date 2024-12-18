import uuid
from pydantic import BaseModel, ConfigDict


class ChatMemberAddRequest(BaseModel):
    chat_id: uuid.UUID
    user_id: uuid.UUID
    is_admin: bool = False


class ChatMemberAdd(BaseModel):
    chat_id: uuid.UUID
    user_id: uuid.UUID
    is_admin: bool = False


class ChatMemberPatch(BaseModel):
    chat_id: uuid.UUID
    user_id: uuid.UUID
    is_admin: bool = False


class ChatMember(BaseModel):
    id: uuid.UUID
    chat_id: uuid.UUID
    user_id: uuid.UUID
    is_admin: bool = False

    model_config = ConfigDict(from_attributes=True)
