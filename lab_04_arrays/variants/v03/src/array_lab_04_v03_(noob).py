n = 8
m = 8
a = [
    -40, 50, 0, -24, 7, 37, 20, 40,
    34, -32, 37, -39, 20, -7, 30, -11,
    -16, 20, 29, 30, 20, 10, 41, -21,
    -11, 41, -21, 26, 9, -39, 45, -32,
    -20, 35, -35, -2, -37, -6, 20, 36,
    9, 14, 10, 33, 16, -23, 6, -28,
    -36, -23, 23, -13, -7, 46, 15, 40,
    -2, 13, 24, 9, 33, 4, 28, 34,
]

transformed = []
for i in range(n):
    first = 0
    second = 0
    for j in range(m):
        x = a[i * m + j]
        if x < 0:
            first = first + x
        if x < 0:
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
print("Сумма и количество по строкам = " + str(result))
