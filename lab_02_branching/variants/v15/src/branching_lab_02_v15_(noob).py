from math import cos, exp, sin


x = 0.5
y = 2.0
a = 1.0

if x < 1 and y > 1:
    z = max(2 * sin(x), 3 * min(x, y), x + a)
elif x > 1 and y > 1:
    z = min((x + exp(2 * x + a)) / 3, max(x, y))
else:
    z = 4 * cos(x * y)

print("x = " + str(x) + ", " + "y = " + str(y) + ", " + "a = " + str(a))
if z is None:
    print("Формула для этих данных не задана.")
else:
    print("Результат = " + str(z))
