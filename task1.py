from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """Повертає функцію fibonacci(n), яка кешує вже обчислені значення."""
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # Значення вже обчислювалось — беремо з кешу
        if n in cache:
            return cache[n]
        # Обчислюємо рекурсивно та зберігаємо в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))  # 55
    print(fib(15))  # 610
