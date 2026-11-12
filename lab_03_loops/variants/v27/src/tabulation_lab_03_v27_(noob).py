from math import exp


a = .1
b = 1.5
h = .1
n = int((b - a) / h + 1e-9) + 1
total = None

print("x | y")
for i in range(n):
    x = round(a + i * h, 12)
    y = x * exp(-x)
    if y is None:
        print(str(x) + " | не определено")
    else:
        print(str(x) + " | " + str(y))
        if total is None or y < total:
            total = y

print("Минимум = " + str(total))
