from math import sin


x = float(input("Введите x: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

if c > 0 and x > 2:
    z = max(c, x / c, sin(c))
elif c < 0 and x > 2:
    z = min(c, c * x + sin(b), max(c, b))
else:
    z = max(c, b)

result = f"x = {x}\nb = {b}\nc = {c}"
if z is None:
    result += "\nФормула для этих данных не задана."
else:
    result += f"\nРезультат = {z:.10g}"
print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
