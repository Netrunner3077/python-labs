from math import exp, log10


x = 1.674
y = -0.533

d = (1 - exp(x * y)) ** 2 / (0.7 * log10(abs(1 - x ** 2)))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
