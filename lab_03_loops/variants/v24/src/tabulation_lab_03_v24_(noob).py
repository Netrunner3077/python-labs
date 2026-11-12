from math import pi, sin


a = -pi
b = pi
h = pi/4
n = int((b - a) / h + 1e-9) + 1
total = 0.0

print("x | y")
for i in range(n):
    x = a + i * h
    y = 1 / (x + 2 * pi) - sin(x)
    if y is None:
        print(str(x) + " | не определено")
    else:
        print(str(x) + " | " + str(y))
        if y < 0:
            total = total + y

print("Сумма = " + str(total))
