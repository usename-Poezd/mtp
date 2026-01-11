"""
Точка входа FastAPI приложения с БД.
"""

from fastapi import FastAPI
from sqlalchemy.orm import Session
from config.settings import Config
from config.database import get_db, init_db
from repositories.product_repository import ProductRepository
from services.product_service import ProductService
from handlers.http_handler import HttpHandler

config = Config()
app = FastAPI(title=config.TITLE, version=config.VERSION)


def create_product_service(db: Session) -> ProductService:
    """Фабрика для создания ProductService."""
    repository = ProductRepository(db)
    return ProductService(repository)


# Инициализация БД при старте
@app.on_event("startup")
def startup_event():
    init_db()


# Инициализация обработчика
http_handler = HttpHandler(create_product_service)

# Регистрация маршрутов
app.include_router(http_handler.router)


@app.get("/")
def read_root():
    """Корневой endpoint."""
    return {
        "message": "FastAPI приложение с базой данных",
        "endpoints": [
            "/docs - Документация API",
            "/api/products - Получить все продукты",
            "/api/products/{product_id} - Получить продукт по ID",
            "POST /api/products - Создать продукт",
            "DELETE /api/products/{product_id} - Удалить продукт"
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.HOST, port=config.PORT)

