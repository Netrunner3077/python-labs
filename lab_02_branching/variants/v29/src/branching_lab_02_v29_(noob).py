from math import cos, exp, log, sin


x = 0.5
y = 0.7
a = 5.0
c = 2.0
d = 1.0

if 0 < x < 1 and 0 < y < 1:
    z = 2 * log(x) * max(min(x, y), sin(c * x), cos(d))
elif x < 0 and y < 0:
    z = min(exp(x + 1), y)
else:
    z = a + x

print("x = " + str(x) + ", " + "y = " + str(y) + ", " + "a = " + str(a) + ", " + "c = " + str(c) + ", " + "d = " + str(d))
if z is None:
    print("Формула для этих данных не задана.")
else:
    print("Результат = " + str(z))
