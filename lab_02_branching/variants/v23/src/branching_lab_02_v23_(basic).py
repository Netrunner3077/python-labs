from math import log10


x = float(input("Введите x: "))
y = float(input("Введите y: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))

if x * y > 3:
    z = x ** 3 + log10(x * y) ** (c * d)
elif 2 < x * y < 3:
    z = 3 * min(x, y, max(c * x, d * y))
elif x * y < 2:
    z = 2 ** (c * d) - x
else:
    z = None

result = f"x = {x}\ny = {y}\nc = {c}\nd = {d}"
if z is None:
    result += "\nФормула для этих данных не задана."
else:
    result += f"\nРезультат = {z:.10g}"
print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
