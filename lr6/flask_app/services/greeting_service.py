"""
Сервис для обработки приветствий.
"""


class GreetingService:
    """Сервис для работы с приветствиями."""
    
    def validate_name(self, name: str) -> tuple[bool, str]:
        """
        Валидация имени.
        
        Args:
            name: Имя для валидации
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not name or not name.strip():
            return False, 'Пожалуйста, введите имя!'
        return True, ''
    
    def process_greeting(self, name: str) -> str:
        """
        Обработать имя для приветствия.
        
        Args:
            name: Имя пользователя
        
        Returns:
            str: Обработанное имя
        """
        return name.strip()

