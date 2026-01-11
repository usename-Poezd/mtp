# Лабораторная работа 8

Цель работы — познакомиться с современными инструментами экосистемы Python:
управление зависимостями, тестирование, TDD, логирование.

## Структура

- [`requirements.txt`](lr8/requirements.txt) – список зависимостей проекта
- [`calculator.py`](lr8/calculator.py) – реализация простого калькулятора
- [`test_calculator.py`](lr8/test_calculator.py) – тесты для калькулятора (TDD, `pytest`)
- [`requests_example.py`](lr8/requests_example.py) – пример использования сторонней библиотеки `requests`
- [`logging_example.py`](lr8/logging_example.py) – пример настройки и использования модуля `logging`

## 1. Управление зависимостями

В файле [`requirements.txt`](lr8/requirements.txt) добавлена зависимость на библиотеку `requests`,
а также `pytest` для запуска тестов:

```bash
pip install -r requirements.txt
```

После установки можно запускать примеры и тесты.

## 2. TDD для калькулятора

Калькулятор реализован в модуле [`calculator.py`](lr8/calculator.py),
а его поведение описано в тестах в файле [`test_calculator.py`](lr8/test_calculator.py).

Поддерживаются операции:

- сложение `add(a, b)`
- вычитание `subtract(a, b)`
- умножение `multiply(a, b)`
- деление `divide(a, b)` (с выбросом `ZeroDivisionError` при делении на ноль)

Запуск тестов (из каталога `lr8`):

```bash
pytest -q
```

## 3. Использование logging

- В модуле [`calculator.py`](lr8/calculator.py) каждая операция пишет отладочную информацию в лог
- В тестах [`test_calculator.py`](lr8/test_calculator.py) включено базовое логирование для наглядности
- В файле [`requests_example.py`](lr8/requests_example.py) логируется выполнение HTTP-запроса
- В модуле [`logging_example.py`](lr8/logging_example.py) настроен именованный логгер с форматированием

Пример запуска скриптов:

```bash
python requests_example.py
python logging_example.py
```

Таким образом в работе показаны: управление зависимостями через `requirements.txt`,
написание модульных тестов с использованием `pytest` по принципам TDD и базовая интеграция
модуля `logging` в прикладной код.
