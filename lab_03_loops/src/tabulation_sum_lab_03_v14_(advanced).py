"""
Лабораторная работа №3. Вариант 14.
Табуляция кусочно-заданной функции и сумма значений y > 0.
"""
from __future__ import annotations

import logging
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Final, Iterator

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

SCRIPT_DIR: Final[Path] = Path(__file__).resolve().parent
RESULTS_DIR: Final[Path] = SCRIPT_DIR.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)
OUTPUT_FILE: Final[Path] = RESULTS_DIR / "result_lab_3_v14.txt"

X_BREAK: Final[float] = 1.5


@dataclass(frozen=True)
class TabRow:
    """Одна строка таблицы: аргумент и значение функции."""
    x: float
    y: float


def read_float(prompt: str) -> float:
    """Безопасный ввод вещественного числа с повторным запросом."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            logger.warning("Некорректный ввод. Введите вещественное число.")


def compute_y(x: float) -> float:
    """Вычисление кусочно-заданной функции в точке x."""
    if x < 0:
        return x * x - 1
    if x < X_BREAK:
        return math.cos(x)
    return math.sin(x - 1)


def tabulate(x_start: float, x_end: float, step: float) -> Iterator[TabRow]:
    """Генератор строк табуляции."""
    if step <= 0:
        raise ValueError("Шаг должен быть положительным")
    if x_end < x_start:
        raise ValueError("Конец отрезка должен быть не меньше начала")

    n = int(round((x_end - x_start) / step)) + 1
    logger.info("Точек табуляции: %d", n)

    for i in range(n):
        x = x_start + i * step
        yield TabRow(x=x, y=compute_y(x))


def write_report(path: Path, rows: list[TabRow], total: float) -> None:
    """Запись таблицы и суммы в текстовый файл."""
    header = f"{'x':>10} | {'y':>14}"
    sep = "-" * len(header)

    with path.open("w", encoding="utf-8") as f:
        f.write(header + "\n")
        f.write(sep + "\n")
        for row in rows:
            f.write(f"{row.x:>10.4f} | {row.y:>14.6f}\n")
        f.write(sep + "\n")
        f.write(f"Сумма положительных y = {total:.6f}\n")


def main() -> None:
    logger.info("Запуск: ЛР №3, вариант 14.")

    x_start = read_float("Введите начало отрезка: ")
    x_end = read_float("Введите конец отрезка: ")
    step = read_float("Введите шаг: ")

    rows = list(tabulate(x_start, x_end, step))
    total = sum(r.y for r in rows if r.y > 0)

    header = f"{'x':>10} | {'y':>14}"
    sep = "-" * len(header)
    print(header)
    print(sep)
    for r in rows:
        print(f"{r.x:>10.4f} | {r.y:>14.6f}")
    print(sep)
    print(f"Сумма положительных y = {total:.6f}")

    write_report(OUTPUT_FILE, rows, total)
    logger.info("Отчёт записан: %s", OUTPUT_FILE)


if __name__ == "__main__":
    main()