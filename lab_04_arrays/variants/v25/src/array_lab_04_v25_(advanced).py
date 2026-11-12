from argparse import ArgumentParser
from math import prod, sqrt
from pathlib import Path
from random import Random
from statistics import geometric_mean, mean


def analyze(matrix: list[list[int]]) -> tuple[list[list[int]], object]:
    a = [value for row in matrix for value in row]
    def keep(x: int, i: int, j: int) -> bool:
        return -30 <= x <= 30

    transformed = [
        [x if keep(x, i, j) else 0 for j, x in enumerate(row)]
        for i, row in enumerate(matrix)
    ]
    selected = [
        (i * len(row) + j + 1, x)
        for i, row in enumerate(matrix)
        for j, x in enumerate(row)
        if keep(x, i, j)
    ]
    values = [x for _, x in selected]
    result = [len(values), prod(values)]
    return transformed, result


def main() -> None:
    parser = ArgumentParser(description="ЛР №4, вариант №25")
    parser.add_argument("--seed", type=int, default=25)
    parser.add_argument("--output", type=Path, default=Path("result.txt"))
    args = parser.parse_args()

    rng = Random(args.seed)
    values = [rng.randint(-60, 10) for _ in range(64)]
    matrix = [values[i:i + 8] for i in range(0, 64, 8)]
    transformed, result = analyze(matrix)
    lines = ["Исходная матрица:"]
    lines.extend(" ".join(map(str, row)) for row in matrix)
    lines.append("Преобразованная матрица:")
    lines.extend(" ".join(map(str, row)) for row in transformed)
    lines.append(f"Количество и произведение = {result}")
    text = "\n".join(lines)
    args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
