"""
Репозиторий для работы с элементами.
"""


class ItemRepository:
    """Репозиторий элементов."""
    
    _items = {
        1: {"id": 1, "name": "Ноутбук", "description": "Игровой ноутбук", "price": 75000},
        2: {"id": 2, "name": "Мышь", "description": "Игровая мышь", "price": 2500},
        3: {"id": 3, "name": "Клавиатура", "description": "Механическая клавиатура", "price": 5000},
    }
    
    @classmethod
    def get_all(cls):
        """Получить все элементы."""
        return list(cls._items.values())
    
    @classmethod
    def get_by_id(cls, item_id: int):
        """Получить элемент по ID."""
        return cls._items.get(item_id)
    
    @classmethod
    def create(cls, item_data: dict):
        """Создать новый элемент."""
        new_id = max(cls._items.keys()) + 1 if cls._items else 1
        item = {
            "id": new_id,
            "name": item_data["name"],
            "description": item_data.get("description"),
            "price": item_data["price"]
        }
        cls._items[new_id] = item
        return item

