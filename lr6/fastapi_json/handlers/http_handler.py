"""
HTTP обработчик для FastAPI JSON приложения.
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.item_service import ItemService
from models.item_model import Item


class HttpHandler:
    """HTTP обработчик, организует роутинг."""
    
    def __init__(self, item_service: ItemService):
        """
        Инициализация обработчика.
        
        Args:
            item_service: Сервис для работы с элементами
        """
        self.item_service = item_service
        self.router = APIRouter()
        self._register_routes()
    
    def _register_routes(self):
        """Регистрация маршрутов."""
        @self.router.get("/api/items")
        def get_items():
            result = self.item_service.get_all_items()
            return JSONResponse(content=result)
        
        @self.router.get("/api/items/{item_id}")
        def get_item(item_id: int):
            item = self.item_service.get_item_by_id(item_id)
            if not item:
                return JSONResponse(content={"error": "Item not found"}, status_code=404)
            return JSONResponse(content=item)
        
        @self.router.post("/api/items")
        def create_item(item: Item):
            result = self.item_service.create_item(item)
            return JSONResponse(content=result)

