"""
Точка входа FastAPI WebSocket приложения.
"""

from fastapi import FastAPI, WebSocket
from config.settings import Config
from repositories.chat_repository import ChatRepository
from services.chat_service import ChatService
from handlers.http_handler import HttpHandler

config = Config()
app = FastAPI(title=config.TITLE, version=config.VERSION)


# Инициализация слоев (снизу вверх)
# 1. Repositories
chat_repository = ChatRepository(max_history=config.MAX_MESSAGE_HISTORY)

# 2. Services (зависят от repositories)
chat_service = ChatService(chat_repository)

# 3. Handlers (зависят от services)
http_handler = HttpHandler(chat_service)


@app.get("/")
def read_root():
    """Корневой endpoint - возвращает HTML страницу чата."""
    return http_handler.serve_chat_page()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint для чата."""
    await http_handler.handle_websocket(websocket)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.HOST, port=config.PORT)

