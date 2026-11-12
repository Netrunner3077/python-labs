from math import pi, sqrt, tan


x = 12.003
y = -5.408

d = pi / 2 - sqrt(2 * x) - (x + y ** 2) / (0.75 * tan(abs(x + y)))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
