import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MessageAddRequest(BaseModel):
    chat_id: uuid.UUID | None = None
    sender_id: uuid.UUID | None = None
    content: str | None = None
    send_at: datetime | None = None
    is_read: bool = False


class MessageAdd(BaseModel):
    chat_id: uuid.UUID | None = None
    sender_id: uuid.UUID | None = None
    content: str | None = None
    files: list[str] | None = None
    send_at: datetime | None = None
    is_read: bool = False


class MessagePatch(BaseModel):
    chat_id: uuid.UUID | None = None
    sender_id: uuid.UUID | None = None
    content: str | None = None
    send_at: datetime | None = None
    is_read: bool = False


class Message(BaseModel):
    id: uuid.UUID
    chat_id: uuid.UUID | None = None
    sender_id: uuid.UUID | None = None
    content: str | None = None
    files: list[str] | None = None
    send_at: datetime | None = None
    is_read: bool = False

    model_config = ConfigDict(from_attributes=True)
