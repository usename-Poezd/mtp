"""
Сервис для работы с продуктами.
"""

from typing import List, Optional
from repositories.product_repository import ProductRepository
from models.product_model import Product
from models.schemas import ProductCreate, ProductResponse


class ProductService:
    """Сервис для работы с продуктами."""
    
    def __init__(self, repository: ProductRepository):
        """
        Инициализация сервиса.
        
        Args:
            repository: Репозиторий продуктов
        """
        self.repository = repository
    
    def get_all_products(self, skip: int = 0, limit: int = 100) -> List[ProductResponse]:
        """
        Получить все продукты.
        
        Args:
            skip: Пропустить N записей
            limit: Максимальное количество записей
        
        Returns:
            List[ProductResponse]: Список продуктов
        """
        products = self.repository.get_all(skip, limit)
        return [ProductResponse.model_validate(p) for p in products]
    
    def get_product_by_id(self, product_id: int) -> Optional[ProductResponse]:
        """
        Получить продукт по ID.
        
        Args:
            product_id: ID продукта
        
        Returns:
            ProductResponse или None: Продукт или None если не найден
        """
        product = self.repository.get_by_id(product_id)
        if not product:
            return None
        return ProductResponse.model_validate(product)
    
    def create_product(self, product: ProductCreate) -> ProductResponse:
        """
        Создать новый продукт.
        
        Args:
            product: Данные продукта
        
        Returns:
            ProductResponse: Созданный продукт
        """
        product_data = {
            "name": product.name,
            "description": product.description,
            "price": product.price
        }
        created = self.repository.create(product_data)
        return ProductResponse.model_validate(created)
    
    def delete_product(self, product_id: int) -> bool:
        """
        Удалить продукт.
        
        Args:
            product_id: ID продукта
        
        Returns:
            bool: True если удален, False если не найден
        """
        product = self.repository.get_by_id(product_id)
        if not product:
            return False
        self.repository.delete(product)
        return True

