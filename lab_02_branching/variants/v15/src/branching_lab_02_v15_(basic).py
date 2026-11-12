from math import cos, exp, sin


x = float(input("Введите x: "))
y = float(input("Введите y: "))
a = float(input("Введите a: "))

if x < 1 and y > 1:
    z = max(2 * sin(x), 3 * min(x, y), x + a)
elif x > 1 and y > 1:
    z = min((x + exp(2 * x + a)) / 3, max(x, y))
else:
    z = 4 * cos(x * y)

result = f"x = {x}\ny = {y}\na = {a}"
if z is None:
    result += "\nФормула для этих данных не задана."
else:
    result += f"\nРезультат = {z:.10g}"
print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
