from math import exp


from math import isfinite, prod
from argparse import ArgumentParser
from pathlib import Path


def value_at(x: float) -> float | None:
    if x > 2:
        y = exp(x)
    elif -2 < x < 2:
        y = x + 4
    elif x < -2:
        y = 0
    else:
        y = None
    return y


def tabulate(a: float, b: float, h: float) -> list[tuple[float, float | None]]:
    if not all(map(isfinite, (a, b, h))) or h <= 0 or b < a:
        raise ValueError("нужны конечные границы, b >= a и положительный шаг")
    n = int((b - a) / h + 1e-9) + 1
    return [(x, value_at(x)) for x in (round(a + i * h, 12) for i in range(n))]


def main() -> None:
    parser = ArgumentParser(description="ЛР №3, вариант №26")
    parser.add_argument("--start", type=float, default=-2)
    parser.add_argument("--end", type=float, default=2)
    parser.add_argument("--step", type=float, default=.25)
    parser.add_argument("--output", type=Path, default=Path("result.txt"))
    args = parser.parse_args()
    try:
        rows = tabulate(args.start, args.end, args.step)
    except ValueError as error:
        parser.exit(1, f"Ошибка: {error}\n")

    values = [y for _, y in rows if y is not None and y < 0]
    total = prod(values)
    lines = ["x | y"]
    for x, y in rows:
        value = "не определено" if y is None else f"{y:.10g}"
        lines.append(f"{x:.8g} | {value}")
    lines.append(f"Произведение = {total}")
    text = "\n".join(lines)
    args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
