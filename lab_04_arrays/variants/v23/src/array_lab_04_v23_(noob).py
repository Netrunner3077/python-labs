n = 9
m = 9
a = [
    -42, 42, 0, 33, -3, 12, 6, 25, 3,
    -26, -18, -8, 14, -41, -14, 37, 16, -39,
    -29, -32, 21, 11, -40, 23, 38, 13, 3,
    -35, -16, -38, 33, 5, 42, -20, 37, -15,
    4, 30, 5, 31, -6, 42, -2, 31, -32,
    18, -20, 19, 33, 15, 40, -22, -19, -20,
    26, -1, 24, -17, 32, -28, -32, -30, 12,
    -38, 30, -7, 31, -7, 33, 0, -29, 5,
    -6, 27, -3, 16, 28, -15, -9, -23, -29,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if i == j:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
value = 1
for x in selected:
    value = value * x
result = [value, len(selected)]

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
print("Произведение и количество = " + str(result))
