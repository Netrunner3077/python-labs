from math import cos, exp, log, sin
from pathlib import Path


def read_float(name: str) -> float:
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(",", "."))
        except ValueError:
            print("Введите вещественное число.")


def calculate(x: float, y: float, a: float, c: float, d: float) -> float | None:
    if 0 < x < 1 and 0 < y < 1:
        z = 2 * log(x) * max(min(x, y), sin(c * x), cos(d))
    elif x < 0 and y < 0:
        z = min(exp(x + 1), y)
    else:
        z = a + x
    if isinstance(z, complex):
        raise ValueError("ожидался вещественный результат")
    return z


def main() -> None:
    x = read_float("x")
    y = read_float("y")
    a = read_float("a")
    c = read_float("c")
    d = read_float("d")

    try:
        value = calculate(x, y, a, c, d)
    except (ArithmeticError, ValueError) as error:
        print(f"Ошибка вычисления: {error}")
        return

    result = f"x = {x}\ny = {y}\na = {a}\nc = {c}\nd = {d}"
    if value is None:
        result += "\nФормула для этих данных не задана."
    else:
        result += f"\nРезультат = {value:.10g}"
    Path("result.txt").write_text(result + "\n", encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
