# лаба 4 функциональное программирование
import time
from functools import reduce  # на всякий случай

# задание 1: применить несколько функций через map
def apply_multiple_functions(data, *functions):
    # применяем функции к списку
    result = []
    for func in functions:
        temp = []
        for item in data:
            temp.append(func(item))
        result.append(temp)
    return result


# задание 2: фильтровать четные числа
def filter_even_numbers(numbers):
    # оставляем только четные
    even = []
    for x in numbers:
        if x % 2 == 0:  # если четное
            even.append(x)
    return even


# задание 3: декоратор для времени
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print("Function", func.__name__, "took", t, "seconds")
        return {"result": res, "execution_time": t, "function_name": func.__name__}
    return wrapper


# задание 4: свой reduce
def custom_reduce(func, iterable, initializer=None):
    # проверяем пустой список
    if len(iterable) == 0:
        if initializer == None:
            raise TypeError("reduce() of empty sequence with no initial value")
        else:
            return initializer
    
    # берем первый элемент или initializer
    if initializer == None:
        acc = iterable[0]
        i = 1
    else:
        acc = initializer
        i = 0
    
    # применяем функцию
    while i < len(iterable):
        acc = func(acc, iterable[i])
        i = i + 1
    
    return acc


# задание 5: карринг
def curry(func):
    def curried(*args, **kwargs):
        # считаем сколько аргументов нужно
        needed = func.__code__.co_argcount
        got = len(args) + len(kwargs)
        
        if got >= needed:
            # если достаточно - вызываем
            return func(*args, **kwargs)
        else:
            # если нет - возвращаем функцию
            def partial(*new_args, **new_kwargs):
                all_args = args + new_args
                all_kwargs = {}
                all_kwargs.update(kwargs)
                all_kwargs.update(new_kwargs)
                return curried(*all_args, **all_kwargs)
            return partial
    return curried


# дополнительные функции
def square(x):
    return x * x

def double(x):
    return 2 * x

def is_positive(x):
    if x > 0:
        return True
    else:
        return False


# композиция функций
def compose(*functions):
    def composed(x):
        res = x
        # применяем функции в обратном порядке
        for i in range(len(functions) - 1, -1, -1):
            res = functions[i](res)
        return res
    return composed


# генератор квадратов
def generator_squares(n):
    i = 0
    while i <= n:
        yield i * i
        i = i + 1


# генератор фибоначчи
def generator_fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        yield a
        # следующее число
        temp = a
        a = b
        b = temp + b
        count = count + 1
