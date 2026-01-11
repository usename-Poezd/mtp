"""
Конфигурация FastAPI WebSocket приложения.
"""

import os


class Config:
    """Конфигурация приложения."""
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8002))
    TITLE = "FastAPI WebSocket Chat"
    VERSION = "1.0.0"
    MAX_MESSAGE_HISTORY = 10

