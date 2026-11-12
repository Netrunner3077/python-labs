n = 6
m = 8
a = [
    -65, 56, 0, 4, 11, 26, -43, -37,
    -49, 16, -6, 32, -12, -39, -38, -47,
    -15, -45, 42, -49, 12, -41, -40, -62,
    -13, -35, -57, -53, -12, 49, -25, 24,
    40, -49, -43, 50, 54, -1, 1, 23,
    27, 19, 37, -31, 13, -36, 52, 21,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if -10 <= x <= 10:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
value = 1
for x in selected:
    value = value * x
result = [len(selected), value]

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
print("Количество и произведение = " + str(result))
