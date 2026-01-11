"""
Конфигурация FastAPI приложения с БД.
"""

import os


class Config:
    """Конфигурация приложения."""
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://user:password@localhost:5432/lab6db"
    )
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8001))
    TITLE = "FastAPI with Database"
    VERSION = "1.0.0"

