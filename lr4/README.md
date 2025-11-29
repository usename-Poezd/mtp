# Лабораторная работа 4: Функциональное программирование в Python

## Описание

Данная лабораторная работа демонстрирует применение функционального стиля программирования в Python. Изучаются фильтрация, reduce, декораторы, мемоизация и декораторы с параметрами.

## Структура проекта

```
lr4/
├── main.py      # Все задания в одном файле
└── README.md    # Документация
```

## Выполненные задания

### 1. Отфильтровать чётные числа из списка

Функция `filter_even_numbers()` отбирает только чётные числа из списка.

**Реализация:**
```python
def filter_even_numbers(numbers):
    even = []
    for x in numbers:
        if x % 2 == 0:
            even.append(x)
    return even
```

**Пример использования:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter_even_numbers(numbers)
# Результат: [2, 4, 6, 8, 10]
```

### 2. Факториал через reduce

Функция `factorial()` вычисляет факториал числа используя `reduce`.

**Реализация:**
```python
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))
```

**Пример использования:**
```python
fact = factorial(5)  # 120
fact = factorial(10)  # 3628800
```

### 3. Декоратор для логирования вызова функции

Декоратор `@log_decorator` логирует вызов функции с временной меткой, аргументами и результатом.

**Реализация:**
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Вызов функции: {func.__name__}")
        print(f"  Аргументы: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  Результат: {result}")
        return result
    return wrapper
```

**Пример использования:**
```python
@log_decorator
def add(a, b):
    return a + b

result = add(5, 3)
# Выводит:
# [2025-11-29 17:26:21] Вызов функции: add
#   Аргументы: args=(5, 3), kwargs={}
#   Результат: 8
```

### 4. Реализовать мемоизацию функции через декоратор

Декоратор `@memoize` кеширует результаты выполнения функции для ускорения повторных вызовов.

**Реализация:**
```python
def memoize(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print(f"Результат для {args} взят из кеша")
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        print(f"Результат для {args} вычислен и сохранен в кеш")
        return result
    
    return wrapper
```

**Пример использования:**
```python
@memoize
def slow_fibonacci(n):
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

# Первый вызов - вычисление
fib1 = slow_fibonacci(5)  # Вычисляется

# Второй вызов - из кеша
fib2 = slow_fibonacci(5)  # Берется из кеша
```

### 5. Создать декоратор с параметрами

Декоратор `@repeat_decorator(times=N)` позволяет выполнить функцию указанное количество раз.

**Реализация:**
```python
def repeat_decorator(times=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"Вызов {i + 1} из {times}")
                result = func(*args, **kwargs)
                results.append(result)
            return results if times > 1 else results[0]
        return wrapper
    return decorator
```

**Пример использования:**
```python
@repeat_decorator(times=3)
def greet(name):
    return f"Привет, {name}!"

result = greet("Мир")
# Выполнится 3 раза
# Результат: ['Привет, Мир!', 'Привет, Мир!', 'Привет, Мир!']
```

## Запуск

Для запуска всех примеров:

```bash
python main.py
```

## Основные концепции

### Фильтрация

Отбор элементов из последовательности по определенному условию. В данной работе реализована через цикл for и проверку условия.

### Reduce

Операция сводит последовательность к одному значению путем последовательного применения функции. Используется для вычисления факториала через умножение всех чисел от 1 до n.

### Декораторы

Функции, которые модифицируют поведение других функций. Позволяют добавлять функциональность без изменения исходного кода.

### Мемоизация

Техника оптимизации, при которой результаты выполнения функции сохраняются в кеше для повторного использования. Особенно полезно для рекурсивных функций.

### Декораторы с параметрами

Декораторы, которые принимают параметры и возвращают декоратор. Позволяют настраивать поведение декоратора при его применении.

## Требования

- Python 3.6+
- Модуль `functools` (встроенный)
- Модуль `datetime` (встроенный)

## Автор

Лабораторная работа выполнена в рамках изучения функционального программирования на Python.
