from math import log10
from pathlib import Path


def read_float(name: str) -> float:
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(",", "."))
        except ValueError:
            print("Введите вещественное число.")


def calculate(x: float, y: float, c: float, d: float) -> float | None:
    if x * y > 3:
        z = x ** 3 + log10(x * y) ** (c * d)
    elif 2 < x * y < 3:
        z = 3 * min(x, y, max(c * x, d * y))
    elif x * y < 2:
        z = 2 ** (c * d) - x
    else:
        z = None
    if isinstance(z, complex):
        raise ValueError("ожидался вещественный результат")
    return z


def main() -> None:
    x = read_float("x")
    y = read_float("y")
    c = read_float("c")
    d = read_float("d")

    try:
        value = calculate(x, y, c, d)
    except (ArithmeticError, ValueError) as error:
        print(f"Ошибка вычисления: {error}")
        return

    result = f"x = {x}\ny = {y}\nc = {c}\nd = {d}"
    if value is None:
        result += "\nФормула для этих данных не задана."
    else:
        result += f"\nРезультат = {value:.10g}"
    Path("result.txt").write_text(result + "\n", encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
