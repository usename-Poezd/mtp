"""
Точка входа Flask приложения.
"""

from flask import Flask
from config.settings import Config
from repositories.data_repository import DataRepository
from services.greeting_service import GreetingService
from services.table_service import TableService
from handlers.http_handler import HttpHandler


def create_app():
    """Создать и настроить Flask приложение."""
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)
    
    # Инициализация слоев (снизу вверх)
    # 1. Repositories
    data_repository = DataRepository()
    
    # 2. Services (зависят от repositories)
    greeting_service = GreetingService()
    table_service = TableService(data_repository)
    
    # 3. Handlers (зависят от services)
    http_handler = HttpHandler(greeting_service, table_service)
    
    # Регистрация маршрутов
    http_handler.register_routes(app)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        debug=app.config['DEBUG'],
        host=app.config['HOST'],
        port=app.config['PORT']
    )

