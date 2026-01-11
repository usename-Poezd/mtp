"""Task 1: Student class with an information output method."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Student:
    first_name: str
    last_name: str
    group: str
    year: int
    gpa: float

    def info(self) -> str:
        """Return a human-readable string with student information."""
        return (
            f"Student: {self.last_name} {self.first_name}; "
            f"group={self.group}; year={self.year}; gpa={self.gpa:.2f}"
        )

    def print_info(self) -> None:
        """Print student info to stdout."""
        print(self.info())


if __name__ == "__main__":
    s = Student("Ivan", "Petrov", "IKBO-01-23", 2, 4.35)
    s.print_info()
