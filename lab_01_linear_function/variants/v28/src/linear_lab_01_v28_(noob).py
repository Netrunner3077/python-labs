from math import pi, sqrt, tan


x = 11.872
y = 1.4517

d = 0.72 * tan(abs(x + y)) / (x ** 2 + y) - sqrt(2 * x) + pi / 2
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
