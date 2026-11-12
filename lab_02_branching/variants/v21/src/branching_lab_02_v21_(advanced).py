from math import sin
from pathlib import Path


def read_float(name: str) -> float:
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(",", "."))
        except ValueError:
            print("Введите вещественное число.")


def calculate(x: float, b: float, c: float) -> float | None:
    if c > 0 and x > 2:
        z = max(c, x / c, sin(c))
    elif c < 0 and x > 2:
        z = min(c, c * x + sin(b), max(c, b))
    else:
        z = max(c, b)
    if isinstance(z, complex):
        raise ValueError("ожидался вещественный результат")
    return z


def main() -> None:
    x = read_float("x")
    b = read_float("b")
    c = read_float("c")

    try:
        value = calculate(x, b, c)
    except (ArithmeticError, ValueError) as error:
        print(f"Ошибка вычисления: {error}")
        return

    result = f"x = {x}\nb = {b}\nc = {c}"
    if value is None:
        result += "\nФормула для этих данных не задана."
    else:
        result += f"\nРезультат = {value:.10g}"
    Path("result.txt").write_text(result + "\n", encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
