x = float(input("Введите x: "))
y = float(input("Введите y: "))
a = float(input("Введите a: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))

if x > 3 and x * y < 2:
    z = max(3 ** (x + a), c + d, min(x, a))
elif x > 3 and x * y > 2:
    z = min(x, a, c, y, d)
else:
    z = 3 * c + d * x

result = f"x = {x}\ny = {y}\na = {a}\nc = {c}\nd = {d}"
if z is None:
    result += "\nФормула для этих данных не задана."
else:
    result += f"\nРезультат = {z:.10g}"
print(result)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result + "\n")
