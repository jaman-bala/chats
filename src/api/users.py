from typing import List
from fastapi import APIRouter, Response, Form, File, UploadFile

from src.api.dependencies import DBDep
from src.exeptions import (
    UserNotFoundException,
    UserNotRegisteredHTTPException,
    IncorrectPasswordException,
    IncorrectPasswordHTTPException,
)
from src.schemas.users import (
    Role,
    UserRequestLogin,
)
from src.service.user import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])


@router.post("/create", summary="Создание пользователя 👨🏽‍💻")
async def register_user(
    db: DBDep,
    firstname: str = Form(..., max_length=100),
    lastname: str = Form(..., max_length=100),
    phone: str = Form(..., max_length=20),
    password: str = Form(...),
    avatar: List[UploadFile] = File(None),
    role: List[Role] = Form(default_factory=lambda: [Role.USER]),
):
    await AuthService(db).register_user(
        firstname=firstname,
        lastname=lastname,
        phone=phone,
        password=password,
        avatars=avatar,
        roles=role,
    )
    return {"message": "Пользователь создан"}


@router.get("")
async def get_user(db: DBDep):
    return await AuthService(db).get_all_users()


@router.post("/login", summary="Вход в систему 👨🏽‍💻")
async def login_user(
    data: UserRequestLogin,
    response: Response,
    db: DBDep,
):
    try:
        result = await AuthService(db).login_user(data)
        access_token = result["access_token"]
        user_id = result["user_id"]
        refresh_token = AuthService(db).create_refresh_token(
            response, access_token, {"user_id": user_id}
        )
    except UserNotFoundException:
        raise UserNotRegisteredHTTPException
    except IncorrectPasswordException:
        raise IncorrectPasswordHTTPException
    response.set_cookie("access_token", access_token)
    response.set_cookie("refresh_token", refresh_token, httponly=True)
    return {"status": "Успешный вход", "access_token": access_token}
