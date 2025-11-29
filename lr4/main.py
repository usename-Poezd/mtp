"""
Основной файл с примерами использования функционального программирования.
"""

from functional_programming import (
    apply_multiple_functions,
    filter_even_numbers,
    timing_decorator,
    custom_reduce,
    curry,
    compose,
    generator_squares,
    generator_fibonacci
)
import time


def demo_map_multiple_functions():
    """Демонстрация применения нескольких функций через map."""
    print("=" * 60)
    print("1. Применение нескольких функций к списку через map")
    print("=" * 60)
    
    numbers = [1, 2, 3, 4, 5]
    print(f"\nИсходный список: {numbers}")
    
    # Применяем несколько функций
    results = apply_multiple_functions(
        numbers,
        lambda x: x * 2,      # Удвоение
        lambda x: x ** 2,     # Возведение в квадрат
        lambda x: x + 10,     # Добавление 10
        lambda x: x - 1       # Вычитание 1
    )
    
    print("\nРезультаты применения функций:")
    print(f"  Удвоение (x * 2):        {results[0]}")
    print(f"  Квадрат (x ** 2):        {results[1]}")
    print(f"  Добавление 10 (x + 10):  {results[2]}")
    print(f"  Вычитание 1 (x - 1):     {results[3]}")
    print()


def demo_filter_even():
    """Демонстрация фильтрации чётных чисел."""
    print("=" * 60)
    print("2. Фильтрация чётных чисел из списка")
    print("=" * 60)
    
    numbers = list(range(1, 21))
    print(f"\nИсходный список (1-20): {numbers}")
    
    even_numbers = filter_even_numbers(numbers)
    print(f"Чётные числа: {even_numbers}")
    print()


def demo_timing_decorator():
    """Демонстрация декоратора замера времени."""
    print("=" * 60)
    print("3. Декоратор замера времени работы функции")
    print("=" * 60)
    
    @timing_decorator
    def fast_function():
        """Быстрая функция."""
        return sum(range(1000))
    
    @timing_decorator
    def slow_function():
        """Медленная функция."""
        time.sleep(0.1)
        return "Done"
    
    @timing_decorator
    def calculate_factorial(n):
        """Вычисление факториала."""
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    print("\nТест 1: Быстрая функция")
    result1 = fast_function()
    print(f"Результат: {result1['result']}")
    print(f"Время выполнения: {result1['execution_time']:.6f} секунд")
    
    print("\nТест 2: Медленная функция")
    result2 = slow_function()
    print(f"Результат: {result2['result']}")
    print(f"Время выполнения: {result2['execution_time']:.6f} секунд")
    
    print("\nТест 3: Факториал 10")
    result3 = calculate_factorial(10)
    print(f"Результат: {result3['result']}")
    print(f"Время выполнения: {result3['execution_time']:.6f} секунд")
    print()


def demo_custom_reduce():
    """Демонстрация собственной реализации reduce."""
    print("=" * 60)
    print("4. Собственная реализация reduce")
    print("=" * 60)
    
    numbers = [1, 2, 3, 4, 5]
    print(f"\nИсходный список: {numbers}")
    
    # Суммирование
    sum_result = custom_reduce(lambda x, y: x + y, numbers)
    print(f"Сумма: {sum_result}")
    
    # Умножение
    product_result = custom_reduce(lambda x, y: x * y, numbers)
    print(f"Произведение: {product_result}")
    
    # Максимум
    max_result = custom_reduce(lambda x, y: x if x > y else y, numbers)
    print(f"Максимум: {max_result}")
    
    # С начальным значением
    numbers2 = [1, 2, 3, 4]
    product_with_init = custom_reduce(lambda x, y: x * y, numbers2, 10)
    print(f"Произведение с начальным значением 10: {product_with_init}")
    
    # Конкатенация строк
    words = ['Hello', ' ', 'World', '!']
    concat_result = custom_reduce(lambda x, y: x + y, words)
    print(f"Конкатенация строк: '{concat_result}'")
    print()


def demo_curry():
    """Демонстрация функции-карринг."""
    print("=" * 60)
    print("5. Функция-карринг")
    print("=" * 60)
    
    # Пример 1: Простое сложение
    def add(a, b):
        return a + b
    
    curried_add = curry(add)
    print("\nПример 1: Каррированное сложение")
    result1 = curried_add(5)(3)
    print(f"curried_add(5)(3) = {result1}")
    
    # Пример 2: Умножение трёх чисел
    def multiply_three(a, b, c):
        return a * b * c
    
    curried_mult = curry(multiply_three)
    print("\nПример 2: Каррированное умножение трёх чисел")
    result2 = curried_mult(2)(3)(4)
    print(f"curried_mult(2)(3)(4) = {result2}")
    
    # Пример 3: Частичное применение
    def power(base, exponent):
        return base ** exponent
    
    curried_power = curry(power)
    square = curried_power(2)  # Частичное применение
    print("\nПример 3: Частичное применение (возведение в квадрат)")
    print(f"square(5) = {square(5)}")
    print(f"square(10) = {square(10)}")
    
    # Пример 4: Сложение трёх чисел
    def add_three(a, b, c):
        return a + b + c
    
    curried_add_three = curry(add_three)
    print("\nПример 4: Каррированное сложение трёх чисел")
    result4 = curried_add_three(1)(2)(3)
    print(f"curried_add_three(1)(2)(3) = {result4}")
    print()


def demo_compose():
    """Демонстрация композиции функций."""
    print("=" * 60)
    print("6. Композиция функций (бонус)")
    print("=" * 60)
    
    def double(x):
        return x * 2
    
    def square(x):
        return x ** 2
    
    def add_one(x):
        return x + 1
    
    # Композиция: сначала удваиваем, потом возводим в квадрат
    composed1 = compose(square, double)
    print(f"\ncompose(square, double)(3) = {composed1(3)}")
    print("  (double(3) = 6, square(6) = 36)")
    
    # Композиция трёх функций
    composed2 = compose(square, double, add_one)
    print(f"\ncompose(square, double, add_one)(2) = {composed2(2)}")
    print("  (add_one(2) = 3, double(3) = 6, square(6) = 36)")
    print()


def demo_generators():
    """Демонстрация генераторов."""
    print("=" * 60)
    print("7. Генераторы (бонус)")
    print("=" * 60)
    
    # Генератор квадратов
    print("\nГенератор квадратов (0-10):")
    squares_gen = generator_squares(10)
    squares_list = list(squares_gen)
    print(f"  {squares_list}")
    
    # Генератор Фибоначчи
    print("\nГенератор чисел Фибоначчи (первые 15):")
    fib_gen = generator_fibonacci(15)
    fib_list = list(fib_gen)
    print(f"  {fib_list}")
    
    # Использование генератора по одному элементу
    print("\nИспользование генератора по одному элементу:")
    fib_gen2 = generator_fibonacci(5)
    print("  ", end="")
    for num in fib_gen2:
        print(f"{num} ", end="")
    print()
    print()


def main():
    """Главная функция для запуска всех демонстраций."""
    demo_map_multiple_functions()
    demo_filter_even()
    demo_timing_decorator()
    demo_custom_reduce()
    demo_curry()
    demo_compose()
    demo_generators()
    
    print("=" * 60)
    print("Для запуска тестов выполните: python test_functional.py")
    print("=" * 60)


if __name__ == '__main__':
    main()

