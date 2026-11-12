n = 8
m = 10
a = [
    -40, 60, 0, -14, 15, 36, 29, -33, -24, 59,
    57, 21, -35, 53, 47, 39, 24, -19, 41, 14,
    -9, 55, 12, 51, -15, 60, 48, -37, 45, -12,
    -22, -24, -13, 36, 21, 57, 9, 6, -9, 34,
    -37, -37, 54, -3, 29, 28, -25, 25, -35, 42,
    -40, 19, 36, 44, 31, 0, 0, 45, 14, 15,
    48, -15, -33, -8, -15, 39, 9, 14, 37, 26,
    -21, -33, -28, -31, -24, 29, 30, 51, 59, -35,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if x < 0:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
value = 0
for x in selected:
    value = value + x
result = None
if selected:
    result = value / len(selected)

print("Исходная матрица:")
for i in range(n):
    row = ""
    for j in range(m):
        row = row + str(a[i * m + j]) + " "
    print(row)

print("Преобразованная матрица:")
for row in transformed:
    text = ""
    for x in row:
        text = text + str(x) + " "
    print(text)
print("Среднее арифметическое = " + str(result))
