"""
Pydantic схемы для продуктов.
"""

from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    """Схема для создания продукта."""
    name: str
    description: Optional[str] = None
    price: float


class ProductResponse(BaseModel):
    """Схема для ответа с продуктом."""
    id: int
    name: str
    description: Optional[str]
    price: float
    
    class Config:
        from_attributes = True  # Для SQLAlchemy 2.0

