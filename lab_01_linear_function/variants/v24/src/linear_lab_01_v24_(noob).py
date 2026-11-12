from math import log10, sin


x = 8.804
y = -0.4915

d = x - 1 / (0.27 * sin(x - 4 * y)) + 21 * log10(abs(x + y))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
