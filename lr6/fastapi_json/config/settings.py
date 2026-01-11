"""
Конфигурация FastAPI JSON приложения.
"""

import os


class Config:
    """Конфигурация приложения."""
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8000))
    TITLE = "FastAPI JSON Endpoints"
    VERSION = "1.0.0"

