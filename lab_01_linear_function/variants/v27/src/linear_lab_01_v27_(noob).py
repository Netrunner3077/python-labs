from math import cos, sqrt


x = 12.615
y = 7.5

d = (sqrt(abs(x ** 3 - 3.4e-3 * y)) + x ** 2 * y) / (3 * cos(x * y))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
