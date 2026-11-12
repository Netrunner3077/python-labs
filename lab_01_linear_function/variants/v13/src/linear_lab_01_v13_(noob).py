from math import cos, pi, sin


x = 4.72
y = 21.35

d = cos(pi / 5) * sin(3 * x - 5 * y) ** 2 / (3.5 * (x + pi))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
