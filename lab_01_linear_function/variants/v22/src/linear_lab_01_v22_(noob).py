from math import pi, sin


x = 4.58
y = 16.34

d = sin(x - 7 * y) ** 2 / (2.5 * (x - pi)) * sin(pi / 4)
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
