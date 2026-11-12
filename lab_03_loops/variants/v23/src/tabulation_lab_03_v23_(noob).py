from math import cos, sin


a = -4
b = 4
h = .6
n = int((b - a) / h + 1e-9) + 1
total = 1.0

print("x | y")
for i in range(n):
    x = round(a + i * h, 12)
    if -1 < x < 1:
        y = sin(x)
    else:
        y = 5 * cos(x)
    if y is None:
        print(str(x) + " | не определено")
    else:
        print(str(x) + " | " + str(y))
        if y < 0:
            total = total * y

print("Произведение = " + str(total))
