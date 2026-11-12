n = 8
m = 8
a = [
    -60, 40, 0, 7, 25, -16, -42, -12,
    -59, -13, 1, -25, 22, -2, 28, 16,
    -31, 11, -60, 24, 19, -42, -4, -13,
    -40, -17, -34, -53, 13, -35, -51, 5,
    27, -17, 27, -9, -49, -58, -53, 24,
    5, -32, -49, -6, -4, -46, 24, -6,
    -43, 9, -20, 19, 11, -40, 29, -54,
    11, -39, 4, -50, -9, 17, -7, 25,
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
    value = value + abs(x)
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
print("Сумма модулей = " + str(result))
