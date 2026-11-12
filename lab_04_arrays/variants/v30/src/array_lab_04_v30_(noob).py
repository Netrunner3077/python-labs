n = 8
m = 11
a = [
    -50, 40, 0, -47, 29, 33, -24, -18, -44, 0, -2,
    32, -33, -40, 9, -50, 16, -19, -47, -41, -30, 26,
    17, 1, 33, -6, 18, -42, 1, -47, -19, 22, 36,
    -15, 4, 22, -38, 36, -15, 31, 21, -36, 28, 13,
    -11, -34, -11, -11, -18, 14, -40, -33, -19, 39, -10,
    -35, -47, 2, 14, -12, -28, 17, 32, -27, 10, 32,
    -8, 15, 7, 34, -8, 16, -7, -42, -48, 33, -37,
    10, 12, -17, 11, -18, 24, -18, 38, 36, -29, 37,
]

transformed = []
for i in range(m):
    first = 0
    second = 0
    for j in range(n):
        x = a[j * m + i]
        if x < 0:
            first = first + x
        if x > 0:
            second = second + 1
    transformed.append([first, second])
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
print("Сумма и количество по столбцам = " + str(result))
