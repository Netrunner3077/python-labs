n = 7
m = 8
a = [
    -35, 35, 0, -14, -11, -14, -24, -16,
    1, -34, 21, 24, -21, -32, 31, -14,
    27, 21, 3, 28, -25, -3, -15, 6,
    4, -26, 34, 11, -31, -8, 5, 8,
    -27, 4, -23, -4, -16, 27, 1, -1,
    0, -10, -24, 28, -16, -17, 6, 26,
    -10, -19, 25, 29, -2, 30, -7, 33,
]

transformed = []
extremes = []
for i in range(n):
    low = a[i * m]
    high = low
    position = 0
    for j in range(m):
        x = a[i * m + j]
        if x < low:
            low = x
            position = j
    transformed.append([low])
    extremes.append(low)
result = max(extremes)

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
print("Максимум минимумов строк = " + str(result))
