import re
from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]:
    """Віддає (yield) усі дійсні числа з тексту, відокремлені пробілами."""
    # Число, перед яким початок рядка/пробіл, а після — пробіл/кінець рядка
    # (кінцеву крапку речення, наприклад "доларів.", число не захоплює)
    for match in re.finditer(r"(?<!\S)\d+\.\d+(?!\S)", text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    """Підсумовує всі числа, які повертає генератор func для тексту."""
    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {round(total_income, 2)}")
