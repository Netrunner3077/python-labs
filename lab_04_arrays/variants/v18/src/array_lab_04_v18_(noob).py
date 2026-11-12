n = 10
m = 7
a = [
    -30, 20, 0, -2, -9, -15, -18,
    1, 10, 1, -19, 0, -12, -1,
    -14, -18, -14, 14, -23, -10, 3,
    13, 18, 20, -19, -15, -20, -15,
    -18, 17, -7, 6, 2, -18, 13,
    18, 1, -17, 15, -11, -14, -30,
    -9, -5, -16, 19, 16, -5, 4,
    -8, 7, 6, 3, -13, -13, 8,
    15, -11, 5, -23, -12, 0, 6,
    2, -21, 1, 13, 20, 10, 20,
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
result = value ** 0.5

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
print("Норма = " + str(result))
