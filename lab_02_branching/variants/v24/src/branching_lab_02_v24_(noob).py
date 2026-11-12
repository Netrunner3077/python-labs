from math import exp, log, sqrt


x = 1.0
y = 2.0
a = 1.0
b = 1.0

if x * y > 0:
    z = 1 - exp(x * y + a * b)
elif x * y == 0:
    z = b - min(a * x, y)
else:
    z = max(x ** 3, exp(y), sqrt(abs(log(y ** 2))))

print("x = " + str(x) + ", " + "y = " + str(y) + ", " + "a = " + str(a) + ", " + "b = " + str(b))
if z is None:
    print("Формула для этих данных не задана.")
else:
    print("Результат = " + str(z))
