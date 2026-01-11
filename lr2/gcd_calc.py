
from __future__ import annotations


def gcd(a: int, b: int) -> int:

    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("НОД =", gcd(a, b))
