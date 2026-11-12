from math import exp


a = -3
b = 3
h = .3
n = int((b - a) / h + 1e-9) + 1
total = 1.0

print("x | y")
for i in range(n):
    x = round(a + i * h, 12)
    if x > 1:
        y = exp(x)
    elif x < 0:
        y = 2 * x - 1
    else:
        y = -1
    if y is None:
        print(str(x) + " | не определено")
    else:
        print(str(x) + " | " + str(y))
        if y < 0:
            total = total * y

print("Произведение = " + str(total))
