"""
FastAPI приложение с базой данных PostgreSQL.
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List, Optional
import os

# Настройки БД из переменных окружения
# Настройки БД из переменных окружения
# Используем psycopg (совместим с Python 3.13)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://user:password@localhost:5432/lab6db"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Модель БД
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)


# Pydantic модели
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    
    class Config:
        orm_mode = True


# Создание таблиц
Base.metadata.create_all(bind=engine)


# Dependency для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="FastAPI with Database", version="1.0.0")


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


@app.get("/api/products", response_model=List[ProductResponse])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить список всех продуктов."""
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


@app.get("/api/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """Получить продукт по ID."""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/api/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Создать новый продукт."""
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete("/api/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Удалить продукт."""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

