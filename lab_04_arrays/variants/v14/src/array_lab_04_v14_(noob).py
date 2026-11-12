n = 10
m = 9
a = [
    -50, 20, 0, -16, -18, -13, -41, 7, -12,
    9, 0, 0, -35, -17, -22, -10, -5, -17,
    -4, 16, -31, -30, 20, -15, -29, -49, -42,
    -35, -7, -47, -40, -15, -24, -2, 1, 6,
    -38, -36, -4, -27, -38, 12, 15, -26, -16,
    7, -23, 12, -14, 14, -18, -37, -35, -39,
    -15, -15, -35, -47, -30, 2, -36, 17, -39,
    4, 11, -29, 18, -1, 8, -11, 12, 8,
    5, 3, -38, -18, 10, 0, -20, 7, 12,
    -42, -32, 12, -16, 6, -48, 1, 4, -48,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if x > 0:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
result = indices

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
print("Номера положительных элементов = " + str(result))
