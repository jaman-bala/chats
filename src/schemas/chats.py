import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ChatAddRequest(BaseModel):
    title: str | None = None
    type: str | None = None


class ChatPatch(BaseModel):
    title: str | None = None
    type: str | None = None


class Chat(BaseModel):
    id: uuid.UUID
    title: str | None = None
    type: str | None = None

    model_config = ConfigDict(from_attributes=True)


class ChatMemberAddRequest(BaseModel):
    chat_id: uuid.UUID | None = None
    user_id: uuid.UUID | None = None
    is_admin: bool | None = None


class ChatMemberPatch(BaseModel):
    chat_id: uuid.UUID | None = None
    user_id: uuid.UUID | None = None
    is_admin: bool | None = None


class ChatMember(BaseModel):
    id: uuid.UUID | None = None
    chat_id: uuid.UUID | None = None
    user_id: uuid.UUID | None = None
    is_admin: bool | None = None

    model_config = ConfigDict(from_attributes=True)


class MessageAddRequest(BaseModel):
    chat_id: uuid.UUID | None = None
    sender_id: uuid.UUID | None = None
    content: str | None = None
    file: str | None = None
    send_at: datetime | None = None
    is_read: bool | None = None


class MessagePatch(BaseModel):
    chat_id: uuid.UUID | None = None
    sender_id: uuid.UUID | None = None
    content: str | None = None
    file: str | None = None
    send_at: datetime | None = None
    is_read: bool | None = None


class Message(BaseModel):
    chat_id: uuid.UUID | None = None
    sender_id: uuid.UUID | None = None
    content: str | None = None
    file: str | None = None
    send_at: datetime | None = None
    is_read: bool | None = None

    model_config = ConfigDict(from_attributes=True)
