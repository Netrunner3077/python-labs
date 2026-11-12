from math import sin, sqrt, tan


x = 10.315
y = -0.2114

d = sin(tan(x) ** 2) * sqrt((2 * x + y) / (0.3 * x))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
