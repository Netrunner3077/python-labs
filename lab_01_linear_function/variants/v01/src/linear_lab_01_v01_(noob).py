from math import cos, pi, sin


x = 3.59
y = 17.53

d = cos(pi / 7) * sin(x - 8 * y) ** 2 / (2.7 * (x - pi))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
