from math import log10, sin


x = 12.678
y = 6.9

d = 120 * log10(x + y) / (x - 1 / (0.45 * sin(x - 8 * y)))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
