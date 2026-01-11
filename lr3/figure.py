from __future__ import annotations

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Figure(ABC):
    """Abstract geometric figure."""

    @abstractmethod
    def area(self) -> float: 
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> float: 
        raise NotImplementedError


@dataclass(frozen=True, slots=True)
class Rectangle(Figure):
    width: float
    height: float

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Rectangle sides must be positive")

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


@dataclass(frozen=True, slots=True)
class Circle(Figure):
    radius: float

    def __post_init__(self) -> None:
        if self.radius <= 0:
            raise ValueError("Circle radius must be positive")

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


@dataclass(frozen=True, slots=True)
class Triangle(Figure):
    a: float
    b: float
    c: float

    def __post_init__(self) -> None:
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError("Triangle sides must be positive")
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError("Triangle inequality is not satisfied")

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def area(self) -> float:
        # Heron's formula
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


if __name__ == "__main__":
    figures: list[Figure] = [
        Rectangle(3, 4),
        Circle(2),
        Triangle(3, 4, 5),
    ]
    for f in figures:
        print(type(f).__name__, "area=", round(f.area(), 3), "perimeter=", round(f.perimeter(), 3))
