n = 10
m = 8
a = [
    -10, 60, 0, 26, 43, 19, 47, -10,
    42, 23, 20, 18, -9, 27, 28, 32,
    8, 29, -8, 18, 22, -8, 9, -7,
    49, 48, 27, 18, 29, 36, 23, 43,
    1, 34, 53, 44, 56, 12, 27, -5,
    26, 0, -10, 56, 37, 20, 52, 9,
    29, 28, 30, 48, 48, -2, 11, 51,
    -9, 46, 52, -9, 50, 5, 48, 0,
    53, -8, 8, 19, 41, 37, -6, 59,
    -5, 41, 30, 51, 55, -1, 19, 30,
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
