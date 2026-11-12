from math import cos, sqrt


def calculate(x, y):
    return (sqrt(abs(x ** 3 - 3.4e-3 * y)) + x ** 2 * y) / (3 * cos(x * y))


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
