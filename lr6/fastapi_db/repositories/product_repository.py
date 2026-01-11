"""
Репозиторий для работы с продуктами в БД.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from models.product_model import Product


class ProductRepository:
    """Репозиторий для продуктов."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Product]:
        """Получить все продукты."""
        return self.db.query(Product).offset(skip).limit(limit).all()
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        """Получить продукт по ID."""
        return self.db.query(Product).filter(Product.id == product_id).first()
    
    def create(self, product_data: dict) -> Product:
        """Создать новый продукт."""
        product = Product(
            name=product_data["name"],
            description=product_data.get("description"),
            price=product_data["price"]
        )
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    def delete(self, product: Product) -> None:
        """Удалить продукт."""
        self.db.delete(product)
        self.db.commit()

