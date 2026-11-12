import math
from typing import NoReturn

def calculate_u(x: float, y: float) -> float:
    """
    Вычисляет значение функции:
        u = (x * e^(x*y) + 4 * cos^2(x)) / (x * (x - y) * (2*x + y))

    :param x: значение переменной x
    :param y: значение переменной y
    :return: значение функции u
    :raises ValueError: если знаменатель равен нулю
    """
    denominator = x * (x - y) * (2 * x + y)

    if math.isclose(denominator, 0.0, abs_tol=1e-15):
        raise ValueError(
            "Знаменатель равен нулю. Убедитесь, что x != 0, x != y и 2*x + y != 0."
        )

    numerator = x * math.exp(x * y) + 4 * math.cos(x) ** 2
    return numerator / denominator

def input_float(prompt: str) -> float:
    """
    Запрашивает у пользователя число с плавающей точкой.
    Повторяет ввод до тех пор, пока не будет введено корректное значение.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число (например, 1.5, -2, 0.0).")

def main() -> None:
    print("Вычисление функции:")
    print("u = (x * e^(x*y) + 4 * cos^2(x)) / (x * (x - y) * (2*x + y))")
    print("-" * 60)

    x = input_float("Введите x: ")
    y = input_float("Введите y: ")

    try:
        u = calculate_u(x, y)
    except ValueError as exc:
        print(f"Ошибка вычисления: {exc}")
    else:
        print(f"Результат: u = {u:.6f}")

if __name__ == "__main__":
    main()