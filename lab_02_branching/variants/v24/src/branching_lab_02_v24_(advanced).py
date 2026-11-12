from math import exp, log, sqrt
from pathlib import Path


def read_float(name: str) -> float:
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(",", "."))
        except ValueError:
            print("Введите вещественное число.")


def calculate(x: float, y: float, a: float, b: float) -> float | None:
    if x * y > 0:
        z = 1 - exp(x * y + a * b)
    elif x * y == 0:
        z = b - min(a * x, y)
    else:
        z = max(x ** 3, exp(y), sqrt(abs(log(y ** 2))))
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
