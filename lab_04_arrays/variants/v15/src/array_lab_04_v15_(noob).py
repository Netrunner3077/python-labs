n = 8
m = 8
a = [
    -10, 90, 0, 84, -6, 10, 20, -8,
    -3, 77, 8, 78, 37, 20, 4, 33,
    49, 80, 35, 25, 40, 23, 34, 19,
    16, 35, 30, 18, 29, 83, 55, 43,
    19, 63, 48, 43, 52, 0, 49, 62,
    36, 46, 62, 30, 78, 72, 47, 41,
    89, -2, 52, -8, 15, 7, 58, 12,
    68, 90, 78, 82, -8, 26, 57, 53,
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
