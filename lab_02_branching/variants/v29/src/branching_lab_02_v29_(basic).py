from math import cos, exp, log, sin


x = float(input("Введите x: "))
y = float(input("Введите y: "))
a = float(input("Введите a: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))

if 0 < x < 1 and 0 < y < 1:
    z = 2 * log(x) * max(min(x, y), sin(c * x), cos(d))
elif x < 0 and y < 0:
    z = min(exp(x + 1), y)
else:
    z = a + x

result = f"x = {x}\ny = {y}\na = {a}\nc = {c}\nd = {d}"
if z is None:
    result += "\nФормула для этих данных не задана."
else:
    result += f"\nРезультат = {z:.10g}"
print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
