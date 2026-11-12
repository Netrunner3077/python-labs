n = 11
m = 9
a = [
    -20, 70, 0, 15, 16, 5, -11, -12, 12,
    49, 22, 12, 27, 31, 3, 11, 10, 42,
    -11, 61, 53, 63, -10, 58, 34, 33, -14,
    64, 36, 24, -19, 62, 41, 12, -3, 58,
    23, 58, 63, 9, 70, 47, -2, -8, 30,
    18, -16, 67, 47, -10, 1, 38, 70, -1,
    13, 49, -14, 2, 63, -19, 37, -1, 24,
    53, 53, 33, -12, 19, 36, 39, 25, -19,
    26, 0, 13, 2, 41, 25, 46, -13, 46,
    11, 1, 6, 42, 51, -9, 22, 23, -13,
    30, 23, 61, -6, 18, 12, 51, 69, 68,
]

transformed = []
extremes = []
for i in range(n):
    low = a[i * m]
    high = low
    position = 0
    for j in range(m):
        x = a[i * m + j]
        if x > low:
            low = x
            position = j
    transformed.append([low])
    extremes.append(low)
result = min(extremes)

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
print("Минимум максимумов строк = " + str(result))
