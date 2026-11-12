n = 12
m = 7
a = [
    -70, 10, 0, -24, -33, -48, -1,
    -35, -56, -67, -39, -21, -17, -38,
    -6, -30, -19, -53, 0, -63, -53,
    -45, -51, -2, 1, -44, -28, -1,
    -55, -62, -31, -18, -60, -6, -10,
    6, -52, -18, -6, -27, -68, -15,
    -23, 3, -64, -25, -64, -9, -23,
    4, -70, -19, -40, -56, 1, -43,
    -39, -3, -24, -63, -36, -62, -35,
    -46, 7, 1, -2, 0, -54, -38,
    -31, -26, -30, -49, -28, -58, 3,
    4, -36, -28, -69, -64, -26, -68,
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
value = 1
for x in selected:
    value = value * x
result = None
if selected:
    result = value ** (1 / len(selected))

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
print("Среднее геометрическое = " + str(result))
