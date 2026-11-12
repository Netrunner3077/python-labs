from argparse import ArgumentParser
from math import prod, sqrt
from pathlib import Path
from random import Random
from statistics import geometric_mean, mean


def analyze(matrix: list[list[int]]) -> tuple[list[list[int]], object]:
    a = [value for row in matrix for value in row]
    transformed = []
    for j, column in enumerate(zip(*matrix), 1):
        best = max(column)
        transformed.append([best, column.index(best) + 1, j])
    result = transformed
    return transformed, result


def main() -> None:
    parser = ArgumentParser(description="ЛР №4, вариант №4")
    parser.add_argument("--seed", type=int, default=4)
    parser.add_argument("--output", type=Path, default=Path("result.txt"))
    args = parser.parse_args()

    rng = Random(args.seed)
    values = [rng.randint(-30, 50) for _ in range(90)]
    matrix = [values[i:i + 9] for i in range(0, 90, 9)]
    transformed, result = analyze(matrix)
    lines = ["Исходная матрица:"]
    lines.extend(" ".join(map(str, row)) for row in matrix)
    lines.append("Преобразованная матрица:")
    lines.extend(" ".join(map(str, row)) for row in transformed)
    lines.append(f"Максимум, строка и столбец = {result}")
    text = "\n".join(lines)
    args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
