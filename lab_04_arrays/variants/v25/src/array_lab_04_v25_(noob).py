n = 8
m = 8
a = [
    -60, 10, 0, -21, 0, -55, -28, -56,
    -21, -6, -48, -45, -35, 5, -20, -37,
    10, -15, 5, 0, 7, -47, -48, -15,
    -7, -15, -36, -40, -2, -51, -51, -9,
    -52, 5, -44, -55, 9, -38, -51, -32,
    -6, -3, -5, 3, 4, 1, -4, -53,
    3, -24, -39, -54, -8, -12, -2, -58,
    1, -32, -6, -16, -52, -44, -45, -49,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if -30 <= x <= 30:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
value = 1
for x in selected:
    value = value * x
result = [len(selected), value]

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
print("Количество и произведение = " + str(result))
