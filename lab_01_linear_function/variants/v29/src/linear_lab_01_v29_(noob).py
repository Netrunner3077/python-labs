from math import exp, log, sin


x = -32.01
y = 1.457

d = (1 - exp(2 * x * y ** 2)) ** 2 / (0.65 * sin(x) * log(abs(1 - y ** 2)))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
