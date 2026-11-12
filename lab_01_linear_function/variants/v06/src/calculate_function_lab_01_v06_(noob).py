from math import exp, sin


x = 1.002
y = -0.5321

if x == 0 or x == y or 3 * x + y == 0:
    print("Знаменатель равен нулю.")
else:
    a = x * exp(x * y) + 8 * sin(x) ** 2
    b = x * (x - y) * (3 * x + y)
    d = a / b
    rounded = round(d, 4)
    print("d = " + str(rounded))
    print("Целая часть = " + str(int(d)))
