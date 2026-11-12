from math import pi, sqrt, tan


x = 15.207
y = -4.415

d = pi / 3 - sqrt(3 * x) + (x ** 2 + y) / (0.55 * tan(abs(x + y)))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
