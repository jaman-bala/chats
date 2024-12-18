import sys
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.config import settings
from src.api.users import router as users_router
from src.api.chats import router as chats_router
from src.api.chats_member import router as members_router
from src.api.message import router as message_router
from src.connectors.websocket import router as websocket_router

app = FastAPI(
    docs=None,
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.mount(
    "/static/avatars", StaticFiles(directory=settings.LINK_IMAGES), name="avatars"
)
app.mount(
    "/static/upload-files",
    StaticFiles(directory=settings.LINK_UPLOAD_FILES),
    name="upload-files",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Разрешить запросы с любых источников. Можете ограничить список доменов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)
app.include_router(users_router)
app.include_router(chats_router)
app.include_router(members_router)
app.include_router(message_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)  # host="0.0.0.0",
