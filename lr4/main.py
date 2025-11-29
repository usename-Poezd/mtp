# лаба 4 функциональное программирование
from functools import reduce
import time
from datetime import datetime

# задание 1: отфильтровать четные числа из списка (функциональный стиль)
def filter_even_numbers(numbers):
    # используем filter и лямбда-функцию
    return list(filter(lambda x: x % 2 == 0, numbers))


# задание 2: факториал через reduce (функциональный стиль)
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    # используем reduce для умножения чисел от 1 до n
    return reduce(lambda x, y: x * y, range(1, n + 1))


# задание 3: декоратор для логирования вызова функции
def log_decorator(func):
    def wrapper(*args, **kwargs):
        # логируем вызов
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Вызов функции: {func.__name__}")
        print(f"  Аргументы: args={args}, kwargs={kwargs}")
        
        # вызываем функцию
        result = func(*args, **kwargs)
        
        # логируем результат
        print(f"  Результат: {result}")
        return result
    
    return wrapper


# задание 4: мемоизация функции через декоратор
def memoize(func):
    # словарь для хранения результатов
    cache = {}
    
    def wrapper(*args):
        # проверяем есть ли результат в кеше
        if args in cache:
            print(f"Результат для {args} взят из кеша")
            return cache[args]
        
        # вычисляем и сохраняем
        result = func(*args)
        cache[args] = result
        print(f"Результат для {args} вычислен и сохранен в кеш")
        return result
    
    return wrapper


# задание 5: декоратор с параметрами
def repeat_decorator(times=1):
    # декоратор который принимает параметр
    def decorator(func):
        def wrapper(*args, **kwargs):
            # используем map для выполнения функции N раз
            results = list(map(lambda _: func(*args, **kwargs), range(times)))
            # выводим информацию о вызовах
            for i in range(times):
                print(f"Вызов {i + 1} из {times}")
            return results if times > 1 else results[0]
        return wrapper
    return decorator


# примеры использования

# задание 1
print("=" * 50)
print("Задание 1: Фильтрация четных чисел (функциональный стиль)")
print("=" * 50)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter_even_numbers(numbers)
print(f"Исходный список: {numbers}")
print(f"Четные числа: {even}")

# дополнительно: фильтрация через list comprehension
even_lc = [x for x in numbers if x % 2 == 0]
print(f"Четные числа (list comprehension): {even_lc}")
print()

# задание 2
print("=" * 50)
print("Задание 2: Факториал через reduce")
print("=" * 50)
factorials = list(map(factorial, [0, 1, 5, 7, 10]))
for i, n in enumerate([0, 1, 5, 7, 10]):
    print(f"Факториал {n} = {factorials[i]}")
print()

# задание 3
print("=" * 50)
print("Задание 3: Декоратор логирования")
print("=" * 50)

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def multiply(x, y):
    return x * y

result1 = add(5, 3)
print()
result2 = multiply(4, 7)
print()

# задание 4
print("=" * 50)
print("Задание 4: Мемоизация")
print("=" * 50)

@memoize
def slow_fibonacci(n):
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

print("Первый вызов (вычисление):")
fib1 = slow_fibonacci(5)
print(f"Результат: {fib1}")
print()

print("Второй вызов (из кеша):")
fib2 = slow_fibonacci(5)
print(f"Результат: {fib2}")
print()

# задание 5
print("=" * 50)
print("Задание 5: Декоратор с параметрами")
print("=" * 50)

@repeat_decorator(times=3)
def greet(name):
    return f"Привет, {name}!"

@repeat_decorator(times=2)
def square(x):
    return x * x

print("Функция greet с repeat_decorator(times=3):")
result = greet("Мир")
print(f"Результат: {result}")
print()

print("Функция square с repeat_decorator(times=2):")
result = square(5)
print(f"Результат: {result}")
print()

# дополнительные примеры функционального стиля
print("=" * 50)
print("Дополнительные примеры функционального стиля")
print("=" * 50)

# map для преобразования
squares = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(f"Квадраты чисел [1,2,3,4,5]: {squares}")

# filter для фильтрации
positive = list(filter(lambda x: x > 0, [-2, -1, 0, 1, 2, 3]))
print(f"Положительные числа [-2,-1,0,1,2,3]: {positive}")

# reduce для суммирования
sum_numbers = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(f"Сумма [1,2,3,4,5]: {sum_numbers}")

# комбинация map и filter
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1, 11))))
print(f"Квадраты четных чисел от 1 до 10: {even_squares}")
