"""
Класс-итератор для последовательного перебора элементов.
"""


class NumberIterator:
    """Итератор для последовательности чисел."""
    
    def __init__(self, start, end, step=1):
        """
        Инициализация итератора.
        
        Args:
            start: Начальное значение
            end: Конечное значение (не включается)
            step: Шаг итерации
        """
        self.start = start
        self.end = end
        self.step = step
        self.current = start
    
    def __iter__(self):
        """Возвращает сам объект как итератор."""
        return self
    
    def __next__(self):
        """Возвращает следующее значение в последовательности."""
        if (self.step > 0 and self.current >= self.end) or \
           (self.step < 0 and self.current <= self.end):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value


class ListIterator:
    """Итератор для перебора элементов списка."""
    
    def __init__(self, items):
        """
        Инициализация итератора.
        
        Args:
            items: Список элементов для итерации
        """
        self.items = items
        self.index = 0
    
    def __iter__(self):
        """Возвращает сам объект как итератор."""
        return self
    
    def __next__(self):
        """Возвращает следующий элемент списка."""
        if self.index >= len(self.items):
            raise StopIteration
        
        value = self.items[self.index]
        self.index += 1
        return value

