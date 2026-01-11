"""
Модели данных для элементов.
"""

from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    """Модель элемента."""
    name: str
    description: Optional[str] = None
    price: float

