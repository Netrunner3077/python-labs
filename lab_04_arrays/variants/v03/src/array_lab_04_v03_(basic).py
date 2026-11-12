from random import Random


def make_values():
    rng = Random(3)
    values = []
    for i in range(64):
        values.append(rng.randint(-40, 50))
    return values


n = 8
m = 8
a = make_values()

transformed = []
for i in range(n):
    first = 0
    second = 0
    for j in range(m):
        x = a[i * m + j]
        if x < 0:
            first = first + x
        if x < 0:
            second = second + 1
    transformed.append([first, second])
result = transformed

lines = ["Исходная матрица:"]
for i in range(n):
    lines.append(" ".join(map(str, a[i * m:(i + 1) * m])))

lines.append("Преобразованная матрица:")
for row in transformed:
    lines.append(" ".join(map(str, row)))
lines.append(f"Сумма и количество по строкам = {result}")
text = "\n".join(lines)
print(text)
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
