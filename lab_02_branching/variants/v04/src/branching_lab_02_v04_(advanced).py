from math import sin
from pathlib import Path


def read_float(name: str) -> float:
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(",", "."))
        except ValueError:
            print("Введите вещественное число.")


def calculate(x: float, a: float, b: float) -> float | None:
    if a > 0 and x > 1:
        z = max(a, x / a, sin(a) ** 2)
    elif a < 0 and x > 1:
        z = min(a, a * x + sin(b), max(a, b))
    else:
        z = max(a, b)
    if isinstance(z, complex):
        raise ValueError("ожидался вещественный результат")
    return z


def main() -> None:
    x = read_float("x")
    a = read_float("a")
    b = read_float("b")

    try:
        value = calculate(x, a, b)
    except (ArithmeticError, ValueError) as error:
        print(f"Ошибка вычисления: {error}")
        return

    result = f"x = {x}\na = {a}\nb = {b}"
    if value is None:
        result += "\nФормула для этих данных не задана."
    else:
        result += f"\nРезультат = {value:.10g}"
    Path("result.txt").write_text(result + "\n", encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
