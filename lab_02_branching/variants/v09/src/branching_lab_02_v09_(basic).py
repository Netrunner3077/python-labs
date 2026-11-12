from math import exp, log, sqrt


x = float(input("Введите x: "))
y = float(input("Введите y: "))
a = float(input("Введите a: "))
b = float(input("Введите b: "))

if x * y > 0:
    z = 1 - exp(x * y + a * b)
elif x * y == 0:
    z = b - min(a * x, y)
else:
    z = max(x ** 3, exp(y), sqrt(abs(log(y ** 2))))

result = f"x = {x}\ny = {y}\na = {a}\nb = {b}"
if z is None:
    result += "\nФормула для этих данных не задана."
else:
    result += f"\nРезультат = {z:.10g}"
print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
