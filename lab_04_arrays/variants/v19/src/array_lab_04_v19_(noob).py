n = 7
m = 8
a = [
    -50, 10, 0, 7, -17, -43, -18, -38,
    -25, -28, -17, -32, -13, -41, -12, -34,
    -44, -34, -24, -30, -33, 3, -44, -1,
    -30, 7, -31, -49, -14, -11, -38, 6,
    -46, 8, -38, -43, -16, -21, -26, 5,
    -4, -46, 1, -44, -24, -49, -44, -13,
    -4, -23, -2, 4, -25, -22, -8, -31,
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
value = 0
for x in selected:
    value = value + x * x
result = value

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
print("Сумма квадратов = " + str(result))
