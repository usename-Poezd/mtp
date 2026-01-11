from __future__ import annotations

import logging


logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    """Сложение двух чисел."""

    logger.debug("Adding %s and %s", a, b)
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычитание ``b`` из ``a``."""

    logger.debug("Subtracting %s and %s", a, b)
    return a - b


def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""

    logger.debug("Multiplying %s and %s", a, b)
    return a * b


def divide(a: float, b: float) -> float:
    """Деление ``a`` на ``b``.

    :raises ZeroDivisionError: при попытке деления на ноль
    """

    logger.debug("Dividing %s by %s", a, b)

    if b == 0:
        logger.error("Division by zero: a=%s, b=%s", a, b)
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b


__all__ = ["add", "subtract", "multiply", "divide"]
