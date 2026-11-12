from math import cos, sin


x = float(input("Введите x: "))
a = float(input("Введите a: "))
b = float(input("Введите b: "))

if a > 0 and x > 1:
    z = max(a, x / a, cos(a))
elif a < 0 and x > 1:
    z = min(a, a * x + sin(b), max(a, b))
else:
    z = max(a, b)

result = f"x = {x}\na = {a}\nb = {b}"
if z is None:
    result += "\nФормула для этих данных не задана."
else:
    result += f"\nРезультат = {z:.10g}"
print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
