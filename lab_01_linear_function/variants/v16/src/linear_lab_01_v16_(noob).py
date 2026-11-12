from math import exp, log10


x = -1.834
y = -0.533

d = (3 - exp(x * y)) ** 2 / (0.5 * log10(1 - x))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
