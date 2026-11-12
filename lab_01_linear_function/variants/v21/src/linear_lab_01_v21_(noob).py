from math import log, pi, tan


x = 11.485
y = -3.231

d = (2 * x + y ** 2) / (0.82 * tan(abs(x + y))) + pi / 4 - log(abs(x + y))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
