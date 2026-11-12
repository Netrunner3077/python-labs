from math import pi, sin


def calculate(x, y):
    return sin(x - 7 * y) ** 2 / (2.5 * (x - pi)) * sin(pi / 4)


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
