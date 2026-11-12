n = 10
m = 9
a = [
    -30, 50, 0, 20, 31, -11, -19, -22, -28,
    21, 40, 7, -23, -2, 36, 38, 16, 5,
    -8, -17, 3, -3, -27, 3, 4, -6, -9,
    9, 7, 50, 17, -19, 47, 13, 19, 34,
    1, -8, 1, 30, 5, -19, 40, 8, -30,
    7, 43, 9, 35, -6, 22, 24, 46, 6,
    25, 27, -10, -1, 9, 3, -25, -20, -25,
    29, 50, 5, 36, 38, 30, 13, -12, -5,
    -22, 22, -5, 50, 26, 5, -7, 15, 25,
    45, 11, 41, -5, 11, -18, -23, -1, 5,
]

transformed = []
for j in range(m):
    best = a[j]
    position = 0
    for i in range(n):
        x = a[i * m + j]
        if x > best:
            best = x
            position = i
    transformed.append([best, position + 1, j + 1])
result = transformed

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
print("Максимум, строка и столбец = " + str(result))
