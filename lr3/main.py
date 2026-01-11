from __future__ import annotations
from student import Student
from figure import Circle, Rectangle, Triangle
from operator_overload import Vector2D
from factory import FigureFactory
from custom_list import ExtendedList


def demo_student() -> None:
    s = Student("Ivan", "Petrov", "IKBO-01-23", 2, 4.35)
    s.print_info()


def demo_figures() -> None:
    figures = [Rectangle(3, 4), Circle(2), Triangle(3, 4, 5)]
    for f in figures:
        print(type(f).__name__, "area=", round(f.area(), 3), "perimeter=", round(f.perimeter(), 3))


def demo_operator_overload() -> None:
    v1 = Vector2D(1, 2)
    v2 = Vector2D(10, -5)
    print("v1 + v2 =", v1 + v2)


def demo_factory() -> None:
    factory = FigureFactory()
    f = factory.create("rectangle", width=5, height=6)
    print("factory ->", type(f).__name__, "area=", f.area())


def demo_extended_list() -> None:
    xs = ExtendedList([1, 2, 2, 3, 3, 3])
    print("unique:", xs.unique())
    print("average:", xs.average())


def main() -> None:
    demo_student()
    demo_figures()
    demo_operator_overload()
    demo_factory()
    demo_extended_list()


if __name__ == "__main__":
    main()
