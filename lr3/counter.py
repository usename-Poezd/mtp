"""
Класс-счётчик для увеличения/уменьшения значения.
"""


class Counter:
    """Класс-счётчик с методами увеличения и уменьшения."""
    
    def __init__(self, initial_value=0, min_value=None, max_value=None):
        """
        Инициализация счётчика.
        
        Args:
            initial_value: Начальное значение счётчика
            min_value: Минимальное значение (None - без ограничения)
            max_value: Максимальное значение (None - без ограничения)
        """
        self._value = initial_value
        self.min_value = min_value
        self.max_value = max_value
    
    def increment(self, step=1):
        """
        Увеличивает значение счётчика.
        
        Args:
            step: Шаг увеличения (по умолчанию 1)
        
        Returns:
            int: Новое значение счётчика
        """
        new_value = self._value + step
        
        if self.max_value is not None and new_value > self.max_value:
            self._value = self.max_value
        else:
            self._value = new_value
        
        return self._value
    
    def decrement(self, step=1):
        """
        Уменьшает значение счётчика.
        
        Args:
            step: Шаг уменьшения (по умолчанию 1)
        
        Returns:
            int: Новое значение счётчика
        """
        new_value = self._value - step
        
        if self.min_value is not None and new_value < self.min_value:
            self._value = self.min_value
        else:
            self._value = new_value
        
        return self._value
    
    def reset(self):
        """Сбрасывает счётчик в начальное значение."""
        self._value = 0
        return self._value
    
    def get_value(self):
        """
        Возвращает текущее значение счётчика.
        
        Returns:
            int: Текущее значение
        """
        return self._value
    
    def __str__(self):
        """Строковое представление счётчика."""
        return f"Counter(value={self._value})"
    
    def __repr__(self):
        """Официальное строковое представление."""
        return f"Counter(value={self._value}, min={self.min_value}, max={self.max_value})"

