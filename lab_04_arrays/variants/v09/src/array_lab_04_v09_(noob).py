n = 9
m = 9
a = [
    -10, 80, 0, 24, 7, 13, 76, -10, 33,
    54, 49, 67, 0, 32, 60, 68, 79, -5,
    38, 11, 80, 47, 44, 10, 11, 20, -4,
    4, 6, 54, 65, -2, 78, 39, 3, 27,
    16, 76, 18, 43, 1, 24, 16, 40, 25,
    33, -5, 15, 80, -10, 42, -3, 38, 52,
    7, -7, 20, 44, 4, 66, -10, 5, 64,
    15, 15, 32, -9, 0, 7, 59, -8, 54,
    0, 63, 53, 58, 15, 43, -2, 40, 14,
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
second = 1
for x in a:
    if x > 0:
        first = first + x
    if x < 0:
        second = second * x
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
print("Сумма положительных и произведение отрицательных = " + str(result))
