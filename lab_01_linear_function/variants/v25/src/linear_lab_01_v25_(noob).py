from math import copysign, pi, sin


x = 20.356
y = 0.523

d = x * (x - y) * (4 * x + y) / (2.7 * (x - pi)) + copysign(abs(0.2 * x / sin(y)) ** (1 / 3), 0.2 * x / sin(y))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
