import sys
from collections import Counter

LEVELS = ("INFO", "DEBUG", "ERROR", "WARNING")


def parse_log_line(line: str) -> dict:
    """Розбирає рядок логу на дату, час, рівень та повідомлення."""
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        raise ValueError(f"Невірний формат рядка: {line.strip()!r}")
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level.upper(), "message": message}


def load_logs(file_path: str) -> list:
    """Завантажує лог-файл і повертає список розібраних записів."""
    with open(file_path, encoding="utf-8") as file:
        # Порожні рядки пропускаємо
        return [parse_log_line(line) for line in file if line.strip()]


def filter_logs_by_level(logs: list, level: str) -> list:
    """Повертає записи лише вказаного рівня."""
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів для кожного рівня."""
    return dict(Counter(log["level"] for log in logs))


def display_log_counts(counts: dict) -> None:
    """Виводить таблицю з кількістю записів за рівнями."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Використання: python task3.py <файл логів> [рівень]")
        return

    try:
        logs = load_logs(sys.argv[1])
    except FileNotFoundError:
        print(f"Файл '{sys.argv[1]}' не знайдено.")
        return
    except (OSError, UnicodeDecodeError) as e:
        print(f"Помилка читання файлу: {e}")
        return
    except ValueError as e:
        print(e)
        return

    # Спершу виводимо найчастіші рівні
    counts = dict(sorted(count_logs_by_level(logs).items(), key=lambda kv: -kv[1]))
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filter_logs_by_level(logs, level):
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
