# Лабораторная работа 4: Функциональное программирование в Python

## Описание

Данная лабораторная работа демонстрирует применение функционального стиля программирования в Python. Изучаются функции высшего порядка, лямбда-функции, операции map/filter/reduce, генераторы и декораторы.

## Структура проекта

```
lr4/
├── functional_programming.py  # Основные функции функционального программирования
├── test_functional.py         # Unit-тесты для всех функций
├── main.py                    # Примеры использования
└── README.md                  # Документация
```

## Выполненные задания

### 1. Применение нескольких функций к списку через map

Функция `apply_multiple_functions()` применяет произвольное количество функций к одному списку данных, используя `map`.

**Пример:**
```python
from functional_programming import apply_multiple_functions

numbers = [1, 2, 3, 4, 5]
results = apply_multiple_functions(
    numbers,
    lambda x: x * 2,      # Удвоение
    lambda x: x ** 2,     # Квадрат
    lambda x: x + 10      # Добавление 10
)
# Результат: [[2, 4, 6, 8, 10], [1, 4, 9, 16, 25], [11, 12, 13, 14, 15]]
```

### 2. Фильтрация чётных чисел из списка

Функция `filter_even_numbers()` использует `filter` и лямбда-функцию для отбора только чётных чисел.

**Пример:**
```python
from functional_programming import filter_even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter_even_numbers(numbers)
# Результат: [2, 4, 6, 8, 10]
```

### 3. Декоратор замера времени работы функции

Декоратор `@timing_decorator` измеряет время выполнения функции и возвращает результат вместе с информацией о времени выполнения.

**Пример:**
```python
from functional_programming import timing_decorator
import time

@timing_decorator
def slow_function():
    time.sleep(0.1)
    return "Done"

result = slow_function()
# Выводит: Function 'slow_function' executed in 0.100123 seconds
# result = {
#     'result': 'Done',
#     'execution_time': 0.100123,
#     'function_name': 'slow_function'
# }
```

### 4. Собственная реализация reduce

Функция `custom_reduce()` реализует функциональность стандартной функции `reduce` из модуля `functools`.

**Пример:**
```python
from functional_programming import custom_reduce

# Суммирование
numbers = [1, 2, 3, 4, 5]
sum_result = custom_reduce(lambda x, y: x + y, numbers)
# Результат: 15

# Умножение с начальным значением
product = custom_reduce(lambda x, y: x * y, [1, 2, 3, 4], 10)
# Результат: 240
```

**Особенности реализации:**
- Поддерживает начальное значение (initializer)
- Корректно обрабатывает пустые последовательности
- Работает с любыми типами данных

### 5. Функция-карринг

Функция `curry()` преобразует функцию от нескольких аргументов в функцию, принимающую аргументы по одному (каррирование).

**Пример:**
```python
from functional_programming import curry

def add(a, b, c):
    return a + b + c

curried_add = curry(add)
result = curried_add(1)(2)(3)
# Результат: 6

# Частичное применение
partial = curried_add(1)(2)
result2 = partial(3)  # Также 6
```

**Применение каррирования:**
- Создание специализированных функций из общих
- Частичное применение аргументов
- Улучшение переиспользования кода

## Дополнительные возможности

### Композиция функций

Функция `compose()` позволяет создавать композицию нескольких функций.

```python
from functional_programming import compose

def double(x):
    return x * 2

def square(x):
    return x ** 2

composed = compose(square, double)
result = composed(3)  # double(3) = 6, square(6) = 36
```

### Генераторы

Реализованы примеры генераторов для демонстрации ленивых вычислений:

**Генератор квадратов:**
```python
from functional_programming import generator_squares

gen = generator_squares(5)
squares = list(gen)  # [0, 1, 4, 9, 16, 25]
```

**Генератор чисел Фибоначчи:**
```python
from functional_programming import generator_fibonacci

gen = generator_fibonacci(10)
fibonacci = list(gen)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Unit-тестирование

Все функции покрыты unit-тестами. Тесты находятся в файле `test_functional.py`.

### Запуск тестов

```bash
python test_functional.py
```

Или с подробным выводом:

```bash
python -m unittest test_functional -v
```

### Покрытие тестами

- **apply_multiple_functions**: 3 теста
- **filter_even_numbers**: 4 теста
- **timing_decorator**: 3 теста
- **custom_reduce**: 7 тестов
- **curry**: 4 теста
- **compose**: 2 теста
- **generators**: 3 теста

**Всего: 26 тестов** - все проходят успешно ✅

## Запуск примеров

Для просмотра примеров использования всех функций:

```bash
python main.py
```

## Основные концепции функционального программирования

### Функции высшего порядка

Функции, которые принимают другие функции в качестве аргументов или возвращают функции. Примеры:
- `map()` - применяет функцию к каждому элементу
- `filter()` - фильтрует элементы по условию
- `reduce()` - сводит последовательность к одному значению

### Лямбда-функции

Анонимные функции, определяемые через ключевое слово `lambda`:

```python
# Вместо:
def square(x):
    return x ** 2

# Можно написать:
square = lambda x: x ** 2
```

### Декораторы

Функции, которые модифицируют поведение других функций:

```python
@decorator
def my_function():
    pass
```

Эквивалентно:
```python
def my_function():
    pass
my_function = decorator(my_function)
```

### Генераторы

Специальные функции, которые возвращают итератор. Используют `yield` вместо `return` и позволяют ленивые вычисления:

```python
def my_generator():
    yield 1
    yield 2
    yield 3
```

### Каррирование

Техника преобразования функции от нескольких аргументов в последовательность функций от одного аргумента:

```python
# Обычная функция
def add(a, b, c):
    return a + b + c

# Каррированная версия
curried_add = curry(add)
result = curried_add(1)(2)(3)  # 6
```

## Преимущества функционального программирования

1. **Читаемость кода** - код становится более декларативным
2. **Переиспользование** - функции легче комбинировать
3. **Тестируемость** - чистые функции легче тестировать
4. **Параллелизм** - отсутствие побочных эффектов упрощает параллельное выполнение
5. **Модульность** - код разбивается на небольшие, независимые функции

## Требования

- Python 3.6+

## Автор

Лабораторная работа выполнена в рамках изучения функционального программирования на Python.

