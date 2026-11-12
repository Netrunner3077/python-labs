n = 9
m = 8
a = [
    -40, 60, 0, 47, -17, 43, -11, 45,
    -22, -12, 42, 53, -17, -24, -31, 28,
    -13, 55, -3, -37, 15, -24, 47, 37,
    -39, -5, -22, -30, -7, 17, 55, 15,
    -23, -8, 5, -11, 22, 56, 30, 32,
    14, 45, 6, 15, 41, 0, 43, -25,
    4, 36, 41, -7, 48, 17, 30, 38,
    55, -23, 16, 46, 53, 16, 28, -18,
    -3, -15, -18, 26, 5, -8, 7, 18,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if x < -20 or x > 30:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
value = 0
for x in selected:
    value = value + x
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
print("Количество и сумма = " + str(result))
