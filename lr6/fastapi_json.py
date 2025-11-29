"""
FastAPI endpoint возвращает JSON.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="FastAPI JSON Endpoints", version="1.0.0")


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


@app.get("/")
def read_root():
    """Корневой endpoint."""
    return JSONResponse(content={
        "message": "FastAPI приложение с JSON endpoints",
        "endpoints": [
            "/api/items - Получить список элементов",
            "/api/items/{item_id} - Получить элемент по ID",
            "POST /api/items - Создать элемент"
        ]
    })


@app.get("/api/items")
def get_items():
    """Endpoint возвращает JSON с элементами."""
    items = [
        {"id": 1, "name": "Ноутбук", "description": "Игровой ноутбук", "price": 75000},
        {"id": 2, "name": "Мышь", "description": "Игровая мышь", "price": 2500},
        {"id": 3, "name": "Клавиатура", "description": "Механическая клавиатура", "price": 5000},
    ]
    return JSONResponse(content={"items": items, "count": len(items)})


@app.get("/api/items/{item_id}")
def get_item(item_id: int):
    """Получить элемент по ID."""
    items = {
        1: {"id": 1, "name": "Ноутбук", "description": "Игровой ноутбук", "price": 75000},
        2: {"id": 2, "name": "Мышь", "description": "Игровая мышь", "price": 2500},
        3: {"id": 3, "name": "Клавиатура", "description": "Механическая клавиатура", "price": 5000},
    }
    if item_id in items:
        return JSONResponse(content=items[item_id])
    return JSONResponse(content={"error": "Item not found"}, status_code=404)


@app.post("/api/items")
def create_item(item: Item):
    """Создать новый элемент."""
    return JSONResponse(content={
        "id": 4,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "message": "Item created successfully"
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

