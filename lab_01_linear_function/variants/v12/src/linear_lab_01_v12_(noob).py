from math import cos, log


x = 25.01
y = -0.5736

d = (x ** 2 * y + log(x)) / (abs(1 - y) * cos(x))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
