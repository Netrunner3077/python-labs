n = 7
m = 8
a = [
    -30, 60, 0, 46, 47, 6, -19, 35,
    14, 20, 23, -28, -26, -17, 26, 53,
    -2, 14, -20, 33, 12, 47, 39, 23,
    -5, 27, -9, -2, 25, 22, 56, 57,
    42, 37, -5, 39, 56, 24, 8, 5,
    35, -2, 22, 30, 36, -12, 9, 8,
    45, 60, 52, 30, 20, 49, -18, 17,
]

transformed = []
for i in range(n):
    first = 0
    second = 1
    for j in range(m):
        x = a[i * m + j]
        if x > 0:
            first = first + x
        if x < 0:
            second = second * x
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
print("Сумма и произведение по строкам = " + str(result))
