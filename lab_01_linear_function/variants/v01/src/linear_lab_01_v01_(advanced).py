from math import cos, pi, sin
from argparse import ArgumentParser
from pathlib import Path


def calculate(x: float, y: float) -> float:
    value = cos(pi / 7) * sin(x - 8 * y) ** 2 / (2.7 * (x - pi))
    if isinstance(value, complex):
        raise ValueError("ожидался вещественный результат")
    return value


def main() -> None:
    parser = ArgumentParser(description="ЛР №1, вариант №1")
    parser.add_argument("--input", type=Path, default=Path("input.txt"))
    parser.add_argument("--output", type=Path, default=Path("result.txt"))
    args = parser.parse_args()

    try:
        x, y = map(float, args.input.read_text(encoding="utf-8").replace(",", ".").split())
        value = calculate(x, y)
        result = f"Результат = {value:.4f}\nЦелая часть = {int(value)}"
        args.output.write_text(result + "\n", encoding="utf-8")
    except (OSError, ValueError, ArithmeticError) as error:
        parser.exit(1, f"Ошибка: {error}\n")
    print(result)


if __name__ == "__main__":
    main()
