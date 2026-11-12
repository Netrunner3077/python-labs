from math import sin, sqrt


x = 1.3802
y = -1.9

d = (x * y ** 2 - sqrt(abs(x ** 2 - 2.5e-3 * y))) / (2 * sin(x * y))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
