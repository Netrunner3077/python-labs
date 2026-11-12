from math import exp


x = 82.578
y = 1.4517

d = 0.8e-5 * (x * exp(-x * (y - 1.2)) - y * x) ** 3
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
