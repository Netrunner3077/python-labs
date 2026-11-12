from random import Random


def make_values():
    rng = Random(21)
    values = []
    for i in range(70):
        values.append(rng.randint(-40, 40))
    return values


n = 10
m = 7
a = make_values()

transformed = []
lo = a[0]
hi = a[0]
for x in a:
    if x < lo:
        lo = x
    if x > hi:
        hi = x
geo = None
if lo >= 0:
    geo = (lo * hi) ** 0.5
transformed = [[lo, hi]]
result = [lo, hi, geo]

lines = ["Исходная матрица:"]
for i in range(n):
    lines.append(" ".join(map(str, a[i * m:(i + 1) * m])))

lines.append("Преобразованная матрица:")
for row in transformed:
    lines.append(" ".join(map(str, row)))
lines.append(f"Минимум, максимум и среднее геометрическое = {result}")
text = "\n".join(lines)
print(text)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
