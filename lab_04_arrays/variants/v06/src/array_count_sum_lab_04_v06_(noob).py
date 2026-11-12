a = [
    -11, -10, 30, 31, -40, 60, 0,
    -25, 37, 21, 5, -28, -28, -20,
    -21, 8, -20, 38, 28, 15, -33,
    12, 50, -3, -18, 22, 43, 6,
    30, -9, -10, 32, 10, -23, 18,
    24, 9, 41, -17, 13, -31, 26,
    -19, 57, -8, -4, 5, -16, 36,
    19, -12, -20, 39, 21, 25, -26,
    -27, 42, 11, 14, 56, -10, 2,
    -29, 27, -14, 44, 29, 33, -30,
]

print("Исходная матрица:")
for i in range(10):
    row = ""
    for j in range(7):
        row = row + str(a[i * 7 + j]) + " "
    print(row)

count = 0
total = 0
print("Преобразованная матрица:")
for i in range(10):
    row = ""
    for j in range(7):
        x = a[i * 7 + j]
        if x < -10 or x > 30:
            count = count + 1
            total = total + x
        else:
            x = 0
        row = row + str(x) + " "
    print(row)

print("Количество = " + str(count))
print("Сумма = " + str(total))
