from __future__ import annotations


VOWELS_RU = "аеёиоуыэюя"
VOWELS_EN = "aeiouy"
VOWELS_ALL = set((VOWELS_RU + VOWELS_EN).lower())


def count_vowels(text: str) -> int:
    return sum(1 for ch in text.lower() if ch in VOWELS_ALL)


if __name__ == "__main__":
    s = input("Введите строку: ")
    print("Количество гласных =", count_vowels(s))
