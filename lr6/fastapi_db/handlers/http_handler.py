"""
HTTP обработчик для FastAPI приложения с БД.
"""

"""
HTTP обработчик для FastAPI приложения с БД.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Callable
from services.product_service import ProductService
from models.schemas import ProductCreate, ProductResponse
from config.database import get_db


class HttpHandler:
    """HTTP обработчик, организует роутинг."""
    
    def __init__(self, service_factory: Callable[[Session], ProductService]):
        """
        Инициализация обработчика.
        
        Args:
            service_factory: Функция для создания ProductService с сессией БД
        """
        self.service_factory = service_factory
        self.router = APIRouter()
        self._register_routes()
    
    def _register_routes(self):
        """Регистрация маршрутов."""
        @self.router.get("/api/products", response_model=List[ProductResponse])
        def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
            service = self.service_factory(db)
            return service.get_all_products(skip, limit)
        
        @self.router.get("/api/products/{product_id}", response_model=ProductResponse)
        def get_product(product_id: int, db: Session = Depends(get_db)):
            from fastapi import HTTPException
            service = self.service_factory(db)
            product = service.get_product_by_id(product_id)
            if not product:
                raise HTTPException(status_code=404, detail="Product not found")
            return product
        
        @self.router.post("/api/products", response_model=ProductResponse)
        def create_product(product: ProductCreate, db: Session = Depends(get_db)):
            service = self.service_factory(db)
            return service.create_product(product)
        
        @self.router.delete("/api/products/{product_id}")
        def delete_product(product_id: int, db: Session = Depends(get_db)):
            from fastapi import HTTPException
            service = self.service_factory(db)
            success = service.delete_product(product_id)
            if not success:
                raise HTTPException(status_code=404, detail="Product not found")
            return {"message": "Product deleted successfully"}

