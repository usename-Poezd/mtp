"""
Сервис для работы с чатом.
"""

from typing import List, Dict
from repositories.chat_repository import ChatRepository


class ChatService:
    """Сервис для работы с чатом."""
    
    def __init__(self, repository: ChatRepository):
        """
        Инициализация сервиса.
        
        Args:
            repository: Репозиторий для сообщений чата
        """
        self.repository = repository
    
    def add_message(self, username: str, message: str) -> Dict:
        """
        Добавить сообщение.
        
        Args:
            username: Имя пользователя
            message: Текст сообщения
        
        Returns:
            dict: Созданное сообщение
        """
        return self.repository.add_message(username, message)
    
    def get_recent_messages(self, count: int) -> List[Dict]:
        """
        Получить последние сообщения.
        
        Args:
            count: Количество сообщений
        
        Returns:
            List[dict]: Список сообщений
        """
        return self.repository.get_recent_messages(count)

