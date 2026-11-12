from random import Random


def make_values():
    rng = Random(24)
    values = []
    for i in range(56):
        values.append(rng.randint(-35, 35))
    return values


n = 7
m = 8
a = make_values()

transformed = []
extremes = []
for i in range(n):
    low = a[i * m]
    high = low
    position = 0
    for j in range(m):
        x = a[i * m + j]
        if x < low:
            low = x
            position = j
    transformed.append([low])
    extremes.append(low)
result = max(extremes)

lines = ["Исходная матрица:"]
for i in range(n):
    lines.append(" ".join(map(str, a[i * m:(i + 1) * m])))

lines.append("Преобразованная матрица:")
for row in transformed:
    lines.append(" ".join(map(str, row)))
lines.append(f"Максимум минимумов строк = {result}")
text = "\n".join(lines)
print(text)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
