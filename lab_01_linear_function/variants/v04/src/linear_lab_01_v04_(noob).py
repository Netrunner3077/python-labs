from math import cos, sin


x = 2.123
y = -1.89

d = (x * y ** 2 - 1) ** 2 / 2 * (cos(y) ** 2 - sin(x ** 2))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
