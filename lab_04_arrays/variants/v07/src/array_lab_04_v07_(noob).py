n = 15
m = 8
a = [
    -70, 70, 0, -58, -52, 67, -46, 23,
    -56, 59, -16, -61, -48, 41, 37, -53,
    -9, -47, 38, -55, -39, -13, -55, 31,
    -58, -14, -59, -36, 4, 37, -34, 68,
    -40, 8, -24, -44, -22, 25, -46, 70,
    -54, -55, -18, 57, 66, 39, 10, 49,
    46, 22, 6, -7, -24, -8, -50, 6,
    64, 56, 17, 44, 3, -52, -40, 61,
    37, -28, 17, -32, 55, 37, -60, -51,
    10, 17, 19, 57, 46, -53, -47, -1,
    51, -54, -55, 9, 44, 2, 28, 18,
    -65, 48, 20, -27, -41, 56, -55, -15,
    3, -37, -7, 31, 30, 57, -50, -28,
    44, 32, 70, 1, -35, 40, 70, 1,
    36, 21, 27, -11, -32, -49, -25, -32,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if x > 0:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
value = 0
for x in selected:
    value = value + x
result = None
if selected:
    result = value / len(selected)

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
print("Среднее арифметическое = " + str(result))
