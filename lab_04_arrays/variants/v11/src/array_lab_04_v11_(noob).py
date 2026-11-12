n = 10
m = 6
a = [
    -10, 70, 0, 47, 55, 65,
    14, 13, 55, 50, 70, 68,
    13, 2, 47, 28, 8, 1,
    58, -5, 66, 40, 47, 68,
    10, 69, -9, 57, -2, -3,
    -6, 14, 20, 66, -7, 49,
    31, 46, 65, 15, 56, 19,
    27, 53, -10, 0, 48, 25,
    42, 60, 0, 22, 30, 19,
    55, 26, -7, -2, 62, 3,
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
print("Номера отрицательных элементов = " + str(result))
