"""
HTTP обработчик для Flask приложения.
"""

from flask import Flask, request, render_template
from services.greeting_service import GreetingService
from services.table_service import TableService


class HttpHandler:
    """HTTP обработчик, организует роутинг."""
    
    def __init__(self, greeting_service: GreetingService, table_service: TableService):
        """
        Инициализация обработчика.
        
        Args:
            greeting_service: Сервис для приветствий
            table_service: Сервис для таблицы
        """
        self.greeting_service = greeting_service
        self.table_service = table_service
    
    def register_routes(self, app: Flask):
        """Регистрация маршрутов."""
        @app.route('/')
        def index():
            return render_template('index.html')
        
        @app.route('/greeting', methods=['GET', 'POST'])
        def greeting():
            if request.method == 'POST':
                name = request.form.get('name', '').strip()
                is_valid, error = self.greeting_service.validate_name(name)
                
                if not is_valid:
                    return render_template('greeting_form.html', error=error)
                
                greeting_name = self.greeting_service.process_greeting(name)
                return render_template('greeting.html', name=greeting_name)
            
            error = request.args.get('error')
            return render_template('greeting_form.html', error=error)
        
        @app.route('/table')
        def table():
            data = self.table_service.get_table_data()
            return render_template('table.html', data=data)

