from math import cos, exp


x = 1.472
y = -0.4342

d = (x * exp(x * y) + 4 * cos(x) ** 2) / (x * (x - y) * (2 * x + y))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
