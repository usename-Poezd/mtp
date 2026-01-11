"""Task 4: Factory pattern (creates figures by type)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from figure import Circle, Figure, Rectangle, Triangle


class FigureFactoryProtocol(Protocol):
    def create(self, kind: str, /, **kwargs: Any) -> Figure: 
        pass


@dataclass(slots=True)
class FigureFactory(FigureFactoryProtocol):

    def create(self, kind: str, /, **kwargs: Any) -> Figure:
        kind = kind.strip().lower()
        match kind:
            case "rectangle" | "rect":
                return Rectangle(
                    width=float(kwargs["width"]),
                    height=float(kwargs["height"]),
                )
            case "circle":
                return Circle(
                    radius=float(kwargs["radius"]),
                )
            case "triangle" | "tri":
                return Triangle(
                    a=float(kwargs["a"]),
                    b=float(kwargs["b"]),
                    c=float(kwargs["c"]),
                )
            case _:
                raise ValueError(f"Unknown figure kind: {kind!r}")



if __name__ == "__main__":
    factory = FigureFactory()
    f1 = factory.create("rectangle", width=3, height=4)
    f2 = factory.create("circle", radius=2)
    print(type(f1).__name__, f1.area(), f1.perimeter())
    print(type(f2).__name__, f2.area(), f2.perimeter())
