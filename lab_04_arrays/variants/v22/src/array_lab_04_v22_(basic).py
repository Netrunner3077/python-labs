from random import Random


def make_values():
    rng = Random(22)
    values = []
    for i in range(66):
        values.append(rng.randint(-30, 70))
    return values


n = 11
m = 6
a = make_values()

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if -20 < x < 20:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
difference = None
if selected:
    difference = selected[0]
    for i in range(1, len(selected)):
        difference = difference - selected[i]
result = [len(selected), difference]

lines = ["Исходная матрица:"]
for i in range(n):
    lines.append(" ".join(map(str, a[i * m:(i + 1) * m])))

lines.append("Преобразованная матрица:")
for row in transformed:
    lines.append(" ".join(map(str, row)))
lines.append(f"Количество и разность = {result}")
text = "\n".join(lines)
print(text)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
