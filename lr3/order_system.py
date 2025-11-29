"""
Система заказов: классы «Товар» и «Корзина».
"""


class Product:
    """Класс для представления товара."""
    
    def __init__(self, name, price, quantity=1):
        """
        Инициализация товара.
        
        Args:
            name: Название товара
            price: Цена товара
            quantity: Количество товара (по умолчанию 1)
        """
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_price(self):
        """
        Возвращает общую стоимость товара (цена * количество).
        
        Returns:
            float: Общая стоимость
        """
        return self.price * self.quantity
    
    def __str__(self):
        """Строковое представление товара."""
        return f"{self.name} - {self.price} руб. (x{self.quantity})"
    
    def __repr__(self):
        """Официальное строковое представление."""
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


class Cart:
    """Класс для представления корзины покупок."""
    
    def __init__(self):
        """Инициализация пустой корзины."""
        self.items = []
    
    def add_product(self, product):
        """
        Добавляет товар в корзину.
        
        Args:
            product: Объект класса Product
        """
        if isinstance(product, Product):
            # Проверяем, есть ли уже такой товар в корзине
            for item in self.items:
                if item.name == product.name and item.price == product.price:
                    item.quantity += product.quantity
                    return
            
            # Если товара нет, добавляем новый
            self.items.append(product)
        else:
            raise TypeError("Можно добавить только объект класса Product")
    
    def remove_product(self, product_name):
        """
        Удаляет товар из корзины по названию.
        
        Args:
            product_name: Название товара для удаления
        
        Returns:
            bool: True если товар был удалён, False если не найден
        """
        for i, item in enumerate(self.items):
            if item.name == product_name:
                del self.items[i]
                return True
        return False
    
    def update_quantity(self, product_name, new_quantity):
        """
        Обновляет количество товара в корзине.
        
        Args:
            product_name: Название товара
            new_quantity: Новое количество
        
        Returns:
            bool: True если количество обновлено, False если товар не найден
        """
        for item in self.items:
            if item.name == product_name:
                if new_quantity <= 0:
                    self.remove_product(product_name)
                else:
                    item.quantity = new_quantity
                return True
        return False
    
    def get_total(self):
        """
        Возвращает общую стоимость всех товаров в корзине.
        
        Returns:
            float: Общая стоимость корзины
        """
        return sum(item.get_total_price() for item in self.items)
    
    def get_items_count(self):
        """
        Возвращает общее количество товаров в корзине.
        
        Returns:
            int: Общее количество товаров
        """
        return sum(item.quantity for item in self.items)
    
    def clear(self):
        """Очищает корзину."""
        self.items = []
    
    def display(self):
        """
        Выводит информацию о содержимом корзины.
        
        Returns:
            str: Строка с информацией о корзине
        """
        if not self.items:
            return "Корзина пуста"
        
        result = "Содержимое корзины:\n"
        for item in self.items:
            result += f"  - {item}\n"
        result += f"\nИтого товаров: {self.get_items_count()}"
        result += f"\nОбщая стоимость: {self.get_total():.2f} руб."
        
        return result
    
    def __str__(self):
        """Строковое представление корзины."""
        return f"Cart({len(self.items)} товаров, сумма: {self.get_total():.2f} руб.)"
    
    def __repr__(self):
        """Официальное строковое представление."""
        return f"Cart(items={self.items})"

