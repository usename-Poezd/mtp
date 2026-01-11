from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Vector2D:
    x: float
    y: float

    def __add__(self, other: object) -> "Vector2D":
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __radd__(self, other: object) -> "Vector2D":
        # Allows: sum([v1, v2, v3], start=Vector2D(0,0))
        if other == 0:
            return self
        return self.__add__(other)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector2D(1, 2)
    v2 = Vector2D(10, -5)
    print("v1 + v2 =", v1 + v2)
    print("sum =", sum([v1, v2], start=Vector2D(0, 0)))
