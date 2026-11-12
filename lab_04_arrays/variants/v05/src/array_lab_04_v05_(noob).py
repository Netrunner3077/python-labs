n = 8
m = 9
a = [
    -20, 80, 0, 25, 68, 74, 63, 47, -17,
    39, 79, 11, 63, -14, 0, -6, 27, 40,
    11, 28, 49, -7, 53, 11, -19, 73, 7,
    32, 15, 3, 78, 29, 0, 77, -11, -3,
    59, 59, 36, -4, -4, -20, -20, 6, 79,
    7, 1, 1, 17, 20, 5, 49, 66, 60,
    6, 3, 68, 5, 29, 18, -18, 26, 33,
    1, -2, 13, -12, 22, 18, 57, 55, -20,
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
    transformed.append([low, i + 1, position + 1])
    extremes.append(low)
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
print("Минимум, строка и столбец = " + str(result))
