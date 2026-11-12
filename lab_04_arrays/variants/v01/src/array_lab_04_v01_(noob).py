n = 10
m = 8
a = [
    -30, 20, 0, -26, -14, -23, 1, 18,
    -2, 0, 11, -6, 20, -17, -24, 1,
    -29, -6, -3, 8, 18, 19, -30, 14,
    -2, -13, 16, -16, 7, -24, -10, -29,
    -29, -29, 11, 4, -30, -6, 13, -17,
    -3, 16, -29, 3, -16, 18, -2, 1,
    5, -16, -8, -16, 13, -16, 18, -1,
    -12, -29, -4, 5, 11, -24, -19, 10,
    16, -12, -23, 17, -9, 16, 15, 2,
    -3, 2, 12, -18, -11, -12, 7, 1,
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
        if x > high:
            high = x
    transformed.append([high - low])
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
print("Разность по строкам = " + str(result))
