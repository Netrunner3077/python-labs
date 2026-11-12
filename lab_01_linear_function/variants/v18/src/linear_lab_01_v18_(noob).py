from math import exp


x = 75.412
y = 1.1745

d = 0.75e-6 * (x * exp(-x * (y - 1.5)) - y * x) ** 2
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
