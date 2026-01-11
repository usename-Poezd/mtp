"""
Сервис для работы с элементами.
"""

from typing import Optional, List, Dict
from repositories.item_repository import ItemRepository
from models.item_model import Item


class ItemService:
    """Сервис для работы с элементами."""
    
    def __init__(self, repository: ItemRepository):
        """
        Инициализация сервиса.
        
        Args:
            repository: Репозиторий элементов
        """
        self.repository = repository
    
    def get_all_items(self) -> Dict:
        """
        Получить все элементы.
        
        Returns:
            dict: Словарь с элементами и количеством
        """
        items = self.repository.get_all()
        return {"items": items, "count": len(items)}
    
    def get_item_by_id(self, item_id: int) -> Optional[Dict]:
        """
        Получить элемент по ID.
        
        Args:
            item_id: ID элемента
        
        Returns:
            dict или None: Элемент или None если не найден
        """
        return self.repository.get_by_id(item_id)
    
    def create_item(self, item: Item) -> Dict:
        """
        Создать новый элемент.
        
        Args:
            item: Модель элемента
        
        Returns:
            dict: Созданный элемент
        """
        item_data = {
            "name": item.name,
            "description": item.description,
            "price": item.price
        }
        created_item = self.repository.create(item_data)
        return {
            "id": created_item["id"],
            "name": created_item["name"],
            "description": created_item["description"],
            "price": created_item["price"],
            "message": "Item created successfully"
        }

