from math import sin, sqrt


x = float(input("Введите x: "))
y = float(input("Введите y: "))
a = float(input("Введите a: "))
b = float(input("Введите b: "))

if x > 0 and y > 2:
    z = min(a * x, y, max(sqrt(x), sin(y ** 2)))
else:
    z = max(b, x, y) / min(x, y + 1)

result = f"x = {x}\ny = {y}\na = {a}\nb = {b}"
if z is None:
    result += "\nФормула для этих данных не задана."
else:
    result += f"\nРезультат = {z:.10g}"
print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
