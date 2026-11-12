from math import sin, sqrt
from pathlib import Path


def read_float(name: str) -> float:
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(",", "."))
        except ValueError:
            print("Введите вещественное число.")


def calculate(x: float, y: float, a: float, b: float) -> float | None:
    if x > 0 and y > 2:
        z = min(a * x, y, max(sqrt(x), sin(y ** 2)))
    else:
        z = max(b, x, y) / min(x, y + 1)
    if isinstance(z, complex):
        raise ValueError("ожидался вещественный результат")
    return z


def main() -> None:
    x = read_float("x")
    y = read_float("y")
    a = read_float("a")
    b = read_float("b")

    try:
        value = calculate(x, y, a, b)
    except (ArithmeticError, ValueError) as error:
        print(f"Ошибка вычисления: {error}")
        return

    result = f"x = {x}\ny = {y}\na = {a}\nb = {b}"
    if value is None:
        result += "\nФормула для этих данных не задана."
    else:
        result += f"\nРезультат = {value:.10g}"
    Path("result.txt").write_text(result + "\n", encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
