from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from typing import List
import uuid

router = APIRouter()

# Словарь для хранения активных WebSocket-соединений, ключом является chat_id
active_connections: dict[uuid.UUID, List[WebSocket]] = {}

@router.websocket("/ws/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: uuid.UUID):
    # Ожидаем подключения клиента
    await websocket.accept()

    # Добавляем подключенного клиента в список активных соединений для конкретного чата
    if chat_id not in active_connections:
        active_connections[chat_id] = []
    active_connections[chat_id].append(websocket)

    try:
        while True:
            # Ожидаем сообщения от клиента
            data = await websocket.receive_text()

            # Отправляем это сообщение всем остальным подключенным клиентам в чат
            for connection in active_connections[chat_id]:
                if connection != websocket:
                    await connection.send_text(data)
    except WebSocketDisconnect:
        # Если клиент отключился, удаляем его из списка подключений
        active_connections[chat_id].remove(websocket)
