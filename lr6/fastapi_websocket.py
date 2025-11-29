"""
FastAPI приложение чат (WebSocket).
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from datetime import datetime
import json

app = FastAPI(title="FastAPI WebSocket Chat", version="1.0.0")

# Хранилище для чата
active_connections: list[WebSocket] = []
chat_messages: list[dict] = []


@app.get("/")
def read_root():
    """Корневой endpoint."""
    return FileResponse("chat.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint для чата."""
    await websocket.accept()
    active_connections.append(websocket)
    
    # Отправляем историю сообщений новому пользователю
    for message in chat_messages[-10:]:  # Последние 10 сообщений
        await websocket.send_json(message)
    
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Создаем сообщение
            message = {
                "username": message_data.get("username", "Anonymous"),
                "message": message_data.get("message", ""),
                "timestamp": datetime.now().isoformat()
            }
            
            # Сохраняем в историю
            chat_messages.append(message)
            
            # Отправляем всем подключенным клиентам
            for connection in active_connections:
                try:
                    await connection.send_json(message)
                except:
                    pass
    
    except WebSocketDisconnect:
        active_connections.remove(websocket)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)

