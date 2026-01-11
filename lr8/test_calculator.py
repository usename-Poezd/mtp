"""
Файл демонстрирует подход TDD: сначала
формализуем ожидаемое поведение в тестах,
затем реализуем функции в самом модуле.
"""

import logging

import pytest

from calculator import add, divide, multiply, subtract


# Базовая настройка логирования для тестового запуска
logging.basicConfig(level=logging.DEBUG)


def test_add_integers() -> None:
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


def test_add_floats() -> None:
    assert add(0.1, 0.2) == pytest.approx(0.3, rel=1e-9)


def test_subtract() -> None:
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2


def test_multiply() -> None:
    assert multiply(3, 4) == 12
    assert multiply(3, 0) == 0


def test_divide() -> None:
    assert divide(10, 2) == 5
    assert divide(9, 2) == 4.5


def test_divide_by_zero_raises() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
