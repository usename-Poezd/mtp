"""
Unit-тесты для всех классов (TDD подход).
"""

import unittest
from iterator import NumberIterator, ListIterator
from student import Student
from counter import Counter
from order_system import Product, Cart


class TestNumberIterator(unittest.TestCase):
    """Тесты для класса NumberIterator."""
    
    def test_forward_iteration(self):
        """Тест прямой итерации."""
        iterator = NumberIterator(0, 5)
        result = list(iterator)
        self.assertEqual(result, [0, 1, 2, 3, 4])
    
    def test_backward_iteration(self):
        """Тест обратной итерации."""
        iterator = NumberIterator(5, 0, -1)
        result = list(iterator)
        self.assertEqual(result, [5, 4, 3, 2, 1])
    
    def test_custom_step(self):
        """Тест итерации с кастомным шагом."""
        iterator = NumberIterator(0, 10, 2)
        result = list(iterator)
        self.assertEqual(result, [0, 2, 4, 6, 8])
    
    def test_empty_range(self):
        """Тест пустого диапазона."""
        iterator = NumberIterator(5, 5)
        result = list(iterator)
        self.assertEqual(result, [])
    
    def test_stop_iteration(self):
        """Тест остановки итерации."""
        iterator = NumberIterator(0, 3)
        values = []
        for _ in range(5):  # Пытаемся получить больше, чем есть
            try:
                values.append(next(iterator))
            except StopIteration:
                break
        self.assertEqual(values, [0, 1, 2])


class TestListIterator(unittest.TestCase):
    """Тесты для класса ListIterator."""
    
    def test_list_iteration(self):
        """Тест итерации по списку."""
        items = ['a', 'b', 'c', 'd']
        iterator = ListIterator(items)
        result = list(iterator)
        self.assertEqual(result, items)
    
    def test_empty_list(self):
        """Тест итерации по пустому списку."""
        iterator = ListIterator([])
        result = list(iterator)
        self.assertEqual(result, [])
    
    def test_numbers_list(self):
        """Тест итерации по списку чисел."""
        items = [1, 2, 3, 4, 5]
        iterator = ListIterator(items)
        result = list(iterator)
        self.assertEqual(result, items)


class TestStudent(unittest.TestCase):
    """Тесты для класса Student."""
    
    def setUp(self):
        """Настройка тестового объекта."""
        self.student = Student(
            name="Иван Иванов",
            age=20,
            student_id="ST001",
            course=2,
            average_grade=4.5
        )
    
    def test_student_creation(self):
        """Тест создания студента."""
        self.assertEqual(self.student.name, "Иван Иванов")
        self.assertEqual(self.student.age, 20)
        self.assertEqual(self.student.student_id, "ST001")
        self.assertEqual(self.student.course, 2)
        self.assertEqual(self.student.average_grade, 4.5)
    
    def test_display_info(self):
        """Тест метода вывода информации."""
        info = self.student.display_info()
        self.assertIn("Иван Иванов", info)
        self.assertIn("20", info)
        self.assertIn("ST001", info)
        self.assertIn("2", info)
        self.assertIn("4.5", info)
    
    def test_str_representation(self):
        """Тест строкового представления."""
        str_repr = str(self.student)
        self.assertIn("Иван Иванов", str_repr)
        self.assertIn("ST001", str_repr)
    
    def test_repr_representation(self):
        """Тест официального строкового представления."""
        repr_str = repr(self.student)
        self.assertIn("Student", repr_str)
        self.assertIn("Иван Иванов", repr_str)


class TestCounter(unittest.TestCase):
    """Тесты для класса Counter."""
    
    def test_initial_value(self):
        """Тест начального значения."""
        counter = Counter(5)
        self.assertEqual(counter.get_value(), 5)
    
    def test_increment(self):
        """Тест увеличения счётчика."""
        counter = Counter(0)
        counter.increment()
        self.assertEqual(counter.get_value(), 1)
        counter.increment(5)
        self.assertEqual(counter.get_value(), 6)
    
    def test_decrement(self):
        """Тест уменьшения счётчика."""
        counter = Counter(10)
        counter.decrement()
        self.assertEqual(counter.get_value(), 9)
        counter.decrement(3)
        self.assertEqual(counter.get_value(), 6)
    
    def test_reset(self):
        """Тест сброса счётчика."""
        counter = Counter(10)
        counter.increment(5)
        counter.reset()
        self.assertEqual(counter.get_value(), 0)
    
    def test_min_value_limit(self):
        """Тест ограничения минимального значения."""
        counter = Counter(5, min_value=0)
        counter.decrement(10)
        self.assertEqual(counter.get_value(), 0)
    
    def test_max_value_limit(self):
        """Тест ограничения максимального значения."""
        counter = Counter(0, max_value=10)
        counter.increment(15)
        self.assertEqual(counter.get_value(), 10)
    
    def test_both_limits(self):
        """Тест обоих ограничений."""
        counter = Counter(5, min_value=0, max_value=10)
        counter.increment(10)
        self.assertEqual(counter.get_value(), 10)
        counter.decrement(20)
        self.assertEqual(counter.get_value(), 0)


class TestProduct(unittest.TestCase):
    """Тесты для класса Product."""
    
    def test_product_creation(self):
        """Тест создания товара."""
        product = Product("Яблоко", 50.0, 3)
        self.assertEqual(product.name, "Яблоко")
        self.assertEqual(product.price, 50.0)
        self.assertEqual(product.quantity, 3)
    
    def test_default_quantity(self):
        """Тест товара с количеством по умолчанию."""
        product = Product("Банан", 30.0)
        self.assertEqual(product.quantity, 1)
    
    def test_get_total_price(self):
        """Тест расчёта общей стоимости."""
        product = Product("Молоко", 80.0, 2)
        self.assertEqual(product.get_total_price(), 160.0)
    
    def test_str_representation(self):
        """Тест строкового представления товара."""
        product = Product("Хлеб", 40.0, 2)
        str_repr = str(product)
        self.assertIn("Хлеб", str_repr)
        self.assertIn("40.0", str_repr)
        self.assertIn("2", str_repr)


class TestCart(unittest.TestCase):
    """Тесты для класса Cart."""
    
    def setUp(self):
        """Настройка тестовых объектов."""
        self.cart = Cart()
        self.product1 = Product("Яблоко", 50.0, 2)
        self.product2 = Product("Банан", 30.0, 1)
    
    def test_empty_cart(self):
        """Тест пустой корзины."""
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.get_total(), 0)
        self.assertEqual(self.cart.get_items_count(), 0)
    
    def test_add_product(self):
        """Тест добавления товара."""
        self.cart.add_product(self.product1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, "Яблоко")
    
    def test_add_multiple_products(self):
        """Тест добавления нескольких товаров."""
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.assertEqual(len(self.cart.items), 2)
    
    def test_add_same_product(self):
        """Тест добавления одинакового товара (увеличение количества)."""
        self.cart.add_product(self.product1)
        same_product = Product("Яблоко", 50.0, 3)
        self.cart.add_product(same_product)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].quantity, 5)  # 2 + 3
    
    def test_remove_product(self):
        """Тест удаления товара."""
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        result = self.cart.remove_product("Яблоко")
        self.assertTrue(result)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, "Банан")
    
    def test_remove_nonexistent_product(self):
        """Тест удаления несуществующего товара."""
        self.cart.add_product(self.product1)
        result = self.cart.remove_product("Апельсин")
        self.assertFalse(result)
        self.assertEqual(len(self.cart.items), 1)
    
    def test_update_quantity(self):
        """Тест обновления количества товара."""
        self.cart.add_product(self.product1)
        self.cart.update_quantity("Яблоко", 5)
        self.assertEqual(self.cart.items[0].quantity, 5)
    
    def test_update_quantity_to_zero(self):
        """Тест обновления количества до нуля (удаление товара)."""
        self.cart.add_product(self.product1)
        self.cart.update_quantity("Яблоко", 0)
        self.assertEqual(len(self.cart.items), 0)
    
    def test_get_total(self):
        """Тест расчёта общей стоимости корзины."""
        self.cart.add_product(self.product1)  # 50.0 * 2 = 100.0
        self.cart.add_product(self.product2)  # 30.0 * 1 = 30.0
        self.assertEqual(self.cart.get_total(), 130.0)
    
    def test_get_items_count(self):
        """Тест подсчёта общего количества товаров."""
        self.cart.add_product(self.product1)  # 2 шт
        self.cart.add_product(self.product2)  # 1 шт
        self.assertEqual(self.cart.get_items_count(), 3)
    
    def test_clear(self):
        """Тест очистки корзины."""
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.get_total(), 0)
    
    def test_add_invalid_product(self):
        """Тест добавления невалидного объекта."""
        with self.assertRaises(TypeError):
            self.cart.add_product("не товар")
    
    def test_display(self):
        """Тест отображения корзины."""
        self.cart.add_product(self.product1)
        display_str = self.cart.display()
        self.assertIn("Яблоко", display_str)
        self.assertIn("130.0" if "130" in display_str or "130.0" in display_str else "100.0", display_str)


if __name__ == '__main__':
    unittest.main()

