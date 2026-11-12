"""
Лабораторная работа №4. Вариант 14.
Одномерный массив {B_i} из k=90 случайных целых чисел в диапазоне [-50; 20],
вывести в виде матрицы 10×9 и определить номера положительных элементов.
"""
from __future__ import annotations

import logging
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Final, Iterator

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

OUTPUT_FILE: Final[Path] = Path("result_lab_4_v14.txt")


@dataclass(frozen=True)
class TaskParams:
    """Параметры задания (вариант 14)."""
    k: int = 90            
    z1: int = -50          
    z2: int = 20           
    n: int = 10            
    m: int = 9             

    def __post_init__(self) -> None:
        if self.k != self.n * self.m:
            raise ValueError(
                f"k={self.k} должно равняться n*m={self.n * self.m}"
            )
        if self.z1 >= self.z2:
            raise ValueError("z1 должно быть меньше z2")


def read_int(prompt: str, default: int) -> int:
    """Безопасный ввод целого числа с возможностью оставить значение по умолчанию."""
    raw = input(f"{prompt} [{default}]: ").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        logger.warning("Некорректный ввод, использую значение по умолчанию: %d", default)
        return default

def input_params() -> TaskParams:
    while True:
        try:
            return TaskParams(
                k=read_int("Введите k (количество элементов)", 90),
                z1=read_int("Введите z1 (нижняя граница)", -50),
                z2=read_int("Введите z2 (верхняя граница)", 20),
                n=read_int("Введите n (число строк)", 10),
                m=read_int("Введите m (число столбцов)", 9),
            )
        except ValueError as exc:
            logger.error("Некорректные параметры: %s. Попробуйте снова.", exc)

def generate_array(params: TaskParams, seed: int | None = None) -> list[int]:
    """Генерация одномерного массива целых чисел в диапазоне [z1; z2]."""
    if seed is not None:
        random.seed(seed)
        logger.info("Seed зафиксирован: %d", seed)
    return [random.randint(params.z1, params.z2) for _ in range(params.k)]


def matrix_rows(array: list[int], params: TaskParams) -> Iterator[list[int]]:
    """Разбивает плоский массив на строки матрицы n x m."""
    for i in range(params.n):
        start = i * params.m
        yield array[start:start + params.m]


def format_matrix(array: list[int], params: TaskParams) -> str:
    """Формирует текстовое представление матрицы n x m."""
    lines: list[str] = ["Исходная матрица:"]
    for row in matrix_rows(array, params):
        lines.append("".join(f"{value:>5}" for value in row))
    return "\n".join(lines)


def find_positive_indices(array: list[int]) -> list[tuple[int, int]]:
    """
    Возвращает список пар (индекс_0_based, значение)
    для всех положительных элементов массива.
    """
    return [(i, v) for i, v in enumerate(array) if v > 0]


def format_positive_report(pairs: list[tuple[int, int]]) -> str:
    """Формирует текстовый отчёт по положительным элементам."""
    if not pairs:
        return "Положительных элементов нет."

    lines = ["Номера положительных элементов массива:"]
    for idx, value in pairs:
        lines.append(f"  B[{idx}] (номер {idx + 1}) = {value}")
    lines.append(f"\nВсего положительных элементов: {len(pairs)}")
    return "\n".join(lines)


def write_report(path: Path, matrix_text: str, positives_text: str) -> None:
    """Запись отчёта в файл."""
    with path.open("w", encoding="utf-8") as f:
        f.write(matrix_text + "\n\n")
        f.write(positives_text + "\n")


def main() -> None:
    logger.info("Запуск: ЛР №4, вариант 14.")

    params = TaskParams(
        k=read_int("Введите k (количество элементов)", 90),
        z1=read_int("Введите z1 (нижняя граница)", -50),
        z2=read_int("Введите z2 (верхняя граница)", 20),
        n=read_int("Введите n (число строк)", 10),
        m=read_int("Введите m (число столбцов)", 9),
    )

    array = generate_array(params, seed=None)

    matrix_text = format_matrix(array, params)
    positives = find_positive_indices(array)
    positives_text = format_positive_report(positives)

    print(matrix_text)
    print()
    print(positives_text)

    write_report(OUTPUT_FILE, matrix_text, positives_text)
    logger.info("Отчёт записан: %s", OUTPUT_FILE.resolve())


if __name__ == "__main__":
    main()