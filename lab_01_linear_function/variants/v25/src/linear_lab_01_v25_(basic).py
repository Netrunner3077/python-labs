from math import copysign, pi, sin


def calculate(x, y):
    return x * (x - y) * (4 * x + y) / (2.7 * (x - pi)) + copysign(abs(0.2 * x / sin(y)) ** (1 / 3), 0.2 * x / sin(y))


with open("input.txt", encoding="utf-8") as file:
    x, y = map(float, file.read().replace(",", ".").split())

try:
    d = calculate(x, y)
    if isinstance(d, complex):
        raise ValueError("ожидался вещественный результат")
    result = f"Результат = {d:.4f}\nЦелая часть = {int(d)}"
except (ArithmeticError, ValueError) as error:
    result = f"Ошибка вычисления: {error}"

print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
