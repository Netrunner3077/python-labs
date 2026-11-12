from math import exp, log, sin
from pathlib import Path


def read_float(name: str) -> float:
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(",", "."))
        except ValueError:
            print("Введите вещественное число.")


def calculate(x: float, y: float) -> float | None:
    if 2 < x + y < 3:
        z = 4 * min(5 ** (2 + x), x + y, -4 * y)
    elif x + y > 3:
        z = max(exp(x - y), 3 * log(x), min(x, y))
    else:
        z = 3.2 * sin(x * y) * max(x, y)
    if isinstance(z, complex):
        raise ValueError("ожидался вещественный результат")
    return z


def main() -> None:
    x = read_float("x")
    y = read_float("y")

    try:
        value = calculate(x, y)
    except (ArithmeticError, ValueError) as error:
        print(f"Ошибка вычисления: {error}")
        return

    result = f"x = {x}\ny = {y}"
    if value is None:
        result += "\nФормула для этих данных не задана."
    else:
        result += f"\nРезультат = {value:.10g}"
    Path("result.txt").write_text(result + "\n", encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
