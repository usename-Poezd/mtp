"""
Сервис для работы с таблицей данных.
"""

from repositories.data_repository import DataRepository


class TableService:
    """Сервис для таблицы данных."""
    
    def __init__(self, repository: DataRepository):
        """
        Инициализация сервиса.
        
        Args:
            repository: Репозиторий данных
        """
        self.repository = repository
    
    def get_table_data(self):
        """
        Получить данные для таблицы.
        
        Returns:
            list: Список данных для таблицы
        """
        return self.repository.get_table_data()

