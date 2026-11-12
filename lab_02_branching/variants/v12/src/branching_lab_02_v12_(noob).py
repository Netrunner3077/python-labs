from math import sin, sqrt


x = 2.0
y = 3.0
a = 1.0
b = 1.0

if x > 0 and y > 2:
    z = min(a * x, y, max(sqrt(x), sin(y)))
else:
    z = max(b, x, y) / min(x, y + 1)

print("x = " + str(x) + ", " + "y = " + str(y) + ", " + "a = " + str(a) + ", " + "b = " + str(b))
if z is None:
    print("Формула для этих данных не задана.")
else:
    print("Результат = " + str(z))
