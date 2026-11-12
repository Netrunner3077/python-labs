from math import log10, sin


x = 12.345
y = 7.5

d = 3 * log10(x + y) + x - 1 / (0.68 * sin(x - 7 * y))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
