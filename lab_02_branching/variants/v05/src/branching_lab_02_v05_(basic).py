from math import exp, log, sin


x = float(input("Введите x: "))
y = float(input("Введите y: "))

if 2 < x + y < 3:
    z = 4 * min(5 ** (3 + x), x + y, -4 * y)
elif x + y > 3:
    z = max(exp(x - y), 3 * log(x), min(x, y))
else:
    z = 2.5 * sin(x * y) * max(x, y)

result = f"x = {x}\ny = {y}"
if z is None:
    result += "\nФормула для этих данных не задана."
else:
    result += f"\nРезультат = {z:.10g}"
print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
