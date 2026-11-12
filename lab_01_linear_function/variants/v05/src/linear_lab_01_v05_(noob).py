from math import copysign, sin, tan


x = 8.402
y = -0.2226

d = copysign(abs((x + y) / (0.2 * x)) ** (1 / 3), (x + y) / (0.2 * x)) * sin(tan(x) ** 2)
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
