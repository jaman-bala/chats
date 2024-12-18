import uuid
from typing import List
from enum import Enum
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.database import Base


class Role(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    firstname: Mapped[str | None] = mapped_column(String(599))
    lastname: Mapped[str | None] = mapped_column(String(599))
    phone: Mapped[str | None] = mapped_column(String(20))
    hashed_password: Mapped[str] = mapped_column(String(200))
    avatar: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True)
    roles: Mapped[List[Role]] = mapped_column(ARRAY(String))
