from math import log, sin


x = 32.01
y = -0.4917

d = (x * y + sin(x)) / (abs(1 - y) * log(x))
print("Результат = " + str(round(d, 4)))
print("Целая часть = " + str(int(d)))
