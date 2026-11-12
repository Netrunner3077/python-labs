from random import Random


def make_values():
    rng = Random(30)
    values = []
    for i in range(88):
        values.append(rng.randint(-50, 40))
    return values


n = 8
m = 11
a = make_values()

transformed = []
for i in range(m):
    first = 0
    second = 0
    for j in range(n):
        x = a[j * m + i]
        if x < 0:
            first = first + x
        if x > 0:
            second = second + 1
    transformed.append([first, second])
result = transformed

lines = ["Исходная матрица:"]
for i in range(n):
    lines.append(" ".join(map(str, a[i * m:(i + 1) * m])))

lines.append("Преобразованная матрица:")
for row in transformed:
    lines.append(" ".join(map(str, row)))
lines.append(f"Сумма и количество по столбцам = {result}")
text = "\n".join(lines)
print(text)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
