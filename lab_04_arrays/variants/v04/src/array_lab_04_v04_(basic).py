from random import Random


def make_values():
    rng = Random(4)
    values = []
    for i in range(90):
        values.append(rng.randint(-30, 50))
    return values


n = 10
m = 9
a = make_values()

transformed = []
for j in range(m):
    best = a[j]
    position = 0
    for i in range(n):
        x = a[i * m + j]
        if x > best:
            best = x
            position = i
    transformed.append([best, position + 1, j + 1])
result = transformed

lines = ["Исходная матрица:"]
for i in range(n):
    lines.append(" ".join(map(str, a[i * m:(i + 1) * m])))

lines.append("Преобразованная матрица:")
for row in transformed:
    lines.append(" ".join(map(str, row)))
lines.append(f"Максимум, строка и столбец = {result}")
text = "\n".join(lines)
print(text)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
