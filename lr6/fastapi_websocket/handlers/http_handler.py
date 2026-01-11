"""
HTTP обработчик для FastAPI WebSocket приложения.
"""

from fastapi import WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
import json
import os
from typing import List
from services.chat_service import ChatService


class HttpHandler:
    """HTTP обработчик, организует роутинг."""
    
    def __init__(self, chat_service: ChatService):
        """
        Инициализация обработчика.
        
        Args:
            chat_service: Сервис для работы с чатом
        """
        self.chat_service = chat_service
        self.active_connections: List[WebSocket] = []
    
    async def handle_websocket(self, websocket: WebSocket):
        """Обработать WebSocket соединение."""
        await websocket.accept()
        self.active_connections.append(websocket)
        
        # Отправляем историю сообщений
        recent_messages = self.chat_service.get_recent_messages(10)
        for message in recent_messages:
            await websocket.send_json(message)
        
        try:
            while True:
                data = await websocket.receive_text()
                message_data = json.loads(data)
                
                username = message_data.get("username", "Anonymous")
                message_text = message_data.get("message", "")
                
                # Добавляем сообщение через сервис
                message = self.chat_service.add_message(username, message_text)
                
                # Отправляем всем подключенным
                await self._broadcast_message(message)
        
        except WebSocketDisconnect:
            self.active_connections.remove(websocket)
    
    async def _broadcast_message(self, message: dict):
        """Отправить сообщение всем подключенным."""
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass
    
    def serve_chat_page(self):
        """Вернуть HTML страницу чата."""
        chat_path = os.path.join(os.path.dirname(__file__), "..", "chat.html")
        return FileResponse(chat_path)

