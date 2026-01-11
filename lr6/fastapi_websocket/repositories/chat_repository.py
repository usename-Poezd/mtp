"""
Репозиторий для работы с сообщениями чата.
"""

from typing import List
from datetime import datetime


class ChatRepository:
    """Репозиторий для сообщений чата."""
    
    def __init__(self, max_history: int = 10):
        self.messages: List[dict] = []
        self.max_history = max_history
    
    def add_message(self, username: str, message: str) -> dict:
        """Добавить сообщение."""
        msg = {
            "username": username,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        self.messages.append(msg)
        # Ограничиваем историю
        if len(self.messages) > self.max_history * 2:
            self.messages = self.messages[-self.max_history:]
        return msg
    
    def get_recent_messages(self, count: int) -> List[dict]:
        """Получить последние сообщения."""
        return self.messages[-count:]

