from math import exp


a = -30  # Начало отрезка в десятых долях
b = 30
h = 3
n = (b - a) // h + 1
p = 1.0
print("x | y")

for i in range(n):
    x = (a + h * i) / 10

    if x > 1:
        y = exp(x)
    elif x < 0:
        y = 2 * x - 1
    else:
        y = -1.0

    print(str(x) + " | " + str(y))
    if y > 0:
        p = p * y

print("Произведение положительных y = " + str(p))
