n = 12
m = 7
a = [
    -20, 50, 0, -19, 6, 39, 42,
    15, 0, -16, 46, 42, 21, -11,
    11, 26, -15, 33, -3, 25, 28,
    33, 16, 13, 38, 2, 18, 26,
    -3, 38, 10, 36, 28, -15, -20,
    10, -3, 4, 18, 48, 26, 10,
    20, 50, 37, 35, 40, -12, 21,
    44, 0, 8, 32, 10, -16, -16,
    43, 18, -11, 48, -10, -1, 29,
    27, -1, -6, -8, 36, 1, 4,
    24, 35, 33, 37, 11, 15, -2,
    46, 2, -5, 14, 38, 18, 1,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if x != 0:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
first = 0
second = 0
for x in a:
    if x < 0:
        first = first + x
    if x > 0:
        second = second + 1
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
print("Сумма отрицательных и количество положительных = " + str(result))
