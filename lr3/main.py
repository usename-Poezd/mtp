"""
Основной файл с примерами использования всех классов.
"""

from iterator import NumberIterator, ListIterator
from student import Student
from counter import Counter
from order_system import Product, Cart


def demo_iterator():
    """Демонстрация работы итераторов."""
    print("=" * 50)
    print("Демонстрация класса-итератора")
    print("=" * 50)
    
    # Итератор чисел
    print("\n1. Итератор чисел от 0 до 5:")
    num_iter = NumberIterator(0, 5)
    for num in num_iter:
        print(f"  {num}", end=" ")
    print()
    
    # Итератор с шагом
    print("\n2. Итератор чисел от 0 до 10 с шагом 2:")
    num_iter = NumberIterator(0, 10, 2)
    for num in num_iter:
        print(f"  {num}", end=" ")
    print()
    
    # Итератор списка
    print("\n3. Итератор списка:")
    list_iter = ListIterator(['яблоко', 'банан', 'апельсин'])
    for item in list_iter:
        print(f"  {item}", end=" ")
    print("\n")


def demo_student():
    """Демонстрация работы класса Студент."""
    print("=" * 50)
    print("Демонстрация класса Студент")
    print("=" * 50)
    
    student1 = Student(
        name="Иван Иванов",
        age=20,
        student_id="ST001",
        course=2,
        average_grade=4.5
    )
    
    student2 = Student(
        name="Мария Петрова",
        age=19,
        student_id="ST002",
        course=1,
        average_grade=4.8
    )
    
    print("\nСтудент 1:")
    print(student1.display_info())
    
    print("\nСтудент 2:")
    print(student2.display_info())
    
    print(f"\nСтроковое представление: {student1}")
    print(f"Официальное представление: {repr(student1)}\n")


def demo_counter():
    """Демонстрация работы класса-счётчика."""
    print("=" * 50)
    print("Демонстрация класса-счётчика")
    print("=" * 50)
    
    # Обычный счётчик
    print("\n1. Обычный счётчик:")
    counter1 = Counter(0)
    print(f"  Начальное значение: {counter1.get_value()}")
    counter1.increment()
    print(f"  После increment(): {counter1.get_value()}")
    counter1.increment(5)
    print(f"  После increment(5): {counter1.get_value()}")
    counter1.decrement(2)
    print(f"  После decrement(2): {counter1.get_value()}")
    
    # Счётчик с ограничениями
    print("\n2. Счётчик с ограничениями (0-10):")
    counter2 = Counter(5, min_value=0, max_value=10)
    print(f"  Начальное значение: {counter2.get_value()}")
    counter2.increment(10)
    print(f"  После increment(10): {counter2.get_value()} (ограничен максимумом)")
    counter2.decrement(20)
    print(f"  После decrement(20): {counter2.get_value()} (ограничен минимумом)")
    
    # Сброс
    print("\n3. Сброс счётчика:")
    counter1.reset()
    print(f"  После reset(): {counter1.get_value()}\n")


def demo_order_system():
    """Демонстрация работы системы заказов."""
    print("=" * 50)
    print("Демонстрация системы заказов")
    print("=" * 50)
    
    # Создание товаров
    product1 = Product("Яблоко", 50.0, 3)
    product2 = Product("Банан", 30.0, 2)
    product3 = Product("Молоко", 80.0, 1)
    
    print("\nСозданные товары:")
    print(f"  {product1}")
    print(f"  {product2}")
    print(f"  {product3}")
    
    # Создание корзины
    cart = Cart()
    
    print("\nДобавление товаров в корзину...")
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)
    
    print("\n" + cart.display())
    
    # Обновление количества
    print("\nОбновление количества товара 'Яблоко' до 5:")
    cart.update_quantity("Яблоко", 5)
    print(f"  Количество товаров: {cart.get_items_count()}")
    print(f"  Общая стоимость: {cart.get_total():.2f} руб.")
    
    # Удаление товара
    print("\nУдаление товара 'Банан':")
    cart.remove_product("Банан")
    print(f"  Количество товаров: {cart.get_items_count()}")
    print(f"  Общая стоимость: {cart.get_total():.2f} руб.")
    
    # Добавление того же товара (увеличение количества)
    print("\nДобавление ещё одного 'Молоко':")
    same_milk = Product("Молоко", 80.0, 1)
    cart.add_product(same_milk)
    print(f"  Количество товаров: {cart.get_items_count()}")
    print(f"  Общая стоимость: {cart.get_total():.2f} руб.")
    
    print("\n" + cart.display() + "\n")


def main():
    """Главная функция для запуска всех демонстраций."""
    demo_iterator()
    demo_student()
    demo_counter()
    demo_order_system()
    
    print("=" * 50)
    print("Для запуска тестов выполните: python test_classes.py")
    print("=" * 50)


if __name__ == '__main__':
    main()

