from argparse import ArgumentParser
from math import prod, sqrt
from pathlib import Path
from random import Random
from statistics import geometric_mean, mean


def analyze(matrix: list[list[int]]) -> tuple[list[list[int]], object]:
    a = [value for row in matrix for value in row]
    transformed = [[sum(x for x in col if x < 0), sum(x > 0 for x in col)] for col in zip(*matrix)]
    result = transformed
    return transformed, result


def main() -> None:
    parser = ArgumentParser(description="ЛР №4, вариант №30")
    parser.add_argument("--seed", type=int, default=30)
    parser.add_argument("--output", type=Path, default=Path("result.txt"))
    args = parser.parse_args()

    rng = Random(args.seed)
    values = [rng.randint(-50, 40) for _ in range(88)]
    matrix = [values[i:i + 11] for i in range(0, 88, 11)]
    transformed, result = analyze(matrix)
    lines = ["Исходная матрица:"]
    lines.extend(" ".join(map(str, row)) for row in matrix)
    lines.append("Преобразованная матрица:")
    lines.extend(" ".join(map(str, row)) for row in transformed)
    lines.append(f"Сумма и количество по столбцам = {result}")
    text = "\n".join(lines)
    args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
