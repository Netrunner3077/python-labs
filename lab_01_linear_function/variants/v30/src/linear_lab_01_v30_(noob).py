from math import cos, pi, sin


x = -10.22
y = 15.368

d = cos(pi / 5) * sin(x - 3 * y) ** 3 / (1.7 * (x - pi))
print("Результат = " + str(round(d, 5)))
print("Целая часть = " + str(int(d)))
