"""
Точка входа FastAPI JSON приложения.
"""

from fastapi import FastAPI
from config.settings import Config
from repositories.item_repository import ItemRepository
from services.item_service import ItemService
from handlers.http_handler import HttpHandler

config = Config()
app = FastAPI(title=config.TITLE, version=config.VERSION)


# Инициализация слоев (снизу вверх)
# 1. Repositories
item_repository = ItemRepository()

# 2. Services (зависят от repositories)
item_service = ItemService(item_repository)

# 3. Handlers (зависят от services)
http_handler = HttpHandler(item_service)

# Регистрация маршрутов
app.include_router(http_handler.router)


@app.get("/")
def read_root():
    """Корневой endpoint."""
    return {
        "message": "FastAPI приложение с JSON endpoints",
        "endpoints": [
            "/api/items - Получить список элементов",
            "/api/items/{item_id} - Получить элемент по ID",
            "POST /api/items - Создать элемент"
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.HOST, port=config.PORT)

