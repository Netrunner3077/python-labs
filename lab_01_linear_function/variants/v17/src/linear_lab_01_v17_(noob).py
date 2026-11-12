from math import cos, sqrt


x = 1.385
y = -1.2

d = (x * y + sqrt(abs(x ** 2 - 3.4e-3 * y))) / (2 * cos(x * y ** 2))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
