from math import exp


a = -2
b = 2
h = .25
n = int((b - a) / h + 1e-9) + 1
total = 1.0

print("x | y")
for i in range(n):
    x = round(a + i * h, 12)
    if x > 2:
        y = exp(x)
    elif -2 < x < 2:
        y = x + 4
    elif x < -2:
        y = 0
    else:
        y = None
    if y is None:
        print(str(x) + " | не определено")
    else:
        print(str(x) + " | " + str(y))
        if y > 0:
            total = total * y

print("Произведение = " + str(total))
