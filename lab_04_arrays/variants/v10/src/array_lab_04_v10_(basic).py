from random import Random


def make_values():
    rng = Random(10)
    values = []
    for i in range(84):
        values.append(rng.randint(-20, 50))
    return values


n = 12
m = 7
a = make_values()

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if x != 0:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
first = 0
second = 0
for x in a:
    if x < 0:
        first = first + x
    if x > 0:
        second = second + 1
result = [first, second]

lines = ["Исходная матрица:"]
for i in range(n):
    lines.append(" ".join(map(str, a[i * m:(i + 1) * m])))

lines.append("Преобразованная матрица:")
for row in transformed:
    lines.append(" ".join(map(str, row)))
lines.append(f"Сумма отрицательных и количество положительных = {result}")
text = "\n".join(lines)
print(text)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
