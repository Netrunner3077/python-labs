from math import cos, sin


a = -4
b = 4
h = .5
n = int((b - a) / h + 1e-9) + 1
total = 0.0

print("x | y")
for i in range(n):
    x = round(a + i * h, 12)
    if x < 0:
        y = x ** 2 - 1
    elif 0 < x < 1.5:
        y = cos(x)
    elif x > 1.5:
        y = sin(x - 1)
    else:
        y = None
    if y is None:
        print(str(x) + " | не определено")
    else:
        print(str(x) + " | " + str(y))
        if y < 0:
            total = total + y

print("Сумма = " + str(total))
