from math import exp


x = 75.447
y = 1.2328

d = (y * exp(-x * (y - 0.8)) + x * y ** 2) ** 3 * 0.9e-4
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
