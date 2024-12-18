import uuid
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, ForeignKey, DateTime

from src.database import Base


class ChatOrm(Base):
    __tablename__ = "chats"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str | None] = mapped_column(String(599))  # TODO: Имя группы
    type: Mapped[str | None] = mapped_column(
        String(599)
    )  # TODO: Тип чата: "personal" или "group"


class ChatMemberOrm(Base):
    __tablename__ = "chat_members"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    chat_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("chats.id")
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id")
    )
    is_admin: Mapped[bool | None] = mapped_column(
        Boolean, default=False
    )  # TODO: Роль в группе


class MessageOrm(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    chat_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("chats.id")
    )
    sender_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id")
    )
    content: Mapped[str | None] = mapped_column(String)  # TODO: Текст сообщения
    files: Mapped[list[str] | None] = mapped_column(
        ARRAY(String), nullable=True
    ) # TODO: Файл для чата
    send_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    is_read: Mapped[bool | None] = mapped_column(
        Boolean, default=False
    )  # TODO: Статус прочтения
