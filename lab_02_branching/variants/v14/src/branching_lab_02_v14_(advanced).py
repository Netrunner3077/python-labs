"""
Лабораторная работа №2. Вариант 14.
Программирование алгоритмов разветвляющейся структуры.
"""
from __future__ import annotations

import logging
import math
from pathlib import Path
from typing import Final

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

OUTPUT_FILE: Final[Path] = Path("result.txt")


def read_float(prompt: str) -> float:
    """Безопасный ввод вещественного числа с повторным запросом при ошибке."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            logger.warning("Некорректный ввод. Введите вещественное число, например 0.5")


def compute_b(x: float, y: float, a: float, c: float, d: float) -> float:
    """
    Вычисление функции варианта 14.

    b = 2*ln(x) * max(min(x, y), sin(c*x), cos(d)),  если 0 < x < 1 и 0 < y < 1
    b = min(e^(x+1), y),                             если x < 0 и y < 0
    b = a + x,                                       в противном случае
    """
    if 0 < x < 1 and 0 < y < 1:
        return 2 * math.log(x) * max(min(x, y), math.sin(c * x), math.cos(d))
    if x < 0 and y < 0:
        return min(math.exp(x + 1), y)
    return a + x


def write_result(
    path: Path,
    x: float, y: float, a: float, c: float, d: float, b: float,
) -> None:
    """Запись исходных данных и результата в текстовый файл."""
    with path.open("w", encoding="utf-8") as f:
        f.write(f"x = {x}\n")
        f.write(f"y = {y}\n")
        f.write(f"a = {a}\n")
        f.write(f"c = {c}\n")
        f.write(f"d = {d}\n")
        f.write(f"b = {b:.6f}\n")


def main() -> None:
    logger.info("Запуск программы. Вариант 14.")

    x = read_float("Введите x: ")
    y = read_float("Введите y: ")
    a = read_float("Введите a: ")
    c = read_float("Введите c: ")
    d = read_float("Введите d: ")

    b = compute_b(x, y, a, c, d)

    print(f"Исходные данные: x={x}, y={y}, a={a}, c={c}, d={d}")
    print(f"Результат: b = {b:.6f}")

    write_result(OUTPUT_FILE, x, y, a, c, d, b)
    logger.info("Результат записан в файл %s", OUTPUT_FILE.resolve())


if __name__ == "__main__":
    main()