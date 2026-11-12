from math import exp, log, sin


x = 2.0
y = 0.5

if 2 < x + y < 3:
    z = 4 * min(5 ** (3 + x), x + y, -4 * y)
elif x + y > 3:
    z = max(exp(x - y), 3 * log(x), min(x, y))
else:
    z = 2.5 * sin(x * y) * max(x, y)

print("x = " + str(x) + ", " + "y = " + str(y))
if z is None:
    print("Формула для этих данных не задана.")
else:
    print("Результат = " + str(z))
