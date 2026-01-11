from __future__ import annotations

from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")

class ExtendedList(list[T]):
    def unique(self) -> "ExtendedList[T]":
        seen: set[object] = set()
        out: ExtendedList[T] = ExtendedList()
        for item in self:
            if item not in seen:
                seen.add(item)
                out.append(item)
        return out

    def flatten(self) -> "ExtendedList[object]":
        out: ExtendedList[object] = ExtendedList()
        for item in self:
            if isinstance(item, (str, bytes)):
                out.append(item)
                continue
            if isinstance(item, Iterable):
                out.extend(item)  # type: ignore[arg-type]
            else:
                out.append(item)
        return out

    def average(self) -> float:
        if not self:
            raise ValueError("Cannot compute average of empty list")
        return float(sum(self)) / len(self)


if __name__ == "__main__":
    xs = ExtendedList([1, 2, 2, 3, 3, 3])
    print("unique:", xs.unique())
    print("average:", xs.average())
    nested = ExtendedList([[1, 2], [3], 4, "abc"])
    print("flatten:", nested.flatten())
