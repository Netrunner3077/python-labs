n = 8
m = 7
a = [
    -50, 50, 0, -34, -26, 40, -45,
    -40, -33, -19, 14, -24, 1, 32,
    -47, 8, 12, 8, -1, 13, 23,
    -26, 1, -39, 12, -21, 47, -48,
    39, -16, 16, 2, 10, -2, 42,
    -36, 34, -17, -38, -42, -1, 29,
    -2, -37, 34, -43, -7, -20, 38,
    -39, 13, 33, 16, -24, 24, -32,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if -10 <= x <= 10:
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
