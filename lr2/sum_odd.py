
from __future__ import annotations


def sum_odd_up_to(n: int) -> int:
    if n <= 0:
        return 0

    last_odd = n if n % 2 == 1 else n - 1
    count = (last_odd + 1) // 2
    return count * (2 * 1 + (count - 1) * 2) // 2


if __name__ == "__main__":
    raw = input("Введите целое N: ")
    n = int(raw)
    print("Сумма нечётных чисел до N =", sum_odd_up_to(n))
