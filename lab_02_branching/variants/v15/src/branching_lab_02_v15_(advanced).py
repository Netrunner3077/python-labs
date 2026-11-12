from math import cos, exp, sin
from pathlib import Path


def read_float(name: str) -> float:
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(",", "."))
        except ValueError:
            print("Введите вещественное число.")


def calculate(x: float, y: float, a: float) -> float | None:
    if x < 1 and y > 1:
        z = max(2 * sin(x), 3 * min(x, y), x + a)
    elif x > 1 and y > 1:
        z = min((x + exp(2 * x + a)) / 3, max(x, y))
    else:
        z = 4 * cos(x * y)
    if isinstance(z, complex):
        raise ValueError("ожидался вещественный результат")
    return z


def main() -> None:
    x = read_float("x")
    y = read_float("y")
    a = read_float("a")

    try:
        value = calculate(x, y, a)
    except (ArithmeticError, ValueError) as error:
        print(f"Ошибка вычисления: {error}")
        return

    result = f"x = {x}\ny = {y}\na = {a}"
    if value is None:
        result += "\nФормула для этих данных не задана."
    else:
        result += f"\nРезультат = {value:.10g}"
    Path("result.txt").write_text(result + "\n", encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
