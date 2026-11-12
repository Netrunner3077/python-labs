n = 10
m = 6
a = [
    -30, 70, 0, 16, -9, 64,
    55, 9, 2, 47, -3, 47,
    -26, 44, 57, -10, 25, 51,
    20, 62, 35, 17, 39, 26,
    34, 4, -26, -27, 16, 29,
    10, 18, 24, 37, -9, 41,
    -8, 0, -1, -27, -8, 11,
    -8, -13, 35, 35, 16, 35,
    56, 41, -7, 27, 23, 64,
    37, 67, 16, 45, 15, 16,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if -5 <= x <= 15:
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
