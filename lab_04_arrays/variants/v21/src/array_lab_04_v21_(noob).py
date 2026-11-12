n = 10
m = 7
a = [
    -40, 40, 0, -4, 21, -13, 20,
    25, -17, 24, 27, -10, -40, -39,
    7, 34, 14, -32, -22, -11, -11,
    -35, 15, 12, 38, 16, -36, 2,
    29, 23, -26, 7, -38, -21, -29,
    -25, -38, 18, -20, 30, 3, 11,
    22, -21, -17, -36, 20, -10, -31,
    -15, -14, 34, -31, -25, 31, 20,
    31, 9, -15, 3, -22, 28, 12,
    -3, 6, 17, 24, 9, 0, 22,
]

transformed = []
lo = a[0]
hi = a[0]
for x in a:
    if x < lo:
        lo = x
    if x > hi:
        hi = x
geo = None
if lo >= 0:
    geo = (lo * hi) ** 0.5
transformed = [[lo, hi]]
result = [lo, hi, geo]

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
print("Минимум, максимум и среднее геометрическое = " + str(result))
