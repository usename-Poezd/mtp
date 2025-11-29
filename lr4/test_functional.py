"""
Unit-тесты для функционального программирования.
"""

import unittest
import time
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


class TestApplyMultipleFunctions(unittest.TestCase):
    """Тесты для применения нескольких функций через map."""
    
    def test_multiple_functions(self):
        """Тест применения нескольких функций к списку."""
        numbers = [1, 2, 3, 4, 5]
        results = apply_multiple_functions(
            numbers,
            lambda x: x * 2,
            lambda x: x ** 2,
            lambda x: x + 10
        )
        
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0], [2, 4, 6, 8, 10])
        self.assertEqual(results[1], [1, 4, 9, 16, 25])
        self.assertEqual(results[2], [11, 12, 13, 14, 15])
    
    def test_single_function(self):
        """Тест применения одной функции."""
        numbers = [1, 2, 3]
        results = apply_multiple_functions(numbers, lambda x: x * 2)
        self.assertEqual(results, [[2, 4, 6]])
    
    def test_empty_list(self):
        """Тест с пустым списком."""
        results = apply_multiple_functions([], lambda x: x * 2)
        self.assertEqual(results, [[]])


class TestFilterEvenNumbers(unittest.TestCase):
    """Тесты для фильтрации чётных чисел."""
    
    def test_filter_even(self):
        """Тест фильтрации чётных чисел."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = filter_even_numbers(numbers)
        self.assertEqual(result, [2, 4, 6, 8, 10])
    
    def test_all_odd(self):
        """Тест со списком только нечётных чисел."""
        numbers = [1, 3, 5, 7, 9]
        result = filter_even_numbers(numbers)
        self.assertEqual(result, [])
    
    def test_all_even(self):
        """Тест со списком только чётных чисел."""
        numbers = [2, 4, 6, 8, 10]
        result = filter_even_numbers(numbers)
        self.assertEqual(result, numbers)
    
    def test_empty_list(self):
        """Тест с пустым списком."""
        result = filter_even_numbers([])
        self.assertEqual(result, [])


class TestTimingDecorator(unittest.TestCase):
    """Тесты для декоратора замера времени."""
    
    def test_timing_decorator(self):
        """Тест декоратора замера времени."""
        @timing_decorator
        def test_function():
            time.sleep(0.01)
            return "test_result"
        
        result = test_function()
        
        self.assertIn('result', result)
        self.assertIn('execution_time', result)
        self.assertIn('function_name', result)
        self.assertEqual(result['result'], "test_result")
        self.assertEqual(result['function_name'], "test_function")
        self.assertGreater(result['execution_time'], 0)
    
    def test_timing_with_args(self):
        """Тест декоратора с аргументами."""
        @timing_decorator
        def add(a, b):
            return a + b
        
        result = add(5, 3)
        self.assertEqual(result['result'], 8)
    
    def test_timing_with_kwargs(self):
        """Тест декоратора с именованными аргументами."""
        @timing_decorator
        def multiply(x, y):
            return x * y
        
        result = multiply(x=4, y=5)
        self.assertEqual(result['result'], 20)


class TestCustomReduce(unittest.TestCase):
    """Тесты для собственной реализации reduce."""
    
    def test_sum(self):
        """Тест суммирования."""
        numbers = [1, 2, 3, 4, 5]
        result = custom_reduce(lambda x, y: x + y, numbers)
        self.assertEqual(result, 15)
    
    def test_product(self):
        """Тест умножения."""
        numbers = [1, 2, 3, 4]
        result = custom_reduce(lambda x, y: x * y, numbers)
        self.assertEqual(result, 24)
    
    def test_with_initializer(self):
        """Тест с начальным значением."""
        numbers = [1, 2, 3, 4]
        result = custom_reduce(lambda x, y: x * y, numbers, 10)
        self.assertEqual(result, 240)
    
    def test_max(self):
        """Тест поиска максимума."""
        numbers = [3, 7, 2, 9, 1, 5]
        result = custom_reduce(lambda x, y: x if x > y else y, numbers)
        self.assertEqual(result, 9)
    
    def test_string_concatenation(self):
        """Тест конкатенации строк."""
        words = ['Hello', ' ', 'World', '!']
        result = custom_reduce(lambda x, y: x + y, words)
        self.assertEqual(result, "Hello World!")
    
    def test_empty_list_with_initializer(self):
        """Тест пустого списка с начальным значением."""
        result = custom_reduce(lambda x, y: x + y, [], 10)
        self.assertEqual(result, 10)
    
    def test_empty_list_without_initializer(self):
        """Тест пустого списка без начального значения."""
        with self.assertRaises(TypeError):
            custom_reduce(lambda x, y: x + y, [])


class TestCurry(unittest.TestCase):
    """Тесты для функции-карринг."""
    
    def test_curry_two_args(self):
        """Тест каррирования функции с двумя аргументами."""
        def add(a, b):
            return a + b
        
        curried_add = curry(add)
        result = curried_add(5)(3)
        self.assertEqual(result, 8)
    
    def test_curry_three_args(self):
        """Тест каррирования функции с тремя аргументами."""
        def multiply_three(a, b, c):
            return a * b * c
        
        curried_mult = curry(multiply_three)
        result = curried_mult(2)(3)(4)
        self.assertEqual(result, 24)
    
    def test_curry_partial_application(self):
        """Тест частичного применения."""
        def add_three(a, b, c):
            return a + b + c
        
        curried = curry(add_three)
        partial = curried(1)(2)
        result = partial(3)
        self.assertEqual(result, 6)
    
    def test_curry_with_kwargs(self):
        """Тест каррирования с именованными аргументами."""
        def power(base, exponent):
            return base ** exponent
        
        curried_power = curry(power)
        result = curried_power(2)(exponent=3)
        self.assertEqual(result, 8)


class TestCompose(unittest.TestCase):
    """Тесты для композиции функций."""
    
    def test_compose_two_functions(self):
        """Тест композиции двух функций."""
        def double(x):
            return x * 2
        
        def square(x):
            return x ** 2
        
        composed = compose(square, double)
        # double(3) = 6, square(6) = 36
        self.assertEqual(composed(3), 36)
    
    def test_compose_three_functions(self):
        """Тест композиции трёх функций."""
        def add_one(x):
            return x + 1
        
        def double(x):
            return x * 2
        
        def square(x):
            return x ** 2
        
        composed = compose(square, double, add_one)
        # add_one(2) = 3, double(3) = 6, square(6) = 36
        self.assertEqual(composed(2), 36)


class TestGenerators(unittest.TestCase):
    """Тесты для генераторов."""
    
    def test_generator_squares(self):
        """Тест генератора квадратов."""
        gen = generator_squares(5)
        result = list(gen)
        self.assertEqual(result, [0, 1, 4, 9, 16, 25])
    
    def test_generator_fibonacci(self):
        """Тест генератора Фибоначчи."""
        gen = generator_fibonacci(10)
        result = list(gen)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)
    
    def test_generator_empty(self):
        """Тест генератора с нулевым количеством."""
        gen = generator_squares(0)
        result = list(gen)
        self.assertEqual(result, [0])


if __name__ == '__main__':
    unittest.main()

