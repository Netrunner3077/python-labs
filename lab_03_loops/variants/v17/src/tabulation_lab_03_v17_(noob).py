a = -2
b = 0
h = .1
n = int((b - a) / h + 1e-9) + 1
total = 1.0

print("x | y")
for i in range(n):
    x = round(a + i * h, 12)
    y = x ** 4 + x ** 3 - 10 * x ** 2 - 34 * x - 25
    if y is None:
        print(str(x) + " | не определено")
    else:
        print(str(x) + " | " + str(y))
        if y < 0:
            total = total * y

print("Произведение = " + str(total))
