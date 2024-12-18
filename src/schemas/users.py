import uuid

from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class Role(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class UserAddRequest(BaseModel):
    firstname: str = Field(default=None, max_length=100)
    lastname: str = Field(default=None, max_length=100)
    password: str
    phone: str
    roles: list[Role]


class UserAdd(BaseModel):
    firstname: str = Field(default=None, max_length=100)
    lastname: str = Field(default=None, max_length=100)
    phone: str
    hashed_password: str
    avatar: list[str]
    roles: list[Role]


class UserPatch(BaseModel):
    firstname: str = Field(default=None, max_length=100)
    lastname: str = Field(default=None, max_length=100)
    avatar: str = Field(default=None, max_length=200)
    phone: str = Field(default=None, max_length=20)


class UserRequestLogin(BaseModel):
    phone: str
    password: str


class User(BaseModel):
    id: uuid.UUID
    firstname: str = Field(default=None, max_length=100)
    lastname: str = Field(default=None, max_length=100)
    avatar: list[str]
    phone: str = Field(default=None, max_length=20)
    roles: list[Role]

    model_config = ConfigDict(from_attributes=True)


class UserWithHashedPassword(User):
    hashed_password: str


class UserRequestUpdatePassword(BaseModel):
    new_password: str
    change_password: str
