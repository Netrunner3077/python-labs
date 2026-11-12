from pathlib import Path


def read_float(name: str) -> float:
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(",", "."))
        except ValueError:
            print("Введите вещественное число.")


def calculate(x: float, y: float, a: float, c: float, d: float) -> float | None:
    if x > 3 and x * y < 2:
        z = max(3 ** (x + a), c + d, min(x, a))
    elif x > 3 and x * y > 2:
        z = min(x, a, c, y, d)
    else:
        z = 3 * c + d * x
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
