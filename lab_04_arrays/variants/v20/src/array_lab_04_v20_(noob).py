n = 9
m = 9
a = [
    -60, 30, 0, 26, 21, -48, -19, 13, -39,
    -57, -8, -8, -51, -47, -44, -20, 0, 14,
    -3, -8, -34, -35, -20, 20, 27, -18, -18,
    -6, -49, 20, 6, 2, -9, -50, -34, 13,
    -29, -56, -35, -48, -50, -36, -28, 28, -24,
    -21, 28, -28, -40, 19, -45, -58, -26, 30,
    -31, -32, 13, -30, -53, -59, 22, 19, -22,
    -25, -43, 28, 22, -18, 16, -3, -41, 21,
    -25, 11, -5, -40, -39, -9, 30, -45, 28,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if x >= 0:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
first = 0
second = 0
for x in a:
    if x == 0:
        first = first + 1
    if x > 0:
        second = second + x
result = [first, second]

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
print("Количество нулей и сумма положительных = " + str(result))
