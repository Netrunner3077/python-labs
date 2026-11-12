n = 11
m = 6
a = [
    -30, 70, 0, 48, 27, -7,
    59, -15, 64, 53, 14, -20,
    -1, 4, -24, 10, 46, -8,
    40, 57, 63, 25, 60, -24,
    43, -28, 45, 3, 9, 23,
    -6, -7, -16, 44, 37, 63,
    69, 42, -23, 59, 11, 48,
    12, 3, -7, 20, 9, 69,
    53, 35, -12, 5, 4, 55,
    58, -7, 25, -24, 13, 38,
    -26, 23, 2, 34, 6, 36,
]

transformed = []
selected = []
indices = []
for i in range(n):
    row = []
    for j in range(m):
        x = a[i * m + j]
        if -20 < x < 20:
            selected.append(x)
            indices.append(i * m + j + 1)
            row.append(x)
        else:
            row.append(0)
    transformed.append(row)
difference = None
if selected:
    difference = selected[0]
    for i in range(1, len(selected)):
        difference = difference - selected[i]
result = [len(selected), difference]

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
print("Количество и разность = " + str(result))
