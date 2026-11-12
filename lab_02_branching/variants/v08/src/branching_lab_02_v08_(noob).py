from math import log10


x = 2.0
y = 2.0
c = 1.0
d = 2.0

if x * y > 3:
    z = x ** 3 + log10(x * y) ** (c * d)
elif 2 < x * y < 3:
    z = 3 * min(x, y, max(c * x, d * y))
elif x * y < 2:
    z = 2 ** (c * d) - x
else:
    z = None

print("x = " + str(x) + ", " + "y = " + str(y) + ", " + "c = " + str(c) + ", " + "d = " + str(d))
if z is None:
    print("Формула для этих данных не задана.")
else:
    print("Результат = " + str(z))
