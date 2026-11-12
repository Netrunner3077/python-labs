from math import cos, sin


x = 2.0
a = 1.0
b = 0.5

if a > 0 and x > 1:
    z = max(a, x / a, cos(a))
elif a < 0 and x > 1:
    z = min(a, a * x + sin(b), max(a, b))
else:
    z = max(a, b)

print("x = " + str(x) + ", " + "a = " + str(a) + ", " + "b = " + str(b))
if z is None:
    print("Формула для этих данных не задана.")
else:
    print("Результат = " + str(z))
