from math import cos, sin


x = 5.422
y = -0.1537

d = ((2 * x + y) / (0.1 * x)) ** 0.25 * cos(sin(x) ** 2)
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
