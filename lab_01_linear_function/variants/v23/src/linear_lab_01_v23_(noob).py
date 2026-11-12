from math import copysign, log, sin


x = 7.428
y = -0.543

d = (1 - y) * log(x) / abs(x * y + sin(x)) + copysign(abs((x + y) / (0.1 * x)) ** (1 / 3), (x + y) / (0.1 * x))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
